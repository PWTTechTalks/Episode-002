# PWT Tech Talk Episode 2 - unzipping with python

## intro

today we are going to show how to selectively extract files from a zip file using very basic python.

This is a common task if you have zipfiles with hundreds of thousands of compressed files in them and you really don't want to .

so of course first we get our imports out of the way

## import zipfile

we are dealing with zipped files

## import datetime

and timestamps

## import os

and some low level file system stuff
 e.timedelta(days=1)

Our premise is that we want to get all of the files that were last modified since midnight yesterday. TO do this we replace the time-parts of the current time with 0 and then go back in time by one day.  

## datapath: str = "c:\\.data"

Just to keep us from having to type this finger twister over again

## submissions_file:str = f'{datapath}\\submissions.zip'

and here is where our zip file is. It is a list of all electronic submissions to the SEC. it is refreshed every night, is just over a GB in size and has about 850,000 compressed files inside.


## submissions: zipfile.PyZipFile = zipfile.PyZipFile(submissions_file)

let's just create the variable for the zipfile itself

## new_submissions: list[zipfile.ZipInfo] = [b for b in submissions.infolist() if datetime.datetime(*b.date_time) > lastrun]

and here is the meat of the script
we are going to get the "zipinfo" objects for each of the compressed files that has a last modified date_time greater than the last time this was run

## for a in new_submissions

notice I am just going to use a basic for loop for this. I could have had a nifty nested comprehensionadded to what we did above  but it didnt save any appreciable runtime and made the code MUCH harder to understand (imho anyway)

## submissions.extract(a.filename,datapath)

<-- we are here -->
so extract the file to the correct location

## thetime : float = datetime.datetime(*a.date_time).timestamp()

figure out the last modified date for the file.
We turn it into a timestamp (basically just seconds since the unix beginning of time) because that is what

## os.utime(datapath + "\\" + a.filename, (thetime,thetime))

utime needs. Utime allows you to change the last accessed and/or the last modified dates on an existing file so there is a SMALL window of time where this file exists with today's date rather than the one we want. we are assuming today that it doesnt matter.

## print("\n\nFrom",len(submissions.infolist()),'compressed files, we extracted',len(new_submissions),'that were modified since', lastrun,'\n\n')

and we  would normally do something more interesting at this point but we will just shout out that we only had to extract a small number of the files that we found

## outro

and that is it for today!

Like and subscribe and leave us a comment down below to help us choose what other topics we should cover

See you on Wrightsville Beach!
