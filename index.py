from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "black")

	def function1(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	def function2(): 
		os.system("python android_cam.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	def on_closing():
		# exit()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", on_closing)
		
	root.title("DROWSINESS DETECTION")
	Label(root, text="DROWSINESS DETECTION",font=("arial",20),fg="white",bg="black",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=20,pady=10)
	Button(root,text="Run",font=("arial",20),bg="#5abb0b",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=15,pady=15)
	Button(root,text="Exit",font=("arial",20),bg="red",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=15,pady=15)

	root.mainloop()