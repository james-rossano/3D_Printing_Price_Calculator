# 3D_Printing_Price_Calculator

This library takes in your 3D printing specifications and preferences and returns a accurate cost and selling point of your print.
* Finds cost of print
* Finds selling price of print
* Finds cost of dual filament prints

## Code

Find material cost of print <br>
`p1 = PrintingCost()`<br>
`p1.findCost(spoolPrice, printWeight, spoolTotalWeight)`

Find the selling price of print via markup and printer work time <br>
`p1.findPrice(printCost, markUp, hoursNumber=None, costPerHour=None, bias=None)`

Find cost of print with two filament via a percent makeup of one of the filaments <br>
`p1.twoSpoolCost(spool1Price, spool1TotalWeight, spool2Price, spool2TotalWeight, percentSpool1Weight, printWeight)`
