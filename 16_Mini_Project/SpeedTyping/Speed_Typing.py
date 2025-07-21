from time import* 
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(start_time,end_time):
    time_delay = end_time - start_time
    time_Roundoff = round(time_delay,2)
    return time_Roundoff


if __name__ == '__main__':
    while True:
        check = input("Ready to begin: yes or no :")
        if check == 'yes':
            test = ["Hello how are you guys",
            "hello world",
            "now i am learning python",
            "i am also preparing for my placements"]

            test1 = r.choice(test)

            print("  ****  Typing Speed  ******")
            print(test1)
            print()
            print()

            time_1 = time()
            testinput = input("Enter : ")
            time_2 = time()

            print('Speed : ',speed_time(time_1,time_2),"sec")

            print('Error : ',mistake(test1,testinput))
        elif check == "no":
            print("Thank you for using it!")
            break
        else:
            print("wrong input")
            break
        
        
        