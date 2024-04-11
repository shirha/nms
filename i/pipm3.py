# type pip0.json | python -m json.tool
# https://www.w3schools.com/colors/colors_picker.asp
#
from inspect import currentframe, getframeinfo
import imutils
import pprint
pp = pprint.PrettyPrinter(indent=2)
import json
import sys
import os
import re
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Anaconda3\Library\bin\tesseract.exe'
stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)

# this = sys.modules[__name__]
logfile = None
i = 0
planet_index = 0

work_image  = np.full((500,600),240,dtype='uint8')
const_image = {}
for image in ["mask","system","technol","salvage","contrab","avail1","avail2","small","card",
              "snow","glyph","visit","steam","xboxx","sicon","bicon","icons","resrc","salt"]: 
  const_image[image] = cv2.imread(f'i/{image}_image.png', cv2.IMREAD_GRAYSCALE)

def log(n, *args):
  global logfile
  if logfile is None:
    if os.path.exists(f'log{n}.txt'):
      os.remove(f'log{n}.txt')
    logfile = open(f'log{n}.txt', 'a')

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
      # [r"Medium Sup\|","Medium Supply"]]

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
null_planet = { 
      'Nomyussko': { 10: 'Eotis' },
      'Doludes': { 6: 'E&#x203A;'},
      'Annana-Anyun': {5: 'Faeli'}
}

