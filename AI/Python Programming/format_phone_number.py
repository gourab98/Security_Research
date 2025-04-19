def format_phone(phonenum):
    area_code = "("+phonenum[:3]+")"
    exchange_code = phonenum[3:6]
    line_number = phonenum[-4:]
    return area_code + " "+ exchange_code + "-" + line_number

print(format_phone('2025551212'))