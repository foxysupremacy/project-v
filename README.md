# Project V (Story only)

Kho lưu trữ bản dịch tiếng Việt cho trò chơi **Umamusume: Pretty Derby**, sử dụng với patch [Hachimi](https://hachimi.noccu.art).

> [!NOTE]
> Nhánh **`dev`** hiện đang trong quá trình phát triển và cập nhật liên tục. Bản dịch tập trung vào phần **cốt truyện (Story)** bằng tiếng Việt, trong khi phần giao diện người dùng (UI), kỹ năng và các dữ liệu hệ thống nền được giữ bằng tiếng Anh từ [UmaTL / hachimi-tl-en](https://github.com/UmaTL/hachimi-tl-en).

---

## Phạm vi hiện tại

Theo cấu hình trong [`localized_data/`](./localized_data):

- **Tiếng Việt:**
  - Cốt truyện nhân vật (`localized_data/assets/story/data/04/` — 103 nhân vật).
  - Tiêu đề cốt truyện nhân vật (nhóm `92` trong `text_data_dict.json`).
  - Lời thoại nhân vật / hệ thống (home, career, đăng nhập, v.v. trong `character_system_text_dict.json`; một số dòng chưa dịch vẫn giữ nguyên bản tiếng Anh).
  - Font hỗ trợ tiếng Việt (`assets/bobonwenttomaccascalibrib.otf`), được đóng gói sẵn cho cả Windows (`includes_win`) và Android (`includes_android`).
- **Tiếng Anh (từ UmaTL / hachimi-tl-en):**
  - Giao diện (UI), menu, mô tả kỹ năng, từ điển hệ thống (`localize_dict.json`, `hashed_dict.json`, `text_data_dict.json`, v.v.) và các asset đồ họa đi kèm (`atlas/`, `textures/`, `uianimation/`, `lyrics/`).

---

## Thiết lập nhánh `dev` vào Hachimi

Project V phân phối bản dịch thông qua chỉ mục GitHub trên nhánh `dev`:

- **Index URL (`index.json`):**
  ```text
  https://raw.githubusercontent.com/foxysupremacy/project-v/dev/index.json
  ```
- **Meta URL (`meta.json`):**
  ```text
  https://raw.githubusercontent.com/foxysupremacy/project-v/dev/meta.json
  ```

### Các bước thiết lập

1. Mở game đã cài sẵn Hachimi, mở menu cấu hình của Hachimi (hoặc chạy lại **First Time Setup** / mở mục cấu hình **Translation**).
2. Trỏ nguồn bản dịch (Translation Repo / Index URL) tới địa chỉ `index.json` của nhánh `dev` ở trên (hoặc chọn/nạp từ `meta.json`).
3. Xác nhận tải dữ liệu bản dịch khi Hachimi kiểm tra và hỏi cập nhật.

### Gợi ý thiết lập trong Hachimi

> [!TIP]
> Trong menu của Hachimi → **Config** → **Gameplay**, bạn nên điều chỉnh thêm 2 tùy chọn sau để đọc cốt truyện tiếng Việt thoải mái hơn:
> - `Story choice auto select delay`: `1.2`
> - `Story text speed multiplier`: `3.0`

### Cập nhật bản dịch

Khi khởi động game, Hachimi sẽ tự động kiểm tra bản cập nhật từ `index.json`. Nếu có bản mới, bạn chỉ cần đồng ý tải về; bản dịch sẽ được áp dụng ngay mà không cần khởi động lại game.

---

## Báo lỗi & Phản hồi

Nếu gặp lỗi chính tả, xưng hô, tràn khung chữ hoặc thiếu/lỗi file khi sử dụng nhánh `dev`, vui lòng tạo Issue tại:
- [GitHub Issues — foxysupremacy/project-v](https://github.com/foxysupremacy/project-v/issues)

---

## Nguồn dữ liệu & Bản quyền

- Dữ liệu gốc của trò chơi thuộc bản quyền của **Cygames**. Project V là dự án cộng đồng phi lợi nhuận và không liên kết dưới bất kỳ hình thức nào với nhà phát triển hoặc nhà phát hành trò chơi.
- Bản dịch giao diện tiếng Anh, từ điển nền và các asset UI được lấy từ [UmaTL / hachimi-tl-en](https://github.com/UmaTL/hachimi-tl-en) ([UmaTL](https://github.com/noccu/umamusu-translate)) cùng các cộng tác viên của họ.
- Theo điều khoản sử dụng dữ liệu của nguồn gốc **UmaTL**:
  - Dữ liệu trong kho lưu trữ này **không** được phát hành theo giấy phép mã nguồn mở (open license).
  - Mọi dữ liệu dịch thuật thuộc quyền của các tác giả và nguồn đóng góp tương ứng; chỉ được phép tái sử dụng trong các dự án cộng đồng liên quan đến trò chơi khi có ghi nguồn đầy đủ và khác phạm vi mục tiêu với UmaTL.
  - **Nghiêm cấm** mọi hình thức sử dụng dữ liệu từ kho lưu trữ này cho mục đích huấn luyện, đánh giá hoặc phát triển các mô hình Machine Learning / AI tạo sinh (generative ML/AI).

---

## Dành cho Maintainer

### Cấu trúc thư mục chính

```text
.
├── meta.json                 # Metadata nguồn repo cho Hachimi (nhánh dev)
├── index_base.json           # Cấu hình base_url / zip_url để sinh index.json
├── index.json                # Danh sách file & hash BLAKE3 do gen_index.py tạo
├── requirements.txt          # Phụ thuộc Python cho script tạo index (pygit2, blake3)
├── localized_data/
│   ├── config.json           # Cấu hình font, text wrapper, extra_asset_bundle
│   ├── info.json             # Thông tin gói dịch hiển thị trong Hachimi
│   ├── includes_win          # Asset bundle font cho Windows
│   ├── includes_android      # Asset bundle font cho Android
│   ├── *_dict.json           # Các từ điển text hệ thống / nhân vật / UI
│   └── assets/               # Story JSON, lyrics, atlas, textures, font .otf
└── scripts/                  # Các công cụ kiểm tra, đồng bộ và đóng gói index
```

### Cấu hình font & Asset Bundle hiện hành

Trong [`localized_data/config.json`](./localized_data/config.json):
- `replacement_font_name`: `assets/bobonwenttomaccascalibrib.otf`
- `extra_asset_bundle`: `includes_win` (Windows) và `includes_android` (Android)

### Các script trong `scripts/`

> [!IMPORTANT]
> Các script xử lý file (`qa_story_04.py`, `sync_story_04_titles.py`, `wrap_story_lines.py`) mặc định chạy ở chế độ **dry-run** (chỉ xem trước, không ghi file). Thêm cờ `--apply` để áp dụng thay đổi.

1. **Làm sạch story category `04`** — [`scripts/qa_story_04.py`](./scripts/qa_story_04.py)
   Loại bỏ ký tự xuống dòng thừa và các lựa chọn (`choice_data_list`) rỗng trong `localized_data/assets/story/data/04/`:
   ```bash
   python3 scripts/qa_story_04.py          # dry-run
   python3 scripts/qa_story_04.py --apply  # ghi thay đổi
   ```

2. **Đồng bộ tiêu đề story `04`** — [`scripts/sync_story_04_titles.py`](./scripts/sync_story_04_titles.py)
   Đối chiếu tiêu đề gốc (`jptitle`) trong `localized_data/assets/story/data/04/` với bảng `text_data` (`category = 92`) trong `master.mdb` của game, rồi thêm tiêu đề tiếng Việt (`title`) vào `localized_data/text_data_dict.json` (không tự ghi đè bản dịch đã có nếu bị xung đột):
   ```bash
   python3 scripts/sync_story_04_titles.py --master /path/to/master.mdb
   python3 scripts/sync_story_04_titles.py --master /path/to/master.mdb --apply
   ```
   *(Có thể đặt biến môi trường `UMA_DATA_DIR` trỏ tới thư mục Persistent của game thay cho `--master`.)*

3. **Ngắt dòng cho các story `no_wrap: true`** — [`scripts/wrap_story_lines.py`](./scripts/wrap_story_lines.py)
   Tự động chèn `\n` theo bề rộng khung thoại cho các category story khác (mặc định bỏ qua category `04`; cần cài `Pillow`):
   ```bash
   python3 scripts/wrap_story_lines.py --font localized_data/assets/bobonwenttomaccascalibrib.otf
   python3 scripts/wrap_story_lines.py --font localized_data/assets/bobonwenttomaccascalibrib.otf --apply
   ```

4. **Tạo lại `index.json`** — [`scripts/gen_index.py`](./scripts/gen_index.py)
   Tính hash BLAKE3 và kích thước cho toàn bộ file trong `localized_data/` ở commit `HEAD` hiện tại (bỏ qua `.gitignore`), kết hợp với `index_base.json` để xuất ra `index.json`. Cần cài phụ thuộc từ `requirements.txt` (`pygit2`, `blake3`) và **commit mọi thay đổi trong `localized_data/` trước khi chạy**:
   ```bash
   python3 scripts/gen_index.py
   ```
