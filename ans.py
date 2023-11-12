"""
Question 7 a
"""

from math import *

print("\n========== 7 (a) ==========\n")

pays = {"Microsoft": {"PC": 0.02},
        "Apple": {"PC": 0.05, "Hand": 1.0, "Gaming": 1.0},
        "Mozilla": {"PC": 0.1}}

quants = {"Microsoft": {"PC": 50000000},
        "Apple": {"PC": 1000000, "Hand": 500000, "Gaming": 10000},
        "Mozilla": {"PC": 3000000}}

def get(comp, typ):
    return quants[comp][typ]*pays[comp][typ]

def option_1():
    sum = 0
    sum += get("Microsoft", "PC") + get("Apple", "Hand") + get("Apple", "Gaming")
    print("Option 1 :", sum)

def option_2():
    sum = 0
    sum += get("Microsoft", "PC") + get("Apple", "Hand") + get("Apple", "Gaming")
    print("Option 2 :", sum)

def option_3():
    sum = 0
    sum += get("Apple", "Hand") + get("Apple", "Gaming") + get("Mozilla", "PC")
    print("Option 3 : min ", sum, "max ", sum + get("Apple", "PC"))

def option_4():
    sum = 0
    sum += get("Apple", "Hand") + get("Apple", "Gaming") + get("Mozilla", "PC")
    print("Option 4 : min ", sum, "max ", sum + get("Apple", "PC"))

if __name__ == "__main__":
    option_1()
    option_2()
    option_3()
    option_4()
