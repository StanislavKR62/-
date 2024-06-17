import datetime
date = datetime.date.today()
weeks = {
'1':'Monday',
'2':'Tuesday',
'3':'Wednesday',
'4':'Thursday',
'5':'Friday',
'6':'Saturday',
'7':'Sunday',
}
#print(weeks['0'])
print(weeks[str(date.weekday())])