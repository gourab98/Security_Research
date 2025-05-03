def sales_price(items_and_price):
    item = ""
    price = ""
    item_or_price = items_and_price.split()

    for x in item_or_price:
        if x.isalpha():
            item = item + x + " "
        else: price = x

    item = item.strip()

    return "{} are on sale for ${}".format(item,price)

print(sales_price("Winter fleece jackets 49.99"))