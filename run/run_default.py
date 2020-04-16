from instapy import InstaPy
from instapy import smart_run
import time

def main():
    user= input("Set your user: ")
    password= input("Set your password: ")
    target= input("User you wan to interact: ")
    amount= int(input("Number of actions you want to do: "))
    delay= int(input("Time to wait between actions: "))
    interaction= input("Press 1 to follow {} followers or press 2 to follow {} following: ".format(target, target))

    try:
        print("Trying to conect to Instagram")
        session= InstaPy(username= user,
                        password= password,
                        headless_browser= False)

        with smart_run(session):
            #General Settings
            session.set_skip_users(skip_private= False,
                                    skip_no_profile_pic= False)
            
            #Follow 
            if interaction == 1:
                session.follow_user_followers(target, 
                                        amount=amount,
                                        randomize=True,
                                        sleep_delay=delay)
            
            elif interaction == 2:
                session.follow_user_following(target,
                                            amount= amount,
                                            randomize= True,
                                            sleep_delay= delay)

            else:
                print("Please insert a valid option")


    except:
        print("An error occurred")
        print("Rerun the executable an if the problem persist comunicate with the developer by GitHub")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Leaving by user cancellation")
        time.sleep(2.4)
        exit()

