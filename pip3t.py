def replace_with_rank(route, rank):
    ranked_route = {}
    for place, goods in route.items():
        ranked_goods = [rank[good] if good in rank else good for good in goods]
        ranked_route[place] = ranked_goods
    return ranked_route

def init_trade_routes():
  return ({
    "Advanced Materials":"Advanced Materials",
    "Trading":"Trading",
    "Manufacturing":"Manufacturing",
    "Power Generation":"Power Generation",
    "Technology":"Technology",
    "Scientific":"Scientific",
    "Mining":"Mining",

    "Alchemical":"Advanced Materials",
    "Commercial":"Trading",
    "Construction":"Manufacturing",
    "Energy Supply":"Power Generation",
    "Engineering":"Technology",
    "Experimental":"Scientific",
    "Fuel Generation":"Power Generation",
    "High Tech":"Technology",
    "High Voltage":"Power Generation",
    "Industrial":"Manufacturing",
    "Mass Production":"Manufacturing",
    "Material Fusion":"Advanced Materials",
    "Mathematical":"Scientific",
    "Mercantile":"Trading",
    "Metal Processing":"Advanced Materials",
    "Minerals":"Mining",
    "Nano-construction":"Technology",
    "Ore Extraction":"Mining",
    "Ore Processing":"Advanced Materials",
    "Prospecting":"Mining",
    "Research":"Scientific",
    "Shipping":"Trading"
  },{  
    "Manufacturing",
    "Mining",
    "Power Generation",
    "Scientific",
    "Technology",
    "Trading",
    "Black Market"
  },{
    "Major Trade Routes":{
      "Mining":{
        "Re-latticed Arc Crystal": "1",
        "Polychromatic Zirconium": "2",
        "Bromide Salt": "3",
        "Unrefined Pyrite Grease": "4",
        "Dirt": "5"},
      "Manufacturing":{
        "Vector Compressors": "1",
        # "High Capcity Vector Compressor": "1",
        "Holographic Crankshaft": "2",
        "Mesh Decouplers": "3",
        # "Six-Pronged Mesh Decouplers": "3",
        "Non-Stick Piston": "4",
        "Enormous Metal Cog": "5"},
      "Technology":{
        "Quantum Accelerator": "1",
        "Autonomous Positioning Unit": "2",
        "Ion Capitor": "3",
        "Welding Soap": "4",
        # "Decommissioned Circuit Board": "5",
        "Decommissioned Circuits": "5"},
      "Power Generation":{
        "Fusion Core": "1",
        "Experimental Power Fluid": "2",
        "Ohmic Gel": "3",
        "Industrial-Grade Battery": "4",
        "Spark Canister": "5"}
    },
    "Minor Trade Routes":{
      "Trading":{
        "Teleport Coordinates": "1",
        "Ion Sphere": "2",
        "Comet Droplets": "3",
        "Star Silk": "4",
        "Decrypted User Data": "5"},
      "Advanced Materials":{
        "Superconducting Fibre": "1",
        # "Five Dimensional Torus": "2",
        "5D Torus": "2",
        "Optical Solvent": "3",
        "Self-Repairing Heridium": "4",
        "Nanotube Crate": "5"},
      "Scientific":{
        "Neural Duct": "1",
        "Organic Piping": "2",
        "Instability Injector": "3",
        "Neutron Microscope": "4",
        # "De-Scented Pheromone Bottle": "5",
        "De-Scented Bottles": "5"}
    }
  },{
    "Advanced Materials": ["Alchemical", "Material Fusion", "Metal Processing", "Ore Processing"],
    "Manufacturing": ["Construction", "Industrial", "Mass Production"],
    "Mining": ["Minerals", "Ore Extraction", "Prospecting"],
    "Power Generation": ["Energy Supply", "Fuel Generation", "High Voltage"],
    "Scientific": ["Experimental", "Mathematical", "Research"],
    "Technology": ["Engineering", "High Tech", "Nano-construction"],
    "Trading": ["Commercial", "Mercantile", "Shipping"]
    })
