#read and modify a file
with open("input.txt","r") as f:
    text = f.read()
    modified_text = text.title().replace("Hello","Brethren")

with open("new.txt","w") as f1:
    f1.write(modified_text)

#ask for filename
filename = input("Enter a file name to read:")

#try to read
try:
    with open(filename,"r") as f2:
        print(f2.read())

#catch the error
except Exception as e:
    print("Sorry we ran into something:",e)