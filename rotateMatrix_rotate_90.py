# SHAR-2: Matritsani 90gradusga buruvchi dastur
mySquare = 4
tuneButton=1
startButton=0

#BIRINCHI FUNKSIYAMIZDA QATORLAR(garizontal/eniga tizilgan datalar) VA USTUNLARNI(vertikal/bo'yiga tizilgan datalar) HARAKATLANISH HARAKTERINI BELGILAB OLISH.
def rotateMatrix_rotate_90(abstract_matrix):
    for a_fold in range(0, int(mySquare / 2)):#NESTED LOOPIMIZNI BIRINCHI DO'NGISIDA ENIGA, BO'YIGA TO'RT TARAFDAN BO'LIB CHIQAMIZ
        for data in range(a_fold, mySquare-a_fold-tuneButton):#IKKINCHI NESTED LOOPIMIZDA ENIGA BO'YIGA TIZILGAN MATRIX HUJAYRALARIDAGI BARCHA DATALARNI LOOP QILAMIZ
            temp = abstract_matrix[a_fold][data]#LOOP QILINGAN BARCHA ENIGA BO'YIGA TIZILGAN DATALARNI SAQLASH UCHUN VAQTINCHALIK O'ZGARUVCHAN YARATMIZ
            abstract_matrix[a_fold][data] = abstract_matrix[data][mySquare-tuneButton-a_fold]# 1) VAQTINCHALIK O'ZGARUVCHANDA SAQLANAYOTGAN DATALARNI O'NG TARAF O'NGDAN YUQORIGA HARAKATLANTIRAMIZ
            abstract_matrix[data][mySquare-tuneButton-a_fold] = abstract_matrix[mySquare-tuneButton-a_fold][mySquare-tuneButton-data]# 2) PAST TARAF CHAPDAN O'NGA 
            abstract_matrix[mySquare-tuneButton-a_fold][mySquare-tuneButton-data] = abstract_matrix[mySquare-tuneButton-data][a_fold]# 3) CHAP TARAF YUQORIDAN PASTGA
            abstract_matrix[mySquare-tuneButton-data][a_fold] = temp#DATALAR HARAKATINI CHAPGA BURADIGAN VAQTINCHALIK O'ZGARUVCHAN YARATAMIZ

# YUQORIDA FUNKSIYAMIZNI CHAQIRAMIZ VA MATRITSA HUJAYRALARINI LOOP QILAMIZ
def matrix_transform( abstract_matrix ):
    for i in range(startButton, mySquare):  
        for j in range(startButton, mySquare):      
            print (abstract_matrix[i][j], end = ' ')
        print ("")
    abstract_matrix=[]
    for x in range(mySquare):
        for y in range(mySquare):
            if y==startButton:
                abstract_matrix.append(y)

#IKKITA FUNKSIYANI BIR FUNKSIYA ICHIGA JOYLAYMIZ(KEYINCHALIK FUNKSIYA OSON CHAQIRILISHI UCHUN)
def print_func(print_this):
    rotateMatrix_rotate_90(print_this)
    matrix_transform(print_this)



## XUSUSIYATLANADIGAN MATRITSAMIZ
concrete_matrix = [ [100, 20, 30, 40 ],
                    [500, 6, 7, 8 ],
                    [900, 10, 11, 12 ],
                    [130, 14, 15, 16 ] ]

#NATIJANI PRINT QILIB MATRITSAMIZ 90 GRADUSGA(SOAT AYLANISHIGA TESKARI) BURAMIZ       
print_func(concrete_matrix)
