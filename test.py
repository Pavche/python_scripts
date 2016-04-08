@step(u'{action:w} the datetime {area:w} by {units:d}')
def modify_date(context, action, area, units):
    # Action can be 'increase' or 'decrease'
    # Area can be year, month, day, hour, minute
    # Unit is a positive integer
    # Get the application instance of GNOME control center
    # in order to use its GUI components
    context.app.instance = root.application('gnome-control-center')
    datetime_frame = context.app.instance.child(name='Date & Time', roleName='frame')
    dt_label = datetime_frame.child(name='Date & Time', roleName='label')
    dt_label.click()

    dt_dialog = context.app.instance.child('Date & Time', roleName = 'dialog')
    if area == "year":
	dt_dialog.child(name='Year', roleName='label').labelee.click()
	for i in range(0,units):
	if action == "increase":
	    pressKey('Up')  # Increase its value by pressing 'Up' arrow N times
	if action == "decrease":
	    pressKey('Down')  # Increase its value by pressing 'Up' arrow N times

    if area == "day":
	dt_dialog.child(name='Day', roleName='label').labelee.click()
	for i in range(0,units):
	if action == "increase":
	    pressKey('Up')  # Increase its value by pressing 'Up' arrow N times
	if action == "decrease":
	    pressKey('Down')  # Increase its value by pressing 'Up' arrow N times

    if area == "hour" or area == "minute":
	# Select a spin button to click on - hours or minutes
	if area == "hour":
	    button = dt_dialog.child('Hour')
	if area == "minute":
	    button = dt_dialog.child('Minute')
	if action == "increase":
	    # Click on upper part : [+] of the button
	    x = button.position[0] + 10
	    y = button.position[1] + 10
	if action == "decrease"
	    # Click on lower part : [-] of the button
	    x = button.position[0] + 10
	    y = button.position[1] + button.size[1] - 10
	# How many times to click = number of units
	for i in range(0,units):
	    click(x,y)

    if area == "month":
	month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
	# Get the current month
	date = datetime.date.today()
	current_month = date.month # number between 1 and 12
	if action == "increase":
	    # Add the number of units
	    if (current_month + units) <= 12:
		month_name = month_list[current_month + units - 1]

	if action == "decrease":
	    # Substract the number of units
	    if (current_month - units) >= 1:
		month_name = month_list[current_month - units - 1]

	# Select the month name from the combo box
	combo_box = dt_dialog.child('Month').labelee
	combo_box.click()
	combo_box.child(name=month_name).select() # Select a menu item from combo box with month name
	sleep(1)
	pressKey('Enter')