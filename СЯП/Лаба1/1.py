n = input("Введите число: ")
sum = 0
 
if n.isdigit(): #проверяем, являются ли введённые данные числом
    n = int(n) #если да, то переводим полученную строку в число, с которым будем работать
    while n != 0: 
        digit = n % 10 #здесь мы берём последнюю цифру полученного числа
        if digit % 2 == 0: #проверяем на чётность
            sum += digit #если всё в порядке, то добавляем в sum
        n //= 10 #делаем целочисленное деление на 10, чтобы убрать последнюю цифру
    print(sum)
else:
    print("Некорректный ввод") #если введённые данные не цифра, а набор символов или цифры с символами, буквами и прочим, то мы получим это сообщение.