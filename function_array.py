def increase_time_minutes():
    print("Increasing the minutes")

def increase_time_hours():
    print("Increasing the hours")

def increase_date_day():
    print("Increasing the days")

def increase_date_months():
    print("Increasing the months")

def increase_date_year():
    print("Increasing the years")

options = {
    'minutes': increase_time_minutes(),
    'hours': increase_time_hours(),
    'days' : increase_date_day(),
    'months' : increase_date_months(),
    'years': increase_date_year(),
    }
time_units='months'
# Invoke the function
print(options['months'])