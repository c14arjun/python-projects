print("Welcome to chat bott!")
import time
from datetime import datetime
current_hour=datetime.now().hour
print(current_hour)
print("hello programmer")
morning_messages="good morning have a nice day ahead"
afternoon_messages="good afternoon keep up the good work"
if 5<= current_hour <12:
    print("morning messages")
elif 12<= current_hour <17:
    print(afternoon_messages)