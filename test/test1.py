import re
import pandas as pd

input_file = "requests1.log"  # File log đầu vào
output_excel = "requests1.csv"  # File Excel đầu ra

# Regex để trích xuất thông tin từ log
log_pattern = re.compile(r"\[GIN\] (\d{4}/\d{2}/\d{2} - \d{2}:\d{2}:\d{2}) \|\s*(\d+)\s*\|\s*([\d\.µms]+)\s*\|\s*([\d\.]+)\s*\|\s*([A-Z]+)\s*\"([^\"]+)\"")

data = []

with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        match = log_pattern.search(line)
        if match:
            timestamp, status, response_time, client_ip, method, endpoint = match.groups()
            data.append([timestamp, int(status), response_time, client_ip, method, endpoint])

# Tạo DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Status", "Response Time", "Client IP", "Method", "Endpoint"])

# Xuất ra Excel
df.to_csv(output_excel, index=False)

print(f"Đã chuyển file log thành DataFrame và lưu vào {output_excel}")
