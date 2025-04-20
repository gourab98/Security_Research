file_counts={"jpg": 10, "txt": 14, "csv":2, "py": 23}

for key in file_counts:
    print(key)

for key, value in file_counts.items():
    print("There are {} files with the .{} extension".format(value,key))

print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)
