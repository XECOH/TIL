# for i in range(1, 5) :
#     print("*" * i)
# #반복될 횟수 +1
#
# i = 1
# while i <= 4 :
#     print("*" * i)
#     i = i + 1
#
# for i in range (1, 3) :
#     for k in range(1, 5) :
#         print("*" * k)

# i, j = 1, 1
# while i <= 2 :
#     while j <= 4 :
#         print("*" * j)
#         j = j + 1
#     i = i + 1
#     j = 1

# i, k = 5, 1
# while i >= 0 :
#     print("{0}{1}".format(" " * i, "*" * (2 * k - 1)))
#     i = i - 1
#     k = k + 1

# scores = [88, 30, 61, 55, 95]
# i=0
# for score in scores :
#     if score >= 60 :
#         print("{0}번 학생은 {1}점으로 합격입니다.".format(i+1, score))
#     else :
#         print("{0}번 학생은 {1}점으로 불합격입니다.".format(i+1, score))
#     i +=1

# total = 0
# for k in range(1,100):
#     if k % 3 == 0 :
#         total += k
# print("1부터 100사이의 숫자 중 3의 배수의 총합: %d" % (total))


from collections import Counter

# students= ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# a=0
# b=0
# o=0
# ab=0
#
# for student in students:
#     if student == 'A':
#         a += 1
#     elif student == 'B':
#         b += 1
#     elif student == 'O':
#         o += 1
#     else :
#         ab += 1
# print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" %(a, o, b, ab))

# students = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
#
# total = 0
# i = 0
# count = len(students)
#
# while i < len(students) :
#     if students[i] >= 80:
#         total += students[i]
#         students.pop(i)
#     i += 1
#
# print(total)

# for i in range(5, 0, -1) :
#     print("*" * i)
# #반복될 횟수 +1

# i = 5
# while i > 0 :
#     print("*" * i)
#     i = i - 1
#

# i, k = 4, 1
# while i >= 0 :
#     print("{0}{1}".format(" " * k, "*" * (2 * i - 1)))
#     i = i - 1
#     k = k + 1

# 6249 모르겠다
# a=input()
# b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print("%d %d %d %d %d %d %d %d %d %d" % ())

#

# text = input()
# l = len(text)
# for i in range(0,l):
#     text[i]
#     print(text[i], end='')
#
# text = input()
# l = len(text)
#
#
#
# for j in range(l-1, -1, -1):
#     b = text[j]
#     word = print(b, end='')
#
# def check_palindrome(w):
#     if w == w[::-1]:
#         print("\n입력하신 단어는 회문(Palindrome)입니다.")
#
# check_palindrome(text)

# p1 = input("플레이어 1의 이름을 입력해주세요")
# p2 = input("플레이어 2의 이름을 입력해주세요")
#
# rsp1 = input("플레이어 1의 가위바위보를 입력해주세요")
# rsp2 = input("플레이어 2의 가위바위보를 입력해주세요")
#
# def rosipa(rsp1, rsp2):
#     if rsp1 == '가위' and rsp2 == '바위':
#         print(f'{rsp2}가 이겼습니다!')
#     elif rsp1 == rsp2 :
#         print('비겼습니다!')
#     elif rsp1 == '바위' and rsp2 == '보' :
#         print(f'{rsp2}가 이겼습니다!')
#     elif rsp1 =='가위' and rsp2 == '보' :
#         print(f'{rsp1}가 이겼습니다!')
#     elif rsp1 == '바위' and rsp2 =='가위':
#         print(f'{rsp1}가 이겼습니다!')
#     elif rsp1 == '보' and rsp2 == '가위':
#         print(f'{rsp2}가 이겼습니다!')
#     else:
#         print(f'{rsp1}가 이겼습니다!')
#
# rosipa(rsp1, rsp2)

# 6321번 문제
# number = int(input())
# def check_prime(n):
#     cnt = 0
#     for i in range (1, n+1):
#         if n % i == 0 :
#             cnt += 1
#     if cnt == 2 :
#         print("소수입니다.")
#     else:
#         print("소수가 아닙니다.")
#
# check_prime(number)

# number = int(input())
#
# def factorial(n):
#     a= 1
#     for i in range(1, n+1):
#         a *= i
#     return a
#
# print(factorial(number))

a, b = input().split(',')
a = int(a)
b = int(b)

def squ(n):
    return print(f'square({n}) => )n**2

print(f'square({a}) => squ({a})')
print(f'square({b}) => squ({b})')


