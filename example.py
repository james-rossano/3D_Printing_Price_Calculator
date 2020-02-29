from Print_Price_Calculator import PrintingCost

p1 = PrintingCost()

myCost = p1.findCost(25,15,100)
print(myCost)

myPrice = p1.findPrice(myCost,1.5,6,3)
print(myPrice)

myCost = p1.twoSpoolCost(20,100,60,100,0.3,20)
print(myCost)

myPrice = p1.findPrice(myCost,1.4,12,2,3)
print(myPrice)