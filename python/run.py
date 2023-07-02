from voice import listen

from chatbot import chatbot1
from save import say

'''
Aseel Bdoor
'''
global qu,ans
def voice():
    global qu,ans
    qu=listen()
    ans=chatbot1(qu)
    # say(qu)
    print(qu)
    say(ans)
    print(ans)
def voicetext () :
    return qu,ans
