# IMPROTANT: don't forget to clear out/0-1 first!
import os
import shutil
from datetime import datetime, timedelta

delta = timedelta(seconds=10)
delta = timedelta(minutes=1)
stime = datetime.strptime("20240415 080000", "%Y%m%d %H%M%S")

for directory in os.listdir('in'):
  directory_path = os.path.join("in", directory)
  if os.path.exists(directory_path) and os.path.isdir(directory_path):
    for filename in os.listdir(directory_path):
      if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        stime += delta
        newname = os.path.join("out", directory_path[-1], f'{stime.strftime("%Y%m%d%H%M%S")}_1.jpg')
        oldname = os.path.join(directory_path, filename)
        shutil.copyfile(oldname, newname)
        print(oldname, '→', newname)
