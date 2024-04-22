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

# file={
#  r'0\20240415080100_1.jpg':
#   {'msg':'''SysInfo: entering...
# 322 SysInfo: mn=0.002 (9, 9) crop.shape=(135, 535)
# SysInfo: station= Dorigue VII
# Celestial Bodies: 5 Planets
# Dominant Lifeform: Korvax
# Economy: Construction // Flourishing
# Conflict level: Stable
# 353 fix: Dorigue VII, Doriguc VII''',
# 'pos':[40,10]},

#  r'0\20240415080200_1.jpg':
# {'msg':'''SysInfo: entering...
# Glyphs: entering... Doriguc VII
# Glyphs: e:0 106202900054''',
# 'pos':[40,10]},

#  r'0\20240415080300_1.jpg':
# {'msg':'''SysInfo: entering...
# Visited: entering... Doriguc VII
# 437 Techno: entering... Doriguc VII
# 445 Techno: avail1: mn=0.002 (145, 39)
# 485 Techno: System : mn=0.017,MPy=5,MPx=22
# 563 Techno: Non-Stick Piston+ 
# 563 Techno: Enormous Metal Cog+ 
# 563 Techno: Mesh Decouplers+ 
# 563 Techno: Holographic Crankshaft+ 
# 563 Techno: Vector Compressors+ 
# 563 Techno: Cobalt''',
# 'pos':[40,10]},

#  r'1\20240415082100_1.jpg':
# {'msg':'''SysInfo: entering...
# Visited: entering... Mazuna
# 806 Visited: Set System: "Doriguc VII" -no card-
# 90 Visited: exiting... (True, 'Doriguc VII', False)''',
# 'pos':[40,10]},
#  r'1\20240415082200_1.jpg':
# {'msg':'''SysInfo: entering...
# Visited: entering... Doriguc VII
# 437 Techno: entering... Doriguc VII
# 448 Techno: avail2: mn=1.000 (0, 0)
# 584 Resource: entering... Doriguc VII
# 598 Resource: resrc1: 0.007 (12, 14)
# 631 Resource: s=Doriguc VII, i=1, p= "Tonda 93/P4"
# 650 Resource: profile= Weather: Infrequent Blizzards
# 650 Resource: profile= Sentinels: Low
# 650 Resource: profile= Flora: Ample
# 650 Resource: profile= Fauna: Rich
# 682 Resource: 0.555 resource= Frost Crystal 
# 682 Resource: 0.520 resource= Silver 
# 682 Resource: 0.468 resource= Dioxite 
# 682 Resource: 0.452 resource= Copper''',
# 'pos':[40,10]},

#  r'1\20240415082300_1.jpg':
# {'msg':'''SysInfo: entering...
# Visited: entering... Doriguc VII
# 437 Techno: entering... Doriguc VII
# 448 Techno: avail2: mn=1.000 (0, 0)
# 584 Resource: entering... Doriguc VII
# 598 Resource: resrc1: 0.007 (12, 14)
# 631 Resource: s=Doriguc VII, i=2, p= "Hats 43/L7"
# 650 Resource: profile= Weather: Perfectly Clear
# 650 Resource: profile= Sentinels: Observant
# 650 Resource: profile= Flora: Lacking
# 650 Resource: profile= Fauna: Undetected
# 682 Resource: 0.417 resource= Sodium 
# 682 Resource: 0.532 resource= Rusted Metal 
# 682 Resource: 0.475 resource= Copper''',
# 'pos':[40,10]}
# }

# print(json.dumps(file,indent=3))
# quit()

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
  "Normal9": ["normal/normal9"],
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
