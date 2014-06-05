__author__ = 'Joshua'
gal = float(raw_input("Please enter the number of gallons of gasoline: "))
lit = 3.7854 * gal
oil = 0.0512820512821 * gal
co2 = 20 * gal
eth = 1.51915455746 * gal
dol = 4 * gal

print "Original number of gallons is: " + str(gal)
print str(gal) + " gallons is the equivalent of " + str(lit) + " liters"
print str(gal) + " gallons of gasoline requires " + str(oil) + " barrels of oil"
print str(gal) + " gallons of gasoline produces " + str(co2) + " pounds of CO2"
print str(gal) + " gallons of gasoline is energy equivalent to " + str(eth) + " gallons of ethanol"
print str(gal) + " gallons of gasoline requires " + str(dol) + " US dollars"
print "Thanks for playing"

