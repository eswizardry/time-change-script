# -*- coding: utf-8 -*-
# @Author: mcsbanch
# @Date:   2016-09-06 18:28:04
# @Last Modified by:   mcsbanch
# @Last Modified time: 2016-09-06 18:33:37
import win32api
import time
import datetime

# get current EPOCH time
# +900 seconds (15minutes)
t = time.time()
t += 900

# Convert EPOCH to datetime format
settime = datetime.datetime.fromtimestamp(t)

# Setting systemtime the -7 to correct timezone GMT+7
win32api.SetSystemTime(settime.year, settime.month, settime.weekday(), settime.day, settime.hour - 7, settime.minute, settime.second, 0)
