#!/usr/bin/env python3.7.4

from shutil import copyfile
whichClass = input("intro, advanced, or ei? ")
whichFile = input("filename? ")
if(whichClass == "intro"):
	students = open("students9-10.txt", "r")
elif(whichClass == "advanced"):
	students = open("students11-12.txt", "r")
elif(whichClass == "ei"):
	students = open("studentsEI.txt", "r")
for line in students:
	student = line.strip()
	src = whichFile + ".docx"
	filename = whichFile + "-"
	dst = f"./{filename}{student}.docx"
	copyfile(src, dst)
students.close()

