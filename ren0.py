import os
import shutil
from datetime import datetime, timedelta

delta = timedelta(minutes = 1)
delta = timedelta(seconds = 10)
stime = datetime.strptime("20240220 120343","%Y%m%d %H%M%S")

directory_path = "in"
for filename in os.listdir(directory_path):
  if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
    stime += delta
    newname = os.path.join("out", f'{stime.strftime("%Y%m%d%H%M%S")}_1.jpg')
    oldname = os.path.join(directory_path, filename)
    shutil.copyfile(oldname, newname)
    print(oldname, '→', newname)

