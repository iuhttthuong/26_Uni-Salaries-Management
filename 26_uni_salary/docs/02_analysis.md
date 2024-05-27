## 2. PHÂN TÍCH

### 2.1 Giới thiệu

#### 2.1.1. Mục đích

Bài toán này tập trung vào việc phát triển một ứng dụng web để quản lý tiền lương cho một trường đại học, nhằm tự động hóa quá trình tính toán và quản lý tiền lương, từ đó giảm thiểu sai sót và tăng cường hiệu quả làm việc của bộ phận nhân sự. 

#### 2.1.2 Phạm vi

Ứng dụng tập trung vào phạm vi một trường đại học cụ thể là giảng viên, kế toán và hiệu trưởng nhà trường


### 2.2 Phân tích yêu cầu

#### 2.2.1 Đặc tả Actors

- Hiệu trưởng: người lãnh đạo của trường đại học đó
- Kiểm toán: nhân viên kiểm duyệt lương bổng của trường đại học
- Giảng viên: nhân sự giảng dạy của nhà trường

#### 2.2.2 Đặc tả Use-cases

- Danh sách các use-cases:
    - UC01: đăng nhập (Đăng nhập bằng tài khoản và mật khẩu mà nhà trường cung cấp)
    - UC02: Phân quyền (Phân quyền thành các chức vụ có trong actors)
    - UC03: Xem thông tin người khác (Người có chức vụ quan trọng có thể xem được thông tin toàn bộ giảng viên)
    - UC04: Xem thông tin cá nhân (Chỉ giảng viên mới có chức năng này vì quyền của giảng viên là thấp nhất)
    - UC05: Tìm kiếm giảng viên (Tìm kiếm các giảng viên có trong cơ sở dữ liệu)
    - UC06: Thêm, xoá, sửa thông tin giảng viên (Thêm, xoá, sửa thông tin giảng viên có trong cơ sở dữ liệu)
    - UC07: Cập nhật hệ số lương (Hệ số lương được quyết định, cập nhật dựa trên các yếu tố)
    - UC08: In phiếu lương (In phiếu lương của nhân sự nhà trường) 
- Liệt kê các use-cases theo actor:
    - Hiệu trưởng:
        - UC01: đăng nhập
        - UC02: Phân quyền
        - UC03: Xem thông tin người khác
        - UC05: Tìm kiếm giảng viên
        - UC08: In phiếu lương
    - Kế toán:
        - UC01: đăng nhập
        - UC03: Xem thông tin người khác
        - UC05: Tìm kiếm giảng viên
        - UC07: Cập nhật hệ số lương
        - UC08: In phiếu lương
    - Giảng viên:
        - UC01: đăng nhập
        - UC04: Xem thông tin cá nhân
