# 5174

# for tc in range(1, int(input())+1):
#     e, n = map(int, input().split())

while True:
    data = input()
    try:
        print(int(data[0])+int(data[2]))
    except IndexError:
        break