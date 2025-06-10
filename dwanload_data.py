
from roboflow import Roboflow
rf = Roboflow(api_key="wRcNYe38p6ZVM5RW89um")
project = rf.workspace("ebraam").project("potholes-detect-uytky-dlqgv")
version = project.version(1)
dataset = version.download("yolov11")
                