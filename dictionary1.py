#!/usr/bin/python3
# This script demonstrates dictionary which is a part of Python programming language.

birthdays = {'Маргарита':'28 март 1960','Румяна':'23 май 1961', 'Красимир':'27 декември' ,'Младен':'25 април 1976','Павлин':'30 юни 1979','Галя':'2 септември 1981', 'Драган':'17 юни 1985','Катерина':'28 октомври 2009','Константин':'29 ноември 2012'}

while True:
	print('Въведи име: (празен ред за край)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' е рождения ден на ' + name)
	else:
		print('Няма информация за рождения ден на ' + name)
		print('Какъв е неговия/нейния рожден ден?')
		bday = input()
		birthdays[name] = bday
		print('Базата от рождени дни бе допълнена.')
