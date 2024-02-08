import random


target_number = random.randint(1, 100)
chance = 7
print("1-100")

while chance != 0 :
    guess_number = int(input("Input guess number : "))
    if guess_number == target_number :
        print("Correct")
        break
    elif guess_number > target_number :
        chance = chance - 1
        print(f"lower. {chance} chance left")
    else :
        chance = chance - 1
        print(f"higher. {chance} chance left")

else :
    print ("no more chance")
