# Импорт функции из модуля в наш проект

# import modul1
# print(modul1.max_1(5,9))

#или

# from modul1 import max_1
# print(max_1(5,9))

# Если не хотим перечислять все функции из модуля,
# можно сделать такую запись

# from modul1 import * 
# print(max_1(5,9))

# Сокращение имени модуля в самой программе

import modul1 as m1
print(m1.max_1(5,9))