@echo off
hugo
py -3 deploy.py
cd ..\mindviewllc.github.io
@echo on
git commit -a -m "update"
git push
cd ..\mindviewllc-hugo
