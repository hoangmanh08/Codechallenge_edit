Ứng dụng LLM AI để hỗ trợ code. Tuy nhiên trong quá trình sử dụng hệ thống bị quá tải. Lý do có thể như sau:
-	Số lượng người dùng quá nhiều
-	Người dùng đẩy nhiều API lên hệ thống. Tần suất đẩy nhiều (theo IP của người dùng)
-	Người dùng đẩy API phức tạp lên hệ thống

Từ dữ liệu log ứng dụng trong file `output.log`, xử lý và đưa ra các thống kê sau:
-	Thống kê tần suất gửi API của tất cả các user. (theo tổng, theo loại, TPS min, max, avg, …). Chỉ ra xem các lệnh nào có thời gian phản hồi chậm nhất…
-	Thống kê tần suất gửi API của từng user , chỉ ra ai hoạt động nhiều nhất,  loại lệnh, … Chỉ xem user nào dùng lệnh nào chậm nhất
-	Vẽ biểu đồ 2 vấn đề trên. Mục đích chỉ ra được ai hoặc lệnh nào đang làm chậm hệ thống.
