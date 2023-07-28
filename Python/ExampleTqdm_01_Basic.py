from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.25)
    text = text + char

text = ""
for char, number in tqdm(zip(["a", "b", "c", "d"], [1, 2, 3, 4]), total=4):
    sleep(0.25)
    text = text + char + str(number)