#working with boolean
israining = True
issunny = True
if israining and issunny:
    print("we might see rainbow")
# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false

# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false
if israining or issunny:
        print('it might be raining or sunny')
# NOT
# true --> false
# false --> true
if not israining:
    print('it must be raining')
    
import math   
print(math.pi)
print(math.e)
print(math.nan)   
print(math.inf)
print(-math.inf)

#Trigonometry
obs_direction = math.cos(math.pi/4)
print(obs_direction) 
obs_direction = math.sin(math.pi/4)
print(obs_direction)

#ceiling and floor
cookie = 10.3
candy = 7.1
candy2 = 7
candy3 = 7.0
print(math.ceil(cookie))# increases the number to the next decimal from 10.3 to 11
print(math.ceil(candy))# increases the number to the next decimal from 7.1 to 7
print(math.ceil(candy2))#remians the number as it is
print(math.ceil(candy3))#remians the number as it is 7.0 remains the same

age = 47.9
print(math.floor(age))# returns only 47
print(math.floor(47.0))# retuns only 
print(math.floor(47.10))# retuns only 47

#factorial and square root
print(math.factorial(3)) # will retun 6 as 3*2*1
print(math.sqrt(64))# will return 8 as 64 is the square root of 8.0 and it sqrt() retuns in decimals.

#greatest common denominator
print(math.gcd(52,8)) # this will result as 4
print(math.gcd(8,52)) # changing the number sequence of the number will not result in a different ouput

#degree and radians
print(math.radians(360)) #will result in 6.283185307179586 radians in a full circle 
print(math.pi*2)# just to verify if the above answer is correct or not
print(math.degrees(math.pi*2))# doing the other side of conversion

#random module
import random
print(random.random())# gives random number between 0 and 1
decider = random.randrange(2)# this is totaly random way of doing a toss,
if decider == 0:
    print('head') # attimes it will print head and at any random time it will print t = ales
else:
    print('tails')    
    
print("your number is " + str(random.randrange(1,7)))  # this is will just behave like a dice  

#random 
lotterywinners= random.sample(range(100),9) # this will sample out 9 numbers list out of 100
print(lotterywinners)
#choice
possible_salary=[1000000,2000000,3000000]
print(random.choice(possible_salary))# it could be any choice at random from above possible_salary
#shuffle function of randoim module.
card = ["jack","queen","king","ace"]
random.shuffle(card)
print(card) # shuffled the cards and each time we do it we get a new shuffled cards
print(random.shuffle(card)) #this will result a "none" printout

# Statistics module 
import statistics
ages = [10,13,14,12,11,10,11,10,15]
print(statistics.mean(ages)) #calculate the mean of ages
print(statistics.mode(ages)) #calculate the ages mode
print(statistics.median(ages)) #calculates the median 
print(sorted(ages)) #sorts the data so that we can verify that our median is correct 
print(statistics.variance(ages))# gives us the variance of the ages
print(statistics.stdev(ages)) #gives us the standard deviation of ages
print(math.sqrt(statistics.variance(ages)))# just to check that our math function also gives the same result.

#itertool
import itertools
#create infinite looping mechanism 
for x in itertools.count(50):# will count untill infinite time 
    print(x)
    if x == 80:
        break;
for x in itertools.count(50,5):# will count untill infinite time but this time by 5
    print(x)
    if x == 80:
        break;      
#infinite cycle 
#Can be used to calculate purmutation and combinations        
#inter tool infinitely cycle through an input.
#for c in itertools.cycle('Ishan Sharma'):
 #   print(c)   #at this point of time the string literals will be printed infinite number of times
#therefore we need to have a beaking condition:
z=0
for c in itertools.cycle('Ishan Sharma'):
    print(c)
    z = z + 1
    if z> 50:
        break 
#infnite repeating 
for c in itertools.repeat(True):
    print(c)
    x = x+1
    if x > 100:
        break
#purmutation and combinations
#purmutation- order matters - same copies with same input but in different order
election = {1:'bob',2:'karen',3:'Erin'} 
for p in itertools.permutations(election.values()):
    print(p)

#combination - order does not matter
color = ['Red','yellow','pink','blue','Black']
for c in itertools.combinations(color,2):# combination takes 2 parameter
    print(c)
    
#command line arguments
    
import sys 
print('number of argument:', len(sys.argv),' arguments.')
print("arguments", sys.argv)    # gets us the command line argument 

#removing the command line
#sys.argv.remove(sys.argv[0])
#print("argument",sys)

arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number 
    except Exception:
        print("bad input")
print(sum)        

#files

myfile = open('ishan.txt','w')# opening the file in the read mode
myfile.write("gbn:100\n ishan") # entering the data in the file
myfile.close()

print("name " + myfile.name) #gives us the name of the file
print("name " + myfile.mode) #gives us the mode of the file


