from ctypes import sizeof
from mimetypes import common_types
import wget
import os
from canvasapi import Canvas

global DIR_HOME
DIR_HOME = "./"
global CANVAS_API_URL
CANVAS_API_URL = "https://oc.sjtu.edu.cn"
global CANVAS_KEY
CANVAS_KEY = ""
global ignore_bit
ignore_bit = 0
global courses_number
courses_number = 0

# GXIZXDBoKMxf2RFVwcbfsq7IE0P0EyGJZadjfKTNmSiOCTJgfZ0XmBiVmKupvjH1

def login():
    if not os.path.exists("log"): 
        os.makedirs("log")
    user_info_w = open("log/user_info.log", "a")
    user_info_r = open("log/user_info.log", "r")
    user_info = user_info_r.readlines()
    global CANVAS_KEY
    if user_info == []: 
        CANVAS_KEY = input("\033[7;31mError: \033[0mPlease use your Canvas token to login: ")
        user_info_w.write(CANVAS_KEY)
    else:
        CANVAS_KEY = user_info[0]
    canvas = Canvas(CANVAS_API_URL, CANVAS_KEY)
    print("\033[7;32mMessage: \033[0m Welcome, ", canvas.get_current_user())
    return canvas

def my_courses(canvas): 
    courses = canvas.get_current_user().get_courses(enrollment_state='active')
    i = 0
    print("\033[7;34mYour active courses: \033[0m")
    for course in courses:
        print("\033[7;34m", i, "\033[0m", "\033[0;34m", course, "\033[0m")
        i += 1
    global courses_number
    courses_number = i + 1
    return courses

def download_from_folder(folder, target_path):
    folder_target_path = target_path + folder.name + "/"
    if not os.path.exists(folder_target_path): 
        os.makedirs(folder_target_path)
    files = folder.get_files()
    global ignore_bit
    for file in files: 
        if file.url: 
            out = folder_target_path + file.display_name
            out = str(out.encode('gbk', 'ignore').decode('gbk'))
            url = str(file.url.encode('gbk', 'ignore').decode('gbk'))
            if os.path.exists(out):
                if ignore_bit == -1:
                    print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                    wget.download(url, out)
                    continue
                if ignore_bit == 1: 
                    print("\n", "\033[7;32mMessage: \033[0m", "Ignore file ", "\033[7;36m", file.display_name, "\033[0m")
                    continue
                print("\033[7;31mWarning: \033[0mFile ", out, " exists, do you still want to download?(yes/no/always download/all ignore) => (y/n/a/i): ")
                command = input()
                if command == "a": 
                    ignore_bit = -1
                    print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                    wget.download(url, out)
                    continue
                if command == "i": 
                    ignore_bit = 1
                    continue
                if command == "y":
                    print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                    wget.download(url, out)
                    continue
                if command == "n": 
                    print("\n", "\033[7;32mMessage: \033[0m", "Ignore file ", "\033[7;36m", file.display_name, "\033[0m")
                    continue
            else: 
                print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                wget.download(url, out)

    son_folders = folder.get_folders()
    for son_folder in son_folders:
        if son_folder == son_folders[0]:
            continue
        download_from_folder(son_folder, folder_target_path)

def download_for_course(course): 
    target_path = DIR_HOME + "/" + str(course.course_code)+"/"
    if not os.path.exists(target_path): 
        os.makedirs(target_path)
    folders = course.get_folders()
    folder = folders[0]
    files = folder.get_files()
    global ignore_bit
    for file in files: 
        if file.url: 
            out = target_path + file.display_name
            out = str(out.encode('gbk', 'ignore').decode('gbk'))
            url = str(file.url.encode('gbk', 'ignore').decode('gbk'))
            if os.path.exists(out):
                if ignore_bit == -1:
                    print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                    wget.download(url, out)
                    continue
                if ignore_bit == 1: 
                    print("\n", "\033[7;32mMessage: \033[0m", "Ignore file ", "\033[7;36m", file.display_name, "\033[0m")
                    continue
                print("\033[7;31mWarning: \033[0mFile ", out, " exists, do you still want to download?(yes/no/always download/all ignore) => (y/n/a/i): ")
                command = input()
                if command == "a": 
                    ignore_bit = -1
                    print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                    wget.download(url, out)
                    continue
                if command == "i": 
                    ignore_bit = 1
                    continue
                if command == "y":
                    print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                    wget.download(url, out)
                    continue
                if command == "n": 
                    print("\n", "\033[7;32mMessage: \033[0m", "Ignore file ", "\033[7;36m", file.display_name, "\033[0m")
                    continue
            else: 
                print("\n", "\033[7;32mMessage: \033[0m", "Download file ", "\033[7;35m", url, "\033[0m", "to", "\033[7;36m", out, "\033[0m")
                wget.download(url, out)

    for folder in folders:
        if folder == folders[0]:
            continue
        download_from_folder(folder, target_path)

def downloader(courses): 
    if not os.path.exists("log"): 
        os.makedirs("log")
    home_info_w = open("log/home_info.log", "a")
    home_info_r = open("log/home_info.log", "r")
    home_info = home_info_r.readlines()
    global DIR_HOME
    if home_info == []:
        DIR_HOME = input("\033[7;31mError: \033[0mPlease set the target dir path: ")
        home_info_w.write(DIR_HOME)
    else: 
        DIR_HOME = home_info[0]

    id = input("\033[7;32mMessage: \033[0minput -1 to update for all courses, input positive index to update for one course: ")
    if id == "-1": 
        for course in courses: 
            download_for_course(course) 
        return
    if int(id) < -1:
        print("Exit")
        return
    global courses_number
    if int(id) > courses_number: 
        print("Exit")
        return
    course = courses[int(id)]
    global ignore_bit
    download_for_course(course)

def downloaderAutoAll(courses): 
    if not os.path.exists("log"): 
        os.makedirs("log")
    home_info_w = open("log/home_info.log", "a")
    home_info_r = open("log/home_info.log", "r")
    home_info = home_info_r.readlines()
    global DIR_HOME
    if home_info == []:
        DIR_HOME = input("\033[7;31mError: \033[0mPlease set the target dir path: ")
        home_info_w.write(DIR_HOME)
    else: 
        DIR_HOME = home_info[0]
    global ignore_bit
    ignore_bit = 1
    for course in courses: 
        download_for_course(course) 

def CanvasFileDownloader():
    print("\033[7;32mCanvasFileDownloader\033[0m")
    canvas = login()
    courses = my_courses(canvas)
    downloader(courses)
    
def CanvasFileDownloaderAutoAll():
    print("\033[7;32mCanvasFileDownloader\033[0m")
    canvas = login()
    courses = my_courses(canvas)
    downloaderAutoAll(courses)
