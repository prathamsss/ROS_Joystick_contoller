#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame as pyg
import sys
import os
import serial
import time

class JoyStick():
    def __init__(self,JN=0):
        pyg.init()
        pyg.joystick.init()
        self.JNmax=pyg.joystick.get_count()
        self.J=pyg.joystick.Joystick(JN)
        self.J.init()
        self.NAX=self.J.get_numaxes()
        self.NBT=self.J.get_numbuttons()
        self.NAM=self.J.get_name()
        self.NBALL=self.J.get_numballs()
        self.NHAT=self.J.get_numhats()
        self.JN=self.J.get_id()
        #print("ID = " , self.NAM)
        #self.JNmax=JNmax

    def read_axis(self):
        self.Jax=[]
        pyg.event.pump()
        for i in range(self.NAX):
            self.Jax.append(self.J.get_axis( i ))
        return  self.Jax

    def read_button(self):
        self.Jbt=[]
        pyg.event.pump()
        for i in range(self.NBT):
            self.Jbt.append(self.J.get_button( i ))
        return self.Jbt
    
    def read_hat(self):
        self.Jhat=[]
        pyg.event.pump()
        for i in range(self.NHAT):
            self.Jhat.append(self.J.get_hat(i))
        return self.Jhat

    def All_Joy_init(self):
        self.J=[]
        for i in range(self.JNmax):
            self.J.append(JY(JN=i))
        return self.J



class SlaveContact():
    def __init__(self, port, baud_rate):
         try:
            self.port = port
            self.baud_rate= baud_rate
            self.slave = serial.Serial(port, 9600, timeout=1,rtscts=True,dsrdtr=True)
            self.slave.flush()
         except SerialException:
               print("Cannot connect given port!")
         except ValueError:
                print("Parameters Baud Rate outoff range! (Check Baud rate)")
    
    def sendData(self,data):
        self.slave.write(data.encode())
         
    def readData(self):
        self.line = self.slave.readline()
        return self.line
        
       

