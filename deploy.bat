@echo off
hugo
py -3 deploy.py
cd ..\SoftwareArchitectureForum.github.io
@echo on
git commit -a -m "update"
git push
cd ..\SoftwareArchitectureForum-hugo
