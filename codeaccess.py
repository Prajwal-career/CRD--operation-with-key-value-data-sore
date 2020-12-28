import code as x
#i have used as library to code.py file
x.create("yash",25)
#to create a new key_name and value given without time limit
x.create("soni",80,3600)
#to create a key with key_name and value and with time_to_live property in 3600 seconds
x.read("yash")
#it returns value of the respective key in jsonobject format"key_name:value"
x.read("soni")
#it returns value of the resp[ective key_name and value with respective jsoon format "key_name:value"if time to live is not expired else if returns an error
x.create("yash",50)
#if the key is already exist the n it give an error
x.delete("vinay")
#if it  already exists in database then it get deleted with it key and values from memory(memory get freed)
t1=Thread(target=(create or read or delete),args=(key+name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key+name,value,timeout))
t2.start()
t2.sleep()
#the code gives other errors like
#"invalid key" if key length is grester then 32kb
#key does not exists if key does not exist or deleted
#"file memory limit reached"if file memory exceed 1gb
