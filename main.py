import CanvasFileDownloader
import os

def help():
    print("\033[7;32mHelp\033[0m")
    print("Command \033[7;34m m \033[0m for \033[7;35m manually download \033[0m")
    print("Command \033[7;34m a \033[0m for \033[7;35m auto update \033[0m")
    print("Command \033[7;34m s \033[0m for \033[7;35m change settings \033[0m")
    print("Command \033[7;34m r \033[0m for \033[7;35m remove settings \033[0m")
    print("Command \033[7;34m e \033[0m for \033[7;35m exit \033[0m")

def setting_change():
    while(1): 
        command = input("\033[7;32mMessage: \033[0mWhich operation do you want do? (\033[7;34m hc \033[0m -> \033[7;35m change target path \033[0m, \033[7;34m uc \033[0m -> \033[7;35m change Canvas token \033[0m, \033[7;34m hr \033[0m -> \033[7;35m read target path \033[0m, \033[7;34m ur \033[0m -> \033[7;35m read Canvas token \033[0m, \033[7;34m anything else \033[0m -> \033[7;35m exit \033[0m): ")
        if command == "hc":
            home_info_w = open("log/home_info.log", "w")
            newcont = input("\033[7;32mMessage: \033[0mNew target path: ")
            home_info_w.write(newcont)
            home_info_w.close()
            continue
        if command == "uc":
            user_info_w = open("log/user_info.log", "w")
            newcont = input("\033[7;32mMessage: \033[0mNew Canvas token: ")
            user_info_w.write(newcont)
            user_info_w.close()
            continue
        if command == "hr":
            home_info_r = open("log/home_info.log", "r")
            nowcont = home_info_r.readline()
            print(nowcont)
            home_info_r.close()
            continue
        if command == "ur":
            user_info_r = open("log/user_info.log", "r")
            nowcont = user_info_r.readline()
            print(nowcont)
            user_info_r.close()
            continue
        return

def setting_remove():
    while(1): 
        command = input("\033[7;32mMessage: \033[0mWhich operation do you want do? (\033[7;34m hr \033[0m -> \033[7;35m remove target path \033[0m, \033[7;34m ur \033[0m -> \033[7;35m remove Canvas token \033[0m, \033[7;34m anything else \033[0m -> \033[7;35m exit \033[0m)")
        if command == "hr":
            os.remove("log/home_info.log")
        if command == "ur":
            os.remove("log/user_info.log")
        return

if __name__ == "__main__":
    while(1):
        command = input("\033[7;32mMessage: \033[0mPlease input your command(input h for help): ")
        if command == "h":
            help()
        if command == "a":
            CanvasFileDownloader.CanvasFileDownloaderAutoAll()
        if command == "m":
            CanvasFileDownloader.CanvasFileDownloader()
        if command == "s": 
            setting_change()
        if command == "r": 
            setting_remove()
        if command == "e":
            exit()