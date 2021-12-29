import numpy as np
import random
#Тестовые экземпляры классов в комментариях в конце. Можно использовать их для проверки

class FirstTask:
    def twoarray(self):
        first_array = list(np.random.randint(1, 6, 10))
        second_array = list(np.random.randint(1, 6, 10))
        new_array = set(first_array + second_array) #Чтобы получить сами значения внутри списков без повторов, для проверки
        count = 0
        result = []
        print("First array: ", first_array)
        print("Second array: ", second_array)
        for i in new_array:
            result = list(np.where(first_array == i))
            result2 = list(np.where(second_array == i))
            count = len(result[0])+len(result2[0])
            print("value: ", i, " indexes: ", result[0], result2[0])
            print("Количество совпадений: ", count)
            print(" ")
           
        
class SecondTask:
    def negativenumber(self):
        my_array = np.random.randint(-5, 6, 10)
        print("Start array: ", my_array)
        result = []
        for i in my_array:
            if i < 0:
                result.append(i)
        result.sort()
        return result

class ThirdTask:
    def sentences(self):
        my_text = "Строка Админ удалил привет Инструменты новый инструментарий про Строка котиков привет"
        words = ["привет", "Строка", "Инструменты"]
        new_text = my_text.split()
        result_text = []
        for word in new_text:
            if word not in words:
                result_text.append(word)
        result = " ".join(result_text)
        return result

first= FirstTask()
first.twoarray()

#second = SecondTask()
#print(second.negativenumber())

#third = ThirdTask()
#print(third.sentences())