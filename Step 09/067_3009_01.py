x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_total = (max(x_list) + min(x_list)) * 2
y_total = (max(y_list) + min(y_list)) * 2

print(x_total - sum(x_list), end=' ')
print(y_total - sum(y_list))