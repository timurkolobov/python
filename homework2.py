"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

Пример:


n = 385916 -> yes
n = 123456 -> no
"""
def is_lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) != 6:
        return False
    
    first_half_sum = sum(int(digit) for digit in ticket_str[:3])
    second_half_sum = sum(int(digit) for digit in ticket_str[3:])
    
    return first_half_sum == second_half_sum

# Пример использования
ticket = int(input("Введите номер билета: "))
if is_lucky_ticket(ticket):
    print("yes")
else:
    print("no")