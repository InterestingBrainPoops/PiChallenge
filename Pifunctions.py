"""
This is the function versrion, the one that uses functions.
"""
global pic,lnum
def picalc(n):
    global pic
    pic = n*(math.sqrt((1/2)-math.cos(360/n)))
    print("Time from start:", time()-start)
    return pic


"""
while True:
    print("HI")
"""
