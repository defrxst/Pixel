import tkinter as tk
import customtkinter 
import time
import os
import random


def save():       
        IPAddress = IPEntry.get()
        Address = AddressEntry.get()
        SocialSec = SSNEntry.get()
        School = SchoolEntry.get()
        Name = NameEntry.get()
        Phone = PhoneEntry.get()
        TikTok = TikTokEntry.get()
        Youtube = YouTubeEntry.get()
        Discord = DiscordEntry.get()
        Snap = SnapchatEntry.get()
        Insta = InstagramEntry.get()
        Facebook = FacebookEntry.get()


        with open('dox.txt', 'w', encoding="utf-8") as f:
            #BASIC INFO
            f.write('                ▄▄▄▄    ▄▄▄        ██████  ██▓ ▄████▄      ██▓ ███▄    █   █████▒▒█████  \n')
            f.write('               ▓█████▄ ▒████▄    ▒██    ▒ ▓██▒▒██▀ ▀█     ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒\n')
            f.write('               ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒██▒▒▓█    ▄    ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒\n')
            f.write('               ▒██░█▀  ░██▄▄▄▄██   ▒   ██▒░██░▒▓▓▄ ▄██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░\n')
            f.write('               ░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░██░▒ ▓███▀ ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░\n')
            f.write('               ░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓  ░ ░▒ ▒  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ \n')
            f.write('               ▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░  ░  ▒       ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ \n')
            f.write('                ░    ░   ░   ▒   ░  ░  ░   ▒ ░░            ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  \n')
            f.write('               ░            ░  ░      ░   ░  ░ ░          ░           ░            ░ ░   \n')

            if IPAddress == '':
                 pass
            else:
                f.write(f'                  •._.••´¯``•.,,.•` IP Address: {IPAddress} `•.,,.•´´¯`••._.•                             \n')
            if Address == '':
                 pass
            else:
                f.write(f'                •._.••´¯``•.,,.•` Street Address: {Address} `•.,,.•´´¯`••._.•                      \n')
            if SocialSec == '':
                pass
            else:
                f.write(f'                      •._.••´¯``•.,,.•` SSN: {SocialSec} `•.,,.•´´¯`••._.•                     \n')
            if Phone == '':
                 pass
            else:
                f.write(f'                 •._.••´¯``•.,,.•` Phone number: {Phone} `•.,,.•´´¯`••._.•                     \n')
            if Name == '':
                 pass
            else:
                f.write(f'                   •._.••´¯``•.,,.•` Full Name: {Name} `•.,,.•´´¯`••._.•                     \n')
            # SOCIALS

            if TikTok == '' and Youtube == '' and Snap == '' and Discord == '' and Insta == '' and Facebook == '':
                 pass
            else:
                 f.write('                ██████  ▒█████   ▄████▄   ██▓ ▄▄▄       ██▓      ██████ \n')
                 f.write('              ▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▒████▄    ▓██▒    ▒██    ▒ \n')
                 f.write('              ░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒██▒▒██  ▀█▄  ▒██░    ░ ▓██▄   \n')
                 f.write('                ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒░██░░██▄▄▄▄██ ▒██░      ▒   ██▒\n')
                 f.write('              ▒██████▒▒░ ████▓▒░▒ ▓███▀ ░░██░ ▓█   ▓██▒░██████▒▒██████▒▒\n')
                 f.write('              ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓   ▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▓▒ ▒ ░\n')
                 f.write('              ░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒    ▒ ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░▒  ░ ░\n')
                 f.write('              ░  ░  ░  ░ ░ ░ ▒  ░         ▒ ░  ░   ▒     ░ ░   ░  ░  ░  \n')
                 f.write('                    ░      ░ ░  ░ ░       ░        ░  ░    ░  ░      ░  \n')
                 if TikTok == '':
                      pass
                 else:
                      f.write(f'                   •._.••´¯``•.,,.•` TikTok: {TikTok} `•.,,.•´´¯`••._.•                    \n')
                 if Youtube == '':
                      pass
                 else:
                      f.write(f'                   •._.••´¯``•.,,.•` YouTube: {Youtube} `•.,,.•´´¯`••._.•                    \n')
                 if Snap == '':
                      pass
                 else:
                      f.write(f'                   •._.••´¯``•.,,.•` Snapchat: {Snap} `•.,,.•´´¯`••._.•                    \n')
                 if Discord == '':
                      pass
                 else:
                      f.write(f'                   •._.••´¯``•.,,.•` Discord: {Discord} `•.,,.•´´¯`••._.•                    \n')
                 if Insta == '':
                      pass
                 else:
                      f.write(f'                   •._.••´¯``•.,,.•` Instagram: {Insta} `•.,,.•´´¯`••._.•                    \n')
                 if Facebook == '':
                      pass
                 else:
                      f.write(f'                   •._.••´¯``•.,,.•` Facebook: {Facebook} `•.,,.•´´¯`••._.•                    \n')

            f.close()
            print("Success!")


#GUI

mainWindow = customtkinter.CTk()


mainWindow.geometry('500x250')
mainWindow.title('Pixel by defrxst on GitHub')

#Entries
IPEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='IP Address', width=130, height=25)
IPEntry.grid(row=0, column=0, padx=10, pady=10)

AddressEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Street Address', width=130, height=25)
AddressEntry.grid(row=1, column=0, padx=10, pady=10)

SSNEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='SSN', width=130, height=25)
SSNEntry.grid(row=2, column=0, padx=10, pady=10)

NameEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Full Name', width=130, height=25)
NameEntry.grid(row=1, column=1, padx=10, pady=10)

PhoneEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Phone Number', width=130, height=25)
PhoneEntry.grid(row=2, column=1, padx=10, pady=10)

SchoolEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='School', width=130, height=25)
SchoolEntry.grid(row=2, column=2, padx=10, pady=10)

#Buttons

saveButton = customtkinter.CTkButton(master=mainWindow, text='Save', command=save)
saveButton.grid(row=5, column=0, padx=10, pady=10)

#Socials

InstagramEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Instagram', width=130, height=25)
FacebookEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Facebook', width=130, height=25)
SnapchatEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Snapchat', width=130, height=25)
TikTokEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='TikTok', width=130, height=25)
DiscordEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='Discord', width=130, height=25)
YouTubeEntry = customtkinter.CTkEntry(master=mainWindow, placeholder_text='YouTube', width=130, height=25)

InstagramEntry.grid(row=0, column=1, padx=10, pady=10)
FacebookEntry.grid(row=0, column=2, padx=10, pady=10)
SnapchatEntry.grid(row=1, column=2, padx=10, pady=10)
TikTokEntry.grid(row=3, column=2, padx=10, pady=10)
DiscordEntry.grid(row=3, column=0, padx=10, pady=10)
YouTubeEntry.grid(row=3, column=1, padx=10, pady=10)

mainWindow.mainloop()

