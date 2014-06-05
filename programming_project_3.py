__author__ = 'Joshua'
mph = float(raw_input("Please enter a speed in miles/hour: "))
bar = 4547009.496 * mph
fur = 2688 * mph
mach = 0.00129789357065 * mph
lit = (1.49116539251 ** -9) * mph

print "The original speed in mph is: " + str(mph)
print "Converted to barleycorn/day is: " + str(bar)
print "Converted to furlongs/fortnight is: " + str(fur)
print "Converted to Mach number is: " + str(mach)
print "Converted to the percentage of the speed of light is: " + str(lit)
print "Thanks for playing"