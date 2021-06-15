#SHART-1: Tubsonlar topishning mukammal algoritmini yozish. N kiritadi Ngacha tubsonlarni chiqarib bersin

myNumber = int(input('sonni kiriting!'))
if myNumber > 1:
    for i in range(2, int(myNumber/2)+1):
        if (myNumber % i) == 0:
            print(myNumber, "tub son emas")
            break
    else:
        print(myNumber, "tub sondir") 
else:
    print(myNumber, "tub son emas")
    

################################ikkinchi urunish
#myNumber = [int(x) for x in "1234567891011121314151617181920".split(",") if x.strip().isdigit()]
##myNumber=list(myList)

# myNumber=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# tub_son=[]
# tub_son_emas=[]

# for n in myNumber:
#     if n > 1:
#         for i in range(2, int(n/2)+1):
#             if (n % i) == 0:
#                  flag = True
#                  break

#             if flag:
#                 tub_son.append(n)
#             else:
#                 tub_son_emas.append(n)
# print(tub_son)