fix = {
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

  # expeditions5 redux
  "Liaiutsia Xl":"Liaiutsia XI",
  "Toxic Monscons":"Toxic Monsoons",
  "KimbI":"Kimbl",
  "Exte X":"Exle X",
  "Inhalce Vil":"Inhalce VII",
  "Muchudl XixX":"Muchudl XIX",
  "Ogaets XIl":"Ogaets XII",
  "Liaiutsia Xl":"Liaiutsia XI",
  "Olsierna Ill":"Olsierna III",
  "Ifton XU":"Ifton XIII",

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
  "Hijinaq":"Apporo II",
  "Ninarb $13":"Ninarb S13",
  "Yardogo XVil":"Yardogo XVII",
  "Gisbrosp XiV":"Gisbrosp XIV",
  "Rinuse XIX":"Rinusc XIX",

  "Photon Cannon Medule":"Photon Cannon",
  "Activated Emeril!":"Activated Emeril",
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
      return True, None

    nl = "\n"
    log(ilog,f'SysInfo: station= {nl.join(sysinfo)}')
    station = sysinfo.pop(0)[:22]
    print('pop=',station)
    station = re.sub(r'[ |_.]+$','',station)
    if station in fix: station = fix[station]
    print(f'station= `{station}`')
    db[station] = {}
    db[station]['System Info'] = sysinfo
    if station in fixsi: 
      db[station]['System Info'] = fixsi[station]
    db[station]['Technology'] = {}
    db[station]['Buy Sell'] = {}
    x = 0
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
    elif k == 78 or k == 110: # N=78,n=110,Y=89,y=121
      ret = False
  work_image[170:170+66,7:7+384] = np.full((66,384),240,dtype="uint8") 
  db[station]['System Info'].append(f'Glyphs: {glyphs}')
  return ret

#----------------------------------------------

def isTechno(imagePath,dbug,ilog,db,large_image,station):
  global work_image
  log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: entering... {station}')
  crop_image = large_image[167:238+25,1185:1401+179]
  result = cv2.matchTemplate(const_image['avail1'], crop_image, cv2.TM_SQDIFF_NORMED)
  avail1 = cv2.minMaxLoc(result)
  result = cv2.matchTemplate(const_image['avail2'], crop_image, cv2.TM_SQDIFF_NORMED)
  avail2 = cv2.minMaxLoc(result)
  mn0,_,mn0Loc,_ = avail1 if avail1[0] < avail2[0] else avail2
  P0x,P0y = mn0Loc
  log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: avail:   mn={mn0:.3f} {mn0Loc}')
  if mn0 > .05: 
    return False

  if 't' in dbug: 
    temp_image = large_image.copy() # Avaiable To Buy | Standing Discount
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
    # temp_image = large_image.copy()
    cv2.rectangle(temp_image,(P0x+17+MPx1-3,P0y+903+MPy1-3),(P0x+17+MPx1+174+2,P0y+MPy1+903+48+2),255,3)
    cv2.imshow('tech_kiosk',gray_image)
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()
    cv2.destroyWindow('tech_kiosk')
    log(ilog,f'{getframeinfo(currentframe()).lineno} Techno: {foot_text:7s} {mn:.3f} {(MPx1,MPy1)}')

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

    s_class = False
    y = 0
    # clear
    work_image[222:222+20,7:7+42] = np.full((20,42),240,dtype="uint8") 
    while y < 6 and thresh[110*y:110*y+34,78:78+34].sum() < 277000:
      line_tech = ''
      if re.match(r'Technol|Salvage', foot_text):
        badge_image = thresh[110*y+20:110*y+40,7:27]
        therm_image = thresh[110*y+25:110*y+81,10:66]
        therm_image = cv2.bitwise_or(therm_image, const_image['mask'])
        work_image[222:222+20, 0: 0+20] = badge_image
        work_image[222:222+56,21:21+56] = therm_image
        line_text2 = stripped(pytesseract.image_to_string(badge_image, config='--psm 10'))
        if re.match('S|s|5|$|x|X', line_text2): # ever saw x_class thermal_protection?
          s_class = True
        else:
          s_class = False


      # Thermal Protection Module; [X]Suspicious Hazard Protection
      line_text = stripped(pytesseract.image_to_string(thresh[110*y:110*y+34,78:500]))
      if foot_text == "Salvage":
        salvage = line_text.split()
        if re.match(r'^M',salvage[-1]):
          salvage.pop()
          line_text = " ".join(salvage)
      line_text = re.sub(' Module','',line_text)
      line_text = re.sub('Suspicious ','',line_text)
      if line_text in fix: 
        line_text = fix[line_text]


      if re.match('Thermal', line_text): 
        # 0.081 20240319120500[1]❄[S]Cold Protection
        # 0.634 20211211115144[3]🔥[S]Hot Protection
        result = cv2.matchTemplate(const_image['snow'], therm_image, cv2.TM_SQDIFF_NORMED)
        mn,_,mnLoc,_ = cv2.minMaxLoc(result)
        if mn < .36: # .081+(.634-.081)/2
          line_text = 'Cold Protection'
        else:
          line_text = 'Hot Protection'

        # retval, buffer = cv2.imencode('.jpg', therm_image)
        # import base64
        # jpg_as_text = base64.b64encode(buffer).decode()
        # html_page.append(f'<div class="centered">{mn:.3f} {imagePath[2:16]}[{y}] <div class="container"><img width="56" height="56" src="data:image/jpeg;base64, {jpg_as_text}"></div> [{line_text2.capitalize()[0]}]{line_text}</div>\n')

      if re.match(r'Technol|Salvage', foot_text):
        line_tech = f'[{line_text2.capitalize()[0]}]{line_text}'

      if (re.match(r'System|Contrab', foot_text) 
      or re.match(r'Technol|Salvage', foot_text) and not re.search(r'Class Reactor',line_tech)): # and s_class):
        # if line_text in fix: 
        #   line_text = fix[line_text]
        kiosk = {'Technol':'Technology','System':'Buy Sell', 'Salvage':'Technology','Contrab':'Buy Sell'}[foot_text]
        db[station][kiosk][[line_tech,line_text][kiosk == 'Buy Sell']] = ''

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

  crop_image  = large_image[318:318+280,147:147+219]
  result      = cv2.matchTemplate(const_image['resrc'], crop_image, cv2.TM_SQDIFF_NORMED)
  # mn0,_,mn0Loc,_ = cv2.minMaxLoc(result)
  # P0x,P0y = mn0Loc
  mn,_,mnLoc,_ = cv2.minMaxLoc(result)
  MPx,MPy = mnLoc

  log(ilog,f'{getframeinfo(currentframe()).lineno} {mn:.3f} {mnLoc} crop.shape={crop_image.shape}')
  if 'r' in dbug:
    temp_image = large_image.copy()
    cv2.rectangle(temp_image,(147-3,318-3),(147+219+2,318+280+2),255,3)
    cv2.rectangle(temp_image,(MPx+147-3,MPy+318-3),(MPx+147+48+2,MPy+318+215+2),255,3)
    temp_image[318-45:318-10,147:147+150] = np.full((35,150),0,dtype="uint8") 
    cv2.putText(temp_image, "isResource?", (147,318-20), 0, 1.0, (255,255,255), 2)     
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()

  if mn < 0.01:
    planet_index += 1

    crop_image = large_image[MPy+304-131:MPy+304-131+60,MPx+143+60:MPx+143+60+575]
    ret,thresh2 = cv2.threshold(crop_image,160,255,cv2.THRESH_BINARY_INV)
    work_image[258:258+60, 7:7+575] = thresh2
    planet = stripped(pytesseract.image_to_string(thresh2))
    planet = re.sub(r'[ |_.]+$','',planet)
    #----------------------------------------
    if planet == '': 
      if station in null_planet and planet_index in null_planet[station]:
        planet = null_planet[station][planet_index]
      else:
        raise Exception(f's={station}, planet_index={planet_index}, p={planet}')
        # log(ilog,f'raise Exception: s={station}, x={planet_index}, p="{planet}"')
    #----------------------------------------
    if planet in fix: planet = fix[planet]
    log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: station= {station}, planet_index={planet_index}, planet= "{planet}"') # {planet.encode().hex()}')
    if planet not in db[station]:
      db[station][planet] = {}
      db[station][planet]['Planet Info'] = []
      db[station][planet]['Resources'  ] = []

    work_image[320:320+24,385:385+175] = np.full((24,175),240,dtype="uint8") 

    if 'r' in dbug:
      cv2.imshow('crop',large_image[MPy+320+19:MPy+320+44+224,MPx+147+48:MPx+147+48+305])
      # k = cv2.waitKey(0) & 0xFF
      # if k == 27:
      #   exit()

    for y in range(4):
      crop_image = large_image[MPy+320+19+y*56:MPy+320+44+y*56,MPx+147+48:MPx+147+48+305]
      ret,thresh = cv2.threshold(crop_image,160,255,cv2.THRESH_BINARY_INV)
      profile = stripped(pytesseract.image_to_string(thresh)).rstrip('.')

      if profile in fix: profile = fix[profile]
      log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: profile= {["Weather: ","Sentinels: ","Flora: ","Fauna: "][y]}{profile}')
      db[station][planet]['Planet Info'].append(["Weather: ","Sentinels: ","Flora: ","Fauna: "][y]+profile)
      work_image[320:320+25,78:78+305] = thresh
      if 'r' in dbug:
        cv2.imshow('work',work_image)
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
          exit()

    if 'r' in dbug:
      # log(ilog,f'{getframeinfo(currentframe()).lineno} imshow(crop)')
      cv2.imshow('crop', cv2.hconcat([
        large_image[MPy+318:MPy+318+327,MPx+147+346:MPx+147+346+47],
        np.full((327,1),240,dtype='uint8'),
        large_image[MPy+318+11:MPy+318+11+327,MPx+143+346+56:MPx+143+346+56+180] ]))
      # k = cv2.waitKey(0) & 0xFF
      # if k == 27:
      #   exit()

    for y in range(5):
      gray_image = large_image[MPy+318+y*56:MPy+318+47+y*56,MPx+147+346:MPx+147+346+47]
      result = cv2.matchTemplate(gray_image, const_image['icons'], cv2.TM_SQDIFF_NORMED)
      mn,_,mnLoc,_ = cv2.minMaxLoc(result)

      if mnLoc[1] > 175: # MPy
        break

      crop_image = large_image[MPy+318+11+y*56:MPy+318+35+y*56,MPx+143+346+56:MPx+143+346+56+180]
      result = cv2.matchTemplate(crop_image, const_image['salt'], cv2.TM_SQDIFF_NORMED)
      mn,_,mnLoc,_ = cv2.minMaxLoc(result)
      ret,thresh = cv2.threshold(crop_image,176,255,cv2.THRESH_BINARY_INV)
      resource = stripped(pytesseract.image_to_string(thresh)).rstrip('.')
      if resource in fix: resource = fix[resource]
      if mn < .005:
        resource = 'Salt'
      log(ilog,f'{getframeinfo(currentframe()).lineno} Resource: resource= {resource}')
      db[station][planet]['Resources'].append(resource)
      work_image[320:320+24,385:385+180] = thresh
      if 'r' in dbug:
        cv2.imshow('work',work_image)
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
          exit()
    if 'r' in dbug: 
      cv2.destroyWindow('crop')

    return True
  return False

