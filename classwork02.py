# Передача функции неизвестного количества элементов

def sum_str(*args):
    res = ""
    for i in args:
        res += i
    return res
print(sum_str('q','a','l'))        
print(sum_str('q','a','l','r','f'))   
#print(sum_str(1,8,9))   