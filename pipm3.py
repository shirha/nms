# type pip0.json | python -m json.tool
# https://www.w3schools.com/colors/colors_picker.asp
# https://giggster.com/guide/complementary-colors/
#
from inspect import currentframe, getframeinfo
import imutils
# import pprint
# pp = pprint.PrettyPrinter(indent=2)
import json
import sys
import os
import re
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\shirha\miniforge3\envs\opencv\Library\bin\tesseract.exe'

stripe = lambda s: "".join(i for i in s if 31 < ord(i) < 127)

def stripped(thresh,ilog,lineno):
  text = pytesseract.image_to_string(thresh)
  text = stripe(text)
  text = re.sub(r'[ |_.;]+$','',text)
  text = fn_fix(ilog,lineno,text)
  return text

def fn_fix(ilog, lineno, text):
  if text in fix:
    log(ilog,f'{lineno} fix: {text}, {fix[text]}')
    return fix[text]
  return text

# https://www.geeksforgeeks.org/python-addition-of-tuples/
def addPt(p1, p2): tuple(map(lambda i, j: i + j, p1, p2))

# this = sys.modules[__name__]
logfile = None
system_index = 0
planet_index = 0

work_image  = np.full((500,600),240,dtype='uint8')
const_image = {}
for image in [
    "mask","system","technol","salvage","contrab","avail1","avail2","small",
    "card","snow","glyph", "visit1","visit2", "steam1","steam2","xboxx",
    "sicon","bicon","icons","resrc1","resrc2","salt","guide","trade1","trade2"]: 
  const_image[image] = cv2.imread(f'i/{image}_image.png', cv2.IMREAD_GRAYSCALE)

# def log(n, *args):
#   global logfile
#   if logfile is None:
#     if os.path.exists(f'log{n}.txt'):
#       os.remove(f'log{n}.txt')
#     logfile = open(f'log{n}.txt', 'a')

def log(n, *args):
  global logfile
  if logfile is None:
    if os.path.exists(f'{n}.log'):
      os.remove(f'{n}.log')
    logfile = open(f'{n}.log', 'a')

  if(len(args)):
    print(args[0])
    logfile.write(args[0] + "\n")
  else:
    if logfile is not None:
      logfile.close()
      logfile = None
      print(f'log{n} closed')

si = [["Celestial Bodies ","Celestial Bodies: "],
      ["Dominant Lifeform ","Dominant Lifeform: "],
      ["Economy ","Economy: "],
      ["Conflict level ","Conflict level: "],
      ["vy'keen","Vy'keen"],
      ["VVy'keen","Vy'keen"]]

fix_info = {
  "Doludes": [
    {"Economy: Experimenta // Booming": "Economy: Experimental // Booming"},
  ],
  "Onrovi": [
    {"Flora: ": "Flora: Low"},
  ]
}

def fix_info_fn(ilog, lineno, db, place_name, dict_type):
  if place_name in fix_info:
    log(ilog,f'{lineno} fix_info_fn:fi: {fix_info[place_name]}')
    log(ilog,f'{lineno} fix_info_fn:b: {place_name}[{dict_type}] {db[place_name][dict_type]}')
    for fix in fix_info[place_name]:
      for old, new in fix.items():
        db[place_name][dict_type] = [
          new if data == old else data for data in db[place_name][dict_type]]
    log(ilog,f'{lineno} fix_info_fn:a: {place_name}[{dict_type}] {db[place_name][dict_type]}')


fixsi = {
  "Apporo II": 
    ["Celestial Bodies: 4 Planets // 2 Moons",
     "Dominant Lifeform: Uncharted",
     "Economy: - Data Unavailable -",
     "Conflict level: - Data Unavailable -",
     "Glyphs: 11B2046EDF93"],
  "Washeyu-Hebe": 
    ["Celestial Bodies: 4 Planets // 1 Moon",
     "Dominant Lifeform: Korvax",
     "Economy: - Data Unavailable -",
     "Conflict level: - Data Unavailable -"],
  "Eibeyt-Guyun IV":
    ["Celestial Bodies: 6 Planets",
     "Dominant Lifeform: Korvax",
     "Economy: Fuel Generation // Medium Supply",
     "Conflict level: Gentle"],
  "Nustanskyv XVI":
    ["Celestial Bodies: 3 Planets",
     "Dominant Lifeform: Vy'keen",
     "Economy: Commercial // Sustainable",
     "Conflict level: Critical"],
  "Limaayv-Dolmu":
    ['Celestial Bodies: 5 Planets // 1 Moon',
     'Dominant Lifeform: Korvax',
     'Economy: - Data Unavailable -',
     'Conflict level: - Data Unavailable -'],
  "Eystem XIX":
    ['Celestial Bodies: 4 Planets',
     'Dominant Lifeform: Korvax',
     'Economy: Mathematical // Low Supply',
     'Conflict level: Unthreatening']
}

corrupted = {  #Corrupted
  "Answer To None",
  "Corrupted",
  "De-Harmonised",
  "Dissonant",
  "Forsaken",
  "Rebellious",
  "Sharded from the Atlas"
}

