# input_file = "output.log"
# output_file = "requests.log"

# # Mở file đọc và ghi
# with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
#     for line in infile:
#         if "[GIN]" in line:  # Kiểm tra dòng có chứa request API không
#             outfile.write(line)  # Ghi dòng request API vào file mới

# print(f"Đã lọc xong request API. Kết quả được lưu vào {output_file}")

import re

input_file = "output.log"  # Tên file log đầu vào
output_file = "requests1.log"  # Tên file đầu ra

# Regex để loại bỏ ký tự ANSI escape sequences
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        if "[GIN]" in line:  # Kiểm tra dòng có chứa request API không
            clean_line = ansi_escape.sub('', line)  # Loại bỏ ký tự ANSI
            outfile.write(clean_line)  # Ghi dòng request API sạch vào file mới

print(f"Đã lọc xong request API và loại bỏ ANSI. Kết quả được lưu vào {output_file}")
