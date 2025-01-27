import shutil,os,re
from pathlib import Path


## MM/DD/YY => DD/MM/YY
pattern=r'^(.*?)((0|1)?[0-9])-([0-3]?[0-9])-(\d{4})(.*?)$'

for filename in os.listdir(Path.home() / Path('python','basic-python-projects','simple_projects','Files','files')):
    search=re.search(pattern,filename)

    if search==None:
        continue

    before_date=search.group(1)
    month=search.group(2)
    day=search.group(4)
    year=search.group(5)
    after_date=search.group(6)
    
    new_file=f'{before_date}{day}-{month}-{year}{after_date}'
    
    old_file=Path.home() / Path('python','basic-python-projects','simple_projects','Files','files') / filename
    new_one=Path.home() / Path('python','basic-python-projects','simple_projects','Files','files') / new_file
    shutil.move(old_file,new_one)
