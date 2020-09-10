#!/usr/bin/env python3
""" fixphotodates: Fixes the dates for photos without them if they have dates in the Photos library """
import csv
import osxphotos
import os

class myPhoto:
    def __init__(self, p):
        self.datetime = p.date
        self.filename = p.original_filename
        self.date = self.datetime.strftime('%Y-%m-%d')

# Now, get the files from the photo library
print('getting photos...this may take a bit!')
photosdb = osxphotos.PhotosDB()
photos = photosdb.photos()
print('processing')
ourphotos = {}
for item in photos:
    photo = myPhoto(item)
    if photo.date not in ourphotos:
        ourphotos[photo.date] = []
    ourphotos[photo.date].append(photo)

# OK, let's create a CSV for each day to feed exiftool
for date in sorted(ourphotos.keys()):
    print(date)
    preface = f'/Volumes/DSS_Photos/holding/{date[0:4]}/{date}'
    with open(f'{date}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(('SourceFile', 'AllDates'))
        for p in ourphotos[date]:
            writer.writerow((os.path.join(preface,p.filename), p.datetime.strftime('%Y-%m-%dT%H:%M:%S%z')))
