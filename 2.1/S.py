product = input()
price = input()
weight = input()
money = input()

product_string = 35 - 6 - len(product)
price_string = 35 - 5 - len(weight) - 5 - len(price) - 6
summ = int(weight) * int(price)
price_summ_string = 35 - 9 - len(str(summ))
money_string = 35 - 11 - len(money)
change = int(money) - summ
change_string = 35 - 9 - len(str(change))

print("================Чек================")
print("Товар:" + product_string * " " + product)
print("Цена:" + price_string * " " + weight + "кг * " + price + "руб/кг")
print("Итого:" + price_summ_string * " " + str(summ) + "руб")
print("Внесено:" + money_string * " " + str(money) + "руб")
print("Сдача:" + change_string * " " + str(change) + "руб")
print(35 * "=")
