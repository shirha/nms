
def replace_with_rank(route, rank):
    # print('$',route,rank)
    ranked_route = {}
    for place, goods in route.items():
        ranked_goods = [str(rank[good]) if good in rank else good for good in goods]
        ranked_route[place] = ranked_goods
    return ranked_route

def init_trade_routes():
  return ({
    "Mining": "Mining",
    "Minerals": "Mining",
    "Ore Extraction": "Mining",
    "Prospecting": "Mining",
    "Manufacturing": "Manufacturing",
    "Construction": "Manufacturing",
    "Industrial": "Manufacturing",
    "Mass Production": "Manufacturing",
    "Technology": "Technology",
    "Engineering": "Technology",
    "High Tech": "Technology",
    "Nano-construction": "Technology",
    "Power Generation": "Power Generation",
    "Energy Supply": "Power Generation",
    "Fuel Generation": "Power Generation",
    "High Voltage": "Power Generation",
    "Trading": "Trading",
    "Commercial": "Trading",
    "Mercantile": "Trading",
    "Shipping": "Trading",
    "Advanced Materials": "Advanced Materials",
    "Alchemical": "Advanced Materials",
    "Material Fusion": "Advanced Materials",
    "Metal Processing": "Advanced Materials",
    "Ore Processing": "Advanced Materials", # Frontiers
    "Scientific": "Scientific",
    "Experimental": "Scientific",
    "Mathematical": "Scientific",
    "Research": "Scientific",
  },{ # keys = {v: {k for k, val in group.items() if val == v} - {v} for v in set(group.values())} 
    "Advanced Materials": ["Alchemical", "Material Fusion", "Metal Processing"],
    "Manufacturing": ["Construction", "Industrial", "Mass Production"],
    "Mining": ["Minerals", "Ore Extraction", "Prospecting"],
    "Power Generation": ["Energy Supply", "Fuel Generation", "High Voltage"],
    "Scientific": ["Experimental", "Mathematical", "Research"],
    "Technology": ["Engineering", "High Tech", "Nano-construction"],
    "Trading": ["Commercial", "Mercantile", "Shipping"]
  },{
    'Major Trade Routes': {
      'Mining': {
        'Dirt': 1,
        'Unrefined Pyrite Grease': 2,
        'Bromide Salt': 3,
        'Polychromatic Zirconium': 4,
        'Re-latticed Arc Crystal': 5
      },
      'Manufacturing': {
        'Enormous Metal Cog': 1,
        'Non-Stick Piston': 2,
      # "Six-Pronged Mesh Decouplers": "3",
        'Mesh Decouplers': 3,
        'Holographic Crankshaft': 4,
      # "High Capcity Vector Compressor": "5",
        'Vector Compressors': 5,
      },
      'Technology': {
      # "Decommissioned Circuit Board": "5",
        'Decommissioned Circuits': 1,
        'Welding Soap': 2,
        'Ion Capitor': 3,
        'Autonomous Positioning Unit': 4,
        'Quantum Accelerator': 5
      },
      'Power Generation': {
        'Spark Canister': 1,
        'Industrial-Grade Battery': 2,
        'Ohmic Gel': 3,
        'Experimental Power Fluid': 4,
        'Fusion Core': 5
      },
    },
    'Minor Trade Routes': {
      'Trading': {
        'Decrypted User Data': 1,
        'Star Silk': 2,
        'Comet Droplets': 3,
        'Ion Sphere': 4,
      # 'Teleport Coordinators ': 5, # Frontiers
        'Teleport Coordinates': 5
      },
      'Advanced Materials': {
        'Nanotube Crate': 1,
        'Self-Repairing Heridium': 2,
        'Optical Solvent': 3,
      # "Five Dimensional Torus": "4",
        '5D Torus': 4,
        'Superconducting Fibre': 5
      },
      'Scientific': {
      # "De-Scented Pheromone Bottle": "1", # Frontiers
        'De-Scented Bottles': 1,
        'Neutron Microscope': 2,
        'Instability Injector': 3,
        'Organic Piping': 4,
        'Neural Duct': 5
      }
    }
  },{
    # Economy tier lookup
    'Declining': 1, 'Destitute': 1, 'Failing': 1, 'Fledgling': 1, 
    'Low Supply': 1, 'Struggling': 1, 'Unsuccessful': 1, 'Unpromising': 1, 
    'Adequate': 2, 'Balanced': 2, 'Comfortable': 2, 'Developing': 2, 
    'Medium Supply': 2, 'Promising': 2, 'Satisfactory': 2, 'Sustainable': 2, 
    'Advanced': 3, 'Affluent': 3, 'Booming': 3, 'Flourishing': 3,
    'High Supply': 3, 'Opulent': 3, 'Prosperous': 3, 'Wealthy': 3
  })

wiki = "https://static.wikia.nocookie.net/nomanssky_gamepedia/images/6/64/Trade_loops_for_no_mans_sky.png"

group = [[
      # Economy Descriptors
      # Weak Economy (★)
      # (T1 economies)
      "Declining",
      "Destitute",
      "Failing",
      "Fledgling",
      "Low Supply",
      "Struggling",
      "Unsuccessful",
      "Unpromising",
    ],
      # Average Economy (★★)
      # (T2 economies)
    [
      "Adequate",
      "Balanced",
      "Comfortable",
      "Developing",
      "Medium Supply",
      "Promising",
      "Satisfactory",
      "Sustainable",
    ],
      # Strong Economy (★★★)
      # (T3 economies)
    [
      "Advanced",
      "Affluent",
      "Booming",
      "Flourishing",
      "High Supply",
      "Opulent",
      "Prosperous",
      "Wealthy",
    ]]

econ_rank = {key: index + 1 for index, values in enumerate(group) for key in values}
print('@',econ_rank)

'''


User
can you convert this to a comprehension?

econ_rank = {}
for index,values in enumerate(group):
  for key in values:
    econ_rank[key] = index + 1
print(econ_rank)

ChatGPT
Certainly! You can convert the nested loop into a dictionary comprehension. Here's how you can do it:

python
Copy code
econ_rank = {key: index + 1 for index, values in enumerate(group) for key in values}
print(econ_rank)

This comprehension iterates over each index-value pair in group using enumerate(group). For each pair, it iterates over each key key in the corresponding values. It then assigns the key key in the econ_rank dictionary to index + 1, where index is the index of the value in group. This will give you the desired econ_rank dictionary.

User
'values' is in the last for-in but 'values' is created in the first for-in. How am I suppose to think about this?

ChatGPT
In Python, the order of comprehension clauses follows the order of nested loops in a traditional loop structure. So, in this comprehension:

python
Copy code
econ_rank = {key: index + 1 for index, values in enumerate(group) for key in values}

The outer loop (for index, values in enumerate(group)) corresponds to the outer loop in the traditional nested loop structure. This loop iterates over the index-value pairs of the group dictionary. For each iteration, the values variable holds the value associated with the current index in the group dictionary.

The inner loop (for key in values) corresponds to the inner loop in the traditional nested loop structure. This loop iterates over each key in the values associated with the current index in the group dictionary.

So, in summary, the comprehension follows the structure:

python
Copy code
{output_expression for outer_loop in outer_iterable for inner_loop in inner_iterable}

Where outer_iterable corresponds to the outer loop and inner_iterable corresponds to the inner loop. In your case, enumerate(group) is the outer iterable, and values (which varies based on the outer loop) is the inner iterable.
'''