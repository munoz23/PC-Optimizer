import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from tkinter.filedialog import askdirectory
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from datetime import datetime
import threading
from random import choices
from tkinter.constants import END
from typing import Literal
from xmlrpc.client import Boolean

from tkinter.scrolledtext import ScrolledText
from pathlib import Path
import time
import asyncio
import pyuac,os,sys
from library.systemUpdate import Updates
from library.excecute import Option,Commands
from library.windowsLocalMachine import Registry
from library.powerShell import PowerShell

PATH = Path(__file__).parent / 'assets'


class Cleaner(ttk.Frame,threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.actived = False
        self.mensaje = Messagebox.ok
        threading.Thread(target=self.espera,args=(ttk.Frame,)).start()
        

        self.pack(fill=BOTH,expand=YES)


        # application images
        self.images = [
            ttk.PhotoImage(
                name='logo',
                file=PATH / 'img1.png'),
            ttk.PhotoImage(
                name='cleaner',
                file=PATH / 'img1.png'),
            ttk.PhotoImage(
                name='registry',
                file=PATH / 'img2.png'),
            ttk.PhotoImage(
                name='tools',
                file=PATH / 'img3.png'),
            ttk.PhotoImage(
                name='options',
                file=PATH / 'img4.png'),
            ttk.PhotoImage(
                name='privacy',
                file=PATH / 'img1.png'),
            ttk.PhotoImage(
                name='junk',
                file=PATH / 'img1.png'),
            ttk.PhotoImage(
                name='protect',
                file=PATH / 'img1.png')
        ]

        # header
        hdr_frame = ttk.Frame(self, padding=20, bootstyle=SECONDARY)
        hdr_frame.pack(fill=X)

        hdr_label = ttk.Label(
            master=hdr_frame,
            image='logo',
            bootstyle=(INVERSE, SECONDARY)
        )
        hdr_label.pack(side=LEFT)

        logo_text = ttk.Label(
            master=hdr_frame,
            text='NetColombiaClear',
            font=('TkDefaultFixed', 30),
            bootstyle=(INVERSE, SECONDARY)
        )
        logo_text.pack(padx=15,side=LEFT)

        # action buttons
        action_frame = ttk.Frame(self)
        action_frame.pack(side=LEFT,fill=BOTH)


      
        cleaner_btn = ttk.Button(
            master=action_frame,
            image='cleaner',
            width=5,
            compound=TOP,
            command=lambda: threading.Thread(target=self.clean_windows,args=('c',)).start().join(),
            bootstyle=INFO
        )
        cleaner_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        registry_btn = ttk.Button(
            master=action_frame,
            image='registry',
            compound=TOP,
            bootstyle=INFO
        )
        registry_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        tools_btn = ttk.Button(
            master=action_frame,
            image='tools',
            compound=TOP,
            bootstyle=INFO
        )
        tools_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        options_btn = ttk.Button(
            master=action_frame,
            image='options',
            compound=TOP,
            bootstyle=INFO
        )
        options_btn.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        # option notebook
        notebook = ttk.Notebook(self)
        notebook.pack(fill=BOTH)

        # windows tab
        windows_tab = ttk.Frame(notebook, padding=10)
        wt_scrollbar = ttk.Scrollbar(windows_tab)
        wt_scrollbar.pack(side=RIGHT, fill=Y)
        wt_scrollbar.set(0, 1)

        wt_canvas = ttk.Canvas(
            master=windows_tab,
            relief=FLAT,
            borderwidth=0,
            selectborderwidth=0,
            highlightthickness=0,
            yscrollcommand=wt_scrollbar.set
        )
        wt_canvas.pack(side=LEFT, fill=BOTH)

        # adjust the scrollregion when the size of the canvas changes
        wt_canvas.bind(
            sequence='<Configure>',
            func=lambda e: wt_canvas.configure(
                scrollregion=wt_canvas.bbox(ALL))
        )
        wt_scrollbar.configure(command=wt_canvas.yview)
        scroll_frame = ttk.Frame(wt_canvas)
        wt_canvas.create_window((0, 0), window=scroll_frame, anchor=NW)

       

        self.edge = ttk.Labelframe(
            master=scroll_frame,
            text='Registro de Acciones',
            padding=(20, 0)
        )
        self.edge.pack(fill=X, expand=YES, padx=0, pady=10)

      

        # add radio buttons to each label frame section
        for section in [self.edge]:
            self.cb = ttk.ScrolledText(section)
            self.cb.pack(side=TOP, pady=0, fill=X,expand=YES)
        notebook.add(windows_tab, text='Log')

        # empty tab for looks
        notebook.add(ttk.Frame(notebook), text='applications')

        # results frame
        results_frame = ttk.Frame(self)
        results_frame.pack()

        # progressbar with text indicator
        

        # result cards
        cards_frame = ttk.Frame(
            master=results_frame,
            name='cards-frame',
            bootstyle=SECONDARY
        )

        # privacy card
        priv_card = ttk.Frame(
            master=cards_frame, 
            padding=1, 
        )
        priv_card.pack(side=LEFT, fill=BOTH, padx=(10, 5), pady=10)

        priv_container = ttk.Frame(
            master=priv_card, 
            padding=40,
        )
        priv_container.pack(fill=BOTH, expand=YES)

        priv_lbl = ttk.Label(
            master=priv_container,
            image='privacy',
            text='PRIVACY',
            compound=TOP,
            anchor=CENTER
        )
        priv_lbl.pack(fill=BOTH, padx=20, pady=(40, 0))

        ttk.Label(
            master=priv_container,
            textvariable='priv_lbl',
            bootstyle=PRIMARY
        ).pack(pady=(0, 20))
        self.setvar('priv_lbl', '6025 tracking file(s) removed')

        # junk card
        junk_card = ttk.Frame(
            master=cards_frame,
            padding=1,
        )
        junk_card.pack(side=LEFT, fill=BOTH, padx=(5, 10), pady=10)

        junk_container = ttk.Frame(junk_card, padding=40)
        junk_container.pack(fill=BOTH, expand=YES)

        junk_lbl = ttk.Label(
            master=junk_container, 
            image='junk',
            text='PRIVACY', 
            compound=TOP, 
            anchor=CENTER,
        )
        junk_lbl.pack(fill=BOTH, padx=20, pady=(40, 0))

        ttk.Label(
            master=junk_container, 
            textvariable='junk_lbl',
            bootstyle=PRIMARY, 
            justify=CENTER
        ).pack(pady=(0, 20))
        self.setvar('junk_lbl', '1,150 MB of unneccesary file(s)\nremoved')

        # user notification
        note_frame = ttk.Frame(
            master=results_frame, 
            bootstyle=SECONDARY, 
            padding=40
        )
        note_frame.pack(fill=BOTH)

        note_msg = ttk.Label(
            master=note_frame, 
            text='We recommend that you better protect your data', 
            anchor=CENTER,
            font=('Helvetica', 12, 'italic'),
            bootstyle=(INVERSE, SECONDARY)
        )
        if Updates.update_version():
            response=Messagebox.show_question(message='Hay una nueva actualizacion, ¿desea descargarla?' )
            print(response)
    def clean_windows(self,prueba) -> None:
            

        if self.actived != True:
            self.actived = True
           # Messagebox.ok('Se comenzara con la optimización del windows')
            print('Limpiando Registros')
            self.cb.insert(END,'**Limpiando Registros**\n')
            print('Registros Limpiados Correctamente')
            commands = Commands.listCommands()
            Registry.write_keys(commands[6]['windows registry optimization'])

            try:
                self.real_time_powershell(commands,'Windows Optimizer',2)
            finally:
                print('termiando')
            
          
            self.cb.insert(END,'**Registros Limpiados Correctamente**\n')


            print('Optimizando Windows')
            self.cb.insert(END,'**Optimizando Windows**\n')
            
          
            option =Messagebox.show_question(message='¿desea realizar la defragmentacion del disco?')
            print(option.lower())
            if option.lower() =='no' or option.lower() == 'not':
                pass
            else:
                self.cb.insert(END,"***Realizando defragmentacion del disco***"+'\n')
                h1 =threading.Thread(target=self.real_time_powershell,args=(commands,'windows Defrag',7))
                h1.start()
              #  with PowerShell.execute_commands_real_time('defrag C: /U /V ') as df:
               #     self.cb.insert(END,'**DEFRAGMENTANDO DISCO C***\n')
                #    while df.poll() is None:
                 #       line = df.stdout.readline().encode('utf8')
                  #      self.cb.insert(END,line.decode('utf8'))
                   # 
            self.actived = False
            Messagebox.ok(message='Se realizo la limpieza correctamente')                   
                  
                     

        else:
            Messagebox.show_error('Ya hay una funcion activa espara que termine')    
   

            
            
        
        
    def real_time_powershell(self,commands,name,index)->None:
        for command in commands[index][name]:
                with PowerShell.execute_commands_real_time(command=command) as pw:
                    while pw.poll() is None:
                        try:
                            line = pw.stdout.readline().encode('utf8')
                            print(line.decode('utf8'))
                            if name == 'windows Defrag':
                                self.cb.insert(END,line.decode('utf8'))
                            else:
                                self.cb.insert(END,"comando realizado:"+command+'\n')
                               
                        except Exception as e:
                            print('error al ejecutar el comando: '+command)
    def main(self,option) -> None :
        pass
       
        
        





        
              


if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        app = ttk.Window("PC Cleaner",
                         "pulse",
                         size=(862,619),
                        )
        Cleaner(app)
        app.mainloop()