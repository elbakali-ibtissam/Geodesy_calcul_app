


#EL BAKALI Ibtissam





import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve,QRect 
from PyQt5.QtGui import QIcon
import sys
import platform


# GUI FILE
from interface_application import Ui_MainWindow
from functions import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Geo_Calcul')
        self.setWindowIcon(QIcon('worldpana.png'))
        self.ui.lineEdit_32.setVisible(False) 
        self.ui.lineEdit_33.setVisible(False)
        self.ui.calcul1.setVisible(False)     
      
   
        self.ui.btn1.clicked.connect(lambda: self.clear_elements_page2())

     
        self.ui.btn2.clicked.connect(lambda: self.clear_elements_page3() )

        self.ui.btn3.clicked.connect(lambda: self.clear_elements_page4())


       
        self.ui.btn12.clicked.connect(lambda: self.clear_elements_page14()) 

    
        self.ui.btn4.clicked.connect(lambda: self.clear_elements_page5())
     
        self.ui.btn5.clicked.connect(lambda: self.clear_elements_page6()) 

   
        self.ui.btn6.clicked.connect(lambda: self.clear_elements_page7())
      
        self.ui.btn7.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_1))
        self.ui.btn8.clicked.connect(lambda: self.clear_elements_page9())
        self.ui.btn9.clicked.connect(lambda: self.clear_elements_page10())
        self.ui.btn10.clicked.connect(lambda: self.clear_elements_page11())
        self.ui.btn13.clicked.connect(lambda: self.clear_elements_page8())



        self.ui.calcul2.clicked.connect(lambda: self.affich_rayons_courbure())


        self.ui.calcul10.clicked.connect(lambda: self.afficher_probleme_direct())
        self.ui.graph.clicked.connect(lambda: self.afficher_graphe())

        self.ui.btn_lat_iso.clicked.connect(lambda: self.afficher_latitude_isometriq())
        self.ui.btn11.clicked.connect(lambda: self.clear_elements_page13())
        self.ui.btn_lat_phi.clicked.connect(lambda: self.afficher_latitude_phi())

        self.ui.calcul3.clicked.connect(lambda: self.afficher_coord_projection())

        self.ui.calcul4.clicked.connect(lambda: self.afficher_coord_geodesiques())

        self.ui.calcul7.clicked.connect(lambda: self.afficher_surface())
        self.ui.btn15.clicked.connect(lambda: self.clear_elements_page12())
        self.ui.calcul1.clicked.connect(lambda: self.calculate_parametres())
        self.ui.btn_enter_prmters.clicked.connect(lambda: self.enter_parametres())
        self.ui.calcul5.clicked.connect(lambda: self.afficher_arc_parallele())
        self.ui.calcul6.clicked.connect(lambda: self.afficher_arc_meridien())
        self.ui.btn_enter_prmters_2.clicked.connect(lambda: self.entrer_valeurs())
        self.ui.calcul8.clicked.connect(lambda: self.afficher_latitudes())
        self.ui.entrer_valrs.clicked.connect(lambda: self.entrer_angles())
        self.ui.calcul9.clicked.connect(lambda: self.afficher_angles())
        self.ui.calcul11.clicked.connect(lambda: self.afficher_probleme_inverse())


    
        self.show()
      



    def clear_elements_page2(self):
        self.ui.lineEdit_32.clear()
        self.ui.lineEdit_33.clear()
        self.ui.lineEdit_32.setVisible(False)
        self.ui.lineEdit_33.setVisible(False)
        self.ui.calcul1.setVisible(False)
        
        self.ui.label_70.clear()
        self.ui.label_71.clear()       
        self.ui.label_67.setVisible(False)
        self.ui.label_68.setVisible(False)
        self.ui.label_13.setVisible(False)
        self.ui.label_66.setVisible(False)
        self.ui.label_75.setVisible(False)
        self.ui.label_76.setVisible(False)
        self.ui.label_77.setVisible(False)
        self.ui.label_69.setVisible(False)
        self.ui.label_73.setVisible(False)
        self.ui.label_74.setVisible(False)
        self.ui.label_72.clear()
        self.ui.pages_widget.setCurrentWidget(self.ui.page_2)



    def clear_elements_page3(self):
        self.ui.label_14.setVisible(False) 
        self.ui.label_15.setVisible(False)
        self.ui.lineEdit_10.clear()
        self.ui.label_16.setVisible(False)
        self.ui.label_17.setVisible(False)
        self.ui.label_19.clear() 
        self.ui.label_18.clear()   
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_8.clear()  
        self.ui.pages_widget.setCurrentWidget(self.ui.page_3)



    def clear_elements_page4(self):

        self.ui.lineEdit_13.clear()
        self.ui.label_30.setVisible(False) 
        self.ui.label_31.clear()
        self.ui.label_32.setVisible(False) 
        self.ui.lineEdit_14.clear()
        self.ui.lineEdit_20.clear()
        self.ui.lineEdit_19.clear()
        self.ui.lineEdit_18.clear()
        self.ui.pages_widget.setCurrentWidget(self.ui.page_4)



    def clear_elements_page5(self):
        
        self.ui.label_36.setVisible(False)  
        self.ui.label_42.setVisible(False) 
        self.ui.label_37.clear() 
        self.ui.lineEdit_15.clear()  
        self.ui.lineEdit_16.clear() 
        self.ui.pages_widget.setCurrentWidget(self.ui.page_5)


    def clear_elements_page6(self):
        self.ui.lineEdit_22.clear() 
        self.ui.lineEdit_23.clear() 
        self.ui.lineEdit_25.clear() 
        self.ui.lineEdit_24.clear() 
        self.ui.lineEdit_26.clear() 
        self.ui.label_62.setVisible(False)  
        self.ui.label_58.setVisible(False)
        self.ui.label_59.setVisible(False)   
        self.ui.label_63.setVisible(False)   
        self.ui.lineEdit_27.clear() 
        self.ui.label_60.clear() 
        self.ui.label_61.clear() 
        self.ui.pages_widget.setCurrentWidget(self.ui.page_6)


    def clear_elements_page9(self):
        self.ui.label_164.setVisible(False)  
        self.ui.label_165.setVisible(False)
        self.ui.lineEdit_28.clear() 
        self.ui.lineEdit_40.clear() 
        self.ui.lineEdit_41.clear() 
        self.ui.lineEdit_42.clear() 
        self.ui.lineEdit_37.clear() 
        self.ui.lineEdit_39.clear() 
        self.ui.lineEdit_38.clear() 
        self.ui.lineEdit_34.clear() 
        self.ui.lineEdit_35.clear() 
        self.ui.lineEdit_36.clear()  
  
        self.ui.label_163.clear()
        self.ui.pages_widget.setCurrentWidget(self.ui.page_9)

    def clear_elements_page7(self):
        self.ui.label_43.setVisible(False)  
        self.ui.label_45.setVisible(False)
        self.ui.lineEdit_20.clear() 
        self.ui.lineEdit_21.clear() 
        self.ui.label_44.clear() 
        self.ui.label_46.clear()
        self.ui.pages_widget.setCurrentWidget(self.ui.page_7)


    def clear_elements_page10(self):
        self.ui.lineEdit_79.clear() 
        self.ui.lineEdit_78.clear() 
        self.ui.lineEdit_72.clear() 
        self.ui.lineEdit_75.clear() 
        self.ui.lineEdit_77.clear() 
        self.ui.lineEdit_73.clear()        
        self.ui.lineEdit_74.clear() 
        self.ui.lineEdit_76.clear() 
        self.ui.label_178.clear() 
        self.ui.label_179.setVisible(False)  
        self.ui.label_178.setVisible(False)
        self.ui.label_180.setVisible(False)
        self.ui.pages_widget.setCurrentWidget(self.ui.ppage_10)


    def clear_elements_page11(self):
        self.ui.lineEdit_80.clear() 
        self.ui.lineEdit_81.clear() 
        self.ui.lineEdit_82.clear() 
        self.ui.lineEdit_83.clear() 
        self.ui.lineEdit_84.clear() 
        self.ui.lineEdit_85.clear()        
        self.ui.label_185.clear() 
        self.ui.label_186.setVisible(False)  
        self.ui.label_187.setVisible(False)
        self.ui.pages_widget.setCurrentWidget(self.ui.ppage_11)


    def clear_elements_page8(self):
        self.ui.lineEdit_43.clear() 
        self.ui.lineEdit_44.clear() 
        self.ui.lineEdit_45.clear() 
        self.ui.lineEdit_46.clear() 
        self.ui.lineEdit_47.clear() 
        self.ui.label_93.clear()        
        self.ui.label_95.clear()
        self.ui.label_92.clear()
        self.ui.label_94.clear()  
        self.ui.graph.setVisible(False) 
        self.ui.label_83.setVisible(False)  
        self.ui.label_84.setVisible(False)
        self.ui.calcul8.setVisible(False)  
        self.ui.label_85.setVisible(False)
        self.ui.label_89.setVisible(False)  
        self.ui.label_87.setVisible(False)
        self.ui.label_90.setVisible(False)  
        self.ui.label_88.setVisible(False)
        self.ui.label_86.clear()
        self.ui.lineEdit_43.setVisible(False)  
        self.ui.lineEdit_44.setVisible(False)
  
        self.ui.lineEdit_47.setVisible(False)
        self.ui.lineEdit_46.setVisible(False)  
        self.ui.lineEdit_45.setVisible(False)
        self.ui.pages_widget.setCurrentWidget(self.ui.page_8)       

    def clear_elements_page12(self):
        self.ui.label_404.setVisible(False)          
        self.ui.label_405.setVisible(False)  
        self.ui.label_403.setVisible(False)  
        self.ui.label_269.setVisible(False) 
        self.ui.label_267.clear() 
        self.ui.label_268.clear() 
        self.ui.lineEdit_110.clear() 
        self.ui.lineEdit_112.clear() 
        self.ui.lineEdit_113.clear()
        self.ui.lineEdit_113.setVisible(False)  
        self.ui.lineEdit_112.setVisible(False)
        self.ui.calcul9.setVisible(False)  
        self.ui.lineEdit_110.setVisible(False)
        self.ui.pages_widget.setCurrentWidget(self.ui.page12)     

    def clear_elements_page13(self):
        self.ui.label_708.setVisible(False)          
        self.ui.label_707.setVisible(False)  
        self.ui.label_705.setVisible(False)  
        self.ui.label_862.setVisible(False)
        self.ui.label_706.setVisible(False)  
        self.ui.label_863.setVisible(False)    

      
        self.ui.lineEdit_167.clear() 
        self.ui.lineEdit_168.clear() 
        self.ui.lineEdit_169.clear()
        self.ui.lineEdit_171.clear() 
        self.ui.lineEdit_172.clear() 
        self.ui.lineEdit_173.clear()
        self.ui.lineEdit_170.clear()
        self.ui.lineEdit_296.clear()
        self.ui.lineEdit_173.clear()
        self.ui.pages_widget.setCurrentWidget(self.ui.page_13) 


    def clear_elements_page14(self):
        self.ui.label_884.setVisible(False)          
        self.ui.label_881.setVisible(False)  
        self.ui.label_882.setVisible(False)  
        self.ui.label_883.setVisible(False) 
        self.ui.label_885.setVisible(False)  
        self.ui.label_886.setVisible(False)    

        self.ui.lineEdit_359.clear() 
        self.ui.lineEdit_361.clear() 
        self.ui.lineEdit_360.clear() 
        self.ui.lineEdit_362.clear()
        self.ui.lineEdit_363.clear()
        self.ui.lineEdit_364.clear() 
        self.ui.lineEdit_365.clear() 
        self.ui.lineEdit_366.clear()                
        self.ui.lineEdit_367.clear() 
        self.ui.lineEdit_368.clear() 
        self.ui.lineEdit_369.clear() 
        self.ui.lineEdit_370.clear() 

        self.ui.pages_widget.setCurrentWidget(self.ui.page14) 


    def calculate_parametres(self):

      
        self.ui.label_67.setVisible(True)
        self.ui.label_68.setVisible(True)
        self.ui.label_13.setVisible(True)
        self.ui.label_66.setVisible(True)
        self.ui.label_75.setVisible(True)
        self.ui.label_76.setVisible(True)
        self.ui.label_77.setVisible(True)
        self.ui.label_69.setVisible(True)
        self.ui.label_73.setVisible(True)
        self.ui.label_74.setVisible(True)

        options = [
            "Demi-grand axe (a) et demi-petit axe (b)",
            "Demi-grand axe (a) et aplatissement (f)",
            "Demi-grand axe (a) et première excentricité (e²)"
            ,"Demi-grand axe (a) et deuxième excentricité (e'²)",
            "Demi-petit axe (b) et aplatissement (f)",
            "Demi-petit axe (b) et première excentricité (e²)",
            "Demi-petit axe (b) et deuxième excentricité (e'²)"
        ]       
        choice = self.ui.comboBox_5.currentText()
        if(options[0]==choice):
            a =float(self.ui.lineEdit_32.text())
            b =float(self.ui.lineEdit_33.text())
            f =(a-b)/a
            premiere_excentricite=(a**2 -b**2)/(a**2)
            deuxieme_excentricite=(a**2 -b**2)/(b**2)
            self.ui.label_70.setText(str(f))
            self.ui.label_69.setText("f :")
            self.ui.label_75.setText("")  
            self.ui.label_73.setText("e² :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(premiere_excentricite))      
            self.ui.label_72.setText(str(deuxieme_excentricite))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("e'² :") 


        elif(options[1]==choice):
            a =float(self.ui.lineEdit_32.text())
            f =float(self.ui.lineEdit_33.text())
            b =(a*((1/f)-1))*f
            premiere_excentricite =(a**2-b**2)/(a**2)
            deuxieme_excentricite=(a**2 -b**2)/b**2
            self.ui.label_70.setText(str(b))
            self.ui.label_69.setText("b :")
            self.ui.label_75.setText("m")  
            self.ui.label_73.setText("e² :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(premiere_excentricite))      
            self.ui.label_72.setText(str(deuxieme_excentricite))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("e'² :") 



        

        elif(options[2]==choice):
            a =float(self.ui.lineEdit_32.text())
            e_carre =float(self.ui.lineEdit_33.text())
            b =sqrt((a**2 )*(1-e_carre))
            f =(a-b)/a
            deuxieme_excentricite=(a**2 -b**2)/b**2

            self.ui.label_70.setText(str(b))
            self.ui.label_69.setText("b :")
            self.ui.label_75.setText("m")  
            self.ui.label_73.setText("f :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(f))      
            self.ui.label_72.setText(str(deuxieme_excentricite))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("e'² :") 



   
        elif(options[3]==choice):
            a =float(self.ui.lineEdit_32.text())
            deuxieme_excentricite =float(self.ui.lineEdit_33.text())
            b =a/(sqrt(1+deuxieme_excentricite))
            f =(a-b)/a
            premiere_excentricite=(a**2 -b**2)/a**2


            self.ui.label_70.setText(str(b))
            self.ui.label_69.setText("b :")
            self.ui.label_75.setText("m")  
            self.ui.label_73.setText("f :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(f))      
            self.ui.label_72.setText(str(premiere_excentricite))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("e² :") 



        elif(options[4]==choice):
       
            b =float(self.ui.lineEdit_32.text())
            f =float(self.ui.lineEdit_33.text())
            a =b/(1-f)
            premiere_excentricite=(a**2 -b**2)/(a**2)
            deuxieme_excentricite=(a**2 -b**2)/(b**2)

            self.ui.label_70.setText(str(a))
            self.ui.label_69.setText("a :")
            self.ui.label_75.setText("m")  
            self.ui.label_73.setText("e² :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(premiere_excentricite))      
            self.ui.label_72.setText(str(deuxieme_excentricite))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("e'² :") 




        elif(options[5]==choice):
            b =float(self.ui.lineEdit_32.text())
            premiere_excentricite =float(self.ui.lineEdit_33.text())

            a =b/sqrt(1-premiere_excentricite)
            f=(a-b)/a
            deuxieme_excentricite=(a**2 -b**2)/(b**2)
            self.ui.label_70.setText(str(a))
            self.ui.label_69.setText("a :")
            self.ui.label_75.setText("m")  
            self.ui.label_73.setText("f :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(f))      
            self.ui.label_72.setText(str(deuxieme_excentricite))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("e'² :") 



        else:
            b =float(self.ui.lineEdit_32.text())
            deuxieme_excentricite =float(self.ui.lineEdit_33.text())

            a =sqrt((b**2)*(1+deuxieme_excentricite))
            premiere_excentricite=(a**2 -b**2)/(a**2)
            f=(a-b)/a
            self.ui.label_70.setText(str(a))
            self.ui.label_69.setText("a :")
            self.ui.label_75.setText("m")  
            self.ui.label_73.setText("e² :")  
            self.ui.label_76.setText("") 
            self.ui.label_71.setText(str(premiere_excentricite))      
            self.ui.label_72.setText(str(f))           
            self.ui.label_77.setText("")   
            self.ui.label_74.setText("f :") 
       













    def enter_parametres(self):
        self.ui.lineEdit_32.setVisible(True)
        self.ui.lineEdit_33.setVisible(True)
        self.ui.calcul1.setVisible(True)
        self.ui.calcul1.setVisible(True)
        self.ui.lineEdit_32.clear()
        self.ui.lineEdit_33.clear()
        self.ui.label_67.setVisible(True)
        self.ui.label_68.setVisible(True)
        self.ui.label_13.setVisible(True)
        self.ui.label_66.setVisible(True)
      
        options = [
            "Demi-grand axe (a) et demi-petit axe (b)",
            "Demi-grand axe (a) et aplatissement (f)",
            "Demi-grand axe (a) et première excentricité (e²)"
            ,"Demi-grand axe (a) et deuxième excentricité (e'²)",
            "Demi-petit axe (b) et aplatissement (f)",
            "Demi-petit axe (b) et première excentricité (e²)",
            "Demi-petit axe (b) et deuxième excentricité (e'²)"
        ]   

        choice = self.ui.comboBox_5.currentText()
        if(options[0]==choice):
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText('a :')
            self.ui.label_66.setText('b :')
            self.ui.label_67.setText ('m')  
            self.ui.label_68.setText ('m') 
        
        elif(options[1]==choice):
        
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText ('a :')
            self.ui.label_66.setText("f :") 
            self.ui.label_67.setText('m') 
            self.ui.label_68.setText ('')
        elif(options[2]==choice):
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText('a :')
            self.ui.label_66.setText("e² :")  
            self.ui.label_67.setText('m')  
            self.ui.label_68.setText ('')                   

        elif(options[3]==choice):
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText ('a :')
            self.ui.label_66.setText ("e'² :")
            self.ui.label_67.setText ('m')  
            self.ui.label_68.setText ('')
        elif(options[4]==choice):
       
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText('b :')
            self.ui.label_66.setText("f :")
            self.ui.label_67.setText('m')
            self.ui.label_68.setText ('')

        elif(options[5]==choice):
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText('b :')
            self.ui.label_66.setText("e² :")
            self.ui.label_67.setText('m')
            self.ui.label_68.setText ('')



        else:
            self.ui.lineEdit_32.setVisible (True)
            self.ui.lineEdit_33.setVisible(True) 
            self.ui.label_13.setText('b :') 
            self.ui.label_66.setText ("e'² :")
            self.ui.label_67.setText ('m')
            self.ui.label_68.setText ('')
       






    def affich_rayons_courbure(self):

        self.ui.label_14.setVisible (True)
        self.ui.label_15.setVisible (True)      
        self.ui.label_17.setVisible (True)    
        self.ui.label_16.setVisible (True)       
        a =float(self.ui.lineEdit_8.text())
        excevtricity1 =float(self.ui.lineEdit_9.text()) 
        phi_deg = float(self.ui.lineEdit_10.text())
        phi_min = float(self.ui.lineEdit_11.text())
        phi_sec = float(self.ui.lineEdit_12.text())
        choice = self.ui.comboBox_6.currentText()
        tuple = functions.calculate_rayouns_courbure(excevtricity1, choice, phi_deg,phi_min, phi_sec, a)
        self.ui.label_18.setText(str(tuple[1]))
        
        self.ui.label_19.setText(str(tuple[0]))
        

    def afficher_latitude_isometriq(self):

        self.ui.label_32.setVisible(True)   
        self.ui.label_30.setVisible(True) 
        a =float(self.ui.lineEdit_13.text())
        excevtricity1 =float(self.ui.lineEdit_19.text()) 
        phi_deg = float(self.ui.lineEdit_14.text())
        phi_min = float(self.ui.lineEdit_17.text())
        phi_sec = float(self.ui.lineEdit_18.text())
        self.ui.label_31.setText(str(functions.calculate_latitude_isométrique(excevtricity1, phi_deg, phi_min, phi_sec)))


    def afficher_latitude_phi(self):
        self.ui.label_36.setVisible(True)  
        self.ui.label_42.setVisible(True) 
        excevtricity1 =float(self.ui.lineEdit_15.text()) 
        U =float(self.ui.lineEdit_16.text())

        self.ui.label_37.setText(functions.calculate_latitude( U, excevtricity1))



    def afficher_coord_projection(self):
        self.ui.label_62.setVisible(True)  
        self.ui.label_58.setVisible(True)
        self.ui.label_59.setVisible(True)  
        self.ui.label_63.setVisible(True)  
        
        phi_deg = float(self.ui.lineEdit_22.text())
        phi_min = float(self.ui.lineEdit_23.text())
        phi_sec = float(self.ui.lineEdit_24.text())
        landa_deg = float(self.ui.lineEdit_25.text())
        landa_min = float(self.ui.lineEdit_26.text())
        landa_sec = float(self.ui.lineEdit_27.text())
        choice = self.ui.comboBox_4.currentText()
        latitude =(phi_deg)+(phi_min/60)+(phi_sec/3600)*pi/180
        longitude = -((landa_deg)+(landa_min/60)+(landa_sec/3600))*pi/180
        tuple = functions.calculate_coord_carto(choice,latitude,longitude)
        self.ui.label_60.setText(str(tuple[0])) 
        self.ui.label_61.setText(str(tuple[1])) 


    def afficher_coord_geodesiques(self):

        self.ui.label_43.setVisible(True)  
        self.ui.label_45.setVisible(True) 

        X = float(self.ui.lineEdit_20.text())
        Y = float(self.ui.lineEdit_21.text())

        choice = self.ui.comboBox_3.currentText()

        tuple = functions.calculer_coord_geog(X,Y,choice)
        self.ui.label_44.setText(tuple[0])
        self.ui.label_46.setText(tuple[1])


    def afficher_arc_parallele(self):

        self.ui.label_164.setVisible(True)  
        self.ui.label_165.setVisible(True)

        N =float(self.ui.lineEdit_28.text())
        phi_deg = float(self.ui.lineEdit_40.text())
        phi_min = float(self.ui.lineEdit_41.text())
        phi_sec = float(self.ui.lineEdit_42.text())
        landa1_deg = float(self.ui.lineEdit_37.text())
        landa1_min = float(self.ui.lineEdit_38.text())
        landa1_sec = float(self.ui.lineEdit_39.text())

        landa2_deg = float(self.ui.lineEdit_34.text())
        landa2_min = float(self.ui.lineEdit_35.text())
        landa2_sec = float(self.ui.lineEdit_36.text())
        choice_phi = self.ui.comboBox_13.currentText()
        choice_land1 = self.ui.comboBox_12.currentText()
        choice_land2 = self.ui.comboBox_11.currentText()
        
        latitude =(phi_deg)+(phi_min/60)+(phi_sec/3600)*pi/180
        longitude1 = (landa1_deg)+(landa1_min/60)+(landa1_sec/3600)*pi/180
        longitude2 = (landa2_deg)+(landa2_min/60)+(landa2_sec/3600)*pi/180
        if(choice_phi=="N" and choice_land1=="E" and choice_land2 =='E'):
            longueur =functions.calculate_arc_parallele(longitude1, longitude2,N, latitude)      
            self.ui.label_163.setText(str(longueur))

            
        elif(choice_phi=="N" and choice_land1=='W' and choice_land2=='W'):
            long1 = -longitude1
            long2 = -longitude2
            longueur =functions.calculate_arc_parallele(long1, long2,N, latitude)
            self.ui.label_163.setText(str(longueur))
        elif(choice_phi=="N" and choice_land1=='E' and choice_land2=='W'):
            long2 = -longitude2
            longueur =functions.calculate_arc_parallele(longitude1, long2,N, latitude)
            self.ui.label_163.setText(str(longueur))
        elif(choice_phi=="N" and choice_land1=='W' and choice_land2=='E'):
            long1 = -longitude1
            longueur =functions.calculate_arc_parallele(long1, longitude2,N, latitude)
            self.ui.label_163.setText(str(longueur))
        elif(choice_phi=="S" and choice_land1=='W' and choice_land2=='W'):
          
            lat = -latitude
            long1 = -longitude1
            long2 = -longitude2
            longueur =functions.calculate_arc_parallele(long1, long2,N, lat) 
            self.ui.label_163.setText(str(longueur))          
        elif(choice_phi=="S" and choice_land1=='W' and choice_land2=='E'):
          
            lat = -latitude
            long1 = -longitude1
          
            longueur =functions.calculate_arc_parallele(long1, longitude2,N, lat) 
            self.ui.label_163.setText(str(longueur))
        elif(choice_phi=="S" and choice_land1=='E' and choice_land2=='W'):
          
            lat = -latitude
            long2 = -longitude2

            longueur =functions.calculate_arc_parallele(longitude1, long2,N, lat) 
            self.ui.label_163.setText(str(longueur))
        else:
          
            lat = -latitude

            longueur =functions.calculate_arc_parallele(longitude1, longitude2,N, lat) 
            self.ui.label_163.setText(str(longueur))



    def afficher_arc_meridien(self):
        self.ui.label_179.setVisible(True)  
        self.ui.label_178.setVisible(True)
        self.ui.label_180.setVisible(True)
        a = float(self.ui.lineEdit_79.text())
        e_carre = float(self.ui.lineEdit_78.text())

        phi1_deg = float(self.ui.lineEdit_72.text())
        phi1_min = float(self.ui.lineEdit_75.text())
        phi1_sec = float(self.ui.lineEdit_77.text())

        phi2_deg = float(self.ui.lineEdit_73.text())
        phi2_min = float(self.ui.lineEdit_74.text())
        phi2_sec = float(self.ui.lineEdit_76.text())
        choice_phi1 = self.ui.comboBox_16.currentText()
        choice_phi2 = self.ui.comboBox_15.currentText()
        latitude2 =(phi2_deg)+(phi2_min/60)+(phi2_sec/3600)      
        latitude1 =(phi1_deg)+(phi1_min/60)+(phi1_sec/3600)
        M1 =(a*(1-e_carre))/((1-e_carre*(sin(latitude1))**2)**(3/2)) 
        M2 =(a*(1-e_carre))/((1-e_carre*(sin(latitude2))**2)**(3/2))  

        if(choice_phi1 =="N" and choice_phi2 =='N'):
            longueur =functions.calculate_arc_meridien(latitude1*(pi/180 ),latitude2*(pi/180 ), a, e_carre,M1 ,M2)
            self.ui.label_178.setText(str(longueur))

        elif(choice_phi1=='S' and choice_phi2 =='S'):
            longueur =functions.calculate_arc_meridien(-latitude1*(pi/180) ,-latitude2*(pi/180 ), a, e_carre,M1 ,M2) 
            self.ui.label_178.setText(str(longueur)) 
        elif(choice_phi1=='N' and choice_phi2 =='S'):
            longueur =functions.calculate_arc_meridien(latitude1*(pi/180 ),-latitude2*(pi/180 ), a, e_carre,M1 ,M2)                       
            self.ui.label_178.setText(str(longueur))
        else:
            longueur =functions.calculate_arc_meridien(-latitude1*(pi/180 ),latitude2*(pi/180 ), a, e_carre,M1 ,M2)  

            self.ui.label_178.setText(str(longueur))




    def afficher_surface(self):
        self.ui.label_186.setVisible(True)  
        self.ui.label_187.setVisible(True)
        b = float(self.ui.lineEdit_80.text())
        e_carre = float(self.ui.lineEdit_81.text())

        phi1 =(float(self.ui.lineEdit_82.text())) *pi/180 
        phi2 = (float(self.ui.lineEdit_83.text()))  *pi/180 
        landa1 = (float(self.ui.lineEdit_85.text())) *pi/180     
        landa2 = (float(self.ui.lineEdit_84.text())) *pi/180 
        S =functions.calculate_surface(b,phi1, phi2, landa1, landa2, e_carre)
        self.ui.label_185.setText(str(S))        



    def entrer_valeurs(self):
        options =["Latitude Géodésique","Latitude Géocentrique","Latitude Réduite"]
        self.ui.lineEdit_43.setVisible(True)  
        self.ui.lineEdit_44.setVisible(True)
        self.ui.calcul8.setVisible(True)    
        self.ui.graph.setVisible(True)   
        self.ui.lineEdit_47.setVisible(True)
        self.ui.lineEdit_46.setVisible(True)  
        self.ui.lineEdit_45.setVisible(True)
        self.ui.label_83.setVisible(True)  
        self.ui.label_84.setVisible(True)
        self.ui.label_86.clear()
        self.ui.label_85.setVisible(True)
        self.ui.label_89.setVisible(True)  
        self.ui.label_87.setVisible(True)
        self.ui.label_90.setVisible(True)  
        self.ui.label_88.setVisible(True)
        choice = self.ui.comboBox_8.currentText()
        if(choice ==options[0]):
            self.ui.label_86.setText(' phi : ')
        elif(choice ==options[1]): 
            self.ui.label_86.setText(' Ψ : ')           
        else:
            self.ui.label_86.setText(' β : ')


    def afficher_latitudes(self):

        options =["Latitude Géodésique","Latitude Géocentrique","Latitude Réduite"]
        a = float(self.ui.lineEdit_46.text())
        b = float(self.ui.lineEdit_47.text())
        lat_deg = float(self.ui.lineEdit_43.text())
        lat_min = float(self.ui.lineEdit_44.text())
        lat_sec = float(self.ui.lineEdit_45.text())      
        choice = self.ui.comboBox_8.currentText()
        latitude =(lat_deg)+(lat_min/60)+(lat_sec/3600)
        tuple = functions.calculate_latitudes(a, b, latitude, choice)
        if(choice ==options[0]):
            self.ui.label_94.setText(' Latitude Géocentrique : ')
            self.ui.label_92.setText(' Latitude paramétrique : ')
            self.ui.label_95.setText(str(tuple[0])+' °')
            self.ui.label_93.setText(str(tuple[1])+' °')
        elif(choice ==options[1]): 
            self.ui.label_92.setText(' Latitude Réduite : ')
            self.ui.label_94.setText(' Latitude Géodésique : ')
            self.ui.label_95.setText(str(tuple[0])+' °')
            self.ui.label_93.setText(str(tuple[1])+' °')         
        else:

            self.ui.label_92.setText(' Latitude Géocentrique : ')
            self.ui.label_94.setText(' Latitude géodésique : ')
            self.ui.label_95.setText(str(tuple[0])+' °')
            self.ui.label_93.setText(str(tuple[1])+' °')


    def afficher_graphe(self):
        options =["Latitude Géodésique","Latitude Géocentrique","Latitude Réduite"]      
        a = float(self.ui.lineEdit_46.text())
        b = float(self.ui.lineEdit_47.text())
        lat_deg = float(self.ui.lineEdit_43.text())
        lat_min = float(self.ui.lineEdit_44.text())
        lat_sec = float(self.ui.lineEdit_45.text())      
        choice = self.ui.comboBox_8.currentText()
        latitude =(lat_deg)+(lat_min/60)+(lat_sec/3600)
        tuple = functions.calculate_latitudes(a, b, latitude, choice)
        if(choice ==options[0]):
            functions.tracer_directions_latitudes(a, b,latitude,tuple[0],tuple[1])
        elif(choice ==options[1]): 
            functions.tracer_directions_latitudes(a, b,tuple[1],latitude,tuple[0])     
        else:
            functions.tracer_directions_latitudes(a, b,tuple[1],tuple[0], latitude)  



    def entrer_angles(self):
        options =["rad","deg","DMS"]
       
        self.ui.label_269.setVisible(False) 
        self.ui.lineEdit_110.setVisible(False)      
        self.ui.label_403.setVisible(False)
        self.ui.lineEdit_110.clear() 
        self.ui.lineEdit_112.clear() 
        self.ui.lineEdit_113.clear()
        self.ui.label_404.setVisible(False)          
        self.ui.label_405.setVisible(False)  
        
        self.ui.calcul9.setVisible(True)  
        self.ui.lineEdit_110.setVisible(True)
        choice = self.ui.comboBox_7.currentText()
        if(choice ==options[0]):
            self.ui.label_269.setVisible(True) 
            self.ui.lineEdit_110.setVisible(True) 
            self.ui.label_404.setVisible(False)          
            self.ui.label_405.setVisible(False) 
            self.ui.lineEdit_112.setVisible(False)  
            self.ui.lineEdit_113.setVisible(False)

        elif(choice ==options[1]): 
            self.ui.label_269.setVisible(True) 
            self.ui.lineEdit_110.setVisible(True) 
            self.ui.label_403.setVisible(True)
            self.ui.lineEdit_112.clear() 
            self.ui.lineEdit_113.clear()
            self.ui.label_404.setVisible(False)          
            self.ui.label_405.setVisible(False) 
            self.ui.lineEdit_112.setVisible(False)  
            self.ui.lineEdit_113.setVisible(False)
        else:
            self.ui.label_269.setVisible(True) 
            self.ui.lineEdit_110.setVisible(True) 
            self.ui.label_403.setVisible(True)
            self.ui.lineEdit_113.setVisible(True)
            self.ui.lineEdit_112.setVisible(True) 
            self.ui.label_405.setVisible(True) 
            self.ui.label_404.setVisible(True)
                    



    def afficher_angles(self):
        options =["rad","deg","DMS"]
        choice = self.ui.comboBox_7.currentText()

        if(choice ==options[0]):
            angle =float(self.ui.lineEdit_110.text())
            resultat =functions.rad_to_deg_dms(angle)
            self.ui.label_267.setText(str(resultat[0])+' °')
            self.ui.label_268.setText(str(resultat[0])+' ° '+str(resultat[1])+" '"+str(resultat[2]) +"''")         
        elif(choice ==options[1]):
            angle =float(self.ui.lineEdit_110.text())
            resultat =functions.deg_to_rad_and_dms(angle)
            self.ui.label_267.setText(str(resultat[0])+'  rad ')
            self.ui.label_268.setText(str(resultat[1])+' ° '+str(resultat[2])+" ' "+str(resultat[3])+" ''" ) 

        else:
            deg =float(self.ui.lineEdit_110.text())
            min =float(self.ui.lineEdit_113.text())
            sec =float(self.ui.lineEdit_112.text())
            resultat =functions.dms_to_rad_and_deg(deg, min, sec)
            self.ui.label_267.setText(str(resultat[0])+'  rad ')
            self.ui.label_268.setText(str(resultat[1])+' ° ') 


    def afficher_probleme_direct(self):
        self.ui.label_708.setVisible(True)          
        self.ui.label_707.setVisible(True)  
        self.ui.label_705.setVisible(True)  
        self.ui.label_862.setVisible(True)
        self.ui.label_706.setVisible(True)  
        self.ui.label_863.setVisible(True)  

        ellipsoide =self.ui.comboBox_58.currentText()
        methode =self.ui.comboBox_72.currentText()
        fi_1 = float(self.ui.lineEdit_167.text())+float(self.ui.lineEdit_169.text())/60 +float(self.ui.lineEdit_168.text())/3600
        landa_1 = float(self.ui.lineEdit_170.text())+float(self.ui.lineEdit_172.text())/60 +float(self.ui.lineEdit_171.text())/3600
        az_aller = float(self.ui.lineEdit_296.text())
        distance = float(self.ui.lineEdit_173.text())
        if(ellipsoide =='Clarke 1880'):
            e_carre =6.8033*pow(10,-3)
            M1 =(6378249.145*(1-6.8033*pow(10, -3)*(sin(fi_1)**2))/ pow(1-6.8033*pow(10, -3), 3/2))
            N1 =(6378249.145/pow(1-6.8033*pow(10, -3)*sin(fi_1)**2, 1/2))
            R =(2*6378249.145 + 6356515.566)/3
            a=6378249.145
            dis =(distance*1000/R)*(180/pi)
            if(methode == 'Gauss legendre'):
                tuple = functions.gauss_legendre_direct(fi_1, landa_1, dis, az_aller)
                if(distance<200 ):
                    self.ui.label_708.setText(str(tuple[0])+' °')  
                    self.ui.label_862.setText(str(tuple[1])+' °')           
                    self.ui.label_863.setText(str(tuple[2])+' °')
                else:
                    QMessageBox.warning(self, 'Avertissement', 'la longueur des cotés dépassent 200 Km')
            elif(methode == 'Puissant'):


                tuple =functions.Puissant_direct(fi_1, landa_1, az_aller,dis,e_carre ,M1,N1,a)

                self.ui.label_708.setText(str(tuple[0])+' °')  
                self.ui.label_862.setText(str(tuple[1])+' °')           
                self.ui.label_863.setText(str(tuple[2])+' °') 
            else:          
                tuple =functions.gauss_midlatitude(dis,landa_1,az_aller, fi_1, N1, M1)

                self.ui.label_708.setText(str(tuple[0])+' °')  
                self.ui.label_862.setText(str(tuple[2])+' °')           
                self.ui.label_863.setText(str(tuple[1])+' °')  
        else:   
            a =6378137            
            R =(2*6378137 +6356752.314)/3
            e_carre =6.694380*pow(10,-3)
            M1 =(6378137*(1-6.694380*pow(10,-3)*(sin(fi_1)**2))/ pow(1-6.694380*pow(10,-3), 3/2))
            N1 =(6378137/pow(1-6.694380*pow(10,-3)*sin(fi_1)**2, 1/2))
           
            
            dis =(distance*1000/R)*(180/pi)
            if(methode == 'Gauss legendre'):
                tuple = functions.gauss_legendre_direct(fi_1, landa_1, dis, az_aller)
                if(distance<200 ):
                    self.ui.label_708.setText(str(tuple[0])+' °')  
                    self.ui.label_862.setText(str(tuple[1])+' °')           
                    self.ui.label_863.setText(str(tuple[2])+' °')
                else:
                    QMessageBox.warning(self, 'Avertissement', 'la longueur des cotés dépassent 200 Km')
            elif(methode == 'Puissant'):


                tuple =functions.Puissant_direct(fi_1, landa_1,az_aller, dis, e_carre ,M1,N1,a)

                self.ui.label_708.setText(str(tuple[0])+' °')  
                self.ui.label_862.setText(str(tuple[1])+' °')           
                self.ui.label_863.setText(str(tuple[2])+' °') 
            else:          
                tuple =functions.gauss_midlatitude(dis,landa_1,az_aller, fi_1, N1, M1)

                self.ui.label_708.setText(str(tuple[0])+' °')  
                self.ui.label_862.setText(str(tuple[2])+' °')           
                self.ui.label_863.setText(str(tuple[1])+' °')  


    def afficher_probleme_inverse(self):
        self.ui.label_884.setVisible(True)          
        self.ui.label_881.setVisible(True)  
        self.ui.label_882.setVisible(True)  
        self.ui.label_883.setVisible(True) 
        self.ui.label_885.setVisible(True)  
        self.ui.label_886.setVisible(True) 
        methode = self.ui.comboBox_73.currentText()
        ellipsoide =self.ui.comboBox_71.currentText()
        
        fi_1 = float(self.ui.lineEdit_359.text())+float(self.ui.lineEdit_362.text())/60 +float(self.ui.lineEdit_361.text())/3600
        landa_1 = float(self.ui.lineEdit_360.text())+float(self.ui.lineEdit_363.text())/60 +float(self.ui.lineEdit_364.text())/3600
        fi_2 = float(self.ui.lineEdit_365.text())+float(self.ui.lineEdit_366.text())/60 +float(self.ui.lineEdit_367.text())/3600
        landa_2 = float(self.ui.lineEdit_368.text())+float(self.ui.lineEdit_369.text())/60 +float(self.ui.lineEdit_370.text())/3600

        if(ellipsoide =='Clarke 1880'):
            R =(2*6378249.145 + 6356515.566)/3
            if(methode =='Gauss legendre'):

                tuple =functions.gauss_legendre_inverse(fi_1, fi_2, landa_1, landa_2)
                self.ui.label_884.setText(str(tuple[0]*R)+' m')  
                self.ui.label_885.setText(str(tuple[1])+' °')           
                self.ui.label_886.setText(str(tuple[2])+' °') 
            else:
                e_carre =6.8033*pow(10,-3)
                M1 =(6378249.145*(1-6.8033*pow(10, -3)*(sin(fi_1)**2))/ pow(1-6.8033*pow(10, -3), 3/2))
                N1 =(6378249.145/pow(1-6.8033*pow(10, -3)*sin(fi_1)**2, 1/2))
                M2 =(6378249.145*(1-6.8033*pow(10, -3)*(sin(fi_2)**2))/ pow(1-6.8033*pow(10, -3), 3/2))
                N2 =(6378249.145/pow(1-6.8033*pow(10, -3)*sin(fi_2)**2, 1/2))
                R =(2*6378249.145 + 6356515.566)/3
                a=6378249.145
                tuple =functions.inverse_gauss_midlatitude(radians(landa_1), radians(landa_2), radians(fi_1), radians(fi_2), N1, M1,N2,M2)
                self.ui.label_884.setText(str(tuple[0])+' m')  
                self.ui.label_885.setText(str(tuple[1])+' °')           
                self.ui.label_886.setText(str(tuple[2])+' °')
        else: 
            R =(2*6378137 +6356752.314)/3
            if(methode =='Gauss legendre'):   
                       
                tuple =functions.gauss_legendre_inverse(fi_1, fi_2, landa_1, landa_2)
                self.ui.label_884.setText(str(tuple[0]*R)+' m')  
                self.ui.label_885.setText(str(tuple[1])+' °')           
                self.ui.label_886.setText(str(tuple[2])+' °') 
            else:
                a =6378137            
                R =(2*6378137 +6356752.314)/3
                e_carre =6.694380*pow(10,-3)
                M1 =(6378137*(1-6.694380*pow(10,-3)*(sin(fi_1)**2))/ pow(1-6.694380*pow(10,-3), 3/2))
                N1 =(6378137/pow(1-6.694380*pow(10,-3)*sin(fi_1)**2, 1/2))
                
            
                M2 =(6378137*(1-6.694380*pow(10, -3)*(sin(fi_2)**2))/ pow(1-6.694380*pow(10, -3), 3/2))
                N2 =(6378137/pow(1-6.694380*pow(10, -3)*sin(fi_2)**2, 1/2))
               
                tuple =functions.inverse_gauss_midlatitude(radians(landa_1), radians(landa_2), radians(fi_1), radians(fi_2), N1, M1,N2,M2)
                self.ui.label_884.setText(str(tuple[0])+' m')  
                self.ui.label_885.setText(str(tuple[1])+' °')           
                self.ui.label_886.setText(str(tuple[2])+' °')
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =MainWindow()
    sys.exit(app.exec_())
























