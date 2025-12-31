print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
#정교한 소수점 계산을 위해 "float" 사용
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#이미 정해진 팁% -> "int" 사용
people = int(input("How many people to split the bill? "))
#이미 정해진 사람수 "int" 사용
#number + 1 means 100 for tip
tip_percent = tip / 100 + 1 #As "tip_percent" easy and clearly formatting
bill_split = bill * tip_percent / people #print as "33.60000000000001"
print(f"Each person should pay {bill_split:4.2f}$") #print as "33.60"
#f"{}" 사용해보기
#num_float 포맷하기 -> f-string 이 호환할 수 있도록 string으로
#: 이후 4(총 자리수) .2f(.소수점 이후 두자리 float)



