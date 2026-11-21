#!/usr/bin/env python3
"""Sync translated category-04 story titles to text_data category 92.

Run without --apply to preview. Set UMA_DATA_DIR or pass --master to the
game's master.mdb. Existing differing translations are reported, not replaced.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
STORY_DIR = ROOT / 'localized_data/assets/story/data/04'
DICT_PATH = ROOT / 'localized_data/text_data_dict.json'
PATTERN = re.compile(r'storytimeline_(04\d{7})\.json')


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--master', type=Path, help='Path to the game master.mdb')
    parser.add_argument('--apply', action='store_true', help='Write verified titles to text_data_dict.json')
    args = parser.parse_args()
    game_dir = os.environ.get('UMA_DATA_DIR')
    master = args.master or (Path(game_dir) / 'master/master.mdb' if game_dir else None)
    if not master or not master.is_file():
        parser.error('Provide --master or set UMA_DATA_DIR to the game Persistent directory')
    dictionary = json.loads(DICT_PATH.read_text(encoding='utf-8-sig'))
    existing = dictionary.get('92', {})
    if not isinstance(existing, dict):
        raise ValueError('text_data_dict category 92 must be an object')
    files = sorted(STORY_DIR.glob('*/*.json'))
    if not files:
        raise ValueError(f'No story files found in {STORY_DIR}')
    additions = {}
    skipped = []
    conflicts = []
    same = 0
    with sqlite3.connect(master.resolve().as_uri() + '?mode=ro', uri=True) as db:
        for path in files:
            match = PATTERN.fullmatch(path.name)
            if not match or path.parent.name != match.group(1)[2:6]:
                raise ValueError(f'Unexpected story path: {path}')
            story = json.loads(path.read_text(encoding='utf-8-sig'))
            title, jp = story.get('title', ''), story.get('jptitle', '')
            if not isinstance(title, str) or not isinstance(jp, str):
                raise ValueError(f'Invalid title in {path}')
            key = str(int(match.group(1)))
            row = db.execute('SELECT text FROM text_data WHERE category = 92 AND "index" = ?', (int(key),)).fetchone()
            if not title.strip() or row is None or row[0] != jp:
                skipped.append((key, path, jp, row[0] if row else None))
                continue
            if key in existing:
                if existing[key] == title:
                    same += 1
                else:
                    conflicts.append((key, path, existing[key], title))
            elif key in additions and additions[key] != title:
                raise ValueError(f'Conflicting source titles for {key}')
            else:
                additions[key] = title
    for key, path, jp, master_title in skipped:
        print(f'SKIP {key} {path}: story={jp!r}, master={master_title!r}')
    for key, path, old, new in conflicts:
        print(f'CONFLICT {key} {path}: existing={old!r}, proposed={new!r}')
    print(f'Files: {len(files)}; new: {len(additions)}; unchanged: {same}; skipped: {len(skipped)}; conflicts: {len(conflicts)}')
    if args.apply and additions:
        dictionary.setdefault('92', {}).update(additions)
        DICT_PATH.write_text(json.dumps(dictionary, ensure_ascii=False, indent=4) + '\n', encoding='utf-8', newline='\n')
        print(f'Updated {DICT_PATH}')
    elif not args.apply:
        print('Preview only; use --apply to write.')
    return 1 if conflicts else 0


if __name__ == '__main__':
    sys.exit(main())