# isResource blank planet names
null_lookup = {
      # '_8_': 'RW',
      'Nomyussko': { 10: 'Eotis' },
      'Doludes': { 6: 'E&#x203A;' },
      # 'Annana-Anyun': {5: 'Faeli'},
      # 'Valhalla': {4: 'Opul'}
}

fix = {
  "Doriguc Vili":"Doriguc VII",
  "New Egonglai":"New Eqonglai",
  "Wokin Vi":"Wokin VII",
  "Gabradet kom":"Gabradet Ikom",
  "Xapht":"Xaphl",
  
  # normal8 orbital
  "Oyook 52/68":"Oyook 52/G8",
  "ikoka 45/G1":"Ikoka 45/G1",
  "Edatmin R38":"Edalmin R38",
  "Oupol ill":"Oupol III",

  "E>":"E&#x203A;",
  "lrie E20":"Irie E20",
  "Ceklavis XIl":"Ceklavis XII",
  "Ceklavis Xil":"Ceklavis XII",
  "Wibordo Vi":"Wibordo VI",
  "Midlin XVi":"Midlin XVI",
  "Anro XIll":"Anro XIII",
  "Anro Xill":"Anro XIII",

  # expeditions6 redux
  "Hijinag":"Hijinaq",
  # expeditions6 blighted
  "IIskommu XIV":"Iskommu XIV",
  "Oweslie-Wagos XIV":"Qweslie-Wagos XIV",
  "Nock Vill":"Nock VIII",
  # expeditions5 exobiology
  "Limaav-Dolmu":"Limaayv-Dolmu",
  "Itrunn VIL":"Itrunn VII",
  # expeditions5 redux
  # "Liaiutsia Xl":"Liaiutsia XI",
  # "KimbI":"Kimbl",
  # "Exte X":"Exle X",
  # "Inhalce Vil":"Inhalce VII",
  "Muchudl XixX":"Muchudl XIX",
  "Ogaets XIl":"Ogaets XII",
  "Liaiutsia Xl":"Liaiutsia XI",
  "Olsierna Ill":"Olsierna III",
  "Ifton XU":"Ifton XIII",
  "Toxic Monscons":"Toxic Monsoons",

  # frontiers
  # "FOG]quest-001 { Enter tt":"[TOG]quest-001 { Enter",
  "idmoutheri Ishi":"Idmoutheri Ishi",

  "Ruga 91/28":"Ruga 91/Z8",
  "Ropuscu Ebaya -":"Ropuscu Ebaya",
  "Vistiragu Hanai":"Vistiraqu Hanai",
  "imiz 98/A8":"Imiz 98/A8",
  "Oupol Ill":"Oupol III",

  "Harsh, ley Winds":"Harsh, Icy Winds", #Weather
  "Ahampteh Xil":"Ahampteh XII",
  "Udere Vi":"Udere VI",
  "Yusvadbeat XI":"Yusvadbeat XII",
  "Yusvadbeat XIl":"Yusvadbeat XII",
  "Yovetrowl Ill":"Yovetrowl III",
  "Dorigue VII":"Doriguc VII",
  "Xetebor Vil":"Xetebor VII",
  "Wokin Vil":"Wokin VII",
  "Aieus $3":"Aieus S3",
  "Robriggle Xi!":"Robriggle XII",
  "Kuzent-Hoen XIll":"Kuzent-Hoen XIII",
  "ittleb Kizaw":"Ittleb Kizaw",

  "Iindustrial-Grade Battery":"Industrial-Grade Battery",
  "industrial-Grade Battery":"Industrial-Grade Battery",
  "Avdelba":"Avdelba I",
  "Moagenzh-Biut XIII":"Moqenzh-Biut XIII",
  "Moaenzh-Biut XIII":"Moqenzh-Biut XIII",
  "lrakihil Prime":"Irakihil Prime",
  "Utumuse Prime":"Utumusc Prime",
  "Audither Vil":"Audither VII",
  "Omyard Xili":"Omyard XIII",
  "irakihif Prime":"Irakihil Prime",
  "Udletch lil":"Udletch III",
  "Udletch Ill":"Udletch III",
  "Eyaksh Vi":"Eyaksh VI",
  "Natan! G19":"Natanl G19",
  "lijiey XV":"Iijiey XV",
  "Dehuiz":"Dehuiz I",
  "Nandf XIll":"Nandf XIII",

  "Idalth XiV":"Idalth XIV",
  "Seforc $5":"Seforc S5",
  "Wisantan 024":"Wisantan O24",
  "Emnika Il":"Emnika III",
  "laue Tau":"Iaue Tau",
  "Itby 1":"Itby II",
  "Emnika Ill":"Emnika III",
  "Nomyussko.":"Nomyussko",
  "Jarn XI":"Jarn XII",
  "Jarn Xi":"Jarn XII",
  "Ifrods XVU":"Ifrods XVII",
  "ltnew W29":"Itnew W29",
  "Adcaseiu Il":"Adcaseiu II",
  "Adcaseiu li":"Adcaseiu II",
  "Letu Ill":"Letu III",
  "Letu lil":"Letu III",

  "Suspicious Neutron Cannon Mox":"Suspicious Neutron Cannon",
  "Suspicious Photon Cannon Modt":"Suspicious Photon Cannon",
  "Suspicious Starship Shield Modt":"Suspicious Starship Shield",

  "Aphas XVill":"Aphas XVIII",
  "lami B7":"Iami B7",
  "Amole":"Ample",
  "common":"Common",

  "Oginic-Roran Il":"Oginic-Roran II",
  "Suspicious Geology Cannon Moc":"Suspicious Geology Cannon",
  "Suspicious Plasma Launcher Mc":"Suspicious Plasma Launcher",
  "Suspicious Photon Cannon Mod":"Suspicious Photon Cannon",
  "Hantury Vil!":"Hantury VIII",
  "Lakelme X1X":"Lakelme XIX",
  "Luxembl VI":"Luxembl VII",
  "Apporo Il":"Apporo II",
  "Apporo tl":"Apporo II",
  # "Hijinaq":"Apporo II",
  "Ninarb $13":"Ninarb S13",
  "Yardogo XVil":"Yardogo XVII",
  "Gisbrosp XiV":"Gisbrosp XIV",
  "Rinuse XIX":"Rinusc XIX",

  "Photon Cannon Medule":"Photon Cannon",
  "Activated Emeril!":"Activated Emeril",
  "Emer!":"Emeril",
  "Gamma Reot":"Gamma Root",
  "indium":"Indium",
  "lon Battery":"Ion Battery",
  "fon Capacitor":"Ion Capacitor",
  "jon Capacitor":"Ion Capacitor",
  "lon Capacitor":"Ion Capacitor",
  "lon Sphere":"Ion Sphere",
  "lonised Cobalt":"Ionised Cobalt",
  "Phosphecrus":"Phosphorus",
  "Phospherus":"Phosphorus",
  "sodium":"Sodium",
  "Sedium":"Sodium"
}

