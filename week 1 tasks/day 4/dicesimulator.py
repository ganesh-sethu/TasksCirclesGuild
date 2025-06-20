import random

    # unicode characters used in this program
    # ●   \u25CF 
    # ┌   \u250C
    # ─   \u2500 
    # ┐   \u2510
    # │   \u2502
    # ┌   \u250C
    # └   \u2514
    # ┘   \u2518 

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
  

dice_arr = []
tot = 0
num_of_dice = int(input("Enter the number of dice you want to roll?"))
print(f"finger's crossed rolling {num_of_dice} dice")

for i in range(num_of_dice):
  dice_arr.append(random.randint(1,6))

# printing the dice in vertical
# for i in range(num_of_dice):
#   for j in dice_art.get(dice_arr[i]):
#     print(j)


# printing the dice in horizontal 
for i in range(5):
  for cube in dice_arr:
    print(dice_art.get(cube)[i],end="")
  # after completing the inner loop which is one line we need to print in the next line so we just give a empty print() statement
  print()

for i in dice_arr:
  tot += i

print(dice_arr)
print(f"total: {tot}")