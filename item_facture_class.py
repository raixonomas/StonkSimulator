class ItemFacture:
    def __init__(self, quantity):
        self.price = 20.00
        self.tax_pcnt = 0.15
        self.is_taxable = False
        self.qty = quantity

    def get_price(self):
        return self.__calculate_price()

    def get_quantity(self):
        return self.qty

    def get_is_taxable(self):
        return self.is_taxable

    def set_is_taxable(self, is_taxable):
        self.is_taxable = is_taxable

    def __calculate_price(self):
        base_price = self.price
        base_price *= self.qty
        if self.is_taxable:
            tax_price = base_price * self.tax_pcnt
            base_price += tax_price
        return base_price
