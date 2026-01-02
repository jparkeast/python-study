#Modulo : 나누고 난 값의 남은 나머지 값만 가져온다. (남은 값이 답)
#print(6 % 2)
#print(6 % 5)
#print(6 % 4)
# int(input), print(input) 터미널에서 할 질문과 내가 입력할 방식을 선택할때 사용!
print("Let's check, would it be odd or even?")
number = int(input("Pick any number you want:"))
modulo_n = int(input("Pick any number to process modulo:"))
#응용해보기
if number % modulo_n == 0:
    print(f"{number}는 {modulo_n}으로 나누어 떨어져 남어지가 0 입니다.")

else:
    print(f"{number}를 {modulo_n}로 나누고 남은 수는 {number % modulo_n}입니다!")

#원본
#안젤라의 원본수업
#number = int(input("숫자를 입력하세요: "))

#if number % 3 == 0:  #무조건 3로만 나눕니다!
#    print("Even")    #3로 나누어떨어지면 무조건 짝수
#else:
#    print("Odd")     #그게 아니면 무조건 홀수
