import webbrowser
import time


counter=0
for i in range(5):
    for i in range(10):
        webbrowser.open_new("http://www.ozgurkavak.com/")
        i += 1
        counter += 1
        print(counter)
        time.sleep(1)
    time.sleep(5)