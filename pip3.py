from inspect import currentframe, getframeinfo
import os
import sys
import json
import cv2
import re
import pipm3 as m
# import glob
import getopt
import time

class_set = set()
title = "Playground"
dbug = ""
ilog = title # '0'
argv = sys.argv[1:] 

try: 
  opts, args = getopt.getopt(argv, "f:t:d:", ["file =", "title =", "dbug ="]) 
except: 
# -d a=all,i=sysinfo,g=glyph,t=techology,r=resource,v=visited,s=stellar
  print("SYNTAX: python pipj.py -f 0|1|2|t -t title -d aigtrvs") 
for opt, arg in opts: 
  if opt in ['-f', '--file']: 
    ilog = arg 
  elif opt in ['-t', '--title']: 
    title = arg 
  elif opt in ['-d', '--dbug']: 
    dbug = arg 
    if 'a' in dbug: 
      dbug = 'igtrvs'

# if ilog == '0' or ilog == 't':
db = {} # {"Apporo II": {'System Info':[],'Technology':{},'Buy Sell':{}}}
# else:
#   with open(f'pip{int(ilog) - 1}.json', "r") as infile: 
#     db = json.load(infile)

m.log(ilog,f'argv={argv} ilog={ilog} title={title} dbug={dbug}')
if argv:
  # print(argv)
  assert argv[0].startswith('-'), "SYNTAX: python pipj.py -f 0|1|2|t -t title -d aigtrv"

sysflag = False
station = None
beg_time = time.perf_counter()
dirs = {
  "Playground": ["normal/playground"],
  "Expeditions": ["expeditions"],
  "Voyagers": ["expeditions/expeditions11 voyagers 2k","normal/playground"],
  "Frontiers": ["normal/frontiers1"],
  "Redux6": ["expeditions/expeditions6 redux"],
  "Orbital": ["normal/normal8 orbital"],
  "Omega": ["expeditions/expeditions12 omega"],
}

for dir in dirs[title]: 
  for root, dirs, files in os.walk("/Downloads/No Man's Sky/" + dir):
    if re.search('voyagers', root): continue
    parts = root.split(os.sep)
    # print(parts,os.path.basename(root))
    if re.match(r'^\d$', os.path.basename(root)) and parts[-2] == 'py': 
  # if re.match(r'^\.\\\d$', root): # .\0 or .\1
      for file in files:
        path = f'{parts[-1]}/{file}'
        large_image = cv2.imread(os.path.join(root,file), cv2.IMREAD_GRAYSCALE)
#
# IMPORTANT: screenshots MUST be 1080 x 1920 or-else raise Exception("station is None!")
#

# for path in glob.glob(f'{ilog}/*.jpg'):
#         large_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        # if re.search(r'20240220131034',path): dbug = 'r'
        m.log(ilog,f'\n{os.path.join(root,file)}')

        ret,res = m.isSysInfo(path,dbug,ilog,db,large_image)
        if ret: 
          if res is not None:
            station = res
            sysflag = True
          continue

        if not sysflag:
          ret,res,sys = m.isVisited2(path,dbug,ilog,db,large_image,station)
          if ret:
            if res is not None:
              station = res
              m.log(ilog,f'{getframeinfo(currentframe()).lineno} Visited: exiting... {ret,res,sys}')

              if sys:
                sysflag = True
            continue

        if sysflag:
          sysflag = False
          ret = m.isGlyphs(path,dbug,ilog,db,large_image,station)
          if ret:
            continue

        if station is None: 
          raise Exception("station is None!")

        ret = m.isTechno(path,dbug,ilog,db,large_image,station,class_set)
        if ret: 
          continue

        ret = m.isResource(path,dbug,ilog,db,large_image,station)
        if ret:
          continue

        ret = m.isStellar(path,dbug,ilog,db,large_image,station)

data = json.dumps(db, indent = 2)
with open(f'{title}.json', 'w') as outfile:
  outfile.write(data)

m.log(ilog,f'\n{data}\n')
m.log(ilog,f'elasped time: {time.perf_counter() - beg_time:.1f}\nclass_set: {class_set}\n')
m.log(ilog) # close

import subprocess
subprocess.run(["python", "pipj.py", "-f", str(ilog), "-t", title])
