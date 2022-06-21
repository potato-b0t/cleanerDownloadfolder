from PIL import Image
import os

loginUser = os.getlogin()

##download path
download_path = f"C:/Users/{loginUser}/Downloads"

##image folder
image_folder = f"C:/Users/{loginUser}/Pictures/downloadImageOptimized"

##sounds folder
sounds = f"C:/Users/{loginUser}/Music/sounds"

##documents folder
documents_folder=f"C:/Users/{loginUser}/Documents/documents"

##video folder
video_folder = f"C:/Users/{loginUser}/Videos/downloadVideo"

##executor folder
exe_folder = f"C:/Users/{loginUser}/Documents/executions"

##compressor and optimizer of images on the computer in folder "downloadImageOptimized"
def pictureMove(filename):
    picture = Image.open(download_path + "/" + filename)

    if image_folder not in os.listdir():
        try:
            os.mkdir(image_folder)
        except:
            pass
    
    picture.save(image_folder + "/compressed_" + filename, optimize=True, quality = 60)
    os.remove(download_path + "/" + filename)

##saved sounds in folder "sounds" from download folder
def soundMove(filename):
    if sounds not in os.listdir():
        try:
            os.mkdir(sounds)
        except:
            pass

    os.rename(download_path + "/" + filename, sounds + "/" + filename)

##saved documents in folder "documents" from download folder
def documentsMove(filename):
    if documents_folder not in os.listdir():
        try:
            os.mkdir(documents_folder)
        except:
            pass

    os.rename(download_path + "/" + filename, documents_folder + "/" + filename)

##saved videos in folder "video" from download folder
def videoMove(filename):
    if video_folder not in os.listdir():
        try:
            os.mkdir(video_folder)
        except:
            pass

    os.rename(download_path + "/" + filename, video_folder + "/" + filename)
        
def executorsMove(filename):
    if exe_folder not in os.listdir():
        try:
            os.mkdir(exe_folder)
        except:
            pass

    os.rename(download_path + "/" + filename, exe_folder + "/" + filename)

if __name__ == "__main__":
    for filename in os.listdir(download_path):

        name, extencion = os.path.splitext(download_path + filename)

        if extencion in [".jpg", ".png", ".jpeg", ".gif", ".bmp"]:
            pictureMove(filename)

        if extencion in [".mp3", ".wav", ".flac", ".aac", ".ogg"]:
            soundMove(filename)

        if extencion in [".pdf", ".docx", ".doc", ".xls", ".xlsx", ".ppt", ".pptx"]:
            documentsMove(filename)

        if extencion in [".mp4", ".mkv", ".avi", ".mov"]:
            videoMove(filename)

        if extencion in [".exe", ".msi"]:
            executorsMove(filename)        

