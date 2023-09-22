import json
import random
with open("play/links.json", "r") as f:
    list = json.load(f)
    max = 3
    video = random.randint(1, int(max))
    video = str(video)
    print("there is your video: " + list[video])