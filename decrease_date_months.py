def decrease_date_months(start_month, value):
    months_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    value=int(value)
    assert start_month.capitalize() in months_list, "Invalid month name was given as parameter."
    assert value > 0, "Cannot decrease month by zero or negative number."
    # months_list[0] ... [11]
    # Find the index in the list of the month with name = start_month
    index = 0
    for i in range(0, len(months_list)):
	if start_month == months_list[i]:
	    index = i
	    break
    assert (index - value) >= 0, "Cannot decrease less than the 1st month."
    month_name = months_list[index - value]
    return month_name

print(decrease_date_months('December',1))
print(decrease_date_months('December',11))
#decrease_date_months('January',1)
#decrease_date_months('jAnUaRy',1)
#decrease_date_months('December',12)
#decrease_date_months('January',0)
#decrease_date_months('January',-1)