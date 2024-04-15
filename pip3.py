from inspect import currentframe, getframeinfo
import os
import sys
import json
import cv2
import re
import pipm3 as m
import glob
import getopt
import time

class_set = set()
ilog = '0'
title = 'Playground'
dbug = ''
argv = sys.argv[1:] 

try: 
  opts, args = getopt.getopt(argv, "f:t:d:", ["file =", "title =", "dbug ="]) 
except: 
# -d a=all,i=sysinfo,g=glyph,t=techology,r=resource,v=visited
  print("SYNTAX: python pipj.py -f 0|1|2|t -t title -d aigtrv") 
for opt, arg in opts: 
  if opt in ['-f', '--file']: 
    ilog = arg 
  elif opt in ['-t', '--title']: 
    title = arg 
  elif opt in ['-d', '--dbug']: 
    dbug = arg 
    if 'a' in dbug: 
      dbug = 'igtrv'

if ilog == '0' or ilog == 't':
  db = {}
else:
  with open(f'pip{int(ilog) - 1}.json', "r") as infile: 
    db = json.load(infile)

m.log(ilog,f'argv={argv} ilog={ilog} title={title} dbug={dbug}')
if argv:
  # print(argv)
  assert argv[0].startswith('-'), "SYNTAX: python pipj.py -f 0|1|2|t -t title -d aigtrv"

sysflag = False
station = None
beg_time = time.perf_counter()

#, "expeditions\\expeditions11 voyagers" 2K
dirs = ["normal\\normal8 orbital", "normal\\frontiers1", "normal\\normal5", "expeditions\\expeditions4", "normal\\normal6", "expeditions\\expeditions1 redux", "expeditions\\expeditions2 redux", "expeditions\\expeditions5 exobiology", "expeditions\\expeditions6 blighted", "expeditions\\expeditions7 leviathan", "expeditions\\expeditions8 polestar", "expeditions\\expeditions5 redux", "expeditions\\expeditions6 redux", "expeditions\\expeditions7 redux", "expeditions\\expeditions8 redux", "normal\\normal7", "expeditions\\expeditions9 utopia", "expeditions\\expeditions10 sigularity", "expeditions\\expeditions12 omega", "normal\\normal9", "derelict-restapi"] 

for dir in ["normal\\normal9"]: #["normal\\normal8 orbital"]: #["normal\\frontiers1"]: #["expeditions\\expeditions12 omega"]: #["normal\\playground"]: #['expeditions\\expeditions7 redux']: #['expeditions\\expeditions6 redux']: #['normal\\normal8 orbital']: #['expeditions\\expeditions6 redux']: #["expeditions\\expeditions5 exobiology"]: #["normal\\frontiers1"]: #['normal\\playground']: #dirs: #filter(lambda x: title.lower() in x, dirs): # ["normal\\playground"]: #["derelict-restapi"]: #["normal\\normal9"]: #["normal\\playground"]: #["expeditions\\expeditions12 omega"]: #["normal\\normal8 omega"]: #['derelict-restapi']: #["normal\\normal9"]: #["expeditions\\expeditions9 utopia"]:  #dirs: #['orbital']: #["expeditions\\expeditions10 sigularity"]: #["normal\\normal8 orbital"]: 
  for root, dirs, files in os.walk("\\Downloads\\No Man's Sky\\" + dir):
    parts = root.split(os.sep)
    if re.match(r'^\d$', os.path.basename(root)) and parts[-2] == 'py':
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

with open(f'pip{ilog}.json', 'w') as outfile:
  outfile.write(json.dumps(db, indent = 2))
  # json.dump(db, outfile)
m.log(ilog,f'\n{json.dumps(db, indent = 2)}\n')
m.log(ilog,f'elasped time: {time.perf_counter() - beg_time:.1f}\nclass_set: {class_set}\n')
m.log(ilog) # close

import subprocess
subprocess.run(["python", "pipj.py", "-f", str(ilog), "-t", title])
