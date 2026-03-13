paths = [["B","C"], ["D","B"], ["C","A"]]
# paths = [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]
# paths = [["A","Z"]]

def destination(paths):
    # Look for 1st destination city in first path
    # Search for the next departure of that city
    # then look for that destination

    departure = paths[0][1]
    current_path = []

    if len(paths) == 1:
         print(paths[0][1])
         return paths[0][1]

    for path in paths:
        if path[0] == departure:
                departure = path[1]
                current_path = path
    
    print(current_path[1])

destination(paths)