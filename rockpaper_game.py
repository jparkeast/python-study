import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    print("!Welcome to Rock Paper Scissors!")
    print("*" * 35 + "\n" + "*" * 35) #input이후에 사용한다면, 입력 이후에 표시됨

    rockpaper_game = [rock, paper, scissors]
    result = ["비겼습니다", "당신이 이겼습니다", "당신이 졌습니다"] #결과 메세지를 리스트에 담기
    logic_rps = [ #임의 가위바위보 이후 결과를 리스트에 담기 [ai 의 선택]
        [0, 1, 2], #user가 0일때(바위), [무, 패, 승]
        [1, 0, 2], #user가 1일때(보), [승, 무, 패]
        [2, 1, 0]  #user가 2일때(가위), [패, 승, 무]
    ]
    valid_choices = [0, 1, 2, 3] #허용하는 값 리스트 지정하기

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Quit"))
    if user_choice not in valid_choices: #if not in 만약 입력값이 이 리스트에 "없다면"
        print("입력이 잘못되었습니다!!!  0, 1, 2, 3중에 하나 골라주세요!")
        continue
    if user_choice == 3:
        print("게임을 종료합니다.")
        break
    ai_choice = random.randint(0, 2) #input시 결과 랜덤으로 돌리기
    print(f"\nuser's pick: {rockpaper_game[user_choice]}") #정해둔 rps를 사용하면
    print(f"\nai's pick: {rockpaper_game[ai_choice]}") #정해둔 ai값으로 받기
    result_print = logic_rps[user_choice][ai_choice] #결과 뽑아주기
    print(result[result_print])
