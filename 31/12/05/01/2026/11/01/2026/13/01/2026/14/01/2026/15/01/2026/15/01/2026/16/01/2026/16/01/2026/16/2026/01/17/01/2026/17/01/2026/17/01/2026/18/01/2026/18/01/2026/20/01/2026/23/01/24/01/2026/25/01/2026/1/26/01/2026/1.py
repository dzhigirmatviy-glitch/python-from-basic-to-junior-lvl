class FruitBasket:
    def __init__(self, owner):
        print(f"created for {owner}")
        self.owner = owner
        self.fruits = []

    def add_fruit(self, fruit_name):
        self.fruits.append(fruit_name)
        print(f"added: {fruit_name} for {self.owner}")

    def show_basket(self):
        print(f"basket {self.owner}: {self.fruits}")

my_basket = FruitBasket("Maria")
friend_basket = FruitBasket("Petya")

my_basket.add_fruit("Apple")
my_basket.add_fruit("Orange")
friend_basket.add_fruit("banan")

my_basket.show_basket()
friend_basket.show_basket()