#!/usr/bin/python
# This script calculates the price of travelling
# by car from CZ,Brno to BG,Varna

bg_varna_facebook_url='https://www.facebook.com/krasivavarna/photos'
bg_varna_map_url='https://www.google.cz/maps/place/Varna,+Bulharsko/@43.2047556,27.8028249,6z/data=!4m2!3m1!1s0x40a4538baaf3d7a1:0x5727941c71a58b7c?hl=cs'
route_brno_bratislava_budapest_arad_varna_url='https://mapy.cz/zakladni?planovani-trasy&x=22.2552947&y=45.7653096&z=7&rc=9mMT8xTuNNuMTSawrsjA&rs=muni&rs=osmm&ri=5740&ri=57908&mrp={%22c%22%3A1%2C%22tt%22%3A1}&mrp={%22c%22%3A1%2C%22tt%22%3A1}&rt=&rt='
route_str='CZ(Brno)\nSK(Bratislava)\nHU(Budapest)\nRO(Arad)\nRO(Bucarest)\nBG(Varna)'

# Vignettes and road taxes
# Country(BG,CZ,RO,SK), period (1 week, 1 month, 1 year)
# Prices are for 2016 in EUR and some of them are approximate
road_taxes = {
	'CZ-1m'  : 17,
	'SK-1m'  : 14, 
	'HU-1m'  : 16, 
	'RO-1m'  : 7,
	'BG-1m'  : 15 
		}
road_taxes_total = 0
currency = 'EUR'
for country, price in road_taxes.iteritems():
    road_taxes_total += price

# For every car is different
# This is for Hyundai i30 cw
avg_fuel_consum = {
    'petrol' : 7, # Litters/100 km
    'gas' : 9, # Litters/100 km
    'diesel' : 6 # Litters/100 km
    }
fuel_price = { # EUR for 1 litter and prices are variable
    'petrol' : 1.04,
    'gas' : 0.44,
    'diesel' : 1.00
    }
# Travel distance Brno - Varna
distance = 1413 # km

# User interface
# ------------------------------------------------------------------------
print("Travelling by car\n")
print("Route:\n%s\n" % route_str)

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
fuel_consum_total = ( distance * (avg_fuel_consum[fuel_type]/100.00) ) * 2 

print("Road taxes (all) : %s %s" % \
    (road_taxes_total, currency) )
print("Travel distance  : %s km in both directions" % (2*distance) )
print("Fuel consumption : %s [L/100 km] of %s average" % \
    (avg_fuel_consum[fuel_type], fuel_type) )
print("Fuel consumption : %s L of %s total" % \
    (fuel_consum_total, fuel_type) )
print("Fuel price       : %s %s" % \
    ( round((fuel_consum_total * fuel_price[fuel_type]), 2), currency ) )
