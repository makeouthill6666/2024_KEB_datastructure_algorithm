katok = ["A", "B", "C", "D", "E"]

def insert_data(position, friend):

    if position <0 or position > len(katok):
        print("error")
        return

    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend



def delte_data(position):

    if position <0 or position > len(katok):
        print("error")
        return
    kLen = len(katok)
    katok[position] = None

    for i in range (position+1, kLen) :
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[kLen-1])
insert_data(2, "LOVE")
delte_data(3)
print(katok)