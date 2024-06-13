from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def setUp(self):
        self.burger= Menu.objects.create(
            title = 'Burger', 
            price = '17.50', 
            inventory = '10'
        )

        self.pasta = Menu.objects.create(
            title = 'Pasta', 
            price = '18.20', 
            inventory = '10' 
        )

        self.pizza = Menu.objects.create(
            title = 'Pizza', 
            price = '20.8', 
            inventory = '10', 
        )

    def test_getall(self):
        self.assertEqual(str(self.burger), "Burger : 17.50")
        self.assertEqual(str(self.pasta), "Pasta : 18.20")
        self.assertEqual(str(self.pizza), "Pizza : 20.8")

    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_delete_all(self): 
        Menu.objects.all().delete()
        self.assertEqual(Menu.objects.count(), 0)

