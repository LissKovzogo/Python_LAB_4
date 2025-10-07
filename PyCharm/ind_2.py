print(f"11. В списке, состоящем из вещественных элементов, вычислить:\nНомер максимального по модулю элемента списка;\nСумму элементов списка, расположенных после первого положительного элемента.\nПреобразовать список таким образом, чтобы сначала располагались все элементы, целая часть которых лежит в интервале от a до b,а потом - все остальные.")
a =  list(map(int, input("Введите список: ").split()))
s = int(input("Ведите нижнюю границу диапазона: "))
b = int(input("Ведите верхнюю границу диапазона: "))
min_a = min(a)
max_a = max(a)
ind = a.index(max_a)
sum_a = 0
if abs(min_a) > max_a:
    ind = a.index(min_a)
ind_s = -1
for i in a:
    if i > 0:
        ind_s = a.index(i)
        break
sum_a  = sum(a[ind_s+1::])
a = sorted(a, key=lambda x: (0 if s <= x <= b else 1, x))
print(ind)
print(sum_a)
print(a)