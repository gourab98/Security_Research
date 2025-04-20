# Create a dictionary
x = {}
print(type(x))

# dictionary
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)
print(file_counts["txt"])
print("csv" in file_counts)

file_counts["jpg"] = 3
print(file_counts)

file_counts["cpp"]=5
print(file_counts)

# Delete 
del file_counts["txt"]
print(file_counts)
