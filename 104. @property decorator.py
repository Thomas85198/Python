class Employee:
    def __init__(self):
        self.income = 0
        # self.__tax = 0

    def earn_money(self, money):
        self.income += money
        # self.__tax += self.income * 0.05

    @property
    def tax_amount(self):
        return self.income * 0.05  # 這是虛擬的方法，會產生一個虛擬的變數 tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20  # 這可以去設定他的 tax_amount 虛擬 property


wilson = Employee()
wilson.earn_money(300)
wilson.tax_amount = 200
print(wilson.income)  # tax_amount is not a real property

# tax_amount virtual property is read-only
wilson.earn_money(500)
print(wilson.tax_amount)
