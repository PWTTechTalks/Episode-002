import zipfile
import datetime
import os

# This should really be an environmnent variable or  parameter or some such but we will set to midnight yesterday

last_run: datetime = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(1)

# in the interests of not having to type magic strings several times

datapath: str = "c:\\.data"

submissions_file: str = f"{datapath}\\submissions.zip"

submissions: zipfile.PyZipFile = zipfile.PyZipFile(submissions_file)

new_submissions: list = [b for b in submissions.infolist() if datetime.datetime(*b.date_time) > last_run ]

for a  in new_submissions:
    submissions.extract(a.filename, datapath)
    thetime: float = datetime.datetime(*a.date_time).timestamp()
    os.utime(datapath + "\\" + a.filename, (thetime, thetime))
        
print (f'From {len(submissions.infolist())} compressed files we extracted {len(new_submissions)} modified since {last_run}')