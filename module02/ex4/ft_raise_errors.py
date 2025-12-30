class PlantErrors(Exception):
    pass

class PlantNameError(PlantErrors):
    pass

class WaterLevelError(PlantErrors):
    pass

class SunlightLevelError(PlantErrors):
    pass

def check_plant_health(plant_name, water_level, sunlight_hours):
try:
    if plant_name == "":
    