import json
import sys
import os
import threading
import time

def create():     #FUNCTION FOR CREATING AND INSERTING NEW KEY VALUE PAIR
  print("PLEASE ENTER KEY")
  k = input()
  path = '/Users/viz/Desktop/datastore.txt';
  size = os.path.getsize(path)
  if (len(k) > 32):     #TO CHECK IF THE KEY VALUE IS CAPPED WITHIN 32 CHARACTERS
    print("SIZE OF KEY MUST BE WITHIN 32 CHARACTERS")
  elif (size > 1073741824):      #TO CHECK IF THE SIZE OF THE FILE IF WITHIN 1GB
    print("SIZE OF THE FILE IS GREATER THAN 1GB")
  else:
    #with open('datastore.txt') as f:    #CONVERTING JSON OBJECT TO DICTIONARY
     # data = json.load(f)

    if k in person_dict:     #TO CHECK IF KEY ENTERED IS ALREADY PRESENT OR NOT
      oldtime = 0
      oldtime = dict_time[k]
      if(oldtime+60<time.time()):      #IF THE KEY IS PRESENT CHECK IF TIME_TO_LIVE NOT EXCEEDED
        print("PLEASE ENTER VALUE")
        value=int(input())      #IF TIME-TO-LIVE EXCEEDED GET NEW VALUEAS INPUT AND UPDATE THE VALUE
        person_dict[k]=value
        with open('datastore.txt', 'w') as json_file:
          json.dump(person_dict, json_file)
      else:     #IF TIME-TO-LIVE NOT EXCEEDED DISPLAY THAT KEY IS ALREADY PRESENT AND CANNOT BE UPDATED
        print("THE KEY IS ALREADY IN THE DICTIONARY")
    else:     #IF KEY IS NOT PRESENT GET VALUE AND ADD TO THE DICTIONARY
      print("PLEASE ENTER VALUE")
      v = input()
      if (sys.getsizeof(v) > 16384):   #TO CHECK IF THE SIZE OF THE VALUE IS WITHIN 16 KB
        print("SIZE OF THE VALUE ENTERED OCCUPIES MORE THAN 16 KB")
      else:
        person_dict[k] = v
        dict_time[k]=time.time()
        with open('datastore.txt', 'w') as json_file:    #CONVERTING DICTIONARY INTO JSON OBJECT AND STORING IN FILE
          json.dump(person_dict, json_file)

def read():   #FUNCTION FOR READING THE VALUE OF A GIVEN KEY
  print("PLEASE ENTER KEY")
  k = input()
  with open('datastore.txt') as f:
    data = json.load(f)
  if k in data:   #TO CKECK IF KEY IS PRESENT
    oldtime=0
    oldtime=dict_time[k]
    if (oldtime + 60 >time.time()):   #TO CKECK IF THE TIME-TO-LIVE HAS NOT EXPIRED
      print(person_dict[k])
    else:
      print("THE TIME-TO-LIVE OF THE KEY IS EXPIRED")
  else:   #IF KEY IS NOT PRESENT IN THE DICTIONARY
    print("THE KEY ENTERED IS NOT PRESENT")

def delete():   #FUNCTION TO DELETE A KEY-VALUE PAIR
  print("PLEASE ENTER KEY")
  k = input()
  with open('datastore.txt') as f:
    data = json.load(f)
  if k in data:   #TO CHECK IF THE KEY IS PRESENT IN THE DICTIONARY
    oldtime = dict_time[k]
    if (oldtime + 60 <time.time()):   #TO CHECK IF THE TIME-TO-LIVE HAS NOT EXPIRED
      print("THE TIME-TO-LIVE OF THE KEY IS EXPIRED")
    else:
      person_dict.pop(k)   #REMOVE KEY-VALUE PAIR
      with open('datastore.txt', 'w') as json_file:
        json.dump(person_dict, json_file)
  else:   #IF KEY NOT PRESENT
    print("THE KEY ENTERED IS NOT PRESENT")


person_dict={}
dict_time={}
#SELECTING THE OPERATION TO PERFORM
while(True):
  print("For create press c")
  print("For read press r")
  print("For delete press d")
  print("For exit press e")
  print("For multithreading press m")

  with open('datastore.txt', 'w') as json_file:
    json.dump(person_dict, json_file)
  inp=input()
  if(inp!="c" and inp!="r" and inp!="d" and inp!="e" and inp!="m"):
    print("PLEASE PRESS  C OR R OR D OR M")
  if(inp=="c"):
    create()
  if (inp == "r"):
    read()
  if(inp=="d"):
    delete()
  if(inp=="m"):
    thread1=threading.Thread(target=(create ),args=())
    thread2 =threading.Thread(target=(delete), args=())
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
  if(inp=="e"):
    break
