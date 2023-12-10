# FILE HANDLING

#  w   - open the file in write only mode , if the files not exist , creates the files in the directory
#  r   - open in read only mode , if not exist exception is Raised
#  r+  - open file in read and write mode , if not exists exception is raised
#  w+  - open file in read and write mode , if not exists file is created
#  a   - open file in append mode , so the content can be appended / written at end of file

"""
# FILE OPERATORS ARE IRREVERSIBLE

f = open('bill.txt', 'w')
print(f)
print(f.name)
print(f.mode)
print(f.writable())
print(f.write("what happening\n"))  #cursor at last
print(f.write("Hi Hello what happening\n"))  #cursor to next line
print(f.write("hey buddy "))
print(f.seek(3))
print(f.close())


f = open("bill.txt",'r')
print(f)
print(f.name,f.mode,f.writable())
print(f.read())
print(f.tell())      # where the cursor is present
print(f.seek(1))     # seek the position of the cursor
print(f.read(6))     # written the words present in that position
print(f.readline())  # print line by line
print(f.close())

fname = input("enter a file name: ")
f = open(f'{fname}','w')
f.seek(0)
while True:
    billrow=input("Enter name,quantity,price: ")
    if billrow=="E":
        f.flush()
        f.close()
        break
    else:
        print(f.writelines(f'{billrow}\n'))


import random
toss=["Head","Tail"]
print(random.choice(toss))



By using this comment in terminal create a file with text in terminal

echo "pip install Flask" > File.txt    - create the file 
pip freeze >File.txt                   - In that file package is selected
pip install -r File.txt                - install that flask module
del filename.txt                       - del file


"""
        




