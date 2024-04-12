from inspect import currentframe, getframeinfo
import sys
import getopt
import json
import re
import getopt 
ilog = 0
dbug = ''
title = 'Playground'
argv = sys.argv[1:] 
try: 
  opts, args = getopt.getopt(argv, "f:t:d:", ["file =", "title =", "dbug ="]) 
except: 
  print("SYNTAX: python pipj.py -f 0|1|2|t -t title") 
for opt, arg in opts: 
  if opt in ['-f', '--file']: 
    ilog = arg 
  elif opt in ['-t', '--title']: 
    title = arg 
  elif opt in ['-d', '--dbug']: 
    dbug = arg 
print(f'{sys.argv}')

# if len(sys.argv) > 1:
#   ilog = sys.argv[1] # json file number
# else:
#   print("SYNTAX: python pipk.py 0|1|2|t")
#   quit()

def legend(sc,t,hn,ai,jf,cc):
  return "".join([
    f'<img src="i/badge-{sc}.png"/>&hairsp;',    
    f'<img src="i/badge-{t}.png"/>&hairsp;',    
    f'<img src="i/badge-{(["hn2","ai"])[ai==1]}.png"/> ',    
    f'<img src="i/class-{cc}.png"/>'])

badges = {
  "Nitogu":   legend(**{'sc':'b','t':2,'hn':1,'ai':0,'jf':1,'cc':'c'}),
  "Achara":   legend(**{'sc':'g','t':2,'hn':0,'ai':1,'jf':1,'cc':'c'}),
  "Lolringor":legend(**{'sc':'g','t':2,'hn':0,'ai':1,'jf':1,'cc':'a'}),
  "Suitaak":  legend(**{'sc':'y','t':2,'hn':1,'ai':0,'jf':1,'cc':'b'}),
  "Doludes":  legend(**{'sc':'y','t':2,'hn':0,'ai':1,'jf':1,'cc':'b'}),
  "Erlingdi": legend(**{'sc':'y','t':2,'hn':0,'ai':1,'jf':1,'cc':'c'})
}

pirates = ["Bandab","Odusha"]
atlas = ["Yelobarn","Yusvadbeat XII","Bandab"]
poi = {
  "Ikoka 45/G1":     ["POI: <div class='poi rd'>Predators</div> <img src='i/paws.png'/>"],
  "Vistiraqu Hanai": ["POI: <div class='poi rd'>Predators</div> <img src='i/paws.png'/>"],
  "Oupol III":       ["POI: <div class='poi bl'>Storm Crystals</div> <img src='i/crystals.png'/>"],
  "Oyook 52/G8":     ["POI: <div class='poi gr'>Curious Deposit</div> <img src='i/curious.png'/>"],
  "Poor":            ["Original Name: <div class='poi on'>Kearbo-Nagyan</div>"],
  "Base":            ["Original Name: <div class='poi on'>Daytosira XIV</div>"],

  "Wibordo VI":      ["POI: <div class='poi bl'>Storm Crystals</div> <img src='i/crystals.png'/>"],
  "Onrovi":          ["POI: <div class='poi bl'>Storm Crystals</div> <img src='i/crystals.png'/>"],
  "Pipinugst":       ["POI: <div class='poi bl'>Storm Crystals</div> <img src='i/crystals.png'/>"],
}

