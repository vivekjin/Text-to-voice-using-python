import os
if __name__ == '__main__':
    print("welcome to RoboSpeaker by vivek")
    while True:
        x = input("enter command \n")
        if x == "":
            break
        command = f'mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{x}"")(window.close)")'
        os.system(command)
