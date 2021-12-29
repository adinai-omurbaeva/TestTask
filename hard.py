import keyboard
from datetime import datetime, time, timedelta
#Тестовые экземпляры классов в комментариях в конце. Можно использовать их для проверки

class TimeCounter:
    def counttime(self):
        my_array = []
        tm = timedelta(hours=0, minutes=0)
        while True:
            print("Чтобы остановить, напечатайте stop")
            num = input('Введите время: ')
            #if keyboard.is_pressed('Ctrl + Q'):
            #    break
            if num == "stop":
                break
            elif type(num) != str or len(num) != 5:
                print("Неверный формат. Напишите полные часы и минуты через двоеточие")
            elif int(num[0:2])  > 24 or int(num[3:]) > 60:
                print("Неверный формат. Слишком большие числа")
            else:
                my_array.append(num.split(":"))
        for i in my_array:
            tm += timedelta(hours=int(i[0]), minutes=int(i[1]))
        print("Сумма всех введенных часов и минут: ", tm)    
            


class Mediana:
    def findmediana(self, data1, data2):
        data1.extend(data2)
        data1.sort()
        a = 0
        b = 0
        result = 0
        if len(data1) % 2 != 0:
            return "merged array =", data1, "and median is ", data1[len(data1)//2]
        else:
            a = len(data1)//2 - 1
            b = len(data1)//2
            result = (data1[a]+data1[b])/2
            return "merged array =", data1, "and median is ", result

class Inversion:
    def inverse(self, my_array):
        return my_array[::-1]

class Concatenation:
    def concatenate(self):
        my_array = ["777", "7", "77", "77"]
        target = "7777"
        j = 0
        i = 0
        print("Valid pairs are:")
        while i < len(my_array):
            if j < len(my_array) and my_array[i] + my_array[j] != target:
                j+=1
            elif j == i:
                j+=1
            elif j >= len(my_array):
                j=0
                i+=1
            else:
                print("(",i,",", j,")", ":", my_array[i], "+", my_array[j])
                j=0
                i+=1

#counter = TimeCounter()
#counter.counttime()

#mediana = Mediana()
#print(mediana.findmediana([1,3,2,4],[5, 7,1,2]))

#inversion = Inversion()
#print(inversion.inverse([1,5,7,9]))

con = Concatenation()
con.concatenate()
#print(con.concatenate(["12", "12", "4", "5"], "124"))