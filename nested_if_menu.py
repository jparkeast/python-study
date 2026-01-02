    # 1. 환영 인사와 메뉴 설명을 '먼저' 합니다.
print("Hi Welcome to my Practice room!")
    # 코드 전체 들여쓰기 command + A + tap, or shift + tap
    # while True: while 구문으로 생동감있게 반복을 돌려줍니다.
    # python 에서는 or 과 and 사용이 가능합니다.
while True:
    #print("\n" + "=" * 30) 구분을 위한 줄 긋기
    print("=" * 60)
    print("Pick the number -> 1. Rollercoaster, 2. BMI checker, 3. Exit")
    choice = input("Which would you choose? ").lower()

    # 1번 방: 롤러코스터
    if choice == "1":
        print("Welcome to the rollercoaster!")
        height = int(input("What is your height in cm? "))
        bill = 0
        # 이 아래는 1번을 골랐을 때만 실행되도록 들여쓰기 해줍니다.
        if height >= 120:
            print("You can ride the rollercoaster")
            age = int(input("What is your age? "))
            if age >= 12:
                bill = 5
                print("Please pay $5.")
            elif age <= 18:
                bill = 7
                print("Please pay $7.")
            else:
                bill = 12
                print("Please pay $12.")
            wants_photo = input("Do you wanna take any photo? Type y for Yes n for No.")
            if wants_photo == "y":
                print()
            bill += 3 # -> bill = bill + 3
            print(f"Your final bill is ${bill}.")
        else:
            print("Sorry you have to grow taller before you can ride.")

    # 2번 방: BMI 계산기
    elif choice == "2":
        print("Welcome to BMI check!")
        # 이 아래는 2번을 골랐을 때만 실행되도록 들여쓰기 해줍니다.
        weight = 85
        height_m = 1.85
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            print("underweight")
        elif bmi >= 18.5 and bmi < 25:
            print("normal weight")
        else:
            print("overweight")

    elif choice == "3" or choice == "exit":
        print("연습실을 종료합니다. 안녕!")
        break  # break를 만나면 while 반복문이 종료됩니다.
    else:
        print("1, 2 또는 3을 입력해주세요.")