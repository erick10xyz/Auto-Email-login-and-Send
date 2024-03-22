import os
# from datetime import date
import pause

# x = date.today()

# Work_contract can be replaced of how many times you want to send email
work_contract = 2
is_resigned = False

#  Send email loop
while not is_resigned:
    os.system("python main.py")
    print(work_contract)
    work_contract -= 1
    if work_contract == 0:
        is_resigned = True
        break
    #  You can decide how many days will you pause then resend your email
    pause.days(90)


