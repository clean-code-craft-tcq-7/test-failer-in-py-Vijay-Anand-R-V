major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
def print_color_map():
    # major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    # minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    op = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            temp = f'{i * 5 + j + 1:2} | {major:6} | {minor:6}'
            op.append(temp)
            print(temp)
    return op

def test_color_map():
    color_map = print_color_map()
    assert(len(color_map) == 25)    
    assert(color_map[0] == " 1 | White  | Blue  ")
    assert(color_map[24] == "25 | Violet | Slate ")
    
test_color_map()
print("All is well (maybe!)")
