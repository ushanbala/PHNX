def console(arg):
    print(arg)

import sys
import os
script_dir= os.path.dirname(os.path.abspath(__file__))
project_root= os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(project_root)
# this is the start of the code

def test(age,name):
    # we check if the user is a minor or an adult here
    if age<18 :
        console('you are still a child {name}')
    else:
        console(f'Aight you are fuckable {name}')
    


# we call the function here

test(18,'ukdzzz')
