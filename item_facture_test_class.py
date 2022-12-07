import unittest
from item_facture_class import ItemFacture as item

item = item(5)


class MyTestCase(unittest.TestCase):
    def test_is_quantity_higher_than_0(self):
        self.assertTrue(item.get_quantity() > 0)

    def test_does_item_have_price(self):
        self.assertTrue(item.get_price() > 0)
        self.assertTrue(item.get_price() is not None)

    def test_when_getting_item_price_it_should_return_correct_price(self):
        if item.is_taxable:
            self.assertEqual(115.00, item.get_price())
        else:
            self.assertEqual(100.00, item.get_price())

    def test_if_item_is_taxable(self):
        self.assertEqual(False, item.get_is_taxable())
        item.set_is_taxable(True)
        self.assertEqual(True, item.get_is_taxable())
        item.set_is_taxable(False)

if __name__ == '__main__':
    unittest.main()

