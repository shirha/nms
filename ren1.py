# IMPROTANT: don't forget to clear out/0-1 first!
import os
import re
import shutil
from datetime import datetime, timedelta

delta = timedelta(seconds=10)
delta = timedelta(minutes=1)
stime = datetime.strptime("20240427 080000", "%Y%m%d %H%M%S")

# delete jpgs from 'out'
for i in range(2):
  filelist = [ f for f in os.listdir(os.path.join('out', str(i))) if f.endswith(".jpg") ]
  for f in filelist:
      os.remove(os.path.join('out', str(i), f))

# copy 'in' to 'out' using last char of 'in' i.e. in/31 -> out/1
for directory in filter(lambda d: re.match(r'^\d\d$', d), os.listdir('in')):
  directory_path = os.path.join("in", directory)
  if os.path.exists(directory_path) and os.path.isdir(directory_path):
    for filename in os.listdir(directory_path):
      if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        stime += delta
        newname = os.path.join("out", directory_path[-1], f'{stime.strftime("%Y%m%d%H%M%S")}_1.jpg')
        oldname = os.path.join(directory_path, filename)
        shutil.copyfile(oldname, newname)
        print(oldname, '→', newname)
