# FILE HANDLING
#  w - open the file in write only mode , if the files not exist , creates the files in the directory
# r - open in read only mode mode , if not exist exception is Raised
# r+  - open file in read and write mode , if not exists exception is raised
#  w +  - open file in read and write mode , if not exists file is created
#  a - open file in append mode , so the content can be appended / written at end of file """

# FILE OPERATORS ARE IRREVERSIBLE

f = open('bill.txt', 'w')
print(f)
print(f.name)
print(f.mode)
print(f.writable())
print(f.write(" Hi Hello "))
print(f.write(" Hi Hello what happening "))
print(f.write(" hey buddy "))
print(f.flush())
print(f.close())



