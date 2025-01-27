
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scopes)
file = gspread.authorize(credentials)
sheet = file.open("my_sheet").sheet1

employees = re.compile("Ahmed|Helal")
print(sheet.findall(employees))
print(sheet.find("Ahmed"))
print(sheet.findall("Ahmed"))
sheet.batch_clear(["A3:C3"])
sheet.clear()

sheet.update_acell(8,2,"=SUM(B2:B7)")
cell = sheet.acell("B8",value_render_option="FORMULA").value
print(cell)