
@echo off
title Jyotirling Shivmath - YouTube Downloader
color 0A

set "DOWNLOAD=%USERPROFILE%\Desktop\YouTube Downloads"

if not exist "%DOWNLOAD%" mkdir "%DOWNLOAD%"

:START
cls
echo ==========================================
echo       YOUTUBE VIDEO DOWNLOADER
echo       JYOTIRLING SHIVMATH
echo ==========================================
echo.
echo Paste YouTube Video Link and press Enter:
echo.

set /p "URL=YouTube Link: "

if "%URL%"=="" goto START

echo.
echo Downloading your video...
echo.

py -m yt_dlp --no-warnings -f "bv*+ba/b" --merge-output-format mp4 -P "%DOWNLOAD%" "%URL%"

echo.
echo ==========================================
echo Download process completed.
echo Download Folder: %DOWNLOAD%
echo ==========================================
echo.
pause
goto START
