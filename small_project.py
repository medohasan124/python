import functools
class Sale:

    total_sales = 0 


    def __init__(self,product_name,price,quantity):
        self.quantity = quantity
        self.product_name = product_name
        self.price = price
        Sale.total_sales +=  1


    @classmethod
    def get_total_sales_count(cls):
        return f"total count item is - {cls.total_sales}"

    def total_price(self):
        return self.price * self.quantity
    
    @staticmethod
    def apply_discount(price, percentage):
        return price - (price *percentage / 100)
    
sale1 = Sale("milk" , 7,4)
sale2 = Sale("orange" , 3,5)
sale3 = Sale("meet" , 30,1)
sale4 = Sale("chiken" , 20,2)

print(Sale.get_total_sales_count())
print(Sale.apply_discount(100, 10))
    

sales_list = [sale1, sale2, sale3, sale4]

total_price = [i.total_price() for i in sales_list]

morthan20 = [i.total_price() for i in sales_list if i.total_price() > 20]

total = functools.reduce(lambda a,b : a+b,total_price)

print(total_price)

print(morthan20)


print(total)

        
