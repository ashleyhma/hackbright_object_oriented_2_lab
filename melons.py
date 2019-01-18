"""Classes for melon orders."""

class AbstractMelonOrder():


    def __init__(self, species, qty, country_code = None, fee = None):
        self.species = species
        self.qty = qty
        self.shipped = False

        if qty < 10: 
            self.fee = 3.00
        elif qty >= 10:
            self.fee = 0

        if country_code:
            self.country_code = country_code


    def get_total(self):
        base_price = 5
        total = ((1 + self.tax) * self.qty * (1.5 * base_price)) + self.fee

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
