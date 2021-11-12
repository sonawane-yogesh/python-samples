import sys
import json

def writefile():

       print("Starting Program...")
       try:

           file=open("D:\sample-1.txt","w") # 'w' mode is for existing file
           file1=open("D:\sample-2.txt","a") # "a" mode open file for writing & if file doesn't exists then create file also  
           L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
           file.write("Hello \n")
           file.writelines(L)
           file.close() # close file to change file access mode
       
       except Exception:
        
        
        print("exception while writing file")

       finally:

         print("In finally block")

def readfile():

        try:
            file=open("D:/sample-1.txt","r+")
            print ("Output of read file")
            print(file.read())
            file.close()

            file1=open("D:/sample-1.txt","r+")
            print("*****Output of readlines*****")
            data=file1.readlines()
            for item in data:
                word=item.split()
                print(word)

            file1.close()
           
        except :
            print(sys.exc_info()[0])       

def readjsonfile():

        try:
            f=open("D:\sample-json.json")   
            data=json.load(f)
            for d in data:
             print(d)
            
        except:
            print(sys.exc_info()[0]) 

def writejsonfile():
        dictionary=[{
        "name" : "abcd",
        "rollno" : 51,
        "cgpa" : 8.1,
        "phonenumber" : "9976770500"
        },{
        "name" : "pqr",
        "rollno" : 52,
        "cgpa" : 8.2,
        "phonenumber" : "1234567890"
        },{
        "name" : "xyz",
        "rollno" : 53,
        "cgpa" : 8.3,
        "phonenumber" : "9158554064"
        },{
        "name" : "lmn",
        "rollno" : 54,
        "cgpa" : 8.4,
        "phonenumber" : "9881794641"
        }]
        try:
            print("writing json files")   
            json_object=json.dumps(dictionary,indent=4)
            with open("D:/student.json","w") as outfile:
                outfile.write(json_object)

        except:
            print(sys.exc_info()[0])


