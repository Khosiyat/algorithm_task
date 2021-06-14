#table.txt fayli berilgan shu fayldan kerak ma'lumotni topuvchi dastur

def searchFor_item(search_word, myFile):
    # search_word = '____ '
    reaidingFile = myFile.read()
    
    if search_word in reaidingFile: 
        print('Siz qidirgan', search_word, 'malumot matnda mavjud emas')
    else: 
        print('Mana', search_word , 'Siz qidirgan malumot') 
    
    myFile.close() 

input = (input('istagan malumotingiz kalit suzini kiriting!'))
my_currentDoc = open("C:/Users/user/Desktop/sentiment_py/positive.txt", "r") #directory ni o'zgaritishingiz mumkun. 

searchFor_item(input, my_currentDoc) 
