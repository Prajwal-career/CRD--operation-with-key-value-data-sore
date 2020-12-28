import threading
#this is for python 3.0
from threading import*
import time
d={}
#create dictionary for storing data 
def create(key,value,timeout=0):
#create() which having three arguments timeout is optional
      if key in d:
          print("error:this key is already exists")
      else:
          if(key.isaplha()):#isaplha() is for checking the is alphabet or not
              if len(d)<(1024*1024*1024) and value<=(16*1024*1024):# due to instrutions file size is less than 1gb and json value is than 16kb
                  if timeout==0:
                      l=[value,timeout]
                  else:
                      l=[value,time.time()+timeout]
                  if len(key)<=32:#for input key_name utpo 32 chars
                      d[key]=l
              else:
                  print("error:Memory limit exceeded!!")
def read(key):
        if key not in d:
            print("error:given key doe not exists in data base.please enter a valid key ")
        else:
            b=d[key]
            if b[1]!=0:
                if time.time()<b[1]:#comparing present time with expiry time
                    stri=str(key)+":"+str(b[0]) #returning the value in the format of json object
                    return stri
                else:
                    print("error:time_to_live of",key,"has expired")
            else:
                stri=str(key)+":"+str(b[0])
                return stri
                
def delete(key):
      if key not in d:
          print("error :given key not exist iin data base,please enter a valid key")
      else:
          b=d[key]
          if b[i]1=0:
              if time.time()<b[1]:
                  del d[key]
                  print("key is successfuilly deleted")
                  
