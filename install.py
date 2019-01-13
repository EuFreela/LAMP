#!/bin/bash
## Text menu in Python

import os
import time
import sys

class Colour:
	PURPLE = '\033[95m'
   	CYAN = '\033[96m'
   	DARKCYAN = '\033[36m'
   	BLUE = '\033[94m'
   	GREEN = '\033[92m'
   	YELLOW = '\033[93m'
   	RED = '\033[91m'
   	BOLD = '\033[1m'
   	UNDERLINE = '\033[4m'
   	END = '\033[0m'
   	DEFAULT = BLUE

class Legend:
	title = "AMBIENTE DE DESENVOLVIMENTO WEB-LEGEND v1.0"
  
Menu = ["UPDATE","UPGRADE","APACHE","MYSQL","PHP","PHPMYADMIN","NODEJS","WORKBANCH","VSCODE","COMPOSER","HEROKU","JRE","INSTALL FULL","TEST SERVICES","SAIR(99)"]
Select = []


def shape_menu():
    os.system('clear')
    print 66 * (Colour.DEFAULT +"="+Colour.END)
    print (Colour.DEFAULT+Legend.title.center(60)+Colour.END)
    print 66 * (Colour.DEFAULT +"="+Colour.END)  

def print_menu():
    shape_menu()
    print "\n"
    strr = ""
    dot = 50
    for i in range(0,len(Menu)):
        if((i+1)>9):
            dot = 50-1
        strr = strr + "["+str(i+1)+"]" + (dot*".") + Menu[i]
        for x in Select:
            if x == (i+1):                
                strr = strr + (Colour.GREEN+" [OK]"+Colour.END)
        strr = strr + "\n"
    
    print strr
    print 67 * "-"
 
loop=True       
 
while loop:          
    print_menu()    
    choice = input("Escolha [1-14]: ")
 
    if choice==1:   
        Select.append(1)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"UPDATE.."+Colour.END)
        os.system('apt update')
        print "\n[ Aguarde ].."
        time.sleep(1)

    elif choice==2:        
        Select.append(2)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"UPGRADE.."+Colour.END)
        os.system('apt upgrade')
        print "\n[ Aguarde ].."
        time.sleep(1)

    elif choice==3:
        Select.append(3)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"LaMP :: APACHE.."+Colour.END)
        os.system('apt install apache2 -y')
        print "\n[ Aguarde ].."
        time.sleep(1)

    elif choice==4:
        Select.append(4)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"LAmP :: MYSQL.."+Colour.END)
        os.system('apt install mysql-server -y')
        os.system('mysql_secure_installation')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==5:
        Select.append(5)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"LAMp :: PHP.."+Colour.END)
        os.system('apt install php libapache2-mod-php php-mysql -y && apt install php-cli -y')
        print "\n[ Aguarde ].."
        time.sleep(1)

    elif choice==6:
        Select.append(6)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"PHPMYADMIN.."+Colour.END)
        os.system('apt-get install phpmyadmin php-mbstring php-gettext -y && phpenmod mcrypt && phpenmod mbstring')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==7:
        Select.append(7)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"NODEJS.."+Colour.END)
        os.system('apt-get install nodejs -y && apt-get install build-essential -y && apt-get install npm -y')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==8:
        Select.append(8)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"WORKBANCH.."+Colour.END)
        os.system('apt install mysql-workbench -y')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==9:
        Select.append(9)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"VSCODE.."+Colour.END)
        os.system('apt-get install snapd snapd-xdg-open -y && snap install --classic vscode')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==10:
        Select.append(10)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"COMPOSER.."+Colour.END)
        os.system('sh composer.sh')        
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==11:
        Select.append(11)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"HEROKU.."+Colour.END)
        #os.system('snap install heroku --classic -y')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==12:
        Select.append(12)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"HEROKU.."+Colour.END)
        #os.system('apt-get install default-jre -y && apt-get install default-jdk -y')
        print "\n[ Aguarde ].."
        time.sleep(1)
    
    elif choice==13:
        Select.append(13)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"INSTALL FULL.."+Colour.END)
        os.system('sh install.sh')
        print "\n[ Aguarde ].."
        time.sleep(1)

    elif choice==14:
        Select.append(14)
        print 20 * (Colour.GREEN+"."+Colour.END),(Colour.GREEN+"INSTALL FULL.."+Colour.END)
        os.system('sh test.sh')
        print "\n[ Aguarde ].."
        time.sleep(1)

    elif choice==99:
        loop=False
        
    else:
        raw_input((Colour.RED+"Opcao errada. Escolha outra ou saia do sistema digitando 99.."+Colour.END))

