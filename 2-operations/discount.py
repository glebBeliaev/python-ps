product_price = float(input("Введите стоимость товара: "))
discount = float(input("Введите размер скидки: "))
discount_price = product_price - (product_price * discount / 100)
print("Стоимость товара со скидкой: " + str(discount_price))
