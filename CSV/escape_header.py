
import csv,os
from pathlib import Path

all_file_names=os.listdir(Path.home() / Path('python/python-basics/csv'))
csv_files=[]
for x in all_file_names:
    x=str(x)
    if '.csv' in x:
        csv_files.append(x)

for x in csv_files:
    file=open(x)
    reader=csv.reader(file)
    new_list=[]
    for line in reader:
        if 'Name' in line:
            continue
        else:
            new_list.append(line)
    
    write_file=open(x,'w')
    writer=csv.writer(write_file)
    writer.writerows(new_list)
    write_file.close()
