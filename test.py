#coding :utf-8 import os,sys from time import sleep from kivymd.app import MDApp from kivy.lang import Builderclear from kivy.core.window import Window from kivy.uix.screenmanager import Screen,ScreenManager from kivymd.uix.textfield import MDTextFieldRound from kivy.config import Config import sqlite3 from kivymd.uix.dialog import MDDialog  Window.size=(330,600) screen_helper=''' Screen:     NavigationLayout:         ScreenManager:             id:s_manager             Screen:                 name:"home"                 MDBoxLayout:                     orientation: 'vertical'                     MDToolbar:                         title: 'Kickthem'                         left_action_items: [['wifi',lambda x: nav_drawer.toggle_nav_drawer()]]                         right_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]                         elevation: 10                     MDBoxLayout:                         orientation:'vertical'                                  MDNavigationDrawer:             id: nav_drawer ''' Config.set('graphics','width','330') Config.set('graphics','height','600')  class demo(MDApp):     def build(self):         self.theme_cls.primary_palette="Red"         screen=Builder.load_string(screen_helper)         return screen  demo().run()  # for i in range(0,100): #     print("Loading. {}%".format(i)) #     sleep(0.5) #     os.system("clear") #     print("Loading.. {}%".format(i)) #     sleep(0.5) #     os.system("clear") #     print("Loading... {}%".format(i)) #     sleep(0.5) #     os.system("clear") #     sleep(0.5)  