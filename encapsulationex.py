# 1.Shopping cart
print("--------------Shopping Card----------------")
class ShoppingCart:
    def __init__(self,cartId,total):
        self.__cartId=cartId
        self.__total=total
    def getcartId(self):
        return self.__cartId
    def gettotal(self):
        return self.__total
    def setcartId(self,cartId):
        self.__cartId = cartId
    def addProduct(self,price):
        self.__total = self.__total + price
        return self.__total
    def removeProduct(self,price):
        if self.__total >= price:
            self.__total = self.__total - price
            return self.__total
        else:
            return "Invalid Amount"
cart = ShoppingCart(1001,2500)
print("Before")
print("Cart Id: ",cart.getcartId())
print("Total: ",cart.getcartId())
# update
print("After adding Product :",cart.addProduct(1000))
print("After removing Product:",cart.removeProduct(500))

print("After")
print("Cart Id:",cart.getcartId())
print("Total:",cart.gettotal())


# Example 2:
print("--------ATM Example---------------")
class ATM:
    def __init__(self,cardNo,pin,balance):
        self.__cardNo = cardNo
        self.__pin = pin
        self.__balance = balance
    def getCardNo(self):
        return self.__cardNo
    def getBalance(self):
        return self.__balance
    def setpin(self,pin):
        self.__pin = pin
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return self.__balance
        else:
            return "Insufficient Balance"
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
atm = ATM(123456,1234,50000)

print("Before")
print("Card No:",atm.getCardNo())
print("Balance:",atm.getBalance())

# update
print("withdraw:",atm.withdraw(60000))

print("After")
print("Card No:",atm.getCardNo())
print("Balance:",atm.getBalance())