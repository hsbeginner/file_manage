# import os , glob
# os.chdir('C:\\Users\\lenovo\\Downloads\\test')

# for file in glob.glob("*.docx"):
#     print(file)


import os
import shutil

#to specifie the dir file where i want to peform  task
for file in os.listdir("C:\\Users\\lenovo\\Downloads"):
    file, f_extension = os.path.splitext(file) #extract file and it's extension
    # to get all .JPG file and move into respective folder"
    if f_extension == ('.JPG' or '.JPEG'):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\JPEG")
    elif f_extension == ('.png'):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\PNG")
    elif f_extension == (".pdf"):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\PDF")
    elif f_extension == (".txt"):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\TXT")
    elif f_extension == (".zip"):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\ZIP")
    elif f_extension == (".html"):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\HTML")
    elif f_extension == (".jpg" or ".jpeg" or " .jpeg"):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\JPEG")
    elif f_extension == (".docx"):
        current_file = (os.path.join("C:\\Users\\lenovo\\Downloads",file+f_extension))
        shutil.move(current_file , "C:\\Users\\lenovo\\Downloads\\DOCX")


    print(f_extension)
