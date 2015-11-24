#!/usr/bin/python3
# This script demonstrates dictionary which is a part of Python programming language.

birthdays = {'Маргарита':'28 март 1960','Румяна':'23 май 1961', 'Красимир':'27 декември' ,'Младен':'25 април 1976','Павлин':'30 юни 1979','Галя':'2 септември 1981', 'Драган':'17 юни 1985','Катерина':'28 октомври 2009','Константин':'29 ноември 2012'}

print('Разпечатва имена')
for i in birthdays.keys():
	print(i)

print('\n')
print('Разпечатва дати')
for j in birthdays.values():
	print(j)

print('\nСмесено отпечатване')
for k in birthdays.items():
	print(k)

