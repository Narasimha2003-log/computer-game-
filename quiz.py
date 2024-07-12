print("wellcome to computer games")
playing=input("do you want to play? ")
if playing .lower()!= "yes":
    quit()
print ("okay lets play :)")
score=0
answer=input("what is an cpu? ")
if answer == "centeral processsing unit":
    print("correct")
    score +=1

else:
    print("wrong")

answer=input("what is an ps? ")
if answer == "personal system":
    print("correct")
    score += 1
else:
    print("wrong")

answer=input("what is an ram? ")
if answer == "random access memory":
    print("correct")
    score +=1

else:
    print("wrong")


answer=input("what is an gpu? ")
if answer == "graphic processing unit":
    print("correct")
    score += 1
else:
    print("wrong")

answer=input("what is an lcm? ")
if answer == "least common multiple":
    print("correct")
    score += 1
else:
    print("wrong")

print("your score is "+str(score ))