"""Classes for melon orders."""

class AbstractMelonOrder():
    shipped = False 

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty

        if country_code:
            self.country_code = country_code


    def get_total(self):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17



    def get_country_code(self):
        """Return the country code."""

        return self.country_code