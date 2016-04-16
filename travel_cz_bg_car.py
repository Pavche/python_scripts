#!/usr/bin/python
# This script calculates the price of travelling
# by car from CZ,Brno to BG,Varna
import os, subprocess
import time

# Burgas on the map
googles_map_url='https://www.google.cz/maps/place/Burgas,+Bulharsko/@44.2665119,19.5417992,6z/data=!4m2!3m1!1s0x40a69266f9fc9d91:0x400a01269bf4df0?hl=cs'
# Route Brno-Bratislava-Budapest-Belgrade-Sofia-Burgas
route_url='https://www.google.cz/maps/dir/Brno/Burgas,+Bulharsko/@45.6055514,16.9457368,6z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x4712943ac03f5111:0x400af0f6614b1b0!2m2!1d16.6068371!2d49.1950602!1m5!1m1!1s0x40a69266f9fc9d91:0x400a01269bf4df0!2m2!1d27.4626361!2d42.5047926?hl=cs'
route_str='Brno,CZ\nBratislava,SK\nBudapest,HU\nBelgrade,SRB\nSofia,BG\nBurgas,BG'

# Vignettes and road taxes
# Countries: CZ,SK,HU,BG period: 1 month
# In Serbia you pay per highway (about 20 Eur in both directions)
# Prices are for 2016 in EUR and some of them are approximate
road_taxes = {
	'CZ-1m'  : 17,
	'SK-1m'  : 14,
	'HU-1m'  : 16,
	'BG-1m'  : 15
		}
total_road_taxes = 20 # Initial value considering taxes in Serbia
currency = 'EUR'
for country, price in road_taxes.iteritems():
    total_road_taxes += price

# For every car is different
# This is for Hyundai i30 cw
avg_fuel_consum = {
    'petrol' : 7, # Litters/100 km
    'gas' : 10, # Litters/100 km
    'diesel' : 6 # Litters/100 km
    }
fuel_price = { # EUR for 1 litter and prices are variable
    'petrol' : 1.04,
    'gas' : 0.44,
    'diesel' : 1.00
    }
# Travel distance Brno - Burgas
distance = 1470 # km

# User interface
# ------------------------------------------------------------------------
os.system('clear') # Clear screen in Linux
print("TRAVELLING FROM BRNO TO BURGAS BY CAR\n")
print("Route:\n%s" % route_str)
print("and RETURN.\n")

# Ask for fuel type
choice = 0
fuel_type = 'None'
while True:
    print("Select your fuel type:\n1) petrol\n2) gas\n3) diesel")
    try:
        choice = int(raw_input("Choice: "))
        if choice in range(1,4):
            if choice == 1:
                fuel_type = 'petrol'
            if choice == 2:
                fuel_type = 'gas'
            if choice == 3:
                fuel_type = 'diesel'
            # Stop choosing
            break
        else:
            print 'Invalid choice.'
    except ValueError:
        print 'Invalid choice.'

# Ask for avg fuel consumption [L/100 km]
# Ask for fuel price
# Both directions
total_fuel_consum = ( distance * (avg_fuel_consum[fuel_type]/100.00) ) * 2

print("Road taxes (all)         : %s %s" % \
    (total_road_taxes, currency) )
print("Travel distance          : %s km in both directions" % (2*distance) )
print("Average fuel consumption : %s [L/100 km] of %s" % \
    (avg_fuel_consum[fuel_type], fuel_type) )
print("Total fuel consumption   : %s L of %s" % \
    (total_fuel_consum, fuel_type) )
total_fuel_price = round((total_fuel_consum * fuel_price[fuel_type]), 2)
print("Fuel price               : %s %s" % \
    ( total_fuel_price, currency ) )
print("Total cost               : %s %s" % ( (total_fuel_price+total_road_taxes),currency) )
