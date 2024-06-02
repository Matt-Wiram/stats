# plist = [1,2,3,4,5]
# pstring = "onomonopoeia"
# print (plist[1:4])
# if 6 in plist:
#     print ("cherry")
# else:
#     print ("taco")
# for x in plist:
#     print (x)
# for x in pstring:
#     print (x)
# print(len(pstring))
x = [0]
def fibonacci():

    while len(x) < 30:
         if len(x) == 1:
             x.append(1)
             print (x)
         else:
            x.append(x[-1] + x[-2])
            print(x)


fibonacci()