# thermal = { # current limit:hot<699240
#   "20210910063900[3]":"22185", # old format
#   "20210910071400[5]":"21930", # old format 
#   "20211001221500[3]":"23460", # old format
#   "20240319120400[0]":[712470,"Hot Protection"]
#   }


def double_slash_corner(thresh):
  print('x,0=',thresh[0,0:3])
  print('x,1=',thresh[1,0:3])
  print('x,2=',thresh[2,0:3])
  print('0,y=',thresh[0:3,0])
  print('1,y=',thresh[0:3,1])
  print('2,y=',thresh[0:3,2])

#----------------------------------------------

def isSysInfo(imagePath,dbug,ilog,db,large_image):
  global planet_index, work_image
  log(ilog,f'SysInfo: entering...')
  crop_image = large_image[790:925,115:650]
  result = cv2.matchTemplate(const_image['small'], crop_image, cv2.TM_SQDIFF_NORMED)
  mn,_,mnLoc,_ = cv2.minMaxLoc(result)
  MPx,MPy = mnLoc

  if MPx == 9 and MPy in [8, 9]:
    log(ilog,f'{getframeinfo(currentframe()).lineno} SysInfo: mn={mn:.3f} {mnLoc} crop.shape={crop_image.shape}')
    work_image  = np.full((500,600),240,dtype='uint8')
    ret,thresh = cv2.threshold(crop_image,175,255,cv2.THRESH_BINARY_INV)
    thresh[MPy:MPy+17,MPx:MPx+34] = 255 # clear //_icon 32w x 15h
    work_image[:135,7:7+535] = thresh

    if 'i' in dbug: 
      temp_image = large_image.copy()
      cv2.rectangle(temp_image,(115-3,790-3),(115+535+2,790+135+2),255,3)
      cv2.putText(temp_image, "isSysInfo?", (115,790-20), 0, 1.0, (255,255,255), 2)     
      cv2.imshow('temp',imutils.resize(temp_image, height=720))
      cv2.imshow('work',work_image)
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

    sysinfo = pytesseract.image_to_string(thresh)
    anysys = False
    for i in range(len(si)): 
      sysinfo = re.sub(si[i][0], si[i][1], sysinfo, re.MULTILINE)
      if re.search(si[i][0][:-1], sysinfo): 
        anysys = True
    # remove last character and all blank lines
    sysinfo = re.findall(r'^.+?$', sysinfo[:-1], re.MULTILINE)
    if not anysys:
      return False, None

    nl = "\n"
    log(ilog,f'SysInfo: station= {nl.join(sysinfo)}')
    station = sysinfo.pop(0)[:22]
    station = re.sub(r'[ |_.]+$','',station)
    station = fn_fix(ilog,getframeinfo(currentframe()).lineno,station)
    db[station] = {}
    db[station]['System Info'] = sysinfo
    if station in fixsi: 
      db[station]['System Info'] = fixsi[station]
    db[station]['Technology'] = {}
    db[station]['Buy Sell'] = {}

    fix_info_fn(ilog, getframeinfo(currentframe()).lineno, db, station, "System Info")

    planet_index = 0
    return True, station
  return False, None

#----------------------------------------------

