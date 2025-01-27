
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json",scopes)
file = gspread.authorize(credentials)

# file = file.create("A new file sheet")
# file.share("ahmedhelalragab@gmail.com",perm_type="user",role="writer")
# sheet = file.add_worksheet("sheet2",rows="100",cols="20")
# sheet.update('B1',13000)

file = file.open("A new file sheet")

sheet = file.worksheet("sheet2")

# sheet.update([["Ahmed",1000,"2020/02/03"],["Helal",2000,"2023/02/05"]],'A1:c2')
# sheet.update("Sayed",'A1')
sheet.update_cell(1,2,2222)
sheet.update_cell(1,1,"soso")




