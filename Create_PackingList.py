import openpyxl
from openpyxl import Workbook, load_workbook

book = load_workbook('empty packinglist.xlsx')
sheet  = book.active

print(sheet['H7'].value)

sheet['H7'].value = 'Prejj'

book.save('empty packinglist.xlsx')
print(sheet['H7'].value)
