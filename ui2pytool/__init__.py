#!/usr/bin/python3
#-*- coding:utf-8 -*-
import os

UI_DIR = "./resources/uifiles"
UICODE_DIR = "./uicode"
UIC5 = "C:/Python35/Lib/site-packages/PyQt5/pyuic5"

UI_EXTs = (".ui", ".UI")


def GetAllUIFiles():
	lFiles = []
	ls = os.listdir(UI_DIR)
	for pa in ls:
		paname = os.path.join(UI_DIR, pa)
		_, ext = os.path.splitext(paname)
		if ext in UI_EXTs:
			lFiles.append(paname)
	return lFiles


def UI2Py(filename):
	basename = os.path.basename(filename)
	front, ext = os.path.splitext(basename)
	if ext not in UI_EXTs:
		print("UI2Py %s error! the file not is ui" % filename)
		return

	basename = front + ".py"
	pyname = os.path.join(UICODE_DIR, basename)
	sCmd = "%s %s -o %s" % (UIC5, filename, pyname)
	os.system(sCmd)
	print("%s to %s success!" %(filename, pyname))


def Run():
	lUIFiles = GetAllUIFiles() 
	for filename in lUIFiles:
		UI2Py(filename)