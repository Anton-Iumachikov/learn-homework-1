sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


for product in sales:
    if product['product'] == 'iPhone 12':
        total_sales = sum(product['items_sold'])
        print(f"Суммарное количество продаж iPhone 12: {total_sales}")
for product in sales:
    if product['product'] == 'Xiaomi Mi11':
        total_sales = sum(product['items_sold'])
        print(f"Суммарное количество продаж Xiaomi Mi11: {total_sales}")
for product in sales:
    if product['product'] == 'Samsung Galaxy 21':
        total_sales = sum(product['items_sold'])
        print(f"Суммарное количество продаж Samsung Galaxy 21: {total_sales}")
for product in sales:
    if product['product'] == 'iPhone 12':
        total_sales = sum(product['items_sold'])/len(product['items_sold'])
        print(f"Среднее количество продаж iPhone 12: {total_sales}")
for product in sales:
    if product['product'] == 'Xiaomi Mi11':
        total_sales = sum(product['items_sold'])/len(product['items_sold'])
        print(f"Среднее количество продаж Xiaomi Mi11: {total_sales}")
for product in sales:
    if product['product'] == 'Samsung Galaxy 21':
        total_sales = sum(product['items_sold'])/len(product['items_sold'])
        print(f"Среднее количество продаж Samsung Galaxy 21: {total_sales}")
total_sales_all = 0
for product in sales:
    total_sales = sum(product['items_sold'])
    total_sales_all += total_sales
print(f"Суммарное количество продаж: {total_sales_all}")
total_sales_all = 0
total_sales_len = 0
for product in sales:
    total_sales = sum(product['items_sold'])
    total_sales_all += total_sales
    total_sales_len += len(product['items_sold'])
all = total_sales_all/total_sales_len
print(f"Среднее количество продаж: {all}")
