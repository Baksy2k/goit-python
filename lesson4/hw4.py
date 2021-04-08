from pathlib import Path
import sys

video = ('.avi', '.mp4', '.mov', '.mkv')
images = ('.jpeg', '.png', '.jpg', '.svg')
documents = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
music = ('.mp3', '.ogg', '.wav', '.amr')
archives = ('.zip', '.gz', '.tar', '.rar')
vid=[]
mus=[]
img=[]
doc=[]
arc=[]
other=[]
all_ext = video + images + documents + music + archives #Известные расширения


def searching_all_files(directory): 
    dirpath = Path(directory)
    assert(dirpath.is_dir())
    global file_list, found_extentions, unknown_ext
    found_extentions=[]
    file_list = []
    unknown_ext=[]
    for x in dirpath.iterdir():
        if x.is_file():
            file_list.append(x.name)

            if x.suffix in video:
                vid.append(x.name)
            elif x.suffix in images:
                img.append(x.name)
            elif x.suffix in documents:
                doc.append(x.name)
            elif x.suffix in music:
                mus.append(x.name)
            elif x.suffix in archives:
                arc.append(x.name)
            else:
                other.append(x.name)
                unknown_ext.append(x.suffix)
            
            found_extentions.append(x.suffix) #Перечисляем найденные расширения

        elif x.is_dir():
            file_list.extend(searching_all_files(x)) #Рекурсивная часть
    return file_list, found_extentions, unknown_ext


#searching_all_files('C:/Users/vlady/Desktop/Python/testfolder/')
searching_all_files(sys.argv[1])

print("Videos: ")
print(*vid, sep = ', ', end= '\n\n')
print(f"Images: ")
print(*img, sep = ', ', end= '\n\n')
print(f"Documents: ")
print(*vid, sep = ', ', end= '\n\n')
print(f"Music: ")
print(*vid, sep = ', ', end= '\n\n')
print(f"Archives: ")
print(*vid, sep = ', ', end= '\n\n')
print(f"Files with unknown extentions: ")
print(*other, sep = ', ', end= '\n\n')
print("-----------------------")
print("Following extentions found in the folder: ",*set(found_extentions), sep = ' ')
print("Unknown extentions found in the folder: ",*set(unknown_ext), sep = ' ')
#print("Known extentions: ",*all_ext, sep = ' ')
#r = [x for x in all_ext if x not in found_extentions]
#print("No files found with following extentions known to the script: ",*r, sep = ' ')