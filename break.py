import time
import webbrowser

num = 0
print "This program started on "+time.ctime()
while num < 3:
    time.sleep(1) # here enter time between breaks. In seconds. 1h = 60*60
    webbrowser.open("http://at02.ru")
    num += 1
