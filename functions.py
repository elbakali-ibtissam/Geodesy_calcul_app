import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Arrow
from sympy import *
from math import *
from matplotlib.patches import Ellipse

class functions():

    def calculate_coord_carto(option,  latitude, longitude):
        options =["lambert 1","lambert 2","lambert 3","lambert 4"]

    
        e_carre =0.0068034876
        a =6378249.2
        k_0 =[0.999625769, 0.999615596, 0.999616304,0.999616437]
        X_0 =[500000, 500000, 1200000,1500000]
        Y_0 =[300000,300000, 400000,400000]
        lambda_0 =-0.0942477796
        fi_0 =[0.5811946409, 0.5183627878, 0.4555309348, 0.3926990817]
       

        U =log(tan(pi/4 + latitude/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(latitude))/(1-sqrt(e_carre)*sin(latitude)))
        if(option == options[0]):
            convergence_meridien =sin(fi_0[0])*(longitude-lambda_0)
            U_0 =log(tan(pi/4+fi_0[0]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[0]))/(1-sqrt(e_carre)*sin(fi_0[0])))
            U_barre =U-U_0
            N_0 =a/sqrt(1-e_carre*pow(sin(fi_0[0]),2))
            ro_0 =k_0[0]*N_0*(1/tan(fi_0[0]))
            X_proj =ro_0*exp(-U_barre*sin(fi_0[0]))*sin(convergence_meridien)
            Y_proj = -ro_0*(exp(-(U_barre*sin(fi_0[0])))*(cos(convergence_meridien))-1)
            X=X_proj+X_0[0]
            Y=Y_proj+Y_0[0]

    




        if(option == options[1]):
            convergence_meridien =sin(fi_0[1])*(longitude-lambda_0)
            U_0 =log(tan(pi/4+fi_0[1]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[1]))/(1-sqrt(e_carre)*sin(fi_0[1])))
            U_barre =U-U_0
            N_0 =a/sqrt(1-e_carre*pow(sin(fi_0[1]),2))
            ro_0 =k_0[1]*N_0*(1/tan(fi_0[1]))
            X_proj =ro_0*exp(-U_barre*sin(fi_0[1]))*sin(convergence_meridien)
            Y_proj = -ro_0*(exp(-(U_barre*sin(fi_0[1])))*(cos(convergence_meridien))-1)
            X=X_proj+X_0[1]
            Y=Y_proj+Y_0[1]




        if(option == options[2]):
            convergence_meridien =sin(fi_0[2])*(longitude-lambda_0)
            U_0 =log(tan(pi/4+fi_0[2]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[2]))/(1-sqrt(e_carre)*sin(fi_0[2])))
            U_barre =U-U_0
            N_0 =a/sqrt(1-e_carre*pow(sin(fi_0[2]),2))
            ro_0 =k_0[2]*N_0*(1/tan(fi_0[2]))
            X_proj =ro_0*exp(-U_barre*sin(fi_0[2]))*sin(convergence_meridien)
            Y_proj = -ro_0*(exp(-(U_barre*sin(fi_0[2])))*(cos(convergence_meridien))-1)
            X=X_proj+X_0[2]
            Y=Y_proj+Y_0[2]
            



        if(option == options[3]):
            convergence_meridien =sin(fi_0[3])*(longitude-lambda_0)
            U_0 =log(tan(pi/4+fi_0[3]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[3]))/(1-sqrt(e_carre)*sin(fi_0[3])))
            U_barre =U-U_0
            N_0 =a/sqrt(1-e_carre*pow(sin(fi_0[3]),2))
            ro_0 =k_0[3]*N_0*(1/tan(fi_0[3]))
            X_proj =ro_0*exp(-U_barre*sin(fi_0[3]))*sin(convergence_meridien)
            Y_proj = -ro_0*(exp(-(U_barre*sin(fi_0[3])))*(cos(convergence_meridien))-1)
            X=X_proj+X_0[3]
            Y=Y_proj+Y_0[3]

        return X ,Y







    def calculer_coord_geog(X,Y,option):
        options =["lambert 1","lambert 2","lambert 3","lambert 4"]      
        e_carre =0.0068034876
        a =6378249.2
        k_0 =[0.999625769, 0.999615596, 0.999616304,0.999616437]
        X_0 =[500000, 500000, 1200000,1500000]
        Y_0 =[300000,300000, 400000,400000]
        lambda_0 =-0.0942477796 # en radian
        fi_0 =[0.5811946409, 0.5183627878, 0.4555309348, 0.3926990817]# converti en radian
       
        if(option ==options[0]):
            X =X-500000
            Y =Y-300000
            ro_0 =k_0[0]*(1/tan(fi_0[0]))*(a/(sqrt(1-e_carre*pow(sin(fi_0[0]),2))))
            lamda_bar =(1/sin(fi_0[0]))*(atan(X/(ro_0-Y)))
            lamda =abs(lambda_0+lamda_bar)
            U_bar =(1/2*sin(fi_0[0]))*log(ro_0**2/(X**2+(ro_0-Y)**2))
            U_0 =log(tan(pi/4+fi_0[0]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[0]))/(1-sqrt(e_carre)*sin(fi_0[0])))
            U =abs(U_0+U_bar)
            #E_0 =(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[0]))/(1-sqrt(e_carre)*sin(fi_0[0])))
            #lat_1 =2*atan((exp(U+E_0)-1)/(exp(U+E_0)+1))
            E_0 =(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[0]))/(1-sqrt(e_carre)*sin(fi_0[0])))
            lat_1 =2*atan((exp(U+E_0)-1)/(exp(U+E_0)+1))
            for i in range(1000000000000000):
                E_i =(e_carre/2)*log((1+sqrt(e_carre)*sin(lat_1))/(1-sqrt(e_carre)*sin(lat_1)))
            
                lat_i=2*atan((exp(U+E_i)-1)/(exp(U+E_i)+1)) 
                
                if(abs(lat_1-lat_i)<=0.00000000000000001):
                    break
                lat_1=lat_i








        elif(option ==options[1]):
            X  =X- 500000
            Y =Y-300000
            ro_0 =k_0[1]*(1/tan(fi_0[1]))*(a/(sqrt(1-e_carre*pow(sin(fi_0[1]),2))))
            lamda_bar =(1/sin(fi_0[1]))*(atan(X/(ro_0-Y)))
            lamda =abs(lambda_0+lamda_bar)
            U_bar =(1/2*sin(fi_0[1]))*log(ro_0**2/(X**2+(ro_0-Y)**2))
            U_0 =log(tan(pi/4+fi_0[1]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[1]))/(1-sqrt(e_carre)*sin(fi_0[1])))
            U =abs(U_0+U_bar)
            E_0 =(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[1]))/(1-sqrt(e_carre)*sin(fi_0[1])))
            lat_1 =2*atan((exp(U+E_0)-1)/(exp(U+E_0)+1))


            for i in range(10000000):
                E_i =(e_carre/2)*log((1+sqrt(e_carre)*sin(lat_1))/(1-sqrt(e_carre)*sin(lat_1)))
                lat_i=2* atan((exp(U+E_i)-1)/(exp(U+E_i)+1))
                
                if(abs(lat_1-lat_i)<=0.0000001):
                    break
                lat_1=lat_i



        elif(option ==options[2]):

            X =X-1200000
            Y =Y- 400000
            ro_0 =k_0[2]*(1/tan(fi_0[2]))*(a/(sqrt(1-e_carre*pow(sin(fi_0[2]),2))))
            lamda_bar =(1/sin(fi_0[2]))*(atan(X/(ro_0-Y)))
            lamda =abs(lambda_0+lamda_bar)
            U_bar =(1/2*sin(fi_0[2]))*log(ro_0**2/(X**2+(ro_0-Y)**2))
            U_0 =log(tan(pi/4+fi_0[2]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[2]))/(1-sqrt(e_carre)*sin(fi_0[2])))
            U =abs(U_0+U_bar)
            E_0 =(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[2]))/(1-sqrt(e_carre)*sin(fi_0[2])))
            lat_1 =2*atan((exp(U+E_0)-1)/(exp(U+E_0)+1))


            for i in range(100000000000000000):
                E_i =(e_carre/2)*log((1+sqrt(e_carre)*sin(lat_1))/(1-sqrt(e_carre)*sin(lat_1)))
                lat_i=2* atan((exp(U+E_i)-1)/(exp(U+E_i)+1))
                
                if(abs(lat_1-lat_i)<=0.0000000000001):
                    break
                lat_1=lat_i



        elif(option ==options[3]):
            X=X-1500000
            Y =Y-400000
            ro_0 =k_0[3]*(1/tan(fi_0[3]))*(a/(sqrt(1-e_carre*pow(sin(fi_0[3]),2))))
            lamda_bar =(1/sin(fi_0[3]))*(atan(X/(ro_0-Y)))
            lamda =abs(lambda_0+lamda_bar)
            U_bar =(1/2*sin(fi_0[3]))*log(ro_0**2/(X**2+(ro_0-Y)**2))
            U_0 =log(tan(pi/4+fi_0[3]/2))-(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[3]))/(1-sqrt(e_carre)*sin(fi_0[3])))
            U =abs(U_0+U_bar)


            E_0 =(e_carre/2)*log((1+sqrt(e_carre)*sin(fi_0[3]))/(1-sqrt(e_carre)*sin(fi_0[3])))
            lat_1 =2*atan((exp(U+E_0)-1)/(exp(U+E_0)+1))


            for i in range(10000000000000000):
                E_i =(e_carre/2)*log((1+sqrt(e_carre)*sin(lat_1))/(1-sqrt(e_carre)*sin(lat_1)))
                lat_i=2* atan((exp(U+E_i)-1)/(exp(U+E_i)+1))
                
                if(abs(lat_1-lat_i)<=0.000000000001):
                    break
                lat_1=lat_i




        lat_i =lat_i*180/pi
        lamda =lamda*180/pi
        latitude_en_degre =int(lat_i)
        min =(lat_i - latitude_en_degre)*60
        latitude_en_minute =int(min)
        latitude_en_seconde =(min -latitude_en_minute)*60

        latitud =str(latitude_en_degre) +" °  " +str(latitude_en_minute)+" '  "+str(latitude_en_seconde)+" '' "+ "  N"

        
        longitude_en_degre =int(lamda)
        lg_min =(lamda - longitude_en_degre)*60
        longitude_en_minute =int(lg_min)
        longitude_en_seconde =(lg_min -longitude_en_minute)*60

        longitud =str(longitude_en_degre )+" °  " +str(longitude_en_minute)+" '  "+str(longitude_en_seconde)+" '' "+ "  W"

        return latitud, longitud

















    def calculate_rayouns_courbure(e_carre, choice,   latitude_deg, latitude_min,latitude_sec,a):
        
        
    
        fi=(latitude_deg)+(latitude_min/60)+(latitude_sec/3600)# convertir la latitude en degré
        lat =(fi*pi)/180 #convertir la latitude en radian
        if(choice =='N'):
            M= (a*(1-e_carre))/(pow((1-(e_carre)*(sin(lat)**2)),1.5)) #Rayon de courbure du Méridien
            N= a/(sqrt(1-(e_carre)*(sin(lat)**2)))#  Rayon de courbure du premier vartical
            return(M,N)
        else:
            lat = -lat
                       
            M= (a*(1-e_carre))/(pow((1-(e_carre)*(sin(lat)**2)),1.5)) #Rayon de courbure du Méridien
            N= a/(sqrt(1-(e_carre)*(sin(lat)**2)))#  Rayon de courbure du premier vartical
            return(M,N)
        


    def calculate_latitude_isométrique( e_carre,    latitude_deg,latitude_min, latitude_sec):
 

      
        fi=latitude_deg+(latitude_min/60)+(latitude_sec/3600)
        lat =(fi*pi)/180

        U =log(tan((pi/4)+(lat/2)))-(e_carre/2)*log((1+sin(lat)*sqrt(e_carre))/(1-sin(lat)*sqrt(e_carre)))
        return U





    def calculate_latitude( U, e_carre):
        

        fi_0=0

        for i in range(10000000000000000000):
            E =(e_carre/2)*(log((1+sqrt(e_carre)*sin(fi_0))/(1-sqrt(e_carre)*sin(fi_0))))       
        
            fi_i =2*atan((exp(U+E)-1)/(exp(U+E)+1))
            if(abs(fi_0-fi_i)<0.0000000000001):
                break
            fi_0=fi_i

        fi_i =fi_i*180/pi

        latitude_en_degre =int(fi_i)
        min =(fi_i - latitude_en_degre)*60
        latitude_en_minute =int(min)
        latitude_en_seconde =(min -latitude_en_minute)*60

        latitud =str(latitude_en_degre) +" °  " +str(latitude_en_minute)+" '  "+str(latitude_en_seconde)+" '' "
        
        return latitud


   
    def calculate_arc_meridien(fi_1,fi_2,a,e_carre, M1, M2):

        M_moy =(M1+M2)/2
        delta_fi =fi_2 -fi_1
        fi_moy =(fi_1 +fi_2)/2
        if(delta_fi <=5 and delta_fi >2):

            S=(((M1+M2+M_moy)*delta_fi)/6)+ (a*e_carre*((delta_fi)**5)*cos(2*fi_moy))/240
            return S
        elif(delta_fi <=2):
            S = (M_moy * delta_fi)+((a*e_carre*cos(2*fi_moy)*(delta_fi)**3)/8)
            return S
        else:
                       
   
            e4 = e_carre*e_carre 
            e6 = e4*e_carre 
            e8 = e6*e_carre 
            e10 = e8*e_carre
            
            
            A = 1+(3/4)*e_carre+(45/64)*e4+(175/256)*e6+(11025/16384)*e8+(43659/65536)*e10 
            B = (3/4)*e_carre+(15/16)*e4+(525/512)*e6+(2205/2048)*e8+(72765/65536)*e10
            C = (15/64)*e4+(105/256)*e6+(2205/4096)*e8+(10395/16384)*e10 
            D = (35/512)*e6+(315/2048)*e8+(31185/131072)*e10 
            E = (315/16384)*e8+(3465/65536)*e10 
            F = (693/131072)*e10 

            term_fi1 =A*fi_1 -(B/2)*sin(2*fi_1)+ (C/4)*sin(4*fi_1) - (D/6)*sin(6*fi_1) +(E/8)*sin(8*fi_1) -(F/10)*sin(10*fi_1)
            term_fi2 =A*fi_2 -(B/2)*sin(2*fi_2)+ (C/4)*sin(4*fi_2) - (D/6)*sin(6*fi_2) +(E/8)*sin(8*fi_2) -(F/10)*sin(10*fi_2)            
            S = a*(1-e_carre)*(term_fi2 - term_fi1)

            return S



    def calculate_arc_parallele(landa1, landa2, N,fi):
        landa1 =radians(landa1)
        landa2 =radians(landa2)
        fi = radians(fi)
        s=N *cos(fi)*(landa2-landa1)
        return s






 

    def calculate_surface(b, fi_1, fi2, landa1, landa2, e_carre):
       # S = b**2 *((landa2 - landa1)/2)*((1/sqrt(e_carre)*2)*(log((1+sqrt(e_carre)*sin(fi2))/(1-sqrt(e_carre)*sin(fi2)))*(sin(fi2)/1-e_carre*sin(fi2)**2))-log((1+sqrt(e_carre)*sin(fi_1))/(1-sqrt(e_carre)*sin(fi_1)))*(sin(fi_1)/1-e_carre*sin(fi_1)**2))
        S = b**2 * ((landa2 - landa1)/2) * ((1/sqrt(e_carre)*2) * (log((1 + sqrt(e_carre)*sin(fi2))/(1 - sqrt(e_carre)*sin(fi2))) * (sin(fi2)/(1 - e_carre*sin(fi2)**2))- log((1 + sqrt(e_carre)*sin(fi_1))/(1 - sqrt(e_carre)*sin(fi_1))) * (sin(fi_1)/(1 - e_carre*sin(fi_1)**2))))

        return S


    def calculate_latitudes(a, b, angle, option):
        options = ["Latitude Géodésique", "Latitude Géocentrique", "Latitude Réduite"]
        
        if option == options[0]:
            beta = atan((a / b) * tan(radians(angle)))
            psi = atan((b**2 / a**2) * tan(radians(angle)))
            return degrees(psi), degrees(beta)
        
        elif option == options[1]:
            beta = atan((a / b) * tan(radians(angle)))
            phi = atan((b**2 / a**2) * tan(radians(angle)))
            return degrees(beta), degrees(phi)
        
        else:
            phi = atan((a / b) * tan(radians(angle)))
            psi = atan((b / a) * tan(radians(angle)))
            return degrees(psi), degrees(phi)



  



    def tracer_directions_latitudes(a, b, phi, psi, beta):
        phi = np.deg2rad(phi)
        psi = np.deg2rad(psi)
        beta = np.deg2rad(beta)
        fig, ax = plt.subplots()
        cercle = plt.Circle((0, 0), a, color='red', fill=False, linestyle='dashed', label='Cercle équatorial')
        ax.add_patch(cercle)

        ellipse = Ellipse((0, 0), 2 * a, 2 * b, angle=np.rad2deg(phi), color='blue', fill=False, label='Ellipse tangente')
        ax.add_patch(ellipse)

        
        angle_geocentric = psi
        x_geocentric_line = np.array([np.cos(angle_geocentric), 0]) * a
        y_geocentric_line = np.array([np.sin(angle_geocentric), 0]) * b
        ax.plot(x_geocentric_line, y_geocentric_line, color='purple', linestyle='dotted', label='Latitude géocentrique')

        angle_normal = phi
        x_normal_line = np.array([np.cos(angle_normal), 0]) * a
        y_normal_line = np.array([np.sin(angle_normal), 0]) * b
        ax.plot(x_normal_line, y_normal_line, color='green', linestyle='dashed', label='Latitude géodésique')

        
        angle_parametric = beta
        x_parametric_line = np.array([np.cos(angle_parametric), 0]) * a
        y_parametric_line = np.array([np.sin(angle_parametric), 0]) * b
        ax.plot(x_parametric_line, y_parametric_line, color='cyan', linestyle='dotted', label='Latitude paramétrique')


        plt.plot(np.linspace(-a, a, 100), np.zeros(100), label='plan de l equateur', color='red')

        ax.set_aspect('equal', 'box')
        ax.set_xlim([-a, a])
        ax.set_ylim([-a * 1.5, a * 1.5])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        


        ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

        plt.show()











    def rad_to_deg_dms(alpha):
        # Conversion en degrés
        angle_in_degrees = alpha * (180/pi)

        # Conversion en DMS
        degrees = int(angle_in_degrees)
        minutes_float = (angle_in_degrees - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60

        return degrees, minutes, seconds


    def dms_to_rad_and_deg(degrees, minutes, seconds):
        # Conversion en degrés décimaux
        angle_in_degrees = degrees + minutes/60 + seconds/3600

        # Conversion en radians
        angle_in_radians = radians(angle_in_degrees)

        return angle_in_radians, angle_in_degrees


    def deg_to_rad_and_dms(degrees):
        # Conversion en radians
        angle_in_radians = radians(degrees)

        # Conversion en DMS
        degrees_int = int(degrees)
        minutes_float = (degrees - degrees_int) * 60
        minutes_int = int(minutes_float)
        seconds = (minutes_float - minutes_int) * 60

        return angle_in_radians, degrees_int, minutes_int, seconds




    def gauss_legendre_direct(fi1, landa1, dist, az_dep):
        fi1 = radians(fi1)
        landa1 = radians(landa1)
        dist = radians(dist)
        az_dep = radians(az_dep)
      
        fi2 = asin(sin(fi1) * cos(dist) + cos(fi1) * sin(dist) * cos(az_dep))
       # landa2 = landa1 + pi/2 - atan((1 / sin(dist)) * ((sin((pi/2)- fi1) / tan(dist)) - cos((pi/2) - fi1) * cos(az_dep)))
        landa2 = landa1+ pi/2 - atan(1 / sin(dist) * (sin(pi/2 - fi1) / tan(dist) - cos(pi/2 - fi1) * cos(az_dep)))
        #landa2 = landa1 + pi/2 - atan((1 / sin(dist)) * ((sin(pi/2 - fi1) / tan(dist)) - cos(pi/2 - fi1) * cos(az_dep)))
        az_retour =( pi/2- atan((1/sin(az_dep)) *(cos(az_dep)*cos(dist) - tan(fi1)*sin(dist))))+pi

        return degrees(fi2),degrees(landa2) , degrees(az_retour)




    



    def gauss_legendre_inverse(phi1, phi2, landa1, landa2):
        delta_lambda = landa2-landa1
        phi1, phi2, delta_lambda = radians(phi1), radians(phi2), radians(delta_lambda)

        sigma_12 = acos(sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(delta_lambda))


       
        cot_A12 = tan(phi2) * cos(phi1) / sin(delta_lambda) - sin(phi1) / tan(delta_lambda)
        A12_rad = atan(1 / cot_A12)

  
        A12_deg = degrees(A12_rad)

      
        cot_A21 = -tan(phi1) * cos(phi2) / sin(delta_lambda) + sin(phi2) / tan(delta_lambda)
        A21_rad = atan(1 / cot_A21)+pi

      

        return sigma_12, A12_deg, degrees(A21_rad)











    def Puissant_direct(fi1,  landa1,az_dep,dist,e_carre, M1, N1, a):
        fi1 = radians(fi1)
        landa1 = radians(landa1)
        dist = radians(dist)
        az_dep = radians(az_dep)


        B =1/M1
        C = (3/2)*((e_carre *sin(fi1)*cos(fi1))/(1-e_carre*(sin(fi1))**2))
        D =tan(fi1)/(2 *M1*N1)
        E =(1+3*(tan(fi1)**2))/6*(N1**2)
        h =(dist/M1)*cos(az_dep)
        #delta_fi_prime = ((dist/N1)*cos(az_dep)-(dist**2/2*(N1**2))*tan(fi1)*(sin(az_dep)**2)-(dist**3/6*(N1**3))*cos(az_dep)*(sin(az_dep)**2)*(1+3*(tan(fi1)**2)))
        delta_fi_prime = ((dist/N1)*cos(az_dep) - (dist**2/(2*N1**2))*tan(fi1)*(sin(az_dep)**2) - (dist**3/(6*N1**3))*cos(az_dep)*(sin(az_dep)**2)*(1+3*(tan(fi1)**2)))



        fi2 = fi1 + dist*cos(az_dep)*B -(dist**2) *(sin(az_dep)**2)*D -h*(dist**2) *E *(sin(az_dep)**2)-C *(( (N1/M1)*delta_fi_prime)**2)
        N2 =(a/(pow(1-e_carre*(sin(fi2)**2), 1/2)))
        delta_lambda =( ((dist/N2) * sin(az_dep))/cos(fi2)) * (1-((dist**2)/6*(N2**2))*(1-(sin(az_dep)**2))/(cos(fi2)**2))

        landa_2 = landa1 + delta_lambda
        delta_alpha_sur2 =pi/2 - atan((cos((fi2 -fi1)/2 )/sin((fi1+fi2)/2))* (1/tan((landa_2 -landa1)/2)))
        if(az_dep >180):
            az_retour =az_dep+pi+2*delta_alpha_sur2
        else:
            az_retour =az_dep-pi+2*delta_alpha_sur2            
        return degrees(fi2),degrees(landa_2),degrees(az_retour)




 






    def gauss_midlatitude(S, landa1,az_dep, fi1, N1, M1):
        fi1 =radians(fi1)
        landa1 =radians(landa1)
        az_dep =radians(az_dep)
        S =radians(S)
        max_iterations=100
        tolerance=1e-9
        delta_Az = 0
        Nm = N1
        fi_moy = fi1
        delta_fi = 0
        delta_landa = S * sin(az_dep) / N1 * cos(fi1)
        delta_half = atan(tan(delta_landa / 2) * sin(fi1) / cos(delta_fi / 2))

        for _ in range(max_iterations):
            delta_Az = 2 * atan(tan(delta_landa / 2) * sin(fi_moy) / cos(delta_fi / 2))
            delta_fi = S * cos(az_dep + delta_Az / 2) / (M1 * cos(delta_landa / 2))
            delta_landa = S * sin(az_dep + delta_Az / 2) / (Nm * cos(fi_moy))

            if abs(delta_Az - delta_half) < tolerance and abs(delta_fi) < tolerance and abs(delta_landa) < tolerance:
                break

            delta_half = delta_Az / 2
            fi_moy = fi1 + delta_fi / 2

        return degrees(fi1 + delta_fi), degrees(az_dep + delta_Az+pi), degrees(landa1+delta_landa)




    def inverse_gauss_midlatitude(landa1, landa2, phi1, phi2, N1, M1, N2, M2):
        fi_moy = (phi1 + phi2) / 2
        delta_phi = (phi2 - phi1) / 2
        N_moy = (N1 + N2) / 2
        M_moy = (M1 + M2) / 2
        delta_alpha_sur2 = atan(tan((landa2 - landa1) / 2) * (sin(fi_moy) / cos(delta_phi)))
        alpha12 = atan((cos(fi_moy) / sin(2*delta_phi * M_moy / (2 * N_moy))) * tan((landa2 - landa1) / 2)) - delta_alpha_sur2


        alpha21 =( 2 * delta_alpha_sur2 + alpha12+pi )


        S = ( N_moy * cos(fi_moy) * (landa2 - landa1) ) / sin(delta_alpha_sur2+alpha12)
        return S, degrees(alpha12), degrees(alpha21)          