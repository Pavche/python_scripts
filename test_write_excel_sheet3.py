# Create an Excel workbook with one sheet
# It contains 9 fields (columns)
# 1st - Location
# 2nd - Host name
# 3rd - IP address
# 4th - MAC address
# 5th - VLAN
# 6th - Switch name
# 7th - Port name
# On row No.5 all cells have bold and italic font, aligment_horiz=Center, aligment_vert=Center

import openpyxl

XLSX_FILE='/home/georgiev/test_host_list.xlsx'
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Host list"

header=['Location','Host name','IP address','MAC address','VLAN','Switch name','Port name']
col=1
for caption in header:
    ws.cell(row=5,column=col).value = caption
    col+=1

wb.save(XLSX_FILE)
print 'Excel workbook '+XLSX_FILE+' was created.'
