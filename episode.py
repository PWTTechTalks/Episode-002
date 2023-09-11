import zipfile
import datetime
import os
import time

# normally this would be "yesterday" -- timedelta(1) but since this was recorded on a monday ... 
last_run: datetime = datetime.datetime.now() - datetime.timedelta(2)

datapath: str = "c:\\.data"

submissions_file: str = f"{datapath}\\submissions.zip"

submissions = zipfile.PyZipFile(submissions_file)

# important to understand the order of execution
# the extract happens BEFORE the time gets set even though from the order in the file it looks like 
# we set the time before we extract the file
# if you find this confusing you can do a standard for loop but comprehensions are often faster
start = time.time()
[
    os.utime(b[0], (b[1], b[1]))
    for b in [
        (submissions.extract(a, datapath), datetime.datetime(*a.date_time).timestamp())
        for a in submissions.infolist()
        if datetime.datetime(*a.date_time) > last_run
    ]
]
end = time.time()
print (end-start)

start = time.time()

for c in submissions.infolist() :
    if datetime.datetime(*c.date_time) > last_run:
        thetime = datetime.datetime(*c.date_time).timestamp()
        os.utime(submissions.extract(c,datapath),(thetime,thetime))

end = time.time()
print (end-start)
        
    