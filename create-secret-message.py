# need to add:
# check if all files here, if folder with files exist, repeat asking text for input is user enter wrong text, skip wrong letters,
# enter more that 26 letters
 
import random
import os
import shutil
 
path = os.getcwd() + '\\alphabet'
# os.chdir(path)
print 'We are here: ' + os.getcwd()
flist = os.listdir(path)
print 'We got list of files for creating our message: '
print flist 
values = ['athens.jpg', 'austin.jpg', 'bangalore.jpg', 'barcelona.jpg', 'beijing.jpg', 'berkeley.jpg', 'bogota.jpg', 'bristol.jpg', 'bucharest.jpg', 'buenos aires.jpg', 'cairo.jpg', 'chennai.jpg', 'chicago.jpg', 'colombo.jpg', 'dallas.jpg', 'delhi.jpg', 'edinbrugh.jpg', 'gainesville.jpg', 'houston.jpg', 'hyderabad.jpg', 'istanbul.jpg', 'ithaca.jpg', 'jacksonville.jpg', 'karachi.jpg', 'kiev.jpg', 'london.jpg', 'los angeles.jpg', 'madrid.jpg']
keys = 'abcdefghijklmnopqrstuvwxyz. '
alphabet = dict(zip(keys, values))
print "This programm create new_prank folder with images need encripted by renamer"
user_text = raw_input("Please insert the text need to encrypt: ")
user_text = user_text.lower()
if not os.path.exists('new_prank'):
        os.makedirs('new_prank')
print 'you statement: ' + user_text
count = 0
for letter in user_text:
        if letter in keys:
                old_file = os.getcwd() + '\\alphabet\\' + alphabet[letter]
                new_name = os.getcwd() + '\\new_prank\\' + str(random.randint(0, 9)) + str(random.randint(0, 9)) + values[count]
                print 'Take this file: ' + old_file
                print 'And place it with name: ' + new_name
                shutil.copyfile(old_file, new_name)
                count+=1
                print 'count = ' + str(count)
        else:
                print "Your text not in abcdefghijklmnopqrstuvwxyz. "
                break
raw_input("The job is done. Press Enter to exit")