# seek
# all the files have seek point to keep the track of where we are in the file
#before writing anything the seek pointer is at 0
#before reading and writting seek will be set to zero
myfile = open('ishan.txt','r')
print("my one line: " + myfile.readline())  # print one line at a time 
myfile.seek(0)

#iterate through each line of a file
for line in myfile:
    newtype = line.replace('gbn','Sharma') #the gbn got replaced with Sharma 
    print(newtype)
myfile.close()     #closing the file

# import tempfile
#used to store data just for program execution 
import tempfile
tempFile = tempfile.TemporaryFile()

tempFile.write(b"Save this number for me:9654261016")
tempFile.seek(0)

print(tempFile.read())
tempFile.close()

#zipmodule

import zipfile

#open and list
zip = zipfile.ZipFile('standard.zip', 'r') #opening the zipfolder in the read mode
print(zip.namelist())

#metadata in the the zipfolder
for meta in zip.infolist(): 
    print(meta)
    
#['purchased.txt', 'wishlist.txt'] this is the meta data
#<ZipInfo filename='purchased.txt' external_attr=0x20 file_size=17>
#<ZipInfo filename='wishlist.txt' external_attr=0x20 file_size=19>
    
print(zip.read("wishlist.txt")) 
with zip.open("wishlist.txt") as f:
    print(f.read())
    
#extract from zipfile 
zip.extract("purchased.txt") # extracting the particular file
#zip.extractall()  #extracting all the file
zip.close()# closing the file
#datetime
from datetime import datetime
now = datetime.now()
print(now.date()) #current date
print(now.year) #current year
print(now.month)#current month
print(now.hour)#current hour
print(now.minute) #current minute
print(now.time())# printing time

#notes
#%a= abbrivated day of week : MON,TUE,WED
#%A=full day of week, Monday, Tuesday Wednesday 
#%d= days of month number 10th for the "10th of january 
print(now.strftime('%a %A %d'))
#%b abbrivated month name: jan, Feb
#%B full month name: January
#%m month as number: 01 for January
print(now.strftime('%b %B %m'))
#Dec December 12
print(now.strftime('%a %B %d'))
 
#formating date and time:time 
#%H hours
#%M minutes    
#%s second
#%p AM or PM
print(now.strftime('%H: %M: %S: %p'))
#formatting years
#%y abbreviated years as two numbers: 17
#%Y abbreviated years as four numbers: 2017
print(now.strftime('%y %Y'))

#from calendar
import calendar
from datetime import datetime, timedelta
testDate = now + timedelta(days=2)
myFirstlinkedInCourse = now - timedelta(weeks=3)
print(testDate.date())
print(myFirstlinkedInCourse.date())

if testDate > myFirstlinkedInCourse:
    print("Comparison Works")
cal = calendar.month(2001,10)  #prints calendar
print(cal)     
Cal2= calendar.month(2001,10) #print calendar
print(Cal2)

print(calendar.isleap(1999))
print(calendar.isleap(2000))

#making a timer
import time
run = input("start? >")
seconds = 0
if run =="yes":
    while seconds != 10:
        print(">",seconds)
        time.sleep(1)
        seconds +=1
    print(">",seconds)    
#html parser
from html.parser import HTMLParser
class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("start tag: ",tag)
        for attr in attrs:
            print("attr:", attr)
    def handle_endtag(self,tag):
        print("end tag: ", tag)
    def handle_comment(self,data):
        print("comment: ", data)
    def handle_data(self,data):
        print('Data: ', data)
parser = HTMLParser()
parser.feed("<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body>/html>")
print()
#Text warp module
#for formatting text   

import textwrap
textcontainer = """ Writers write descriptive paragraphs because their purpose is to describe something.
 Their point is that something is beautiful or disgusting or strangely intriguing. 
 Writers write persuasive and argument paragraphs because their purpose is to persuade or convince someone"""

print("No dedent:")
print(textwrap.fill(textcontainer)) # here the textwrap automatically breaks the paragraph.


print("Dedent")
dedent_text = textwrap.dedent(textcontainer).strip() #keeps the initial spaces. In our original text, the paragraph dendent is kept 
print(dedent_text)

print("Fill")
print()
print(textwrap.fill(dedent_text,50)) #fills 50 characters in the screen

print("contolling Indent")
print(textwrap.fill(dedent_text, initial_indent= "  ", subsequent_indent="  " ))

print("Shorting text")
short = textwrap.shorten("Ishan is a Graduate Student", width= 15, placeholder="....")
print(short)

#HTTP module
import json
import urllib.request

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
    text = f.read()
    decodedtext = text.decode('utf-8')
    print(textwrap.fill(decodedtext,width=50))
print()

obj=json.loads(decodedtext)  
print(obj['kind'])  

print(obj ['items'][0]['searchInfo'] ['textSnippet'])
