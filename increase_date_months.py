def increase_date_months(start_month, value):
    months_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    value=int(value)
    assert start_month.capitalize() in months_list, "Invalid month name was given as parameter."
    assert value > 0, "Cannot increase month by zero or negative number."
    # months_list[0] ... [11]
    # Find the index in the list of the month with name = start_month
    index = 0
    for i in range(0, len(months_list)):
	if start_month == months_list[i]:
	    index = i
	    break
    # Cannot increase behind the 12th month
    # Index in between 0 and 11 for 12 months
    assert (index + value) <= 11, "Cannot increase more than the 12th month."
    month_name = months_list[index + value]
    return month_name

print(increase_date_months('January',1))
print(increase_date_months('jAnUaRy',1))
print(increase_date_months('January',11))
#increase_date_months('January',12)
#increase_date_months('January',0)
#increase_date_months('January',-1)