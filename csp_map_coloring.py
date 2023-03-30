

# R = restrictions/constraint
R = []

# this functions colors the given city with the given color
# returns false if not possible, returns the set of new restrictions if possible
def addColor(R, city, color):
    ans = []
    for rr in R:
        res = checkRestriction(rr, city, color)
        if res == False:
            return False
        elif res == None:
            continue
        else:
            ans.append(res)
    return ans
        
# checks if the restrition "rr" allows the given city to have the given color
# returns false if not possible, otherwise returns the new restriction

def checkRestriction(rr, city, color):

    #finding the index of the city (saved to index)
    index = -1
    other = -1
    if rr[0] == city:
        index = 0
        other = 1
    elif rr[1] == city:
        index = 1
        other = 0
    else:
        return rr

    # Check if the rr[other] is an integer:
    if isinstance(rr[other], int):
        # other component is a color
        if (color != rr[other]):
            return None
        else:
            return False
    else:
        return [rr[other], color]


# solving the CSP by variable elimination
# recursive structure: ci is the city index to be colored (0 = gresik, 1 = lamongan, etc)
# n is the number of colors
# cits is a list of cities
# if coloring is possible returns the city-> color map, otherwise False
# ==========================================
def solveCSP(cities, n, R, ci):
    if ci == 0:
        # in the beginning any color can be assigned to the first city, let's say 1
        newR = addColor(R, cities[0], 1)
        if newR == False:
            return False
        ans = {cities[0]:1}
        res = solveCSP(cities, n, newR, 1)
        if res == False:
            return False
        ans.update(res)
        return ans
    elif ci == len(cities):
        return {}

    # branching over all possible colors for cities[ci]
    # in this section, implemented backtracking algorithm.
    for color in range(1, n+1):
        ans = {cities[ci]: color}
        newR = addColor(R, cities[ci], color)
        if newR == False:
            continue
        res = solveCSP(cities, n, newR, ci+1)
        if res != False:  # update ans if the res is true
            ans.update(res)
            return ans

    # no choice for the current city
    return False


def assign_color(number):
    colors=[]
    for i in range(1,number+1):
        colors.append(i)






# main program starts
# ===================================================

# creating map of indonesia
# cmap[x] gives the neighbors of the city x  
cmap = {}
cmap["gresik"] = ["lamongan","bandung","surabaya"]
cmap["lamongan"] = ["brebes", "bandung", "gresik"]
cmap["malang"] = ["surabaya","madiun","madura"]
cmap["ponorogo"] = ["indramayu", "cirebon", "pekanbaru"]
cmap["cirebon"] = ["ponorogo", "pekanbaru"]
cmap["tegal"] = ["indramayu"]
cmap["bandung"] = ["lamongan", "brebes", "gresik", "surabaya", "madiun"]
cmap["madiun"] = ["bandung", "malang"]
cmap["madura"] = ["malang", "indramayu"]
cmap["pekanbaru"] = ["ponorogo", "cirebon"]
cmap["indramayu"] = ["madura", "ponorogo", "tegal"]
cmap["surabaya"] = ["gresik", "malang", "bandung"]
cmap["brebes"] = ["lamongan", "bandung"]

# CSP restrictions
# each restriction is modeled as a pair [a,b] which means the city a's
# color is not equal to b, where b is either a color (a number 1 to n) or
# another city. Examples ['gresik', 'lamongan'] means the color of gresik should
# not be equal to lamongan -- ["gresik",4] means the color of bc should not be 4

# initiaitiong restrictions based on the city neighborhood

for x in cmap:
    for y in cmap[x]:
        R.append([x,y])

# initiating a list of cities
cities = []
for p in cmap:
    cities.append(p)


while(1):
    num=int(input("Enter number of the color? "))
    assign_color(num)
    print(solveCSP(cities, num, R, 0))

