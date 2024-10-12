class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.weight} - {self.category}"


class Shop:
    __file_name = 'products.txt'
    def get_products(self):

        try:
            with open(self.__file_name, 'r', encoding='utf-8', errors='replace') as file:
                products = file.read()
            return products
        except FileNotFoundError:
            return 'Файл не найден. Продукты отсутствуют.'
    def add(self, *products):
        existing_products = self.get_products()

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a', encoding='utf-8') as file:
                    file.write(f'{product}\n')
                    print(f'Продукт {product.name} добавлен в магазин.')









s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')


s1.add(p1, p2, p3)

print(s1.get_products())