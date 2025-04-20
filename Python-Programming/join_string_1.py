def list_elements(list_name, elements):
    return "The "+ list_name + "list includes: " + ", ".join(elements)


# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"
print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))