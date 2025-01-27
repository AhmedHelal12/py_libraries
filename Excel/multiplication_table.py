
from pathlib import Path
import sys,openpyxl
from openpyxl.styles import Font

if len(sys.argv)==2:
    
    try:
        number=int(sys.argv[1])
    except Exception as e:
        print(e)
    
    n=0
    excel_file=openpyxl.Workbook()
    sheet=excel_file.active
    

    for x in range(number+1):
        for y in range(number+1):
            isheader=False

            if x==0 and y==0:
                isheader=True
                n=''
            elif x==0:
                n=y
                isheader=True
            elif y==0:
                n=x
                isheader=True
            
            else:
                n=x*y

            cell=sheet.cell(row=x+1,column=y+1)            
            
            if isheader:
                cell.font=Font(bold=True)
            
            cell.value=n
    
    file=Path.home() / Path('Desktop') / 'mul.xlsx'
    excel_file.save(file)


else:
    print('Please enter two arguments')