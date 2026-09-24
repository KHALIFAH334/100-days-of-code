raw_log = ["SUCCESS: user_01", "ERROR: user_44", "SUCCESS: user_99", "ERROR: user_12", "ERROR: user_44"]
error_data = []

for item in raw_log:
    if "ERROR" in item:
        error_data.append(item)

total_error_count = len(error_data)

print(error_data)
print(total_error_count)