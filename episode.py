import zipfile
import datetime
import os

lastrun:datetime = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=1)

datapath: str = "c:\\.data"

submissions_file:str = f'{datapath}\\submissions.zip'

submissions: zipfile.PyZipFile = zipfile.PyZipFile(submissions_file)

new_submissions: list[zipfile.ZipInfo] = [b for b in submissions.infolist() if datetime.datetime(*b.date_time) > lastrun]

for a in new_submissions:
    submissions.extract(a.filename,datapath)
    thetime : float = datetime.datetime(*a.date_time).timestamp()
    os.utime(datapath + "\\" + a.filename, (thetime,thetime))

print("\n\nFrom",len(submissions.infolist()),'compressed files, we extracted',len(new_submissions),'that were modified since', lastrun,'\n\n')