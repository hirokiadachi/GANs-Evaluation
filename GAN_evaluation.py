#!/usr/bin/env python3
#coding:utf-8

import os 
import sys
import glob
import copy
import PIL.Image, PIL.ImageTk
import pickle
import random
import numpy as np
from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        self.all_num = 100
        self.num = 0
        self.img1 = 0
        self.img2 = 0
        self.n1 = 0
        self.n2 = 0
        self.m1 = 0
        self.m2 = 0
        self.num_of_skip = 0
        self.args = sys.argv

        Frame.__init__(self, master)
        self.master.title('Subjective Evaluation')
        self.init()
        self.pack()

    def init(self):
        self.Attr_name = ['Female', 'Female+Eyeglasses',
                          'Female+Eyeglasses+Smiling', 'Female+Smiling',
                          'Male', 'Male+Eyeglasses',
                          'Male+Eyeglasses+Goatee', 'Male+Goatee',
                          'Male+Goatee+Smiling', 'Male+Smiling']
        print('======================================================')
        print('Please waiting.\nImage loading from pickle file now.\n')
        self.img_list = self.load_pickle()
        self.pattern = [0, 1]

        if self.args[1] == '0':
            self.gan_name = ['Conditional DCGAN', 'Weighted Conditional DCGAN']
        elif self.args[1] == '1':
            self.gan_name = ['Conditional PGGAN', 'Weighted Conditional PGGAN']
            
        self.val = IntVar()
        self.val.set(0)
        self.font = ("Helevetica", 13, "bold")

        ##  Make Entry box
        self.Box = Entry(width=12)
        self.Box.insert(END, '')
        #self.Box.grid(row=0, column=0)
        self.Box.place(x=10)

        ##  Make Insert Button
        id_button = Button(self, text='Insert')
        id_button.bind('<Button-1>', self.ID)
        id_button.grid(row=0, column=1)

        ##  Make Button with Image
        self.button1 = Label(self, bg='#1E90FF', width=5, height=5)
        #self.button1.bind('<Button-1>', self.image_loader)
        self.button1.grid(row=1, column=0)
        self.button2 = Label(self, bg='#1E90FF', width=5, height=5)
        #self.button2.bind('<Button-1>', self.image_loader)
        self.button2.grid(row=1, column=1)

        ## Skip Button
        self.skip = Button(self, text='Skip image')
        self.skip.bind('<Button-1>', self.both_image_fake)
        self.skip.grid(row=3, column=1)


        ##  Make Radio_Button
        self.radio1 = Radiobutton(self, variable=self.val, value=0, command=self.radio_button_img_loader)
        self.radio1.grid(row=2, column=0)
        self.radio2 = Radiobutton(self, variable=self.val, value=1, command=self.radio_button_img_loader)
        self.radio2.grid(row=2, column=1)

        label = Label(self, text='Which image is clear?')
        label.grid(row=4, column=0)

        ##  Make counter label
        self.label_num = Label(self)
        self.label_num.grid(row=4, column=1)


	## Attribute Name Label
        self.attr_label = Label(self)
        self.attr_label.grid(row=3, column=0)

        self.result = Label(self)
        self.result.grid(row=5, column=1)

    def load_pickle(self):
        if self.args[1] == '0':
            file_name = 'DCGAN_eval.pickle'
        elif self.args[1] == '1':
            file_name = 'PGGAN_eval.pickle'

        ## pickelファイルがpython2系で作成してあるので，
        ## 下のコードを使用する．

        ## python2系の時
        #with open(file_name, 'rb') as f:
        #    img_list = pickle.load(f)
        
        ## python3系の時
        with open(file_name, 'rb') as f:
            img_list = pickle.load(f, encoding='bytes')
        
        return img_list
    
    def random_number(self, num):
        return np.random.randint(num)

    def random_choice(self, data):
        return np.random.choice(data, 2, replace=False)

    def image_number_choice(self):
        all_pattern = self.choice_number_counter()

        if all_pattern.size == 2:
            all_pattern = self.pattern = all_pattern
            return all_pattern
        else:
            pattern = self.pattern = random.choice(all_pattern)
            return pattern

    def get_image(self):
        i, j = self.random_choice(self.pattern)

        num1 = self.num1 = i
        num2 = self.num2 = j
        attr = self.attr = self.random_number(10)
        im_num1 = self.im_num1 = self.random_number(250)
        im_num2 = self.im_num2 = self.random_number(250)

        ## loading first Image from pickle file
        img1 = self.img_list[num1][self.attr][im_num1]
        img1 = img1.astype(np.uint8)
        img1 = PIL.Image.fromarray(img1)

        ## loading second Image from pickle file
        img2 = self.img_list[num2][attr][im_num2]
        img2 = img2.astype(np.uint8)
        img2 = PIL.Image.fromarray(img2)

        self.attr_label.config(text=self.Attr_name[attr], font=self.font)
        return img1, img2, num1, num2

    def image_loader(self):
        ## This function is displaying two images
        img1, img2, _, _ = self.get_image()
        self.image1 = PIL.ImageTk.PhotoImage(img1)
        self.image2 = PIL.ImageTk.PhotoImage(img2)
        self.button1.config(image=self.image1, width=self.image1.width(),
                            height=self.image1.height())
        self.button2.config(image=self.image2, width=self.image2.width(),
                            height=self.image2.height())

        count_number = self.counter()
        self.label_num.config(text=count_number)

    def ID(self, event):
        insert_str = self.Box.get()
        save_dir = 'Text_files'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        self.image_loader() 
        if self.args[1] == '0':
            txtname = str(insert_str) + '_dcgan.txt'
        elif self.args[1] == '1':
            txtname = str(insert_str) + '_pggan.txt'
        print('your file name is {}.'.format(txtname))
        print('======================================================')
        txtname = save_dir+'/'+txtname
        if os.path.exists(txtname):
            os.remove(txtname)
        self.txtfile = open(txtname, 'a')

    def both_image_fake(self, event):
        self.num_of_skip += 1
        img1, img2, _, _ = self.get_image()
        self.image1 = PIL.ImageTk.PhotoImage(img1)
        self.image2 = PIL.ImageTk.PhotoImage(img2)
        self.button1.config(image=self.image1, width=self.image1.width(),
                            height=self.image2.height())
        self.button2.config(image=self.image2, width=self.image2.width(),
                            height=self.image2.height())
        

    def choose_image_counter(self, n1, n2):
        if self.val.get() == 0:
            if n1 == 0:
                self.img1 += 1
                m_name1 = self.gan_name[n1]
                self.txtfile.writelines('No.{}     Choice Method: {}     Attribute: {}\n'\
	                                .format(self.num, m_name1, self.Attr_name[self.attr]))
            elif n1 == 1:
                self.img2 += 1
                m_name2 = self.gan_name[n1]
                self.txtfile.writelines('No.{}     Choice Method: {}     Attribute: {}\n'\
	                                .format(self.num, m_name2, self.Attr_name[self.attr]))
        elif self.val.get() == 1:
            if n2 == 0:
                self.img1 += 1
                m_name3 = self.gan_name[n2]
                self.txtfile.writelines('No.{}     Choice Method: {}     Attribute: {}\n'\
	                                .format(self.num, m_name3, self.Attr_name[self.attr]))
            elif n2 == 1:
                self.img2 += 1
                m_name4 = self.gan_name[n2]
                self.txtfile.writelines('No.{}     Choice Method: {}     Attribute: {}\n'\
	                                .format(self.num, m_name4, self.Attr_name[self.attr]))
        if self.num == self.all_num:
            result = '{}: {}/100\n{}: {}/100\nNumber of Skip: {}\n'\
                      .format(self.gan_name[0], self.img1, self.gan_name[1], self.img2, self.num_of_skip)
            self.txtfile.writelines(result)

            self.master.withdraw()
            exit(-1)
            #self.skip.config(text='End')
            #self.skip.bind('<Button-1>', self.destroy_window)
            #self.skip.grid(row=3, column=1)
            self.result.config(text=result, font=self.font)

    def radio_button_img_loader(self):
        if self.img1 == 0 and self.img2 == 0:
            self.choose_image_counter(self.num1, self.num2)
        else:
            self.choose_image_counter(self.n1, self.n2)

        img1, img2, self.n1, self.n2 = self.get_image()
        self.image1 = PIL.ImageTk.PhotoImage(img1)
        self.image2 = PIL.ImageTk.PhotoImage(img2)
        self.button1.config(image=self.image1, width=self.image1.width(),
                            height=self.image1.height())
        self.button2.config(image=self.image2, width=self.image2.width(),
                            height=self.image2.height())
        #self.method_apper_counter()
        count_number = self.counter()
        self.label_num.config(text=count_number)
        
    def method_apper_counter(self):
        if self.pattern[0] == self.pattern1[0] and self.pattern[1] == self.pattern1[1]:
            self.method1 += 1
        elif self.pattern[0] == self.pattern2[0] and self.pattern[1] == self.pattern2[1]:
            self.method2 += 1
        elif self.pattern[0] == self.pattern3[0] and self.pattern[1] == self.pattern3[1]:
            self.method3 += 1
        
    def counter(self):

        if not self.num >= self.all_num:
            self.num += 1
        else:
            self.num = 0

        count_number = '{}/{}'.format(self.num, self.all_num)
        return count_number

if __name__ == '__main__':
    app = App()
    app.pack()
    app.mainloop()

