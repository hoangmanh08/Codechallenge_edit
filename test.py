import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('requests1.csv')


# Function to convert response time to seconds
def convert_to_seconds(time_str):
    if 'ms' in time_str:
        return float(time_str.replace('ms', '')) / 1000  # Convert milliseconds to seconds
    elif 's' in time_str:
        return float(time_str.replace('s', ''))  # Already in seconds
    elif 'µs' in time_str:
        return float(time_str.replace('µs', '')) / 1_000_000  # Convert microseconds to seconds
    return 0

# Apply conversion to 'Response Time' column
df['Response Time'] = df['Response Time'].apply(convert_to_seconds)

# Save the updated DataFrame to a new CSV file
df.to_csv('test.csv', index=False)

print("File has been successfully created as 'converted_response_times.csv'.")
