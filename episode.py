import zipfile
import datetime
import os


last_run: datetime = datetime.datetime.now() - datetime.timedelta(4)

datapath: str =  f'{os.curdir}\\.data'

submissions_file: str = f"{datapath}\\submissions.zip"

submissions = zipfile.PyZipFile(submissions_file)

submissions_extracted = [
    submissions.extract(a, datapath)
    for a in submissions.infolist()
    if datetime.datetime(*a.date_time) > last_run
]
