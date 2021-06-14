#EN|BUTTONS ARE CREATED THOSE MOVE THE DATA STORED BOTH HORIZONTALLY AND VERTICALLY
#UZ| ENIGA VA BO'YOIGA TIZILGAN DATALARNI HARAKATLANTIRUVCHI TUGMALARNI YARATAMIZ
tuneButton=1
startButton=0

#EN| A: FIRST FUNCTION IS TO SET THE MOVEMENT CHARRACTER OF BOTH COLUMNS(a range of horizontal data) AND INDEXES(a range of vertical data)
#UZ| A: BIRINCHI FUNKSIYAMIZDA QATORLAR(garizontal/eniga tizilgan datalar) VA USTUNLARNI(vertikal/bo'yiga tizilgan datalar) HARAKATLANISH HARAKTERINI BELGILAB OLISH.
def myMatrix_ROTATION(null_matrix):
    
	if not len(null_matrix):
		return
	vertical_top = startButton
	vertical_bottom = len(null_matrix)-tuneButton

	horizontal_left = startButton
	horizontal_right = len(null_matrix[0])-tuneButton

	while horizontal_left < horizontal_right and vertical_top < vertical_bottom:
		previos_turn = null_matrix[vertical_top+tuneButton][horizontal_left]
        #EN: 1) FROM TOP LEFT TO TOP RIGHT
        #UZ: 1) CHAP YUQORIDAN CHAP O'NGA
		for i in range(horizontal_left, horizontal_right+tuneButton):#
			currentPoint = null_matrix[vertical_top][i]
			null_matrix[vertical_top][i] = previos_turn
			previos_turn = currentPoint

		vertical_top += tuneButton
        #EN: 2) FROM THE RIGHT TOP TO THE RIGHT BOTTOM 
        #UZ: 2) YUQORI O'NGDAN PAST O'NGA
		for i in range(vertical_top, vertical_bottom+tuneButton):
			currentPoint = null_matrix[i][horizontal_right]
			null_matrix[i][horizontal_right] = previos_turn
			previos_turn = currentPoint

		horizontal_right -= tuneButton
        #EN: 3)FROM THE BOTTOM RIGHT TO THE BOTTOM LEFT
        #UZ: 3)PAST ON'GDAN PAST CHAPGA
		for i in range(horizontal_right, horizontal_left-tuneButton, -tuneButton):
			currentPoint = null_matrix[vertical_bottom][i]
			null_matrix[vertical_bottom][i] = previos_turn
			previos_turn = currentPoint

		vertical_bottom -= tuneButton
        #EN: 4)FROM THE LEFT BOTTOM TO THE LEFT TOP 
        #UZ: 4)PAST CHAPDAN YUQORI CHAPGA
		for i in range(vertical_bottom, vertical_top-tuneButton, -tuneButton):
			currentPoint = null_matrix[i][horizontal_left]
			null_matrix[i][horizontal_left] = previos_turn
			previos_turn = currentPoint

		horizontal_left += tuneButton

	return null_matrix

#EN| B: SEPERATE FUNCTION TO ITERATE/LOOP THROUGH THE CUSTOMIZABLE MATRIX
#UZ| B: XUSUSIYATLANADIGAN MATRITSANI LOOP(DO'NDIRISH) QILISH UCHUN ALOHIDA FUNKSIYA
def matrix_generator(matrix_input):
	for horizontal_loc in matrix_input:
		print (horizontal_loc)
    
        
## CUSTOMIZABLE MATRIX
## XUSUSIYATLANADIGAN MATRITSAMIZ
matrixData =[
			[1, 2, 3, 4 ],
			[5, 6, 7, 8 ],
			[9, 10, 11, 12 ],
			[13, 14, 15, 16 ]
		]

## CALL BOTH OF THE FUNCTIONS PROGRAMMED ABOVE
## YUQORIDA DASTURLAGAN IKKKITA FUNKSIYAMIZNI CHAQIRAMIZ
matrixData = myMatrix_ROTATION(matrixData)
matrix_generator(matrixData)
