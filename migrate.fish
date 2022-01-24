#!/bin/fish


python3 manage.py makemigrations && python3 manage.py migrate && set_color green && echo "Migrate Successed!" && set Successed "True" || if Successed = "Ture"
 set_color red && echo "Migrate Failed!"
 end
set_color normal
