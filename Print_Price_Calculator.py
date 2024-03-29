#3D Printing Cost Calculator
#James Rossano
	
class PrintingCost:
	
	def __init__(self):
		pass

	def findCost(self, spoolPrice, printWeight, spoolTotalWeight):
		self.costPerGram = spoolPrice / spoolTotalWeight
		self.printCost = (self.costPerGram * printWeight)
		return round(self.printCost,2)

	def findPrice(self, printCost,markUp,hoursNumber=None,costPerHour=None,bias=None):
		self.bias = bias or 0
		self.hoursNumber = hoursNumber or 0
		self.costPerHour = costPerHour or 1
		self.printPrice = (printCost * markUp) + (self.hoursNumber * self.costPerHour) + self.bias
		return round(self.printPrice,2)

	def twoSpoolCost(self, spool1Price, spool1TotalWeight, spool2Price, spool2TotalWeight, percentSpool1Weight, printWeight):
		self.costPerGram1 = spool1Price / spool1TotalWeight
		self.costPerGram2 = spool2Price / spool2TotalWeight
		self.section1Cost = (self.costPerGram1 * printWeight) * percentSpool1Weight
		self.section2Cost = (self.costPerGram2 * printWeight) * (1 - percentSpool1Weight)
		self.totalCost = self.section1Cost + self.section2Cost
		return round(self.totalCost,2)


