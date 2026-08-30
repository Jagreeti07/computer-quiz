print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is computer? ")
if answer.lower() == "machine":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is os stands for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is ALU stands for? ")
if answer.lower() == "arithmetic logic unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("give one example of os? ")
if answer.lower() == "windows":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is SSD stands for? ")
if answer.lower() == "solid state drive":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("give one example of output device? ")
if answer.lower() == "printer":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    


        

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")