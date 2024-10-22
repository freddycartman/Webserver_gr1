Phải đưa file exe vào môi trường Window để chạy dự án

Để đưa php.exe vào biến môi trường trên Windows, thầy có thể làm theo các bước sau:

Bước 1: Tìm đường dẫn đến php.exe

Trước tiên, thầy cần xác định đường dẫn đầy đủ đến tệp php.exe. Nếu thầy đã cài đặt PHP, tệp này thường nằm trong thư mục cài đặt PHP, ví dụ như C:\php\ hoặc C:\xampp\php\.

Bước 2: Thêm đường dẫn vào biến môi trường

 1. Mở Cài đặt Hệ thống:
 • Nhấn Windows + R để mở hộp thoại Run.
 • Nhập sysdm.cpl và nhấn Enter. Điều này sẽ mở cửa sổ “System Properties”.
 2. Chọn tab “Advanced”:
 • Trong cửa sổ “System Properties”, chọn tab “Advanced”.
 3. Nhấn vào nút “Environment Variables”:
 • Nhấn nút “Environment Variables” ở dưới cùng của tab “Advanced”.
 4. Chỉnh sửa biến Path:
 • Trong phần “System variables”, tìm biến có tên Path và chọn nó.
 • Nhấn nút “Edit”.
 5. Thêm đường dẫn đến php.exe:
 • Nhấn nút “New” và nhập đường dẫn đến thư mục chứa php.exe (ví dụ: C:\xampp\php hoặc C:\php).
 • Nhấn “OK” để lưu lại.
 6. Xác nhận và đóng:
 • Nhấn “OK” trong tất cả các cửa sổ đã mở để xác nhận và đóng chúng.

 Sau đó thầy nhập localhost:8080/webcafe/index.php để chạy file
