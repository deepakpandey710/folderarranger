import os, shutil

# audio_extension = ('.mp3', '.wav', '.m4a', '.flac')
#document_extension = ('.pdf','.doc','docx','.ppt', '.txt')
#video_extension = ('.mp4','.mkv','.mpeg','MKV')
   ####doing this by dictionary so we can call every file extension at once
dict_extensions = {
    'audio_extension' : ('.mp3', '.wav', '.m4a', '.flac'),
    'image_extension' : ('.jpg', '.jpeg', '.png'),
    'document_extension' : ('.pdf','.doc','docx','.ppt', '.txt'),
    'video_extension ': ('.mp4','.mkv','.mpeg','MKV'),
}

folderpath = input('folder path : ')
def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
#print(file_finder(folderpath,image_extension))
for extension_type, extension_tuple in dict_extensions.items():
    #print('calling function')
    #print(file_finder(folderpath,extension_tuple))
    if len(file_finder(folderpath,extension_tuple)) > 0 : 
        folder_name = extension_type.split('_')[0] + 'files'
        folder_path = os.path.join(folderpath,folder_name)
        if os.path.exists(folder_path):
            print(f'{folder_name} already exist')
        else:
            os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tuple):
        
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)



    ####this is another way to create same project####
# os.mkdir('Documents')
# os.mkdir('image_files')
# os.mkdir('jupyter_files')
# folderpath = input('folder path : ')
# for item in os.listdir(folderpath):   # we can also write os.getcwd() in place of folder path
#     if item.endswith('.txt') or item.endswith('.pdf') or item.endswith('.docx'):
#         shutil.move(item,'Documents')
#     elif item.endswith('.jpg') or item.endswith('.png'):
#         shutil.move(item,'image_files')
#     elif item.endswith('.ipynb'):
#         shutil.move(item,'jupyter_files')
#     else:
#         pass