def isGlyphs(imagePath,dbug,ilog,db,large_image,station):
  global work_image
  log(ilog,f'Glyphs: entering... {station}')
  stack_image, e, glyphs = np.zeros((64,600),dtype='uint8'), 0, ''
  gray_image = large_image[1015:1047,11:395]
  # ret,gray_image = cv2.threshold(gray_image,160,255,cv2.THRESH_BINARY) # this works for lighter backgrounds! I just don't like it
  stack_image[:32, :384] = gray_image
  for i in range(12):
    result = cv2.matchTemplate(gray_image[:, i*32:i*32+32], const_image['glyph'], cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc
    n = round(MPx / 32)
    e += MPx % 32
    glyphs += '0123456789abcdef'[n]
    stack_image[32:,i*32:i*32+32] = const_image['glyph'][:, n*32:n*32+32]
  log(ilog,f'Glyphs: e:{e} {glyphs}')
  stack_image = cv2.bitwise_not(stack_image)
  work_image[138:138+64,7:7+384] = stack_image[0:,0:384]

  ret = True
  if 'g' in dbug:
    temp_image = large_image.copy()
    cv2.putText(work_image, "Do these glyphs match? y|n", (10,228), 0, .7, (0,0,0), 1)     
    cv2.rectangle(temp_image,(11-4,1015-4),(11+384+3,1015+32+3),255,3)
    cv2.putText(temp_image, "isGlyph?", (11,1015-20), 0, 1.0, (255,255,255), 2)     
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    cv2.imshow('work',work_image)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()
    elif k in [78, 110]: # N=78,n=110,Y=89,y=121
      ret = False
  work_image[170:170+66,7:7+384] = np.full((66,384),240,dtype="uint8") 
  db[station]['System Info'].append(f'Glyphs: {glyphs}')
  return ret

#----------------------------------------------


def isTechno(imagePath,dbug,ilog,db,large_image,station,class_set):
  global work_image

  def local_trade(img):
    # print(img.shape)
    # cv2.imshow('trade',img)
    # k = cv2.waitKey(0) & 0xFF
    # if k == 27:
    #   exit()

    # if 'cached_trade' in globals():
    #   result = cv2.matchTemplate(const_image[globals()['cached_trade']], img, cv2.TM_SQDIFF_NORMED)
    #   mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    #   log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: {globals()["cached_trade"]}: {mn:.3f}')
    #   return ['','+'][mn < .01]
    # else:
      result = cv2.matchTemplate(const_image['trade1'], img, cv2.TM_SQDIFF_NORMED)
      trade1 = cv2.minMaxLoc(result)
      result = cv2.matchTemplate(const_image['trade2'], img, cv2.TM_SQDIFF_NORMED)
      trade2 = cv2.minMaxLoc(result)
      if .01 > trade1[0] < trade2[0]:
        globals()['cached_trade'] = 'trade1'
        return '+'
      else:
        if .01 > trade2[0] < trade1[0]:    
          globals()['cached_trade'] = 'trade2'
          return '+'
      return ''

  log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: entering... {station}')
  crop_image = large_image[167:238+25,1185:1401+179]
  result = cv2.matchTemplate(const_image['avail1'], crop_image, cv2.TM_SQDIFF_NORMED)
  avail1 = cv2.minMaxLoc(result)
  result = cv2.matchTemplate(const_image['avail2'], crop_image, cv2.TM_SQDIFF_NORMED)
  avail2 = cv2.minMaxLoc(result)
  if avail1[0] < avail2[0]:
    mn0,_,mn0Loc,_ = avail1 
    log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: avail1: mn={mn0:.3f} {mn0Loc}')
  else:
    mn0,_,mn0Loc,_ = avail2
    log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: avail2: mn={mn0:.3f} {mn0Loc}')
  P0x,P0y = mn0Loc

  # Available To Buy | Standing Discount
  if mn0 > .05: 
    return False

  if 't' in dbug: 
    temp_image = large_image.copy() 
    cv2.rectangle(temp_image,(1185-3,167-3),(1580+2,263+2),255,3)
    cv2.rectangle(temp_image,(P0x+1185-3,P0y+167-3),(P0x+1185+167+2,P0y+167+25+2),255,3)
    temp_image[167-45:167-10,1185:1185+150] = np.full((35,150),0,dtype="uint8") 
    cv2.putText(temp_image, "isTechno?", (1185,167-20), 0, 1.0, (255,255,255), 2)     
    cv2.imshow('tech_avail',crop_image)
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()
    cv2.destroyWindow('tech_avail')

  # Techno|System
  mn, MPx1, MPy1, foot_text = 1, 0, 0, "System"
  gray_image = large_image[P0y+903:P0y+970,P0x+17:P0x+300] # pre-orbital

  # cv2.imshow('gray',gray_image)
  # k = cv2.waitKey(0) & 0xFF
  # if k == 27:
  #   exit()

  for kiosk in ['system','technol','salvage','contrab']:
    result = cv2.matchTemplate(gray_image, const_image[kiosk], cv2.TM_SQDIFF_NORMED)
    mn1,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPxx,MPyy = mnLoc
    if mn > mn1:
      mn = mn1
      MPx1,MPy1 = mnLoc
      foot_text = kiosk.capitalize()
  log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: {foot_text:7s}: mn={mn:.3f},MPy={MPy1},MPx={MPx1}')


  if 't' in dbug: 
    cv2.rectangle(temp_image,(P0x+17+MPx1-3,P0y+903+MPy1-3),(P0x+17+MPx1+174+2,P0y+MPy1+903+48+2),255,3)
    cv2.imshow('tech_kiosk',gray_image)
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()
    cv2.destroyWindow('tech_kiosk')
    log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: {foot_text:7s} {mn:.3f} {(MPx1,MPy1)}')

  # if not re.match(r'System', foot_text): return True #sjh
  if re.match(r'Technol|System|Contrab|Salvage', foot_text):
    work_image[172:172+48,7:7+176] = np.full((48,176),240,dtype='uint8')
    cv2.putText(work_image, foot_text.capitalize(), (10,205), 0, 1.5, (0,0,0), 2)     
    gray_image = large_image[P0y+167+55:P0y+167+700,P0x+1185-262:P0x+1185+238]
    ret,thresh = cv2.threshold(gray_image,210,255,cv2.THRESH_BINARY_INV)

    if 't' in dbug: 
      print(getframeinfo(currentframe()).lineno)
      cv2.imshow('tech3',thresh)
      # k = cv2.waitKey(0) & 0xFF
      # if k == 27:
      #   exit()

    y = 0
    work_image[222:222+20,7:7+42] = np.full((20,42),240,dtype="uint8") # clear
    while y < 6 and thresh[110*y:110*y+34,78:78+34].sum() < 277000:
      line_tech = 'None'
      if re.match(r'Technol|Salvage', foot_text):
        badge_image = thresh[110*y+20:110*y+40,7:27]
        therm_image = thresh[110*y+25:110*y+81,10:66]
        therm_image = cv2.bitwise_or(therm_image, const_image['mask'])
        work_image[222:222+20, 0: 0+20] = badge_image
        work_image[222:222+56,21:21+56] = therm_image
        line_text2 = stripe(pytesseract.image_to_string(badge_image, config='--psm 10'))

      # Thermal Protection Module; [X]Suspicious Hazard Protection ₜ
      line_text = stripped(thresh[110*y:110*y+34,78:500],ilog,getframeinfo(currentframe()).lineno)
      if foot_text == "Salvage":
        salvage = line_text.split()
        if re.match(r'^M',salvage[-1]):
          salvage.pop()
          line_text = " ".join(salvage)
      line_text = re.sub(' Module','',line_text)
      line_text = re.sub('Suspicious ','',line_text)
      # if line_text in fix: 
      line_text = fn_fix(ilog,getframeinfo(currentframe()).lineno,line_text)

      if re.match('Thermal', line_text): 
        # 0.081 20240319120500[1] - [S]Cold Protection
        # 0.634 20211211115144[3] - [S]Hot Protection
        result = cv2.matchTemplate(const_image['snow'], therm_image, cv2.TM_SQDIFF_NORMED)
        mn,_,mnLoc,_ = cv2.minMaxLoc(result)
        if mn < .36: # .081+(.634-.081)/2
          line_text = 'Cold Protection'
        else:
          line_text = 'Hot Protection'

      if re.match(r'Technol|Salvage', foot_text):
        line_tech = f'[{line_text2.capitalize()[0]}]{line_text}'
        if not "Class Reactor" in line_text:
          class_set.add(line_tech[1])
          # if not line_tech[1] in "ABCSX": raise Exception(f'{line_text}')
      else:
        if re.match(r'System', foot_text):
          line_text += local_trade(gray_image[110*y:110*y+110,78:500])

      if (re.match(r'System|Contrab', foot_text) 
      or re.match(r'Technol|Salvage', foot_text) and not re.search(r'Class Reactor',line_tech)):
        # if line_text in fix: 
        #   line_text = fix[line_text]
        kiosk = {'Technol':'Technology','System':'Buy Sell', 'Salvage':'Technology','Contrab':'Buy Sell'}[foot_text]
        item = [line_tech,line_text][kiosk == 'Buy Sell']
        # print(f'{station},{kiosk},{line_tech},{line_text},{db}')
        db[station][kiosk][[line_tech,line_text][kiosk == 'Buy Sell']] = ''
        log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: {item} {["","Tech Class error"][kiosk == "Technology" and not item[1] in "ABCSX"]}')

      work_image[222:222+34,78:78+422] = thresh[110*y:110*y+34,78:78+422]
      if 't' in dbug:
        cv2.imshow('work',work_image)
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
          exit()
          break
      y += 1

    if 't' in dbug: 
      cv2.destroyWindow('tech3')

    return True
  return False

#----------------------------------------------

def isResource(imagePath,dbug,ilog,db,large_image,station):
  global planet_index, work_image
  log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: entering... {station}') # x:[{x}]')

  #------------------ resource search window ----------------------------

  PDx, PDy, PDo, RIx, RDx, RDo, PNo, tag = 49, 55, 23, 347, 399, 12, 146, 'resrc1'
  crop_image = large_image[304:304+294,135:135+226]
  result = cv2.matchTemplate(const_image['resrc1'], crop_image, cv2.TM_SQDIFF_NORMED)
  mn,_,mnLoc,_ = cv2.minMaxLoc(result)
  result = cv2.matchTemplate(const_image['resrc2'], crop_image, cv2.TM_SQDIFF_NORMED)
  resrc  = cv2.minMaxLoc(result)
  if resrc[0] < mn:
    PDx, PDy, PDo, RIx, RDx, RDo, PNo, tag = 50, 47, 21, 347, 392, 11, 132, 'resrc2'
    mn,_,mnLoc,_ = resrc

  log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: {tag}: {mn:.3f} {mnLoc}')
  MPx,MPy = mnLoc

  if 'r' in dbug:
    temp_image = large_image.copy()
    cv2.rectangle(temp_image,(135-3,304-3),(146+231+2,304+294+2),255,3)
    cv2.rectangle(temp_image,(MPx+135-3,MPy+304-3),(MPx+135+48+2,MPy+304+215+2),255,3)
    temp_image[304-45:304-10,135:135+150] = np.full((35,150),0,dtype="uint8") 
    cv2.putText(temp_image, "isResource?", (135,304-20), 0, 1.0, (255,255,255), 2)     
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()

  if not mn < 0.04:
    return False

  planet_index += 1
  crop_image = large_image[304+MPy-PNo:304+MPy-PNo+60,135+MPx+64:135+MPx+64+575]
  # cv2.rectangle(temp_image,(135+MPx+64-3,304+MPy-129-3),(135+MPx+64+575+2,304+MPy-129+60+2),255,3)
  ret,thresh2 = cv2.threshold(crop_image,160,255,cv2.THRESH_BINARY_INV)
  work_image[258:258+60, 7:7+575] = thresh2
  planet = stripped(thresh2,ilog,getframeinfo(currentframe()).lineno)

  if planet == '': 
    if station in null_lookup and planet_index in null_lookup[station]:
      planet = null_lookup[station][planet_index]
    else:
      planet = f'_{planet_index}_'
      # raise Exception(f's={station}, planet_index={planet_index}, p={planet}')

  # if planet in fix: 
  planet = fn_fix(ilog,getframeinfo(currentframe()).lineno,planet)
  log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: s={station}, i={planet_index}, p= "{planet}"') # {planet.encode().hex()}')

  # KeyError: {station}, keys: {db.keys()}
  if station not in db:
    station = f'_{station}_'
    db[station] = {'System Info':[],'Technology':{},'Buy Sell':{}}

  if planet not in db[station]:
    db[station][planet] = {'Planet Info':[],'Resources':[]}

  work_image[320:320+25,385:385+175] = np.full((25,175),240,dtype="uint8") 

  if 'r' in dbug:
    cv2.imshow('crop',large_image[304+MPy+PDo:304+MPy+PDo+224,135+MPx+PDx:135+MPx+PDx+305])

  for y in range(4):
    crop_image = large_image[304+MPy+PDo+y*PDy:304+MPy+PDo+25+y*PDy,135+MPx+PDx:135+MPx+PDx+305]
    ret,thresh = cv2.threshold(crop_image,160,255,cv2.THRESH_BINARY_INV)
    profile = stripped(thresh,ilog,getframeinfo(currentframe()).lineno)
    log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: profile= {["Weather: ","Sentinels: ","Flora: ","Fauna: "][y]}{profile}')
    db[station][planet]['Planet Info'].append(["Weather: ","Sentinels: ","Flora: ","Fauna: "][y]+profile)
    work_image[320:320+25,78:78+305] = thresh

    if 'r' in dbug:
      cv2.imshow('work',work_image)
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

  fix_info_fn(ilog, getframeinfo(currentframe()).lineno, db[station], planet, "Planet Info")

  if 'r' in dbug:
    cv2.imshow('crop', large_image[304+MPy:304+MPy+224,135+MPx+RIx:135+MPx+RIx+305])

  for y in range(5):
    gray_image = large_image[304+MPy+y*PDy:304+MPy+47+y*PDy,135+MPx+RIx:135+MPx+RIx+47]
    result = cv2.matchTemplate(gray_image, const_image['icons'], cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    if mnLoc[1] > 165: break # 4*47-23=165

    crop_image = large_image[304+MPy+RDo+y*PDy:304+MPy+RDo+25+y*PDy,135+MPx+RDx:135+MPx+RDx+180]
    result = cv2.matchTemplate(crop_image, const_image['salt'], cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    ret,thresh = cv2.threshold(crop_image,176,255,cv2.THRESH_BINARY_INV)
    resource = stripped(thresh,ilog,getframeinfo(currentframe()).lineno)
    tag = ''
    if mn < .01: 
      if resource != 'Salt': 
        tag = '!'
      resource = 'Salt'
    log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: {mn:.3f} resource= {resource} {tag}')
    db[station][planet]['Resources'].append(resource)
    work_image[320:320+25,385:385+180] = thresh

    if 'r' in dbug:
      cv2.imshow('icon',large_image[304+MPy+y*PDy:304+MPy+47+y*PDy,135+MPx+RIx:135+MPx+RIx+47])
      cv2.imshow('work',work_image)
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

  if 'r' in dbug: 
    cv2.destroyWindow('icon')
    cv2.destroyWindow('crop')

  return True

#----------------------------------------------

def isVisited2(imagePath,dbug,ilog,db,large_image,station):
  global system_index, planet_index, work_image

  temp_image = large_image.copy()

  # needs scope to large_image and temp_image
  def search_area(icon, p1x, p1y, p2x, p2y):

    # draw rectangle around search area
    cv2.rectangle(temp_image,(p1x-3,p1y-3),(p2x+2,p2y+2),255,3)

    crop_image = large_image[p1y:p2y, p1x:p2x]
    result = cv2.matchTemplate(const_image[icon], crop_image, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    x, y = mnLoc
    h, w = const_image[icon].shape

    # draw rectangle around icon
    if mn < .01:
      cv2.rectangle(temp_image,(p1x+x-3,p1y+y-3),(p1x+x+w+2,p1y+y+h+2),255,3)

    if 'v' in dbug:
      log(ilog,f'trace: {mn:.3f} {p1x+x,p1y+y}')
      cv2.imshow('temp', imutils.resize(temp_image, height=720))
      cv2.imshow('icon', cv2.hconcat([
        large_image[p1y+y:p1y+y+h,p1x+x:p1x+x+w],
        np.full((h, 1), 240, dtype='uint8'),
        const_image[icon] ]))
      k = cv2.waitKey(0) & 0xFF
      # log(ilog,f'search area: k={k}')
      if k == 27:
        exit()
      cv2.destroyWindow('icon')

    return mn, p1x+x, p1y+y

  def clear_icon(icon, img):
    result = cv2.matchTemplate(const_image[icon], img, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc
    log(ilog,f'clear={mn:.3f} {mnLoc}')
    if mn < .01: 
      y, x = const_image[icon].shape
      img[MPy:MPy + y, MPx:MPx + x] = img[MPy + y -1, MPx + x -1]

  #------------------ visited search window ----------------------------

  log(ilog,f'Visited: entering... {station}')

  crop_image = large_image[141:226,213:329+211]
  result = cv2.matchTemplate(const_image['visit1'], crop_image, cv2.TM_SQDIFF_NORMED)
  visit1 = cv2.minMaxLoc(result)
  result = cv2.matchTemplate(const_image['visit2'], crop_image, cv2.TM_SQDIFF_NORMED)
  visit2 = cv2.minMaxLoc(result)
  mn0,_,mn0Loc,_ = visit1 if visit1[0] < visit2[0] else visit2
  # P0x,P0y = addPt(mn0Loc, (213,141))
  P0x, P0y = (mn0Loc[0]+213,mn0Loc[1]+141)

  # draw rect around visited
  cv2.rectangle(temp_image,(213-3,141-3),(540+2,226+2),255,3)
  cv2.rectangle(temp_image,(P0x-3,P0y-3),(P0x+211+2,P0y+20+2),255,3)
  temp_image[141-45:141-10,213:213+150] = np.full((35,150),0,dtype="uint8") 
  cv2.putText(temp_image, "isVisited?", (213,141-20), 0, 1.0, (255,255,255), 2)     

  if 'v' in dbug:
    log(ilog,f'{getframeinfo(currentframe()).lineno}')
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()

  if not mn0 < .01:
    return False, None, False

  # card search area
  mn1, P1x, P1y = search_area('card',P0x+966, P0y+85, P0x+995+68, P0y+850)

  #------------------ set system name ----------------------------

  if not mn1 < .01:
    planet_index = 0
    system_index += 1

    # scan system name at top
    crop_image = large_image[P0y:P0y+58,P0x+535:P0x+535+575]
    cv2.rectangle(temp_image,(P0x+535,P0y),(P0x+535+575,P0y+58),255,3)
    ret,thresh = cv2.threshold(crop_image,160,255,cv2.THRESH_BINARY_INV)
    tentative = stripped(thresh,ilog,getframeinfo(currentframe()).lineno)

    if tentative not in db:
      if f'_{system_index}_' in null_lookup:
        tentative = null_lookup[f'_{system_index}_']
      else:
        log(ilog,f'tentative= "{tentative}"')
        tentative = f'_{[tentative,system_index][tentative==""]}_'
      db[tentative] = {'System Info':[],'Technology':{},'Buy Sell':{}}

    work_image[346:346+58,7:7+575] = thresh
    if 'v' in dbug:
      cv2.imshow('work',work_image)
      cv2.imshow('temp',imutils.resize(temp_image, height=720))
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

    log(ilog,f'{getframeinfo(currentframe()).lineno} Visited: Set System: "{tentative}" -no card-')
    return True, tentative, False # visited but no card

    # ---------------------------------------------------------------------------------------

  P2x, P2y = P1x-596, P1y+80

    # locate card title

  # log(ilog,f'{getframeinfo(currentframe()).lineno} locate card title')
  clear_icon('steam1', large_image[P1y+7:P1y+68,P2x:P2x+420])
  gray2_image = large_image[P1y+7:P1y+7+35,P2x:P2x+420]
  ret,thresh = cv2.threshold(gray2_image,160,255,cv2.THRESH_BINARY_INV)
  card_title = stripped(thresh,ilog,getframeinfo(currentframe()).lineno)[:22]

  log(ilog,f'{getframeinfo(currentframe()).lineno} card title= "{card_title}"')

  work_image[406:406+35,7:7+420] = thresh
  if 'v' in dbug:
    cv2.imshow('work',work_image)

  mn, MPx, MPy = search_area('sicon',P2x, P1y+68, P2x+72, P1y+241)

  #------------------ extract Biome ---------------------------------

  if not mn < .01:
    mn, MPx, MPy = search_area('bicon',P2x, P1y+68, P2x+72, P1y+241)

    # handle bicon
    if mn < .01:
      work_image[443:443+51,7:7+51] = large_image[MPy:MPy+51,MPx:MPx+51] # base_image
      P2y += 89

    # biome
    gray_image = large_image[P2y:P2y+28,P2x+15:P2x+265]
    ret,thresh = cv2.threshold(gray_image,160,255,cv2.THRESH_BINARY_INV)
    work_image[443:443+28,78:78+250] = thresh

    if 'v' in dbug:
      cv2.imshow('work',work_image)
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

    type_title = stripped(thresh,ilog,getframeinfo(currentframe()).lineno)
    if station in db and card_title in db[station]:
      log(ilog,f'{getframeinfo(currentframe()).lineno} Visited: Set Biome: "{type_title}"')
      db[station][card_title]['Planet Info'].insert(0, "Biome: "+type_title)

      if any(any(key in info for key in corrupted) for info in db[station][card_title]['Planet Info']):
        db[station][card_title]['Resources'].append('Dissonance detected')
    else:
      log(ilog,f'{getframeinfo(currentframe()).lineno} Biome: error: db[{station}][{card_title}]')
      if station not in db:
        station = f'_{station}_'
        db[station] = {'System Info':[],'Technology':{},'Buy Sell':{}}
      if card_title not in db[station]:
        # card_title = f'_{card_title}_'
        db[station][card_title] = {'Planet Info':[],'Resources':[]}
      db[station][card_title]['Planet Info'].insert(0, "Biome: "+type_title)
    # print('planet type=',type_title)

    return True, None, False

  #------------------ handle sicon ----------------------------------

  # system name (card title)
  gray_image = large_image[P1y+7:P1y+7+35,P2x:P2x+420]
  ret,thresh = cv2.threshold(gray_image,160,255,cv2.THRESH_BINARY_INV)
  work_image[:135,7:7+535] = 255
  work_image[:35,7:7+420] = thresh

  # sysinfo
  gray_image = large_image[MPy-3:MPy+98,MPx+60:MPx+60+435]
  ret,thresh = cv2.threshold(gray_image,110,255,cv2.THRESH_BINARY_INV)
  work_image[35:35+101,7:7+435] = thresh

  if 'v' in dbug:
    cv2.imshow('info',gray_image)
    cv2.imshow('work',work_image)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()
    cv2.destroyWindow('info')

  sysinfo = pytesseract.image_to_string(thresh)
  for i in range(6): 
    sysinfo = re.sub(si[i][0], si[i][1], sysinfo, re.MULTILINE)
  sysinfo = re.findall(r'^.+?$', sysinfo[:-1], re.MULTILINE)
  nl = "\n"
  log(ilog, f'{nl.join(sysinfo)}')

  tentative = card_title
  sysflag = False
  if tentative not in db:
    sysflag = True
    db[tentative] = {}
    db[tentative]['System Info'] = sysinfo
    if tentative in fixsi: 
      db[tentative]['System Info'] = fixsi[tentative]
    db[tentative]['Technology'] = {} # it's important that these two follow "Sytem Info"
    db[tentative]['Buy Sell'] = {}
  else:
    db[tentative]['System Info'] = sysinfo
    if tentative in fixsi: 
      db[tentative]['System Info'] = fixsi[tentative]

  log(ilog,f'SysInfo: station= {nl.join(sysinfo)}')
  fix_info_fn(ilog, getframeinfo(currentframe()).lineno, db, tentative, "System Info")
    
  # log(ilog,f'{getframeinfo(currentframe()).lineno} Visited: Exiting: sysinfo card')
  x = 0
  return True, tentative, sysflag # visited plus sicon

#----------------------------------------------

# dt = re.search(r'(\d{14})',imagePath)
# filename = f'sysinfo_{dt.group(1)}.png'
# cv2.imwrite(filename, temp_image)

def isStellar(imagePath,dbug,ilog,db,large_image,station):
  log(ilog,f'Stellar: entering...')

  crop_image = large_image[184:297,732:1084]
  result = cv2.matchTemplate(const_image['guide'], crop_image, cv2.TM_SQDIFF_NORMED)
  mn,_,mnLoc,_ = cv2.minMaxLoc(result)
  MPx,MPy = (mnLoc[0]+732,mnLoc[1]+184)
  if mn > .01: 
    return

  crop_image = large_image[MPy+340:MPy+366,MPx+29:MPx+280]
  print(crop_image.shape)
  ret,thresh = cv2.threshold(crop_image,130,255,cv2.THRESH_BINARY_INV)
  star_color = stripped(thresh,ilog,getframeinfo(currentframe()).lineno)
  # if not "Stellar Classification" in db[station]['System Info'][0]:
  db[station]['System Info'].insert(0, star_color)
  log(ilog,f'Stellar: mn={mn:.3f} {mnLoc} {star_color}')

  if 's' in dbug: 
    temp_image = large_image.copy()
    cv2.rectangle(temp_image,(732-3,184-3),(1084+2,297+2),255,3)
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    cv2.imshow('crop',thresh)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()
