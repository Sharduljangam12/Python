# 2. Store names of people and their favorite colors, then print all people who like "blue".
# Use a dictionary for this.
favourite_colours = {
    "Alice": "blue",
    "Bob": "red",
    "Charlie": "blue",
    "David": "green",
}

for name , colours in favourite_colours.items():
    if colours == "blue":
        print(name)
        print(len(favourite_colours))