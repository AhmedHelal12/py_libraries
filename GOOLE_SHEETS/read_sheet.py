
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scopes)
file = gspread.authorize(credentials)
sheet = file.open("my_sheet")
sheet.update_cell(2,1,"Hello World Again!")

sheet = file.open_by_url('https://docs.google.com/spreadsheets/d/1jMmPHgd4mjRMOFo9ANdKP0qmILCiQdCUwn1NcTg4zgo/edit?usp=drive_link')
sheet1 = sheet.get_worksheet(0)
sheet2 = sheet.worksheet("sheet2")
sheets = sheet.worksheets()
# print(sheet1)
# print(sheet2)
# print(sheets)

print(sheet1.acell("A1").value)
print(sheet1.acell("A3").value)
print(sheet1.cell(1,3).value)

print(sheet1.row_values(2))
print(sheet1.col_values(2))
print(sheet1.get_all_values())
print(sheet1.get_all_records())


