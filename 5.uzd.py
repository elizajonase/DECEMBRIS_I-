import datetime

def sveiciens():
    stunda = datetime.datetime.now().hour

    if 6 <= stunda < 12:
        print("Labrīt!")
    elif 12 <= stunda < 18:
        print("Labdien!")
    else:
        print("Labvakar!")

sveiciens()