'''
  # print(f'sc:{sc.upper()},t:{t},hn:{hn},ai:{ai},jf:{jf},cl:{cc}-{color[cc]}')
# f'CL: <div class="pol {color[cc]} k">{cc.upper()}</div>'])
# print(legend(**{'s':'r','t':2,'hn':0,'ai':0,'jf':1,'cl':'a'}))
# quit()

# <div>SC: <div class="pol yl">Y</div> T: <div class="pol bl">2</div> DF: <div class="pol br">HN</div> <div class="pol no">AI</div> <div class="pol gr">JF</div> CL: <img class="cc" src="b.png"/></div>

  "Ikoka 45/G1":     ["POI: <div class=\"poi rd\">Predators</div> <img src=\"predator_icon.png\"/>"],
  "Vistiraqu Hanai": ["POI: <div class=\"poi rd\">Predators</div> <img src=\"predator_icon.png\"/>"],
  "Oupol III":       ["POI: <div class=\"poi bl\">Storm Crystals</div>"],
  "Oyook 52/G8":     ["POI: <div class=\"poi gr\">Curious Deposit</div>"],
  "Poor":            ["Original Name: <div class=\"poi on\">Kearbo-Nagyan</div>"],
  "Base":            ["Original Name: <div class=\"poi on\">Daytosira XIV</div>"],

  "Toyabe IX":       ["<div class=\"poi tr\">Tip:</div> Buy 100&times; Salt, Artifact Chart, Solar Mirror &rarr; <a href=\"https://nomanssky.fandom.com/wiki/High-Power_Sonar\">High-Power Sonar <img src='linkicon1.png'></a>"],
  "Nafut Gamma":     ["POI: <div class=\"poi yl\">Ms 1.3</div> Exobotany",
                      "<blockquote>Discover planetary flora: 6</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> A-class Scanner",
                      "POI: <div class=\"poi yl\">Ms 3.3</div> Life In All Its Forms",
                      "<blockquote>Discover planetary fauna: 12</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> Haz-Mat Gauntlets plans",
                      "POI: <div class=\"poi yl\">Ms 3.1</div> One Man's Treasure",
                      "<blockquote>Dig up buried items: 3</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> &times;13 Salvaged Data &rarr; .7M u",
                      "POI: <div class=\"poi yl\">Ms 1.6</div> Scavenger",
                      "<blockquote>Repair damaged starship components: 3</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> Decorative Base Parts Set",
                      "<div class=\"poi tr\">Tip:</div> Mine Copper, Silver",
                      "POI: <div class=\"poi yl\">Ms 2.3</div> Stardust",
                      "<blockquote>Destroy astroids: 55</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> Wonder Project plans",
                      "POI: <div class=\"poi yl\">Ms 1.1</div> Escape Velocity",
                      "<blockquote>Take to the stars</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 5.2</div> Astrolinguistics",
                      "<blockquote>Learn new words: 16</blockquote>"],
  "Nash 33/W4":      ["POI: <div class=\"poi yl\">Ms 1.2</div> Homecoming",
                      "<blockquote>Establish a base</blockquote>",
                      "<div class=\"poi tr\">Tip:</div> <a target='_blank' href='homecoming.jpg'>Wait \"Base Computer Online\" <small>&#x2639;</small> <img src='linkicon1.png'></a>",
                      "POI: <div class=\"poi yl\">Ms 2.4</div> Expansion",
                      "<blockquote>Grow your base</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> Pre-Packaged Personal Refiner",
                      "POI: <div class=\"poi yl\">Ms 2.6</div> Memento",
                      "<blockquote>Build a Wonder Project</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 3.2</div> Grand Tour",
                      "<blockquote><table>"
                      "<tr><td>Scorched:&nbsp;<td>Doriguc VII // Rowbrig Delta"
                      "<tr><td>Airless: <td>Doriguc VII // Hats 43/L7"
                      "<tr><td>Frozen: <td>Doriguc VII // Nash 33/W4</table></blockquote>",
                      "<div class=\"poi tr\">Reward:</div> Nutrient Processor"],
  "Hunslowe":        ["POI: <div class=\"poi yl\">Ms 1.7</div> <div class=scx>r1</div> Archive <div class=sca>-28.04, +144.27</div>"],
  "Spinarr Kesen":   ["POI: <div class=\"poi yl\">Ms 2.7</div> <div class=scx>r2</div> Portal <div class=sca>-12.89, +67.56</div>",
                      "POI: <div class=\"poi yl\">Ms 4.1</div> Relic Hunter",
                      "<blockquote>Collect ancient artifact: 1</blockquote>",
                      "<div class=\"poi tr\">Reward:</div> High-Power Sonar",
                      "POI: <div class=\"poi yl\">Ms 4.2</div> Fallen Giants",
                      "<blockquote>Visit the site of a sunken freigther</blockquote>"],
                      # "<div class=\"poi tr\">Base:</div> Sunken Freighter Omega Expedition <div class=sca>+24.14, +63.65</div>"],
  "Bandab":          ["<div class=scp><b>Distance:</b></div> 8 ly &rarr; Doriguc VII",
                      "POI: <div class=\"poi yl\">Ms 1.4</div> Interstellar",
                      "<blockquote>Warp to new system</blockquote>",
                      "POI: <div id=tip class=\"poi yl\">Ms 1.5</div> Anomaly's Heart",
                      "<blockquote>Explore the Anomaly</blockquote>",
                      "<div class=\"poi tr\">Tip:</div>",
                      "<div><div> Construction: Ceiling Light (1&times; Salvaged Data)</div></div>",
                      "<div><div> Ares: 1&times; Photon Cannon C-class (80&times; Nanites &rarr; 125&times; Cadmium)</div></div>",
                      "<div><div> Synth: Acid, Lubricant, Unstable Gel, Liquid Explosives (1000&times; Nanites)</div></div>",
                      "<div><div> Eos: Advanced Mining Laser (75&times; Nanites) [Optional]</div></div>",
                      "<div><div> Use Anomaly Teleport to finish <div class=\"poi yl\">Ms 2.4</div> Expansion<i>!</i></div></div>",
                      "POI: <div class=\"poi yl\">Ms 3.4</div> Hot Pursuit",
                      "<blockquote>Smuggle contraband: 120,000 units</blockquote>",
                      "<div class=\"poi tr\">Tip:</div> Buy 100&times; Pugneum [Optional]",
                      "<div class=\"poi tr\">Reward:</div> Craftable component plans",
                      "&nbsp;",
                      "<div class=\"poi rd\">Note:</div> Must complete <div class=\"poi yl\">Ms 1.7</div> <div class=scx>r1</div> first<i>!</i>",
                      # "just talk to Nada before the Atlas. <br>There is an interceptor crash site "
                      # "26 ly away at Mazuna // Onana <div class=sca>+44.42, +25.95</div>",
                      "POI: <div class=\"poi yl\">Ms 2.1</div> Atlas Rises",
                      "<div class=\"poi tr\">Reward:</div> Memory of Ocean",
                      "<div>99&times; Silicate Powder<br>66&times; Tritium<br>33&times; Salt</div>",
                      "<div class=\"poi tr\">2<sup>nd</sup> Reward:</div> S-class Hyperdrive",
                      "POI: <div class=\"poi yl\">Ms 2.2</div> Reality Grains",
                      "<div class=\"poi tr\">Reward:</div> Memory of Conquest",
                      "<div>99&times; Chromatic Metal<br>66&times; Magnetised Ferrite<br>33&times; Sodium Nitrate</div>",
                      "<div class=\"poi tr\">2<sup>nd</sup> Reward:</div> Carrier AI Fragment",
                      "<blockquote>Locates crashed interceptors</blockquote>"
                      "POI: <div class=\"poi yl\">Ms 3.6</div> Unbounded",
                      "<div class=\"poi tr\">Reward:</div> Memory of Bones",
                      "<div>99&times; <a href=\"javascript:sv('tip')\">Cadmium <img src='linkicon1.png'></a><br>66&times; Di-hydrogen<br>33&times; Ionised Cobalt</div>",
                      "POI: <div class=\"poi yl\">Ms 4.6</div> Depp Glass",
                      "<div class=\"poi tr\">Reward:</div> Memory of Void",
                      "<div>99&times; Pugneum<br>66&times; Condensed Carbon<br>33&times; Gold</div>",
                      "POI: <div class=\"poi yl\">Ms 5.5</div> Creation",
                      "<blockquote>Witness the final memory</blockquote>"],
  "Haku 57/Q1":      ["POI: <div class=\"poi yl\">Ms 3.7</div> <div class=scx>r3</div> Crashed Freighter <div class=sca> -20.97, -85.18</div>"],
  "New Wadhabie":    ["POI: <div class=\"poi yl\">Ms 4.7</div> <div class=scx>r4</div> Portal <div class=sca> +32.94, +179.59</div>",
                      "<div class=\"poi tr\">Tip:</div> <a href='https://youtu.be/UiyooZ3SVA4?t=1693'>Jason Plays <img src='linkicon1.png'></a>",
                      "POI: <div class=\"poi yl\">Ms 4.5</div> Palate Cleanser",
                      "<blockquote>Bake some biscuits</blockquote><div>"
                      "Sweet Root &rarr; Processed Sugar<br>"
                      "Heptaploid Wheat &rarr; Refined Flour<br>"
                      "Processed Sugar + Refined Flour &rarr; Sugar Dough<br>"
                      "Sugar Dough + Salt &rarr; Salty Cruncher</div>",
                      "<div class=\"poi tr\">Reward:</div> 2&times; S-class Mining Beam",
                      "POI: <div class=\"poi yl\">Ms 5.1</div> The Fallen",
                      "<blockquote>Visit traveler gravesite</blockquote>",
                      "<div class=\"poi tr\">Tip:</div> 820u West of <div class=scx>r4</div> Portal",
                      "<div class=\"poi tr\">Reward:</div> Indium Hyperdrive",
                      "POI: <div class=\"poi yl\">Ms 4.4</div> Boundary Failure",
                      "<blockquote>Eliminate Sentinels: 25</blockquote>"],
  "Gartfol X":       ["POI: <div class=\"poi yl\">Ms 3.5</div> Assembly Required",
                      "<blockquote>Manufactured Liquid Explosives</blockquote><div>"
                      "Cactus Flesh &times;200 &raquo; Unstable Gel &times;1<br>"
                      "Mordite &times;25 + Fungal Mould &times;200 &raquo; Acid &times;1<br>"
                      "Acid &times;1 + Unstable Gel &times;1 &raquo; Liquid Explosive &times;1</div>",
                      "<div class=\"poi tr\">Tip:</div>", 
                      "<div>Okubun-Chadr // Aratae XIV &rarr; Fungal Mould</div>",
                      "<div>Faecium x3 &rarr; Mordite x2</div>",
                      "<div class=\"poi tr\">Reward:</div> S-class Movement"],
  "Yovetrowl III":   ["POI: <div class=\"poi bl\">Storm Crystals</div>",
                      "POI: <div class=\"poi yl\">Ms 4.3</div> Radiant Flight",
                      "<blockquote>Repair a crashed interceptor</blockquote>",
                      "<div class=\"poi tr\">Base:</div> Bucefaldkowo <div class=sca>+19.47, +13.66</div>",
                      "<div class=\"poi tr\">Tip:</div> Phase 3 Reward: Atlas Sceptre has an Advanced Mining Laser",
                      "<div><div><div><div><div>Use Carrier AI Fragment to locate a crashed interceptor</div></div></div></div></div>"],
  "Mazuna":          ["<div class=scp><b>Original Name:</b></div> Mazuna-Puqia",
                      "<div class=scp><b>Distance:</b></div> 26 ly &rarr; Bandab"],
  "Onana":           ["POI: <div class=\"poi yl\">Ms 4.3</div> Radiant Flight",
                      "<blockquote>Repair a crashed interceptor <div class=\"sca n\">+44.42, +25.95</div></blockquote>",
                      #"<div class=\"poi tr\">Base:</div> Bucefaldkowo <div class=sca>+44.42, +25.95</div>",
                      "<div class=\"poi tr\">Tip:</div> Phase 3 Reward: Atlas Sceptre has an Advanced Mining Laser"],
  "Yusvadbeat XII":  ["POI: <div class=\"poi yl\">Ms 5.6</div> Eclipse",
                      "<blockquote>Return to the Atlas</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 2.5</div> To Infinity",
                      "<blockquote>Enter a black hole</blockquote>",
                      "<div><div class=scp><b>Distance:</b></div> 12 ly &rarr; Ilnyev</div>"],
  "Upacton Sigma":   ["POI: <div class=\"poi yl\">Ms 5.4</div> Xenophile",
                      "<blockquote>Discover exotic creatures: 1</blockquote>"],
  "Gezhel-Olin":     ["Stellar Class: E2<span class='dot gr'></span>",
                      "Dissonance: Detected<span class='dot co'></span>",
                      "<div class=scp><b>Distance:</b></div> 22 ly &rarr; Dovour-Jaus"],
  "Amling":          ["Stellar Class: B1pf<span class='dot bl'></span>",
                      "POI: <div class=\"poi yl\">Ms 5.3</div> Blue Expanse",
                      "<blockquote>Visit a blue star</blockquote>"],
  "Boeot Prime":     ["POI: <div class=\"poi yl\">Ms 5.7</div> <div class=scx>r5</div> Portal <div class=sca> +27.44, +11.24</div>"],
  

  # "Yelobarn":        ["<div class=\"poi tr\">Note:</div> You may be sent to Bandab instead, "
  #                     "just talk to Nada before the Atlas. <br>There is an interceptor crash site "
  #                     "26 ly away at Mazuna // Onana <div class=sca>+44.42, +25.95</div>",
  #                     "POI: <div class=\"poi yl\">Ms 2.1</div> Atlas Rises",
  #                     "<div class=\"poi tr\">Reward:</div> Memory of Ocean",
  #                     "<div>99&times; Silicate Powder<br>66&times; Tritium<br>33&times; Salt</div>",
  #                     "POI: <div class=\"poi yl\">Ms 2.2</div> Reality Grains",
  #                     "<div class=\"poi tr\">Reward:</div> Memory of Conquest",
  #                     "<div>99&times; Chromatic Metal<br>66&times; Magnetised Ferrite<br>33&times; Sodium Nitrate</div>",
  #                     "<div class=\"poi tr\">2<sup>nd</sup> Reward:</div> Carrier AI Fragment",
  #                     # "Talk to Nada before the Atlas. I got the reward, Memory of Ocean from the atlas and completed"
  #                     "<blockquote>Locates crashed interceptors</blockquote>"
  #                     # "1<sup>st</sup>: Create a restore point before you use it<br>"
  #                     # "2<sup>nd</sup>: Don't get out of your ship until you see the crash site</blockquote>",
  #                     "POI: <div class=\"poi yl\">Ms 3.6</div> Unbounded",
  #                     "<div class=\"poi tr\">Reward:</div> Memory of Bones",
  #                     "<div>99&times; <a href=\"javascript:sv('tip')\">Cadmium <img src='linkicon1.png'></a><br>66&times; Di-hydrogen<br>33&times; Ionised Cobalt</div>",
  #                     "POI: <div class=\"poi yl\">Ms 4.6</div> Depp Glass",
  #                     "<div class=\"poi tr\">Reward:</div> Memory of Void",
  #                     "<div>99&times; Pugneum<br>66&times; Condensed Carbon<br>33&times; Gold</div>",
  #                     "POI: <div class=\"poi yl\">Ms 5.5</div> Creation",
  #                     "<blockquote>Witness the final memory</blockquote>"],

  "Oishida":         ["POI: <div class=\"poi yl\">Ms 1.7</div> Words for Friends",
                      "<blockquote>Learn Gek Words: 6</blockquote>",
                      "<div><div class=\"poi tr\">Tip:</div> Talk to every Korvax in every space station you see.</div>",
                      "POI: <div class=\"poi yl\">Ms 5.8</div> Stardust",
                      "<blockquote>Destroy asteroids: 40</blockquote>"],
  "Aieus S3":        ["POI: <div class=\"poi rd\">Predators</div> <img src=\"predator_icon.png\"/>",
                      "POI: <div class=\"poi yl\">Ms 2.5</div> Hunter/Killer",
                      "<blockquote>predator aggresion over 27.5pav</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 1.6</div> Companionship",
                      "<blockquote>Adopt companions: 2</blockquote>"],
  "Leigha Yamak":    ["POI: <div class=\"poi yl\">Ms 1.1</div> Planetside",
                      "<div><div class=\"poi tr\">Reward:</div> Hyperdrive plans</div>",
                      "POI: <div class=\"poi yl\">Ms 3.5</div> Mystery Vortex",
                      "<blockquote>Aquire Vortex Cubes: 6</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Craftable Components plans</div>",
                      "POI: <div class=\"poi yl\">Ms 3.7</div> Fear the Sun",
                      "<blockquote>Tunnel underground: 2400u&sup3;</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Portal glyph set</div>",
                      "POI: <div class=\"poi yl\">Ms 4.5</div> Under Pressure",
                      "<blockquote>80u below sea level</blockquote>"],
  "Lehave":          ["POI: <div class=\"poi yl\">Ms 1.8</div> <div class=scx>r1</div> Archive <div class=sca> -52.72, -18.26</div>",
                      "POI: <div class=\"poi yl\">Ms 2.2</div> The Hills are Alive",
                      "<blockquote>Summit a mountain: 625u</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 2.6</div> Deep Freeze",
                      "<blockquote>Planet under -80 &deg;C</blockquote>",
                      "<div><div class=\"poi tr\">Tip:</div> Triggers on a storm.</div>"],
  "Leyc X42":        ["POI: <div class=\"poi yl\">Ms 2.1</div> <div class=scx>r2</div> Archive <div class=sca> +28.08, +148.80</div>"],
  "Keda 50/Q7":      ["POI: <div class=\"poi yl\">Ms 3.1</div> <div class=scx>r3</div> Portal <div class=sca> +15.37, -126.05</div>",
                      "POI: <div class=\"poi yl\">Ms 3.2</div><a style=\"border:0\" href=\"https://youtu.be/lqlIXzMldGI?t=6196\">Unwelcome <img src=\"linkicon1.png\"></a>",
                      "<blockquote>Planet hostility quotient over 84&#37;</blockquote>",
                      "<div>Jiyoda VII // Rediton<br><span>60C3&nbsp;&nbsp;FB52&nbsp;&nbsp;C484</span></div>",
                      "POI: <div class=\"poi yl\">Ms 4.2</div> Anomalous Travel",
                      "<blockquote>Use a Portal</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 5.5</div><a style=\"border:0\" href=\"https://www.reddit.com/r/NoMansSkyTheGame/comments/168okns/voyager_expedition_xenobiology/\">Xenobiology <img src=\"linkicon1.png\"></a>",
                      "<blockquote>Discover 6 exotic creatures</blockquote>",
                      "<div>Flagod XII // Arabab          <br><span>21B3&nbsp;&nbsp;FB52&nbsp;&nbsp;B484</span></div>",
                      "<div>Gurobe-Saco // Hippenwor Ebet <br><a class=pg href=\"javascript:sv('Hippenwor_Ebet')\"><span>100A&nbsp;&nbsp;FB52&nbsp;&nbsp;7484</span> <img src=\"linkicon1.png\"></a></div>",
                      "<div>Erkinf II // Needhab Sigma    <br><span>20B5&nbsp;&nbsp;FB52&nbsp;&nbsp;A484</span></div>",
                      "<div>Brefrid-Wanab // Omle Delta   <br><span>1052&nbsp;&nbsp;0394&nbsp;&nbsp;DEF2</span></div>",
                      "<div>Aechuz // Sori Minor          <br><span>103F&nbsp;&nbsp;FB52&nbsp;&nbsp;9484</span></div>",
                      "<div>Gesorda // Major              <br><span>105C&nbsp;&nbsp;FB52&nbsp;&nbsp;6483</span></div>"],
  "Hippenwor Ebet":  ["POI: <div class=\"poi yl\">Ms 5.5</div> Xenobiology",
                      "<blockquote>Discover 6 exotic creatures</blockquote>"],
  "Aturm Major":     ["POI: <div class=\"poi yl\">Ms 4.1</div> <div class=scx>r4</div> Crashed Freighter <div class=sca> +48.59, -145.32</div>"],
  "Enaica K14":      ["POI: <div class=\"poi yl\">Ms 5.1</div> <div class=scx>r5</div> Archive <div class=sca> -67.01, -111.52</div>"],
  "Ambatu-Don":      ["POI: <div class=\"poi yl\">Ms 1.2</div> Interstellar",
                      "<blockquote>Went to a new system</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Base Computer plans</div>",
                      "POI: <div class=\"poi yl\">Ms 3.8</div> Grah! Grah! Grah!",
                      "<blockquote>Learn Vy'keen Words: 7</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 4.6</div> Event Horizon",
                      "<blockquote>Enter a Black Hole</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Salvaged Frigate Module &times;15</div>"],
  "Efkad":           ["POI: <div class=\"poi bl\">Storm Crystals</div>",
                      "POI: <div class=\"poi yl\">Ms 2.3</div> Bottled Lightning",
                      "<blockquote>Collect Storm Crystals: 7</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Wonder Projector plans</div>",
                      "POI: <div class=\"poi yl\">Ms 1.3</div> Home Coming",
                      "<blockquote>Establish a base</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 2.7</div> The Collector",
                      "<blockquote>Build a Wonder Projector</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Specialized warp blueprints</div>",
                      "POI: <div class=\"poi yl\">Ms 2.8</div> All That Glitters <img src=\"scrapicon.png\">",
                      "<blockquote>Salvageable Scrap: 1</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 5.4</div><a style=\"border:0\" href=\"herbivore.jpg\">Hooves of Thunder <img src=\"photoicon2.png\"></a>", 
                      "<blockquote>Herbivore 7m high</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 4.3</div> Priceless",
                      "<blockquote>Earn 200000 on a creature scan</blockquote>",
                      "<div><div class=\"poi tr\">Tip:</div> Scanner modules need:<br>'Fauna Analysis Rewards'</div>"],
  "Batan 36/R3":     ["POI: <div class=\"poi yl\">Ms 2.4</div> Corrosive Blood",
                      "<blockquote>Creature blood pH under 2.5</blockquote>",
                      "<div><div class=\"poi tr\">Reward:</div> Pre-Packaged Haz-Mat Gauntlets</div>"],
  "Myon XV":         ["POI: <div class=\"poi yl\">Ms 3.4</div> Hot Blooded",
                      "<blockquote>Creature body temp over 60 &deg;C</blockquote>"],
  "Gurobe-Saco":     ["POI: <div class=\"poi yl\">Ms 5.3</div> Eternal Garden",
                      "<blockquote>Planet paradise quotient over 90&#37;</blockquote>"],
  "Gatreadle X":     ["POI: <div class=\"poi bl\">Storm Crystals</div>"],
                     #"POI: <div class=\"poi bl\">100 Feet deep (base) -18.54, +135.98</div>"],

  "Ahei XV":         ["POI: <div class=\"poi yl\">Ms 1.1</div> They Hear Us"],
  "Dalnye":          ["POI: <div class=\"poi yl\">Ms 1.2</div> The Wayfarer"],
  "Sudb":            ["POI: <div class=\"poi on\">Colossal Archive</div>"],
  "Minemo Alpha":    ["POI: <div class=\"poi on\">Colossal Archive</div>"],
  "Irakihil Prime":  ["POI: <div class=\"poi yl\">Ms 1.3</div> Etched in Glass - <div class=\"poi on\">Colossal Archive</div>",
                      "POI: <div class=\"poi yl\">Ms 1.4</div> Eyes to See",
                      "<div><div class=\"poi bh\">Construct Head</div><br>&times;4 Metal Plating<br>&times;1 Ion Battery<br>&times;1 Microprocessor</div>",
                      "<div><div class=\"poi tr\">Reward:</div> Advanced Mining Laser</div>"],
  "Xigbartta":       ["POI: <div class=\"poi yl\">Ms 1.5</div> Prayer I",
                      "POI: <div class=\"poi yl\">Ms 1.6</div> Atlas Seed",
                      "<div><div class=\"poi bh\">Seed of Dreams</div><br>&times;100 Chromatic Metal</div>"],
  "Eyaksh VI":       ["POI: <div class=\"poi yl\">Ms 2.3</div> Radiance - Harvest Radiant Shard: 16",
                      "POI: <div class=\"poi yl\">Ms 2.7</div> The Living Void - Harvest Alantideum: 256",
                      "<div><div class=\"poi tr\">Reward:</div> Quad Servo</div>",
                      "POI: <div class=\"poi yl\">Ms 1.7</div> Pilgrimage 1 <div class=sca> +30.84, -22.74</div>"],
  "Riko":            ["POI: <div class=\"poi yl\">Ms 2.1</div> Pilgrimage 2 <div class=sca> -20.27, +77.41</div>",
                      "POI: <div class=\"poi yl\">Ms 2.2</div> To Cast a Shadow",
                      "<div><div class=\"poi tr\">Reward:</div> Blueprint</div>",
                      "<div><div class=\"poi bh\">Lubricant</div><br>&times;50 Facium<br>&times;500 Gamma Root</div>",
                      "POI: <div class=\"poi yl\">Ms 2.4</div> Hands to Grasp",
                      "<div><div class=\"poi bh\">Construct Limbs</div><br>&times;1 Quad Servo "
                     +"<a style=\"border:0\" href=\"javascript:sv('Eyaksh_VI')\"><img src=\"linkicon.png\"></a>"
                     +"<br>&times;3 Carbon Nanotubes<br>&times;1 Wiring Loom</div>",
                      "<div><div class=\"poi tr\">Reward:</div> Haz-Mat Gauntlets</div>"],
  "Braindead":       ["POI: <div class=\"poi yl\">Ms 2.5</div> Prayer II",
                      "POI: <div class=\"poi yl\">Ms 2.6</div> Atlas Seed",
                      "<div><div class=\"poi bh\">Seed of Power</div><br>&times;1 Seed of Dreams<br>&times;100 Pure Ferrite</div>"],
  "Nodalloma Hita":  ["POI: <div class=\"poi yl\">Ms 3.1</div> Pilgrimage 3: <div class=sca> -15.19, +67.26</div>",
                      "POI: <div class=\"poi yl\">Ms 3.2</div> The Will to Exist",
                      "POI: <div class=\"poi yl\">Ms 3.4</div> A Shell to Make Whole",
                      "<div><div class=\"poi bh\">Construct Shell</div><br>&times;210 Magnetised Ferrite<br>&times;3 Crystal Sulphide<br>&times;2 Life Support Gel"],
  "Iijiey XV":       ["POI: <div class=\"poi yl\">Ms 3.5</div> Prayer III",
                      "POI: <div class=\"poi yl\">Ms 3.6</div> Atlas Seed",
                      "<div><div class=\"poi bh\">Seed of Will</div><br>&times;1 Seed of Power<br>&times;100 Ionised Cobalt</div>"],
  "Olivere Omega":   ["POI: <div class=\"poi bl\">Storm Crystals</div>",
                      "POI: <div class=\"poi yl\">Ms 4.1</div> Pilgrimage 4 <div class=sca>+8.97, -39.20</div>",
                      "POI: <div class=\"poi yl\">Ms 4.2</div> Independent Spirit",
                      "POI: <div class=\"poi yl\">Ms 4.3</div> Feet to Roam",
                      "<div><div class=\"poi bh\">Construct Legs</div><br>&times;2 Hydraulic Wiring<br>&times;1 Magnetic Resonator<br>&times;2 Lubricant</div>",
                      "<div class=\"sca\">Anomoly: </div><div class=\"poi yl\">Ms 4.6</div> Grand Divergence - Start",
                      "<blockquote>Consult Priest Nada before proceeding to the Atlas.<br>Complete the 'Grand Divergence' milestone to proceed.</blockquote>"],
  "Akraguer Sigma":  ["POI: <div class=\"poi rd\">Predators</div> <img src=\"predator_icon.png\"/>",
                      "POI: <div class=\"poi yl\">Ms 4.6</div> Grand Divergence - Finish",
                      "<div><div class=\"poi tr\">Reward:</div> Echo Seed</div>",
                      # "<blockquote style=\"max-width:450px;\"><div class=\"poi tr\">Tip:</div> Say \"1. Let the tetrahedron in\" to the Monolith before talking to the 'Discordant Interface' and recieve the Pulse Spitter blueprint! Dismantle &times;3 C-Class Pulse Engine modules from Ares in the Anomoly for &times;225 Deuterium. Grab S-Class Shield and Pulse Spitter modules at Yillemma.</blockquote>",
                      # "<div><div class=\"poi tr\">Reward:</div> Pulse Spitter</div>",
                      "POI: <div class=\"poi yl\">Ms 3.3</div> Rampancy - Eliminate Corrupt Sentinels: 19"],
  "Yillemma":        ["POI: <div class=\"poi yl\">Ms 4.4</div> Prayer IV",
                      "<div><div class=\"poi tr\">Reward:</div> Gravitino Balls &times;3</div>",
                      "POI: <div class=\"poi yl\">Ms 4.5</div> Atlas Seed",
                      "<div><div class=\"poi bh\">Seed of Life</div><br>&times;1 Seed of Will<br>&times;5 Magnetised Ferrite</div>",
                      "<div class=\"sca\">Anomoly: </div><div class=\"poi yl\">Ms 4.7</div> The Lifeboat",
                      "<div class=\"sca\">Anomoly: </div><div class=\"poi yl\">Ms 4.8</div> Lost Souls",
                      "<div><div class=\"poi tr\">Reward:</div> Schematic</div>",
                      "<div><div class=\"poi bh\">Resonance Amplifier</div><br>&times;160 Di-hydrogen<br>&times;3 Gravitino Balls"
                     # +"<a style=\"border:0\" href=\"javascript:sv('Toibal')\"><img src=\"linkicon.png\"></a>"
                     +"<br>&times;1 Radiant Shard"],
# "Usaling":         ["POI: <div class=\"poi bl\">Storm Crystals</div>",
  "Usaling":         ["POI: <div class=\"poi yl\">Ms 5.1</div> Pilgrimage 5 <div class=sca>+10.34, +17.16</div>",
                      "POI: <div class=\"poi yl\">Ms 5.2</div> Rebirth",
                      "<div><div class=\"poi bh\">Atlantid Reactor</div><br>&times;1 Antimatter Housing<br>&times;75 Ionised Cobalt<br>&times;1 Crystalised Heart"],
  "Riesid":          ["POI: <div class=\"poi yl\">Ms 5.4</div> Prayer V",
                      "POI: <div class=\"poi yl\">Ms 5.5</div> Atlas Seed",
                      "<div><div class=\"poi bh\">Seed of Hope</div><br>&times;1 Seed of Life<br>&times;25 Chromatic Metal</div>",
                      "<div class=\"sca\">Anomoly: </div><div class=\"poi yl\">Ms 5.6</div> Ignitioin"],



  "Bakkin":          ["<div style=\"display:block; max-width:500px;\"><div class=\"poi tr\">Tip:</div> Create a \"Restore Point\" before <b>learning</b> any upgrade or <b>cooking</b> any recipe. Also, be sure to select the milestone first. <a style=\"border: 0px solid #808080; padding: 0; text-decoration: underline;\" href=\"https://www.youtube.com/watch?v=-2aGoVWiYx0\">How To Speed Run The Utopia Expedition In No Man's Sky</a></div>"],
  "New Kehille":     ["POI: <div class=\"poi yl\">Ms 1.1</div> Foundations - Establish a base",
                      "POI: <div class=\"poi yl\">Ms 1.3</div> Ground Control - Upload a base",
                      "POI: <div class=\"poi yl\">Ms 1.2</div> Provisions - <div class=sct>Checklist</div>:"
                     # +"<blockquote><div class=sct>Checklist before leaving base:</div>"
                     +  "<blockquote>Boltcaster<br>Ammunition<br>Life Support Gel<br>Hermatic Seal<br>Di-hydrogen Jelly<br>Metal Plating</blockquote>",
                     # +"<blockquote>Optional:"
                     # +  "<blockquote>Nutrient Processor: Metal Plating&times;2, Hermetic Seal&times;1, Sodium&times;25<blockquote>Recipe: Carbon &rarr; Creature Pellets</blockquote>Humming Sacs&times;5<blockquote><div class=sct>Reward:</div> Haz-Mat Gauntlets</blockquote>Star Bulbs &rarr; Pilgrimberry &rarr; Pilgrim's Tonic<br>Impulse Beans &rarr; Bittersweet Cocoa<blockquote><div class=sct>Reward:</div> Assortment of cakes</blockquote>Companion (Predators are fast!)</blockquote></blockquote>",
                      "POI: <div class=\"poi yl\">Ms 1.4</div> Planet Link - Deploy an Exocraft",
                      "POI: <div class=\"poi yl\">Ms 2.6</div> Companion - Adopt a companion"
                     +"<blockquote>Predators are fast!</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 2.5</div> Albumen Spawn - Harvest Humming Sacs: 5"
                     +"<blockquote><div class=sct>Reward:</div> Haz-Mat Gauntlets</blockquote>" 
                      "POI: <div class=\"poi yl\">Ms 3.7</div> Local Delicacies"
                     +"<blockquote>Star Bulbs &rarr; Pilgrimberry &rarr; Pilgrim's Tonic<br>Impulse Beans &rarr; Bittersweet Cocoa<br><div class=sct>Reward:</div> Assortment of cakes. Money for Uranium and Pyrite on s.s.</blockquote>",
                     # Nutrient Processor: Metal Plating&times;2, Hermetic Seal&times;1, Sodium&times;25<br>
                     # +"<blockquote><div class=sct>Reward: </div>Haz-Mat Gauntlets<blockquote>" 
                      "POI: <div class=\"poi yl\">Ms 1.6</div> Scenic Route - Travel by Exocraft: 2000u",
                      "POI: <div class=\"poi yl\">Ms 1.5</div> System Link - Locate and Repair your starship",
                      "POI: <div class=\"poi yl\">Ms 1.7</div> Outpost Alpha - Archive +15.11, -14.21"
                     +"<blockquote><div class=\"poi tr\">Tip:</div> Mine Copper,2300 here.</blockquote>"],
  "Pehaelump":       ["POI: <div class=\"poi yl\">Ms 2.7</div> Caldera - Summit a valcano"
                     +"<blockquote><div class=sct>Reward:</div> Pure Ferrite x999, Carbon x999</blockquote>" 
                     +"<blockquote><div class=\"poi tr\">Tip:</div> Mine Pure Ferrite,1000 on the volcano. No sentinels!</blockquote>",
                      "POI: <div class=\"poi yl\">Ms 2.1</div> Outpost Beta - Archive +75.49, +152.10",
                     #  "POI: <div class=\"poi yl\">Settlement #2</div>"
                     # +"<blockquote><div class=scr><b>BUGGED:</b></div> Save before you learn any upgrade.<br> The milestone must be selected to register.<br> You've been <b>WARNED!</b><blockquote> Ironclad<br>Advanced Mechanics<br>Omni-Tool<br>Flight Calculations<blockquote><blockquote>",
                     "POI: <div class=\"poi yl\">Ms 2.4</div> Ironclad"
                     +"<blockquote><div class=sct>Reward:</div> Airburst Engine plans<br><div class=\"poi tr\">Tip:</div> Don't install! <br>Wait for the pre-packaged one at <div class=\"poi yl\">Ms 3.2</div> Assignment Gamma<blockquote>"],
  "New Sesto":       ["POI: <div class=\"poi yl\">Ms 3.1</div> Outpost Gamma - Archive +57.84, +56.40"],
  "Idalth XIV":      ["POI: <div class=\"poi yl\">Ms 4.1</div> Outpost Delta - Trade Post -49.51, +120.77",
                      "POI: <div class=\"poi yl\">Ms 4.6</div> The Cleanse"
                     +"<blockquote><div class=sct>Reward:</div> Construction History<br>"
                     +"<div class=\"poi tr\">Tip:</div> Buy 1x Quantum Computer, 3x Magnetic Resonators and 5x Microprocessors now!</blockquote>"],
  "Endil A8":        ["POI: <div class=\"poi yl\">Ms 5.1</div> Outpost Epsilon - Archive -13.53, +168.79"],


  "Maccleetaw Tami": ["POI: <div class=\"poi yl\">R1</div> Crashed Freighter"],
  "Ammanue":         ["POI: <div class=\"poi yl\">R2</div> Crashed Freighter"],
  "Partlefa P34":    ["POI: <div class=\"poi yl\">R3</div> Crashed Freighter"],
  "Yowoo":           ["POI: <div class=\"poi yl\">R4</div> Crashed Freighter"],
  "Eotis":           ["POI: <div class=\"poi yl\">R5</div> Crashed Freighter"],
  "Odvigal":         ["<div class=scp><b>Distance:</b></div> 55 ly &rarr; Nomyussko"],
  "Erylanaith Otsu": ["POI: <div class=\"poi bl\">Storm Crystals</div>"],
  "Jarn XII":        ["POI: <div class=\"poi yl\">Ms 4.4</div> Reclamation - Restore a crashed ship"
                     +"<blockquote><div class=sct>Base:</div> Crashed class-A Shuttle -4.09, +36.04<blockquote>"],


  "Oginic-Roran II":["Distance: 35 ly &rarr; Hantury VIII"],
  "Gaapo VI":      ["POI: <div class=\"poi yl\">Ms 3.4</div> Calcified Echoes - Collect Storm Crystals: 2"
                   +"<blockquote>Credit: <a href=\"https://youtu.be/7-p2lJsgIKk?t=82\" target=_blank><img src=yt_icon.png> Scottish Rod</a></blockquote>"], # .encode('utf-8'),
  "Loydon K25":    ["POI: Tamable non-aggressive predators <img src=\"predator_i_icon.png\"/>",
                    "POI: <div class=\"poi yl\">Ms 2.2</div> The Anchor - Establish a base on an infested world"],
  "Chater-Muk X":  ["Stellar Class: K9<span class='dot rd'></span>",
                    "Distance: 98 ly &rarr; Kusinst"
                   +"<blockquote>Credit: <a href=\"https://youtu.be/PxOG_OcmqVo?t=746\" target=_blank><img src=yt_icon.png> Xaine's World</a></blockquote>"], # .encode('utf-8'),
  "Neyang-Uga":    ["Distance: 57 ly &rarr; Chater-Muk X",
                    "POI: <div class=\"poi yl\">Ms 4.3</div> Hot Pursuit - Smuggle contraband: 500,000 units"],
  "Washeyu-Hebe":  ["Stellar Class: E5f<span class='dot gr'></span>"],
  "Yilis IV":      ["POI: <div class=\"poi yl\">Ms 2.6</div> Fallen Giants - Explore a freighter crash site"
                   +"<blockquote><div class=sct>Base:</div> Crashed Freighter -15.79, -137.77<blockquote>"],
  "Abuj Tau":      ["POI: <div class=\"poi yl\">Ms 4.4</div> Banished Glass - Shut down Sentinel Pillar"
                   +"<blockquote><div class=sct>Base:</div> Pillar -16.20, +42.37<blockquote>"],
  "Lowest Mano":   ["POI: <div class=\"poi yl\">Starting Planet</div>",
                    "POI: Tamable non-aggressive predators <img src=\"predator_i_icon.png\"/>",
                    "POI: <div class=\"poi yl\">Ms 1.4</div> Iterate / Repeat - <div class=\"poi rd\">Die</div>",
                    "POI: <div class=\"poi yl\">Ms 1.1</div> Remembrance - Absorb a memory fragment",
                    "POI: <div class=\"poi yl\">Ms 1.2</div> A New Beginning - Locate your starship",
                    "POI: <div class=\"poi yl\">Ms 1.3</div> Observing The Cycle - Repair your starship"
                   +"<blockquote><div class=sct>Reward:</div> Solar Ray plans<blockquote>Magnetised Ferrite &times;50<br>Cobalt &times;50</blockquote></blockquote>", # .encode('utf-8')
                    "POI: <div class=\"poi yl\">Ms 1.5</div> Bounds Testing - Help Polo collect \"Patterns in the loop\""
                   +"<blockquote>1. 250 Liquid Sun<br>"
                   +"2. 200 Ancestral Memories<br>"
                   +"3. 100 Somnal Dust</blockquote>",
                    "POI: <div class=\"poi yl\">Ms 5.3</div> Partners In Time - Help Polo collect \"Patterns in the loop\": 5"],
  "Eynsihept B35": ["POI: <div class=\"poi yl\">Ap 1</div> Portal +59.66, -54.45"
                   +"<blockquote><div class=sct>Reward:</div> Memory Resonator plans<blockquote>Ancestral Memories &times;16<br>Gold &times;40<br>Chromatic Metal &times;30</blockquote></blockquote>",
                    "POI: <div class=\"poi yl\">Ms 1.7</div> Wake The Past <img src=\"grave_icon.png\"/> Grave"],
  "Oger Alpha":    ["POI: <div class=\"poi yl\">Ap 2</div> Portal +34.82, +16.52",
                    "POI: <div class=\"poi yl\">Ms 2.2</div> To Crave The Stars <img src=\"grave_icon.png\"/> Grave"],
  "Ninarb S13":    ["POI: <div class=\"poi yl\">Ap 3</div> Portal -13.49, -48.56",
                    "POI: <div class=\"poi yl\">Ms 3.2</div> Obsession <img src=\"grave_icon.png\"/> Grave"
                   +"<blockquote><div class=sct>Reward:</div> Memory Fragment plans<blockquote>Wiring Loom &times;2<br>Silver &times;50<br>Pugneum &times;100</blockquote></blockquote>",
                    "POI: <div class=\"poi yl\">Ms 4.6</div> Cluster Horde - Earn nanites: 1000"
                   +"<blockquote><div class=sct>Reward:</div><blockquote>Wiring Loom &times;10<br>Silver &times;250<br>Pugneum &times;500</blockquote></blockquote>",                    
                    "POI: <div class=\"poi yl\">Ms 3.5</div> Self Improvement - Summon your own memory fragment"],
  "Bognorth V":    ["POI: <div class=\"poi yl\">Ap 4</div> Portal +11.46, +6.11",
                    "POI: <div class=\"poi yl\">Ms 4.2</div> Monomania <img src=\"grave_icon.png\"/> Grave"],
  "Yardogo XVII":  ["POI: <div class=\"poi yl\">Ap 5</div> Portal +2.45, -124.65",
                    "POI: <div class=\"poi yl\">Ms 5.2</div> Another Chance <img src=\"grave_icon.png\"/> Grave",
                    "POI: <div class=\"poi yl\">Ms 5.4</div> A Shattered Past - Pulse to a derelict freighter"
                    +"<blockquote><div class=sct>Reward:</div> Whalesong Flute plans<blockquote>Liquid Sun &times;32<br>Ancestral Memories &times;32<br>Somnal Dust &times;32</blockquote></blockquote>",
                    "POI: <div class=\"poi yl\">Ms 5.5</div> The Siren - Assemble the Whalesong",
                    "POI: <div class=\"poi yl\">Ms 5.6</div> Leviathan - Call the Leviathan"],
  "Mebayasicis Gatag": ["POI: <div class=\"poi yl\">Ms 2.5</div>Atonement - Tame a predator <img src=\"predator_icon.png\"/>"],
  # "Apporo II":     ["Stellar Class: K2 <span class='dot rd'></span>",
  #                   "Distance: 33 ly &rarr; Denayanov"],
  # "Likeggle":      ["POI: <div class=\"poi bl\">Storm Crystals</div>"
  #                  +"<blockquote>Note: Safer to get them at Oginic-Roran II // Gaapo VI</blockquote>"], # .encode('utf-8'),
  # "Azlichin":      ["Distance: 37 ly &rarr; Denayanov",
  #                   "POI: <div class=\"poi yl\">Ms 4.4</div> Hot Pursuit - Smuggle contraband: 500,000 units"],
                  #  "<blockquote>Note: If you don't want to go to a Red system to collect Cadmium,<br>"
                  # +"just put a base near 'Ap 1' to portal to Washeyu-Hebe <a href=\"https://youtu.be/PxOG_OcmqVo\">Xaine's World</a><img src=linkicon.png></blockquote>",

  "Wighanbrin Teba": ["Galaxy 98: Apmaneessu",
                      "POI: <div class=\"poi yl\">Starting Planet</div>"],
  "Drupsh-Ogusi X":  ["POI: <div class=\"poi yl\">Ms 1.3</div> Liberation - Rescue a freighter from pirates"
                     +"<blockquote>Pirate Map Fragment 1 of 3</blockquote>"],
  "Hecharaw XII":    ["POI: <div class=\"poi yl\">Ms 2.4</div> Covited Suns - Collect Gravitino Balls: 16"],
  "Waburydes IX":    ["POI: <div class=\"poi bl\">Storm Crystals</div>",
                      "POI: <div class=\"poi yl\">R1</div> Trade Post -20.11, +84.10"
                     +"<blockquote><b>Note</b>: Only 83 ly &rarr; R3 - Gasertan</blockquote>"],
  "Pacasp VIII":     ["POI: <div class=\"poi yl\">R2</div> Grave -61.43, -8.51"],
  "Robian XIV":      ["POI: <div class=\"poi yl\">Ms 2.2</div> A Freighter Blighted - Seek the lost freighter"
                     +"<blockquote>Pirate Map Fragment 2 of 3</blockquote>"],
  "Kufastro":        ["POI: <div class=\"poi yl\">R3</div> Alien Ruin +38.10, +77.80"],
  "Pushiy Alpha":    ["POI: <div class=\"poi yl\">Ms 3.2</div> Submerged - Deploy the Nautilon",
                      "POI: <div class=\"poi yl\">Ms 3.3</div> The Last Piece - Seek the lost pilot"
                     +"<blockquote>Pirate Map Fragment 3 of 3</blockquote>",
                     "POI: <div class=\"poi yl\">Ms 3.4</div> Leagues Under the Sea - Reach ocean depths: 60u",
                     "POI: <div class=\"poi yl\">Ms 3.5</div> Sunken Antiquity - Acquire an aquatic treasure"],
  "Cuset":           ["POI: <div class=\"poi yl\">R4</div> Colossal Archive +26.60, +166.36",
                      "POI: <div class=\"poi yl\">Ms 4.5</div> Treasure Hunt Portal to R5"],
  "Akino 74/R7":     ["POI: <div class=\"poi yl\">Ms 4.2</div> Counterfire - Sentinel Pillar +36.22, +116.31"],
  "Yacenei Nomats":  ["POI: <div class=\"poi yl\">R5</div> Portal"
                     +"<blockquote>Destination of Treasure Hunt Portal on Cuset</blockquote>"],
  "Liviat Delta":    ["POI: <div class=\"poi yl\">Ms 4.5</div> Treasure Hunt Chest"],
  "RW":              ["Galaxy 99: Hicanpaav"],
  "Kesmante":        ["<b>Note</b>: Gateway System - 3003 ly &rarr; Galactic Core"],
  "Gazazele":        ["POI: <div class=\"poi yl\">Ms 5.4</div> Intergalactic - Leave the galaxy",
                      "POI: <div class=\"poi yl\">Ms 5.5</div> Breadcrumbs - Establish a base"],
  "Rangyi VI":       ["POI: <div class=\"poi yl\">Ms 2.3</div> Lawless Sky - Visit a pirate system"
                     +"<blockquote>Distance: 53 ly &rarr; <a href=20221209115400.jpg>Eibeyt-Guyun IV <img src=linkicon.png></a><blockquote>",
                     "POI: <div class=\"poi yl\">Ms 5.5</div> Galactic Defender - 'Bounty Master' mission"],

  "Rivojipo Major":  ["POI: Predators <img src=\"predator_icon.png\"/>"],
  "Tono 23/R5":      ["POI: <div class=\"poi bl\">Storm Crystals</div>",
                      "POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Radioactive"],
  "Hivaleyms III":   ["Distance: <div class=\"poi yl\">15 ly</div> &rarr; Ogaets XII", 
                      "POI: <div class=\"poi tr\">Traveller</div> Ocleontiu"],
  "Izonakr X":       ["POI: <div class=\"poi yl\">Ms 3.2</div> Best-Laid Plans - Tall eggs",
                      "POI: <div class=\"poi yl\">Ms 3.4</div> Sweet Tooth - Bake a cake"
                     +"<blockquote>cream &rarr; churned butter<br>"
                     +"churned butter + processed sugar &rarr; sweetened butter<br>"
                     +"sweetened butter + refined flour + Any eggs &rarr; cake batter<br>"
                     +"cake batter + synthetic honey &rarr; glittering honey cake</blockquote>"],
  "Baaliara Omega":  ["POI: <div class=\"poi bl\">Storm Crystals</div>"],
  "Yuga 81/A9":      ["POI: <div class=\"poi bl\">Storm Crystals</div>"],
  "Atelen Gamma":    ["POI: <div class=\"poi bl\">Storm Crystals</div>",
                      "POI: <div class=\"poi tr\">Grave</div> +11.55, -57.53"
                     +"<blockquote>Base: Outpost 2/Bones -28.32,-177.81 &mdash; "
                     +"<a href=20221201131420_1.jpg>14 bones</a> + 4 SC within 66 u</blockquote>"],
  "Liaiutsia XI":    ["Stellar Class: B7 <span class='dot bl'></span>"],
  "Koma":            ["POI: <div class=\"poi yl\">Starting Planet</div>",
                      "POI: <div class=\"poi tr\">Grave</div> -32.12, +170.03"],
  "Sasa 16/W9":      ["POI: <div class=\"poi yl\">R1</div> Colossal Archive +86.61, -7.17",
                      "POI: <div class=\"poi yl\">Ms 1.3</div> Best Friend's Portrait",
                      "POI: <div class=\"poi yl\">Ms 1.7</div> Next Generation - Induce an egg",
                      "POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Lush"],
  "Retleibe":        ["POI: <div class=\"poi yl\">R2</div> Monolith -29.09, +108.77",
                      "POI: <div class=\"poi yl\">Ms 2.3</div> Coleopterology - Adopt a beetle",
                      "POI: <div class=\"poi yl\">Ms 5.3</div> Wingspan - Fly 2000 u"],
  "Inhalce VII":     ["POI: <div class=\"poi yl\">R3</div> Ancient Ruin -0.03, +25.78"],
  "Oneza 38/U6":     ["POI: <div class=\"poi yl\">R4</div> Holographic Comms Tower -29.17, -162.33",
                      "POI: <div class=\"poi yl\">Ms 5.2</div> A Crowded Universe - 13 Fauna"],
  "Aess Major":      ["POI: <div class=\"poi yl\">R5</div> Portal -9.91, -13.13",
                      "POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Unusual",
                      "POI: <div class=\"poi yl\">Ms 5.4</div> Xenobiology - Scan exotic creature"],
  "Cutumus Sigma":   ["POI: <div class=\"poi yl\">Ms 3.2</div> Best-Laid Plans - Giant &amp; Creature eggs",
                      "POI: <div class=\"poi yl\">Ms 4.6</div> What Lurks Below - Abyssal Horror"
                     +"<blockquote>Base: Abyssal, creature eggs, G eggs -13.54, +124.46</blockquote>"],
  "Harote":          ["POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Swamp", 
                      "POI: <div class=\"poi yl\">Ms 4.4</div> Eyes in the Reeds - Scan swamp creature"],
  "Muchudl XIX":     ["POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Airless"],
  "New Ronessle":    ["POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Volcanic"],
#  "Yetrichmo Major": ["POI: <div class=\"poi yl\">Ms 3.3</div> Sightseer - Unusual",
#                      "POI: <div class=\"poi yl\">Ms 5.4</div> Xenobiology - Scan exotic creature"],
  "Moga":            ["POI: <div class=\"poi yl\">Ms 5.6</div> Ancestors - Excavate 10 bones"],

  "Icyonghu Oriya":["POI: Predators <img src=\"predator_icon.png\"/>"],
  "Yawachi XIX":   ["Distance: 6 ly &rarr; Wazaki"],
  "Sappo 77/G3":   ["POI: <div class=\"poi tr\">Glitch</div> Electric Cube"],
  "Usinos-Zuo":    ["Stellar Class: F3f <span class='dot yl'></span>",
                    "Distance: 18 ly &rarr; Romestovot",
                    "POI: Milestone 4.3: Hot Pursuit"],
  "Christole Oich":["POI: Predators <img src=\"predator_icon.png\"/>"],
  "Ennect":        ["POI: <div class=\"poi yl\">AP1</div> Portal -56.86,+11.12"],
  "Alecapae Beta": ["POI: <div class=\"poi yl\">AP2</div> Portal +19.43,+56.58"],
  "Rora 15/J5":    ["POI: <div class=\"poi yl\">AP3</div> Portal -12.51,-164.04"],
  "Haumeadl M26":  ["POI: <div class=\"poi yl\">AP4</div> Portal -45.66,-157.54",
                    "POI: <div class=\"poi bl\">Storm Crystals</div>"],
  "Mapan VIII":    ["POI: <div class=\"poi bl\">Storm Crystals</div>"],
  "Kaok 84/O4":    ["POI: <div class=\"poi yl\">AP5</div> Portal +7.02,+20.67"],
  "Chistor-Olev XIII":["Traveller: Xumunde"],

  "Hudle W33?":     ["POI: <div class=\"poi rd\">Sentinel Pillar</div> -6.51,+153.19"],
  "Ilskommu XIV":["Note: 98 ly from Kohango XV"],
  "Umanta":      ["Note: 71 ly from Zudnoyer X"],
  "Odetsimo":    ["Note: 52 ly from Releniem"],
  "Tuchica S46": ["POI: <div class=\"poi stroke\">R1</div> Trading Post -31.69,+41.21"],
  "Xahilli":     ["POI: <div class=\"poi stroke\">R2</div> Traveller\'s Grave -0.82,-168.74"],
  "Mida 88/G4":  ["POI: <div class=\"poi stroke\">R3</div> Ancient Ruin +66.44,+46.38"],
  "Oezenus E50": ["POI: <div class=\"poi stroke\">R4</div> Planetary Archive +0.46,-145.83"],
  "Recouls":     ["POI: <div class=\"poi stroke\">R5</div> Portal Destination"],
  "Releniem":    ["Travellers: Aceronya, Eworoksvil"],
  "New Edmon":   ["Note: Sentinel Pillar +1.02,-103.98"],
  "Eccaff T49":  ["Note: Treasure Hunt Teleporter +31.33,-72.04"]
}
'''
dangerous = { # set
  # Weather
  "Acidic Deluges",
  "Blasted Atmosphere",
  "Blighted Planet",
  "Blistering Floods",
  "Billowing Dust Storms",
  "Bone-Stripping Acid Storms",
  "Cataclysmic Monsoons",
  "Corrosive Rainstorms",
  "Corrosive Storms",
  "Caustic Floods",
  "Dangerously Toxic Rain",
  "Deep Freeze",
  "Drifting Firestorms",
  "Extreme Radioactivity",
  "Icy Tempests",
  "Inferno Winds",
  "Intense Cold",
  "Intense Heatbursts",
  "Lung-Burning Night Wind",
  "Magma Rain",
  "Painfully Hot Rain",
  "Particulate Winds",
  "Roaring Ice Storms",
  "Scalding Rainstorms",
  "Self-Igniting Storms",
  "Superheated Rain",
  "Torrential Acid",
  "Torrential Heat",
  "Toxic Monsoons",
  "Winds from Beyond",
  # Sentinel
  "Aggressive",
  "Frenzied",
  "High Security",
  "Hostile Patrols",
  "Hateful",
  "Inescapable",
  "Threatening",
  "Zealous",
  #Corrupted
  "Answer To None",
  "Corrupted",
  "De-Harmonised",
  "Dissonant",
  "Forsaken",
  "Rebellious",
  "Sharded from the Atlas",
  #Contraband
  "Banned Weapons",
  "Blood Salt",
  "Counterfeit Circuits",
  "First Spawn Relics",
  "GrahGrah",
  "Moon Ether",
  "NipNip Buds",
  "Prismatic Feathers",
  "Stolen DNA Samples"
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

checklist = '''
<div style="color:#551a8b;"><small><br>* Only the top class upgrades are shown in the System Summary<br>System Detail only shows upgrades found in System Summary</small></div>
<h2 style="display:none; padding-top: 8px;">Checklist -- see e12 Omega</h2>
'''

h = ['''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="mobile-web-app-capable" content="yes">
  <title>{0}</title>
<style> 
@font-face {font-family: "NMS Geo"; src: url("geonms-webfont.ttf");}
@font-face {font-family: "NMS Glyphs"; src: url("NMS-Glyphs-Mono.ttf");}
h2 {text-align: center; max-width: 800px; font-size: 1.25em;}
body {background: url("screenshot.jpg") fixed no-repeat; background-size: cover; font-size: 18px;}
table {border-spacing: 0;}
td {padding: 0;}
div {padding-left: 10px;}
img {height: 18px; vertical-align: middle; margin-bottom: 4px;}
.poi {display: inline-block; border-radius: 8px; padding: 0 8px; margin: 1px 0; font-style: normal;}
/*.pol {display: inline-block; border-radius: 8px; padding: 0 8px; margin: 1px 0; border-radius: 5px; border: 1px solid #888;}*/
.tr {background-color: greenyellow; color: black;}  /* traveler - #BD104C; https://giggster.com/guide/complementary-colors/ */
.bh {background-color: #E1C16E;}    /* #ffcfff; lightgrey; black hole */
.bl {background-color: #b0e0ff;}   /* powderblue; storm crystal */
.rd {background-color: pink;}         /* predator */
.gr {background-color: #99ff66;} 
.on {background-color: #f8f8f8;} /* #f8f8f8 */
.co {background-color: #d9b3ff;} /* #debde4; corrupted */
.yl {background-color: yellow;} 
.br {background-color: #D2B48C;}        /* horrific nest */
.bio {padding-left:30px;}
.cc {height: 24px; margin: 0; padding-left: 0;}
.badge {display: inline-block; padding: 0;}
.badge div {display: inline-block; padding: 0;}
blockquote {margin: 0; padding: 0 10px; font-style: italic; color: #551a8b;} /* navy;} */
.bq {font-style: italic; color: #551a8b;} /* navy;} */
.stroke {
  background: lightgrey; /* border: 1px solid #222; */ color: white; font-weight: bold;
  text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
}
/* https://stackoverflow.com/questions/4919076/outline-effect-to-text */
.s, .p {padding-top: 8px;} 
td {vertical-align: top;}
button {font-size: 18px; padding: 2px 10px; margin-top: 15px; border-radius: 8px; border: 1px solid #222; background-color: greenyellow;}
.gl {font-family: "NMS Glyphs"; font-size: larger; font-weight: bold; height: 22px; display: inline-block; padding:0;} 
span {font-family: "NMS Glyphs"; font-size: larger; font-weight: bold;} 
.k {font-family: "NMS Kerned"; font-weight: bold;} 
.disabled {font-family: "NMS Glyphs"; font-size: larger; font-weight: bold; color: #a0a0a0;} 
.dot {border-radius: 50%; border: 1px solid black; height: 10px; width: 10px; display: inline-block; margin-left: 8px;}
.fl td::first-letter {font-weight: normal;}
.c {display: inline-block; vertical-align: top; padding-top: 8px;}
.pl:link {color: #551a8b;} .pl:visited {color: #551a8b !important;} .pl:hover {color: #0000ee;}
.sy:link {color: #0000ee;} .sy:visited {color: #0000ee !important;} .sy:hover {color: #551a8b;}
.sy {font-family: Arial;}
a {color:black; white-space: nowrap; border-radius: 6px; padding: 1px 6px; text-decoration: none; margin-bottom: 5px; border: 1px solid #808080;}
.a {color:black; white-space: nowrap; border-radius: 6px; padding: 1px 6px; text-decoration: none; border: 1px solid #808080;
    background-color: #dae6f1; background-image: linear-gradient(45deg, #dae6f1, white); display: inline-block;}
.n {font-style: normal;}
.sca {display: inline-block; padding-left: 0; color:#0000ee !important;}
.scx {display: inline-block; padding-left: 0; color: #600080 !important; font-family: Arial; font-variant: small-caps; /*font-weight:bold; font-style: italic; border: 1px solid darkgrey; border-radius: 8px;padding: 0 6px;*/}
.scy {display: inline-block; padding-left: 0; color:yellow !important;}
.sms {display: inline-block; color:black; font-style: normal; padding: 0; font-family: Arial; font-size: 18px; font-variant: small-caps;}
.scr {display: inline-block; padding-left: 0; color:#DC143C !important;}
.scg {display: inline-block; padding-left: 0; color:limegreen !important;}
.scb {display: inline-block; padding-left: 0; color:blue !important;}
.sct {display: inline-block; padding-left: 0; color:teal !important;}
.scp {display: inline-block; padding-left: 0; color:purple !important;}
.tbl {display: inline-block; padding-left: 0; width:130px;}
.pg  {border: 0; padding: 0;}
.pg img {vertical-align: top;}
#sum {border-spacing: 4px; border-collapse: separate;}
#sum td {padding-bottom: 5px;}
.r {margin-top: 10px;}
.pu {font-style: italic; color: purple; padding-left: 0; display: inline-block;}
.tc div {display: inline-block; border: 1px solid #bbb; width: 13px; border-radius: 4px;  
    text-align: center; padding: 0 2px; font-size: 14px; font-family: 'NMS Geo'}
.tcs {background-color: #ffc100;}
.tca {background-color: #d9b3ff;}
.tcb {background-color: #aad9f7;}
.tcc {background-color: #99ff66;}
.tcx {background-color: #ddd;}
.bca {background-color: #d9b3ff; border-radius: 8px;}


/* https://stackoverflow.com/questions/14387690/how-can-i-show-only-corner-borders/61913549#61913549 */
.box {
  --b: 1px;    /* thickness of the border */
  --c: #888;   /* color of the border */
  --w: 20px;   /* width of border */
  
  border: var(--b) solid #0000; /* space for the border */
  --_g: #0000 90deg,var(--c) 0;
  --_p: var(--w) var(--w) border-box no-repeat;
  background:
    conic-gradient(from 90deg  at top    var(--b) left  var(--b),var(--_g)) 0    0    / var(--_p),
    conic-gradient(from 180deg at top    var(--b) right var(--b),var(--_g)) 100% 0    / var(--_p),
    conic-gradient(from 0deg   at bottom var(--b) left  var(--b),var(--_g)) 0    100% / var(--_p),
    conic-gradient(from -90deg at bottom var(--b) right var(--b),var(--_g)) 100% 100% / var(--_p);
  width:300px; 
  padding: 10px;
}
#option1 {display:block;}
#option2 {display:none;}
#shelter {white-space: nowrap; border-radius:0; padding: 0; text-decoration: underline; margin-bottom: 5px; border: 0px solid #808080;}
.minus {display:inline-block;padding:0;background-color:pink;border-radius:50%;}

.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  max-width: 800px;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: #474e5d;
}
.modal img {width: 80%; height: auto; margin: 10%;}

</style></head><body>
<div id="id01" class="modal">
  <img src="help.png">
</div>
''']

def stellar(system):
  if system in poi: 
    m = list(filter(lambda e: len(e), map(lambda x: re.findall(r"Stellar Class: (.)",x),poi[system])))
    if len(m):
      return f'&nbsp;<div class=sc{"yyrrgbb"[["F","G","K","M","E","B","O"].index(m[0][0])]}>&#9679;</div>'
  return ""

dot    = lambda p: ("","&nbsp;<div class=scy>&#9679;</div>")[p in poi and any(re.match('POI', x) for x in poi[p])]
ptag   = lambda p: f'\n  <a class=pl href=#{re.sub(" ","_",p)}>{p+dot(p)}</a>'
stag   = lambda p: f'<a class=sy href=#{re.sub(" ","_",p)}>{p+stellar(p)+dot(p)}</a>'

with open(f'pip{ilog}.json', "r") as infile: 
  db = json.load(infile)
  # print(json.dumps(db,indent=2))
  # quit()

  for s in db:
    db[s]['Technology'] = sorted(db[s]['Technology'].keys(),key=lambda x:x[3:])
    db[s]['Buy Sell'  ] = sorted(db[s]['Buy Sell'  ].keys())
    # add points of interest; 
    #   [s]:travelers, black holes, atlas; 
    #   [s,p]:predators,storm crystals
    if s in poi:
      # print('dbug=',s, 'poi=', poi[s])
      if "Original Name:" in poi[s][0]:                                  # sjh - insert "Original Name:"
        db[s]['System Info'].insert(0, poi[s][0])
      else:
        db[s]['System Info'].extend(poi[s])
    for p in db[s]:
      if p in poi:
        db[s][p]['Planet Info'].extend(poi[p])
        if dbug: print(getframeinfo(currentframe()).lineno, f's={s}, p={p}, poi[p][0]={poi[p][0]}')

  h.append('<h2>{0} System Summary</h2>')
  h.append('<table id=sum><tr><th>Systems</th><th>Planets</th></tr>')
  nl = '<br>\n'
  sum = {}
  spelling = {}
  for station in db:
    print(station)
    planets = []
    for planet in db[station].keys():
      if not planet in ["System Info","Technology","Buy Sell"]:
        planets.append(planet)
        p = list(filter(lambda x: 'Biome:' in x, db[station][planet]['Planet Info']))
        print(f'!! {p}, #{planet}')
        if p: 
          item = p[0][7:]
          if not item in spelling:
            spelling[item] = 0
          spelling[item] += 1
    h.append(f'<tr><td nowrap>{badges[station] if station in badges else ""} {stag(station)}</td><td>{" ".join(map(ptag, planets))}</td></tr>')
  h.append('</table>')
  sum['Biome'] = b = sorted(spelling.keys())

  spelling = {}
  for station in db:
    for item in db[station]['Technology']: 
      m = re.search(r'(...)(.+)', item)
      if not m.group(2) in spelling:
        spelling[m.group(2)] = []
      spelling[m.group(2)].append(m.group(1))

    #-------------------------- sort tech class within item (in place) ---------------------------
    for item in spelling:
      spelling[item].sort(key=lambda x:'SABCX'.index(x[1:2]))

  sum['Technology'] = sorted([spelling[i][0] + i for i in spelling], key=lambda x: x[3:])
  tech_set = {i for i in sum['Technology']}

  for station in db:
    #-------------------------- show all Suspicious, don't filter ---------------------------
    if not any("Pirate Controlled" in x for x in db[station]["System Info"]):
      db[station]['Technology'] = filter(lambda x: x in tech_set, db[station]['Technology'])
      #-------------------------- show only tech in system summary --------------------------

  spelling = {}
  for station in db:
    for item in db[station]['Buy Sell'  ]: 
      if not item in spelling: 
        spelling[item] = 0
      spelling[item] += 1
  sum['Buy Sell'] = sorted(spelling.keys())


  spelling = {}
  for station in db:
    for planet in db[station]:
      if not planet in ["System Info","Technology","Buy Sell"]:
        for item in db[station][planet]['Resources']:
          if not item in spelling: 
            spelling[item] = 0
          spelling[item] += 1
  sum['Resources'] = sorted(spelling.keys())

  def contraband(sum):
    return map(lambda i: (i, f'<div class="scp">{i}</div>')[i in dangerous],sum) # (answer tuple)[truth index]
      
  def dissonance(sum):
    return map(lambda i: (i, f'<div class="scp">{i}</div>')[  i == 'Dissonance detected'      ],sum) 
  # return map(lambda i:     f'<div class="scp">{i}</div>' if i == 'Dissonance detected' else i,sum) # ternary

  def decorate_tech(sum):
    rows = []
    for item in sum:
      m = re.search(r'.(.).(.+)', item)
      rows.append(f'<div class=tc><div class=tc{m.group(1).lower()}>{m.group(1)}</div>&hairsp;{m.group(2)}</div>\n')
    return ''.join(rows)

  h.append(f'<div class=c><center><b>Technology</b></center>{decorate_tech(sum["Technology"])}</div>')
  h.append(f'<div class=c><center><b>Buy Sell</b></center>{nl.join(contraband(sum["Buy Sell"]))}</div>')
  h.append(f'<div class=c><center><b>Resources</b></center>{nl.join(dissonance(sum["Resources"]))}</div>')
  h.append(f'<div class=c><center><b>Biome</b></center>{nl.join(sum["Biome"])}</div>')

  # ---------------------------------------------------------------------------------

  h.append('<h2>{0} System Detail</h2>')
  for s in db:
    p = re.sub(" ","_",s)
    h.append(f'<div class=s id={p}>{badges[s] if s in badges else ""} <a class=sy href="javascript:clr();">{s}</a>')
    for c in db[s]:
      # print(f'c= {c}, sys= {s}')
      p = re.sub(" ","_",c)
      if c in ["System Info","Technology","Buy Sell"]:
        h.append(f'  <div>{c}')
      else:
        h.append(f'  <div class=p id={p}><a class=pl href="javascript:clr();">{c}</a>')

      for i in db[s][c]:
        if c in ["System Info","Technology","Buy Sell"]:
          i = re.sub(r'(Glyphs: )([\da-f]{6})([\da-f]{6})',r'\1<div class=gl>\2&nbsp;\3</div>', i)
          #-------------------------- contraband ---------------------------------------------
          if c == "Buy Sell" and i in dangerous:
            h.append(f'      <div><div class="scp">{i}</div></div>')
          else:
          #-------------------------- upgrade class ------------------------------------------
            if c == "Technology":
              m = re.search(r'.(.).(.+)', i) # see decorate_tech
              h.append(f'    <div class=tc><div class=tc{m.group(1).lower()}>{m.group(1)}</div>&hairsp;{m.group(2)}</div>\n')
            else:
              h.append(f'    <div>{i}</div>')
        else: 
          h.append(f'    <div>{i}')
          for j in db[s][c][i]:
            if i == 'Planet Info':
              if dbug: print(getframeinfo(currentframe()).lineno, f's={s}, c={c}, i={i}, j={j}')
            #--------------------------- dangerous -------------------------------------------
            m = re.search(r'^((Weather|Sentinels): )(.+)$',j)
            if m and m.group(3) in dangerous:
              print("dangerous= ",m.group(1),m.group(3))
              if(m.group(2) == "Sentinels" and m.group(3) in corrupted):
                h.append(f'      <div>{m.group(1)}<div class="poi co">{m.group(3)}</div></div>')
              else:
                h.append(f'      <div>{m.group(1)}<div class="poi rd">{m.group(3)}</div></div>')
            else:
            #--------------------------- dissonance ------------------------------------------
              if i == 'Resources' and j == 'Dissonance detected':
                print(getframeinfo(currentframe()).lineno, f's={s}, c={c}, i={i}, j={j}')
                h.append(f'      <div><div class="scp">{j}</div></div>')
              else:
                h.append(f'      <div>{j}</div>')
            #---------------------------------------------------------------------------------
          h.append('    </div>')
      h.append('  </div>')
    h.append('</div>')
h.append('''<button>Collapse All</button>
~
<div style="margin-top: 700px;"></div>
<script>
function clr(){
  window.scrollTo(0, 0);
  window.location.href = window.location.href.split('#')[0];
  return false;
}

function sv(id){
  document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

// https://stackoverflow.com/questions/37098405/javascript-queryselector-find-div-by-innertext
document.querySelector('button').addEventListener('click', function(){
  document.querySelectorAll('.c')
    .forEach(e => e.style.display = 'none');

  [...document.querySelectorAll('.p')]
    .filter(e => !/POI:/.test(e.textContent))
    .forEach(e => e.style.display = "none");

  document.querySelectorAll('.s')
    .forEach(e => {
      [...e.querySelectorAll('div')]
        .filter(e => /^(Technology|Buy Sell|Resources)/.test(e.textContent))
        .forEach(e => e.style.display = 'none')
    });
  document.querySelector('button').style.display = 'none';
});

let cbox = document.querySelectorAll('input[type=checkbox]');

for (let i = 0; i < cbox.length; i++) {
  cbox[i].addEventListener("click", function(e) {
    let key = e.target.nextSibling.nextSibling.innerHTML;
    if(localStorage.getItem(key) === null){
      localStorage.setItem(key, true);
      e.target.checked == true;
    }else{
      localStorage.removeItem(key);
      e.target.checked == false;
    }
  });

  ms = cbox[i].nextSibling.nextSibling.innerHTML;
  if(!(localStorage.getItem(ms) === null)){ 
    console.log(ms);
    cbox[i].checked = true;
  }
}

function clearCheckbox(){
  if(confirm("Are you sure?")){
    Object.keys(localStorage)
      .filter(key => /Ms \d\.\d/.test(key))
      .map(key => localStorage.removeItem(key));
    [...cbox].map(e => e.checked = false);
  }
}

const modal = document.getElementById('id01'),
  handleModal = () => modal.style.display='block';

[...document.querySelectorAll('img')]
  .filter(e => /badge|class/.test(e.src))
  .forEach(e => e.addEventListener('click', handleModal));

window.onclick = function(event) {
  if (event.target.parentNode == modal || event.target == modal) {
    modal.style.display = "none";

    [...document.querySelectorAll('img')]
      .filter(e => /badge|class/.test(e.src))
      .forEach(e => e.removeEventListener('click', handleModal));
  }
}

</script></body></html>''')
h = re.sub(r'\{0\}', title, '\n'.join(h))
# with open(f'index{ilog}.html','w') as outfile:
with open(f'{title}.html','w') as outfile:
  for pirate in pirates:
    h = re.sub(rf'(>{pirate})',r'\1 <img src="i/pirate_icon.png"/>', h)
  for at in atlas:
    h = re.sub(rf'(>{at})',r'\1 <img src="i/atlas_icon.png"/>', h)
  h = re.sub("~",checklist,h)
  outfile.write(h)

# import glob
# import cv2
# import numpy as np
# import pipm as m
#
# TODO: fix return code == NULL if m.glyph() not a glyph image
# TODO: list class A tech for missing class S
#
# https://www.w3schools.com/colors/colors_picker.asp
# https://www.reddit.com/r/NMSCoordinateExchange/comments/y32eyo/highquality_class_icons/



'''
Doriguc VII
Nafut Gamma
 POI: Ms 1.6 Scavenger
 POI: Ms 1.3 Exobotany
 POI: Ms 3.3 Life in all its forms
 POI: Ms 3.1 One Man's Treasure
 POI: Ms 4.4 Boundary Failure
 POI: Ms 1.1 Escape Velocity
 POI: Ms 2.3 Stardust
 POI: Ms 5.2 Astrolinguistics
Nash 33/W4
 POI: Ms 1.2 Homecomming
 POI: Ms 2.4 Expansion
 POI: Ms 2.6 Memento
 POI: Ms 3.2 Grand Tour
Bandab
 POI: Ms 1.4 Interstellar
 POI: Ms 1.5 Anomaly's Heart
Tip:
Construction: Ceiling Light (1× Salvaged Data)
Helios: 2× Pulse Engine C-class (162× Nanites → 150× Cadmium)
Synth: Acid, Lubricant, Unstable Gel, Liquid Explosives (1000× Nanites)
 POI: Ms 3.4 Hot Pursuit
Toyabe IX
Tip:
Buy 100× Salt, Artifact Chart, Solar Mirror → High-Power Sonar
Hunslowe
 POI: Ms 1.7 r1 Archive -28.04, +144.27
Bandab
 POI: Ms 2.1 Atlas Rises
 POI: Ms 2.2 Reality Grains
 POI: Ms 4.6 Depp Glass
 POI: Ms 5.5 Creation
Jiyose-Aishe XIV
Spinarr Kesen
 POI: Ms 2.7 r2 Portal -12.89, +67.56
 POI: Ms 4.1 Relic Hunter
 POI: Ms 4.2 Fallen Giants
Gartfol X
 POI: Ms 3.5 Assembly Required
Okubun-Chadr
Haku 57/Q1
 POI: Ms 3.7 r3 Crashed Freighter -20.97, -85.18
Aratae XIV
 POI: Ms 3.5 Assembly Required
Dovour-Jaus
New Wadhabie
 POI: Ms 4.7 r4 Portal +32.94, +179.59
 POI: Ms 4.5 Palate Cleanser
 POI: Ms 5.1 The Fallen
Yusvadbeat XII
 POI: Ms 5.6 Eclipse
 POI: Ms 2.5 To Infinity
Upacton Sigma
 POI: Ms 5.4 Xenophile
Amling
 POI: Ms 5.3 Blue Expanse
Boeot Prime
 POI: Ms 5.7 r5 Portal +27.44, +11.24
Mazuna
Onana
 POI: Ms 4.3 Radiant Flight'''