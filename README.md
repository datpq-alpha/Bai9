# Bài 9 — Lưu thành phố yêu thích

## Mục tiêu LAB

Bài 9 tiếp tục từ sản phẩm tra cứu thời tiết của Bài 8. Em sẽ dùng SQLite để:

- Lưu một thành phố yêu thích.
- Đọc danh sách đã lưu.
- Xóa một thành phố.
- Xử lý trường hợp lưu trùng.

Mã tra cứu thời tiết đã hoàn chỉnh. Bài có năm vị trí `TODO` tập trung vào thao tác dữ liệu.

## 1. Cài môi trường

- Vào repo https://github.com/datpq-alpha/Bai9 và fork về tài khoản cá nhân
- Vào trang GitHub cá nhân và coppy link repo của mình, ví dụ: https://github.com/<tk của em>/Bai9.git
- Mở CMD gõ lần lượt các lệnh:
```
cd Desktop
git clone https://github.com/<tk của em>/Bai9.git Bai9
```
- Sau đó, repo Bai9 trên trang cá nhân đã được đồng bộ url về repo Bai9 trên máy.

Mở Terminal tại thư mục `Bai9`.

Windows PowerShell (chạy từng lệnh một):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Nếu PowerShell chặn script, chạy một lần Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser .
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 2. Điền API key

Sao chép `.env.example` thành `.env`:

```env
OPENWEATHER_API_KEY=api_key_that_cua_em
```

Không commit `.env` lên GitHub.

## 3. Trình tự hoàn thành

1. Trong `backend/main.py`, tạo bảng `favorite_cities`:
   - `id INTEGER PRIMARY KEY AUTOINCREMENT`
   - `city_name TEXT NOT NULL UNIQUE`
2. Viết câu lệnh `SELECT` để lấy danh sách.
3. Viết câu lệnh `INSERT`; bắt `sqlite3.IntegrityError` khi tên bị trùng.
4. Viết câu lệnh `DELETE` dùng tham số `?`, không ghép chuỗi SQL.
5. Trong `frontend/app.py`, gửi `POST` với JSON dạng `{"city_name": "Hanoi"}`.

Sau thao tác làm thay đổi dữ liệu, nhớ gọi `connection.commit()`.

## 4. Chạy ứng dụng

Terminal 1:

```powershell
python -m uvicorn backend.main:app --reload
```

Terminal 2:

```powershell
python -m streamlit run frontend/app.py
```

Trang API: <http://localhost:8000/docs>  
Giao diện: địa chỉ được Streamlit in trên Terminal.

## Hoàn thành khi

1. Tìm được một thành phố.
2. Lưu được thành phố đó.
3. Tab **Đã lưu** hiển thị thành phố sau khi tải lại.
4. Lưu trùng nhận thông báo phù hợp.
5. Nút **Xóa** loại bỏ đúng thành phố.

File `weather.db` được tạo tự động và đã nằm trong `.gitignore`.

## Yêu cầu nộp bài

Repository đã được **fork** vào tài khoản GitHub của em và **clone** về máy từ đầu buổi học. Vì vậy, em không chạy `git init` và không tạo repository mới.

1. Mở Terminal tại thư mục repository đã clone và kiểm tra remote:

   ```powershell
   git remote -v
   ```

   Địa chỉ `origin` phải là repository trong tài khoản GitHub của em.

2. Kiểm tra các file đã thay đổi:

   ```powershell
   git status
   ```

   Đảm bảo `.env`, `.venv`, `weather.db` và các file chứa API key không xuất hiện trong danh sách chuẩn bị commit.

3. Thêm bài làm và tạo commit:

   ```powershell
   git add .
   git status
   git commit -m "Hoan thanh Bai 9"
   ```

4. Đẩy nhánh hiện tại lên repository đã fork:

   ```powershell
   git push origin HEAD
   ```

5. Mở repository của em trên GitHub, kiểm tra các file đã được cập nhật rồi nộp:

   - Đường dẫn repository GitHub đã fork.
   - Đường dẫn commit mới nhất của bài làm.
   - Ảnh chụp chức năng lưu và xóa thành phố chạy thành công.

Không nộp API key, file `.env`, `weather.db` hoặc thư mục `.venv`.
