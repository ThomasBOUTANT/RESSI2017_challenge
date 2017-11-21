#!/usr/bin/python2.7
# -*- coding: ASCII -*-

import os,sys
os.environ[ 'HOME' ] = '/tmp/'
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cgi
import msvcrt
import cgitb
cgitb.enable()
import cStringIO

d=datetime.datetime.today()

x=[]
y=[]

format= "png"
sio = cStringIO.StringIO()



for j in range(10):
    try : 
        log = open("log"+str(j+1)+".txt", "r")
        temps=["00:00:00"]
        valeurs=[]
        x=[]
        y=[]
        tmp=log.read().split("[info] ")
        for i in tmp:
            if (i.split(" ")[0]=="echo:"):
                if (i.split(" ")[1]=="time"): temps.append(i.split(" ")[2].split("\n")[0])
                else: valeurs.append(int(i.split(" ")[1].split(",")[0]))
        log.close()
        yi=0
        for i in range(len(valeurs)):
            xi=datetime.datetime.strptime(temps[i],"%H:%M:%S")
            yi+=float(valeurs[i]);
            print yi
            x.append(xi)
            y.append(yi)
                
        color=""
        label=""
        if (j==0):
            courbe1,=plt.plot(x,y,"b",label="Team 1")
        if (j==1): 
            courbe2,=plt.plot(x,y,"o",label="Team 2")
        if (j==2): 
            courbe3,=plt.plot(x,y,"y",label="Team 3")
        if (j==3): 
            courbe4,=plt.plot(x,y,"p",label="Team 4")
        if (j==4): 
            courbe5,=plt.plot(x,y,"g",label="Team 5")
        if (j==5): 
            courbe6,=plt.plot(x,y,"_g",label="Team 6")
        if (j==6): 
            courbe7,=plt.plot(x,y,"r",label="Team 7")
        if (j==7): 
            courbe8,=plt.plot(x,y,"_r",label="Team 8")
        if (j==8): 
            courbe9,=plt.plot(x,y,"k",label="Team 9")
        if (j==9): 
            courbe10,=plt.plot(x,y,"_k",label="Team 10")
        plt.legend(handles=[courbe1,courbe2,courbe3,courbe4,courbe5,courbe6,courbe7,courbe8,courbe9,courbe10])
    
    except : print("no log found")
    
    

plt.savefig(sio, format=format)

print "Content-Type: image/%s\n" % format
msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
sys.stdout.write(sio.getvalue())


