@echo off
if not defined TAG (
    set TAG=1
    start wt -p "cmd" %0
    exit
)
cd E:\Develop\CanvasFileDownloader&&python main.py