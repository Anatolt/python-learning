import time
import webbrowser

num = 0
print "This program started on "+time.ctime()
while num < 3: # how many breaks you want
    time.sleep(1) # here enter time between breaks. In seconds. 1h = 60*60
    webbrowser.open("http://at02.ru/category/code/") # what do you want to open
    num += 1