#----------------------------------------------

def isVisited(imagePath,dbug,ilog,db,large_image,station):
  global i, planet_index, work_image
  i += 1
  log(ilog,f'Visited: entering... {station}')

  #------------------ visited search window ----------------------------

  crop_image = large_image[141:226,213:329+211]
  result = cv2.matchTemplate(const_image['visit'], crop_image, cv2.TM_SQDIFF_NORMED)
  mn0,_,mn0Loc,_ = cv2.minMaxLoc(result)
  P0x,P0y = mn0Loc
  log(ilog,f'{getframeinfo(currentframe()).lineno} {mn0:.3f} {mn0Loc} crop={crop_image.shape}')


  if 'v' in dbug:
    temp_image = large_image.copy()
    cv2.rectangle(temp_image,(213-3,141-3),(540+2,226+2),255,3)
    cv2.rectangle(temp_image,(P0x+213-3,P0y+141-3),(P0x+213+211+2,P0y+141+20+2),255,3)
    temp_image[141-45:141-10,213:213+150] = np.full((35,150),0,dtype="uint8") 
    cv2.putText(temp_image, "isVisited?", (213,141-20), 0, 1.0, (255,255,255), 2)     
    # cv2.imwrite(f'{i:02d}_planet_crop.png', temp_image)
    cv2.imshow('temp',imutils.resize(temp_image, height=720))
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
      exit()

  if mn0 < 0.01:
    log(ilog,f'{getframeinfo(currentframe()).lineno} Visited matched')

    # scan system name at top
    crop_image = large_image[P0y+141:P0y+141+58,P0x+214+535:P0x+214+535+575]
    ret,thresh = cv2.threshold(crop_image,160,255,cv2.THRESH_BINARY_INV)
    tentative = stripped(pytesseract.image_to_string(thresh))
    tentative = re.sub(r'[ |_.]+$','',tentative)
    log(ilog,f'{getframeinfo(currentframe()).lineno} tentative: \'{tentative}\', shape:{crop_image.shape}')
    if tentative in fix: 
      tentative = fix[tentative]
      print(f'fixed={tentative}')
    work_image[346:346+58,7:7+575] = thresh
    if 'v' in dbug:
      cv2.imshow('work',work_image)

    #------------------ card search window ----------------------------

    log(ilog,f'{getframeinfo(currentframe()).lineno} locate card icon in search area')
    # crop_image = large_image[P0y+142+84:P0y+142+84+643,P0x+220+363:P0x+220+363+688]
    crop_image = large_image[P0y+226:P0y+226+643,P0x+583:P0x+583+688]
    result = cv2.matchTemplate(const_image['card'], crop_image, cv2.TM_SQDIFF_NORMED)
    mn1,_,mn1Loc,_ = cv2.minMaxLoc(result)
    P1x,P1y = mn1Loc


    log(ilog,f'{getframeinfo(currentframe()).lineno} Visited: card {mn1:.3f} {mn1Loc}')
    if 'v' in dbug:
      cv2.imshow('card',crop_image)
      # cv2.rectangle(temp_image,(P0x+213-3,P0y+141-3),(P0x+213+211+2,P0y+141+20+2),255,3) # visited system
      cv2.rectangle(temp_image,(P0x+583+P1x-3,P0y+226+P1y-3),(P0x+583+P1x+68+2,P0y+226+P1y+68+2),255,3) # card
      cv2.imshow('temp',imutils.resize(temp_image, height=720))
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

    if mn1 > 0.01:
      x = 0
      log(ilog,f'{getframeinfo(currentframe()).lineno} Exiting: no card station= {tentative}')

      return True, tentative, False # visited but no card

    # ---------------------------------------------------------------------------------------

    # locate card title
    log(ilog,f'{getframeinfo(currentframe()).lineno} locate card title')
    gray2_image = large_image[P0y+226+P1y+7:P0y+226+P1y+7+35,P0x+583+20:P0x+583+20+420]
    ret,thresh = cv2.threshold(gray2_image,160,255,cv2.THRESH_BINARY_INV)
    card_title = stripped(pytesseract.image_to_string(thresh))[:22]
    card_title = re.sub(r'[ |_.]+$','',card_title)
    if card_title in fix: card_title = fix[card_title]
    log(ilog,f'card title= [{card_title}]')

    work_image[406:406+35,7:7+420] = thresh
    if 'v' in dbug:
      cv2.imshow('work',work_image)

    # is this a system card? mn < 0.01 (valid check !)
    card2_image = large_image[P0y+226+P1y+86:P0y+226+P1y+86+240,P0x+583+24:P0x+583+24+60]
    result = cv2.matchTemplate(const_image['sicon'], card2_image, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    M3x,M3y = mnLoc
    log(ilog,f'{getframeinfo(currentframe()).lineno} Biome: sicon {mn:.3f} {mnLoc} does planet card have a system icon?')

    if 'v' in dbug:
      cv2.rectangle(temp_image,(P0x+583+24-3,P0y+226+P1y+86-3),(P0x+583+24+60+2,P0y+226+P1y+86+240+2),255,3) # card
      cv2.imshow('icon',cv2.hconcat([
        card2_image[M3y:M3y+52,M3x:M3x+52],
        np.full((52,2),240,dtype='uint8'),
        const_image['sicon'] ]))
      cv2.imshow('temp',imutils.resize(temp_image, height=720))
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()
      cv2.destroyWindow('icon')

    # ---------------------------------------------------------------------------------------

    if mn < 0.05:
 
      # locate system name
      gray_image = crop_image[P1y+7:P1y+7+35,20:20+420]
      ret,thresh = cv2.threshold(gray_image,160,255,cv2.THRESH_BINARY_INV)
      work_image[:35,7:7+420] = thresh
      card_title = stripped(pytesseract.image_to_string(thresh))[:22]
      card_title = re.sub(r'[ |_.]+$','',card_title)
      if card_title in fix: 
        card_title = fix[card_title]
        # print(f'fixed={card_title}')
      log(ilog,f'{getframeinfo(currentframe()).lineno} system title="{card_title}"')

      gray_image = crop_image[P1y+39+M3y+45:P1y+39+M3y+45+101,85:85+435]
      print(gray_image.shape)
      ret,thresh = cv2.threshold(gray_image,110,255,cv2.THRESH_BINARY_INV)

      if 'v' in dbug:
        cv2.imshow('info',gray_image)
        cv2.imshow('work',work_image)
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
          exit()
        cv2.destroyWindow('info')
      work_image[35:35+101,7:7+435] = thresh

      sysinfo = pytesseract.image_to_string(thresh)
      for i in range(6): 
        sysinfo = re.sub(si[i][0], si[i][1], sysinfo, re.MULTILINE)
      sysinfo = re.findall(r'^.+?$', sysinfo[:-1], re.MULTILINE)

      nl = "\n"
      log(ilog, f'{nl.join(sysinfo)}')
      if tentative not in db:
        db[tentative] = {}
        db[tentative]['System Info'] = sysinfo
        if tentative in fixsi: 
          db[tentative]['System Info'] = fixsi[tentative]
        db[tentative]['Technology'] = {}
        db[tentative]['Buy Sell'] = {}
      else:
        db[tentative]['System Info'] = sysinfo
        if tentative in fixsi: 
          db[tentative]['System Info'] = fixsi[tentative]
        
      log(ilog,f'{getframeinfo(currentframe()).lineno} Exiting: sysinfo card')
      x = 0
      return True, tentative, True # visited plus sicon

    # ---------------------------------------------------------------------------------------

    # does planet card have a base icon?
    # base_image = crop_image[P1y+91:P1y+91+52,30:30+51]
    result = cv2.matchTemplate(const_image['bicon'], card2_image, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    M3x,M3y = mnLoc
    log(ilog,f'{getframeinfo(currentframe()).lineno} Biome: bicon {mn:.3f} {mnLoc} does planet card have a base icon?')

    if 'v' in dbug:
      print(cv2.minMaxLoc(result))#,base_image.shape)
      cv2.imshow('icon',card2_image[M3y:M3y+51,M3x:M3x+51])
      # cv2.imshow('icon',cv2.hconcat([
      #   base_image,
      #   np.full((51,1),240,dtype='uint8'),
      #   const_image['bicon'] ]))
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()
      cv2.destroyWindow('icon')


    work_image[443:443+51,7:7+51] = np.full((51,51),240,dtype="uint8") 
    if mn < .01:
      P1y += 89
      work_image[443:443+51,7:7+51] = card2_image[M3y:M3y+51,M3x:M3x+51] # base_image

    # locate planet type
    gray_image = crop_image[P1y+39+40:P1y+39+40+28,30:30+250]
    ret,thresh = cv2.threshold(gray_image,160,255,cv2.THRESH_BINARY_INV)
    work_image[443:443+28,78:78+250] = thresh
    if 'v' in dbug:
      cv2.imshow('work',work_image)
      k = cv2.waitKey(0) & 0xFF
      if k == 27:
        exit()

    station = tentative
    if card_title not in db[station]:
      db[station][card_title] = {}
      db[station][card_title]['Planet Info'] = []
      db[station][card_title]['Resources'  ] = []

    type_title = stripped(pytesseract.image_to_string(thresh))
    type_title = re.sub(r'[ |_.]+$','',type_title)
    if type_title in fix: type_title = fix[type_title]
    if station in db and card_title in db[station]:
      log(ilog,f'{getframeinfo(currentframe()).lineno} Biome= `{type_title}`')
      db[station][card_title]['Planet Info'].insert(0, "Biome: "+type_title)

      if any(any(key in info for key in corrupted) for info in db[station][card_title]['Planet Info']):
        db[station][card_title]['Resources'].append('Dissonance detected')
    else:
      log(ilog,f'{getframeinfo(currentframe()).lineno} Biome: error: db[{station}][{card_title}]')
    print('planet type=',type_title)

    return True, tentative, False
  return False, None, False
