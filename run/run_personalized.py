from instapy import InstaPy
from instapy import smart_run
import time
import argparse

parser=argparse.ArgumentParser(description= "Instagram automatitioner")

# Parameters
# -- Your account --
parser.add_argument('-u', '--user', help="Your user")
parser.add_argument('-p', '--password', help="Your password")

# -- Account to interact --
parser.add_argument('-t', '--target', help="User that you want to follow his followers")

# -- Some more arguments --
parser.add_argument('-a', '--amount', help="Cantidad")
parser.add_argument('-d', '--delay', help="Delay between actions(in seconds)")

#
parser.add_argument('-fs', '--follow_users_following', help= "Follow the users who follow the target")
parser.add_argument('-fg', '--follow_users_followers', help= "Follow the users the victim follows")

parser= parser.parse_args()

def main():
    if parser.user:
        print("User set correctly: {}".format(parser.user))
        if parser.password:
            print("Password set correctly: {}".format(parser.password))
            try:
                print("Trying to conect to Instagram")
                session= InstaPy(username= parser.user,
                                password= parser.password,
                                headless_browser= False)
                with smart_run(session):
                    #General Settings
                    session.set_skip_users(skip_private= False,
                                            skip_no_profile_pic= False)
                    
                    #Follow 
                    if parser.follow_users_followers:
                        session.follow_user_followers([parser.target], 
                                                amount=int(parser.amount),
                                                randomize=True,
                                                sleep_delay=int(parser.delay))
                    
                    elif parser.follow_users_following:
                        session.follow_user_following([parser.target],
                                                    amount= int(parser.amount),
                                                    randomize= True,
                                                    sleep_delay= int(parser.delay))

                    else:
                        print("You need to insert an option (-fs or -fg)")


            except:
                print("An error occurred")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Leaving by user cancellation")
        time.sleep(2.4)
        exit()

