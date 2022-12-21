# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


myPathLog = "/Users/brossathugo/Desktop/DATALAKE/"
myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"


###############################################################################
###############################################################################

#==============================================================================
#-- Parcourir un dossier et stocker les noms de fichiers dans une liste
#==============================================================================
#-- Import des bibliotheque
import sys, os, fnmatch

#-- Initialisation des variable
myListOfFile = []
myListOfFileTmp = []

myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"

#-- Recupere les noms longs  des fichiers dans le path
myListOfFileTmp = os.listdir(myPathHtml)



#-- Filtrer les fichiers concernés : Linkedin
myPattern = "*INFO-EMP*"

#-- Parcour de tous les fichiers trouvés
for myEntry in myListOfFileTmp :  
    #-- On n'ajoute que les fichiers concernés
    if fnmatch.fnmatch(myEntry, myPattern)==True:
        myListOfFile.append(myEntry)

print(len(myListOfFileTmp))
#-- Affichage du résultat
for i in myListOfFile : print("Ligne : " + i)

print(len(myListOfFile))
for myFileName in myListOfFile: print(myPathHtml + " --> " + str(myFileName))


#-- Initialisation des colonnes du fichier de métadonnées
myFilePathName = myPathLog + "1_LANDING_ZONE/metadata.csv"

myFilePtr = open(myFilePathName, "a", encoding = "utf-8")

myListeDeLigneAEcrire = [] 
myListeDeLigneAEcrire.append('"cle_unique";"colonne";"valeur"')

for myLigneAEcrire in myListeDeLigneAEcrire:
    myFilePtr.write(myLigneAEcrire+"\n")
    
myFilePtr.close()


#==============================================================================
#-- Fonction renvoyant <datetime_ingestion> du fichier
#==============================================================================
from datetime import datetime
def Get_datetime_ingestion_AVI():
    Result = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return(Result)
    
print(Get_datetime_ingestion_AVI())



#==============================================================================
#-- Fonction renvoyant <approximate_size> du fichier
#============================================================================== 

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))





###############################################################################
#==============================================================================
#-- Copier des fichier d'une répertoir dans un autre en prenant les metadonnées
#==============================================================================
import shutil

for i in myListOfFile: print(i)

myPathHtmlIn = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"
myPathHtmlOut = "/Users/brossathugo/Desktop/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/"


#--------------
for monNomDeFichier in myListOfFile:
    print("Traitement :du fichier :", monNomDeFichier)
    monPathFile_Test_IN = myPathHtmlIn + "/" + monNomDeFichier
    monPathFile_Test_OUT = myPathHtmlOut + "/" + monNomDeFichier
    print(monPathFile_Test_IN)
    print(monPathFile_Test_OUT)
    shutil.copy(monPathFile_Test_IN, monPathFile_Test_OUT)
    
    metadata = os.stat(myPathHtml + monNomDeFichier)
    myFilePtr = open(myFilePathName, "a", encoding = "utf-8")
    
    myListeDeLigneAEcrire = []
    #enregistrement en clé valeur !

    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';datetime;'+Get_datetime_ingestion_AVI())
    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';taille;'+approximate_size(metadata.st_size))
    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';emplacement_source;'+myPathHtml)

    for myLigneAEcrire in myListeDeLigneAEcrire:
        myFilePtr.write(myLigneAEcrire+"\n")
   
    myFilePtr.close()



###############################################################################



#-- Initialisation des variable
myListOfFile = []
myListOfFileTmp = []

myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"

#-- Recupere les noms longs  des fichiers dans le path
myListOfFileTmp = os.listdir(myPathHtml)

#-- Filtrer les fichiers concernés : Avis des société Glassdoor
myPattern = "*AVIS-SOC*"

#-- Parcour de tous les fichiers trouvés
for myEntry in myListOfFileTmp :  
    #-- On n'ajoute que les fichiers concernés
    if fnmatch.fnmatch(myEntry, myPattern)==True:
        myListOfFile.append(myEntry)

for myFileName in myListOfFile: print(myPathHtml + " --> " + str(myFileName))
        

myPathHtmlOut = "/Users/brossathugo/Desktop/DATALAKE/1_LANDING_ZONE/GLASSDOOR/AVI/"

#--------------
for monNomDeFichier in myListOfFile:
    print("Traitement :du fichier :", monNomDeFichier)
    monPathFile_Test_IN = myPathHtmlIn + "/" + monNomDeFichier
    monPathFile_Test_OUT = myPathHtmlOut + "/" + monNomDeFichier
    print(monPathFile_Test_IN)
    print(monPathFile_Test_OUT)
    shutil.copy(monPathFile_Test_IN, monPathFile_Test_OUT)
    
    metadata = os.stat(myPathHtml + monNomDeFichier)
    myFilePtr = open(myFilePathName, "a", encoding = "utf-8")
    
    myListeDeLigneAEcrire = []
    #enregistrement en clé valeur !

    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';datetime;'+Get_datetime_ingestion_AVI())
    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';taille;'+approximate_size(metadata.st_size))
    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';emplacement_source;'+myPathHtml)

    for myLigneAEcrire in myListeDeLigneAEcrire:
        myFilePtr.write(myLigneAEcrire+"\n")
   
    myFilePtr.close()
    
    
    
###############################################################################


#-- Initialisation des variable
myListOfFile = []
myListOfFileTmp = []

myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"

#-- Recupere les noms longs  des fichiers dans le path
myListOfFileTmp = os.listdir(myPathHtml)

#-- Filtrer les fichiers concernés : Info des sociétés Glassdoor
myPattern = "*INFO-SOC*"

#-- Parcour de tous les fichiers trouvés
for myEntry in myListOfFileTmp :  
    #-- On n'ajoute que les fichiers concernés
    if fnmatch.fnmatch(myEntry, myPattern)==True:
        myListOfFile.append(myEntry)

for myFileName in myListOfFile: print(myPathHtml + " --> " + str(myFileName))
        

myPathHtmlOut = "/Users/brossathugo/Desktop/DATALAKE/1_LANDING_ZONE/GLASSDOOR/INFO/"



import os, csv

#--------------
for monNomDeFichier in myListOfFile:
    print("Traitement :du fichier :", monNomDeFichier)
    monPathFile_Test_IN = myPathHtmlIn + "/" + monNomDeFichier
    monPathFile_Test_OUT = myPathHtmlOut + "/" + monNomDeFichier
    print(monPathFile_Test_IN)
    print(monPathFile_Test_OUT)
    shutil.copy(monPathFile_Test_IN, monPathFile_Test_OUT)
    
    metadata = os.stat(myPathHtml + monNomDeFichier)
    myFilePtr = open(myFilePathName, "a", encoding = "utf-8")
    
    myListeDeLigneAEcrire = []
    #enregistrement en clé valeur !

    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';datetime;'+Get_datetime_ingestion_AVI())
    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';taille;'+approximate_size(metadata.st_size))
    myListeDeLigneAEcrire.append(monNomDeFichier[:14]+';emplacement_source;'+myPathHtml)

    for myLigneAEcrire in myListeDeLigneAEcrire:
        myFilePtr.write(myLigneAEcrire+"\n")
   
    myFilePtr.close()





############################################################################### 
#
#Exemple : GLASSDOOR (extraction INFOS et AVIS SUR ENTREPRISE)
#
###############################################################################
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
#-----------------------------------------------------------------------------
#-- 1er CAS : Ouverture d'un fichier HTML sur le disque dur
#-----------------------------------------------------------------------------
#myHTMLPathFileName = "C:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/SOC/13790-INFO-SOC-GLASSDOOR-E9028_P1.html"

#!!!!RQ-EKL: Utiliser le slash "/" et pas le backslash "\" pour le path avec beautifullsoup
myHTMLPathFileName = myPathHtml + "13550-INFO-SOC-GLASSDOOR-E10686_P1.html"

f = open(myHTMLPathFileName, "r", encoding="utf8")
myHTMLContents = f.read()
f.close()

print(myHTMLContents)

#-----------------------------------------------------------------------------
#-- 2eme CAS : Ouverture d'un flux HTML sur le Web 
#-----------------------------------------------------------------------------
#import requests
#myURL = "https://www.glassdoor.fr/Pr%C3%A9sentation/Travailler-chez-Atos-EI_IE10686.16,20.html"
#myHeaders = {'User-Agent': 'Mozilla/5.0'}
#myResponse = requests.get(str(myURL), headers=myHeaders)
#myHTMLContents = myResponse.text

#-----------------------------------------------------------------------------
#-- Commun aux 1er et 2eme CAS -  HTML File et URL
#-----------------------------------------------------------------------------
mySoup = BeautifulSoup(myHTMLContents, 'lxml')
print(mySoup.h2)
print(mySoup.head)
print(mySoup.li)  
print(mySoup.prettify())








#-------------------------------------------------------------------------------------------
##-- Création des fonctions permettant la récupération d'informations dans les fichiers html
#-------------------------------------------------------------------------------------------

#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le nom de l'entreprise
#==============================================================================
import re
def Get_nom_entreprise_SOC(Soup):
    myTest = []
    try: myTest = Soup.find_all('h1', attrs = {"strong tightAll"})[0]
    except : print ("Pas le nom de l'entreprise sur cette page html" + myFileName)#pour ne pas arreter le script si une info est pas trouvée dans un fichier

    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class="strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la ville de l'entreprise
#==============================================================================

def Get_ville_entreprise_SOC(Soup):
    myTest = []
    try : myTest = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[1].span.contents[0])
    except : print ("Pas la ville de l'entreprise sur cette page html"+ myFileName)
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la taille de l'entreprise
#==============================================================================

def Get_taille_entreprise_SOC(Soup):
    myTest = []
    try :myTest = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[2].span.contents[0])
    except : print ("Pas la taille de l'entreprise sur cette page html"+ myFileName)
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la description de l'entreprise 
#==============================================================================

def Get_description_entreprise_SOC(Soup):
#    myTest = str(mySoup.find_all('div', attrs = {'class':"infoEntity"})[1].span.contents[0])
    myTest = str(Soup.find_all('div', attrs = {'id':"EmpBasicInfo"}))
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Soup2 = Soup(myTest, 'lxml')
        myTxtTmp = str(Soup2.find_all('div', attrs = {'class':""})[2])
        myTxtTmp1 = re.sub(r'(.*)data-full="(.*).<br/>(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


#==============================================================================
#-- GLASSDOOR (AVIS) : Fonction renvoyant <datetime_ingestion>
#==============================================================================
from datetime import datetime
def Get_datetime_ingestion_AVI():
    Result = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return(Result)
    

#==============================================================================
#-- GLASSDOOR (AVIS) : Fonction renvoyant <nom_entreprise>
#==============================================================================
def Get_nom_entreprise_AVI (Soup):
    myTest = []
    try: myTest = Soup.find_all('div', attrs = {"class":"header cell info"})[0].span.contents[0]
    except : print ("Pas le nom de l'entreprise sur cette page html"+ myFileName)
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = myTest
    return(Result)


#==============================================================================
#-- GLASSDOOR (AVIS) : Fonction renvoyant <Note_moy_entreprise>
#==============================================================================
def Get_note_moy_entreprise_AVI(Soup):
    myTest = []
    try : myTest = Soup.find_all('div', attrs = {'class':'v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large'})[0].contents[0]
    except : print ("Pas de note pour cette sur cette page html: "+ myFileName) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = myTest  
    return(Result)


#==============================================================================
#-- LINKEDIN (EMPLOI) : Libellé de l'offre
#==============================================================================
def Get_libelle_emploi_EMP(Soup):
    myTest = Soup.find_all('h1', attrs = {'class':'topcard__title'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)


#==============================================================================
#-- LINKEDIN (EMPLOI) : Nom de la Société demandeuse
#==============================================================================
def Get_nom_entreprise_EMP(Soup):
    myTest = Soup.find_all('span', attrs = {'class':'topcard__flavor'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)


#==============================================================================
#-- LINKEDIN (EMPLOI) : Ville de l'emploi proposé
#==============================================================================
def Get_ville_emploi_EMP (Soup):
    myTest = Soup.find_all('span', attrs = {'class':'topcard__flavor topcard__flavor--bullet'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)

#==============================================================================
#-- LINKEDIN (EMPLOI) : Texte de l'offre d'emploi
#==============================================================================
def Get_texte_emploi_EMP (Soup):
    myTest = Soup.find_all('div', attrs = {"description__text description__text--rich"})
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)


#---------------------------------------------------------------------------------
#-- Récuperation des informations sur les emplois Linkedin et création fichier csv
#----------------------------------------------------------------------------------

##-- Chargement de ma liste de fichiers pour avoir les fichiers "Linkedin"

myListOfFile = []
myListOfFileTmp = []

#-- Path ou l'on souhaite mettre notre fichier csv
myPathLog = "/Users/brossathugo/Desktop/DATALAKE/2_CURATED_ZONE/LINKEDIN/EMP/"


#-- Path ou l'on va chercher nos fichiers html
myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"

#-- Recupere les noms longs  des fichiers dans le path
myListOfFileTmp = os.listdir(myPathHtml)

#-- Filtrer les fichiers concernés 
myPattern = "*LINKEDIN*"

#-- Parcours de tous les fichiers trouvés
for myEntry in myListOfFileTmp :  
    #-- On n'ajoute que les fichiers concernés
    if fnmatch.fnmatch(myEntry, myPattern)==True:
        myListOfFile.append(myEntry)


#-- 1er CAS : Ouverture d'un fichier HTML sur le disque dur

myFilePathName = myPathLog + "Linkedin.csv"

#-- Ouverture du fichier en création (raz)
#------------------------------------------------------------------------------
myFilePtr = open(myFilePathName, "w", encoding = "utf-8")

#-- Ouverture du fichier en ajout (modification)
#------------------------------------------------------------------------------
myFilePtr = open(myFilePathName, "a", encoding = "utf-8")

ListLinkedin = [] 

ListLinkedin.append('"Clé";"colonne";"valeur"')


#-- Boucle permettant de récupérer le poste, le nom de l'entreprise, la ville et la description
for myFileName in myListOfFile:
  myHTMLPathFileName = myPathHtml + myFileName
  myFilePtr = open(myFilePathName, "w", encoding = "utf-8")
  f = open(myHTMLPathFileName, "r", encoding="utf-8", errors='ignore')
  myHTMLContents = f.read()
  f.close()
  
  mySoup = BeautifulSoup(myHTMLContents, 'lxml')
  
  ListLinkedin.append(myFileName[:14]+';"nom_poste";' +Get_libelle_emploi_EMP(mySoup))
  ListLinkedin.append(myFileName[:14]+';"nom_entreprise";' +Get_nom_entreprise_EMP(mySoup))
  ListLinkedin.append(myFileName[:14]+';"ville";' +Get_ville_emploi_EMP(mySoup))
  ListLinkedin.append(myFileName[:14]+';"description";' +Get_texte_emploi_EMP(mySoup))


#-- Test1 : Boucle d'écriture de chaque ligne de la liste d'éléments dans le fichier 
for myLigneAEcrire in ListLinkedin:
    myFilePtr.write(myLigneAEcrire+"\n")
    
myFilePtr.close()


  
#---------------------------------------------------------
#-- Récuperation des avis Glassdoor et création fichier csv
#---------------------------------------------------------

##Changement de ma liste de fichiers pour avoir les fichiers "Avis Glassdoor"

myListOfFile = []
myListOfFileTmp = []

#-- Path ou l'on souhaite mettre notre fichier csv
myPathLog = "/Users/brossathugo/Desktop/DATALAKE/2_CURATED_ZONE/GLASSDOOR/AVI/"

#-- Path ou l'on va chercher nos fichiers html
myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"

#-- Recupere les noms longs  des fichiers dans le path
myListOfFileTmp = os.listdir(myPathHtml)

#-- Filtrer les fichiers concernés 
myPattern = "*AVI*"

#-- Parcour de tous les fichiers trouvés
for myEntry in myListOfFileTmp :  
    #-- On n'ajoute que les fichiers concernés
    if fnmatch.fnmatch(myEntry, myPattern)==True:
        myListOfFile.append(myEntry)


  #-- 1er CAS : Ouverture d'un fichier HTML sur le disque dur

    myFilePathName = myPathLog + "GlassdoorDetailAvis.csv"

  #-- Ouverture du fichier en création (raz)
  #------------------------------------------------------------------------------
    myFilePtr2 = open(myFilePathName, "w", encoding = "utf-8")

  #-- Ouverture du fichier en ajout (modification)
  #------------------------------------------------------------------------------
    myFilePtr2 = open(myFilePathName, "a", encoding = "utf-8")

    ListGlassdoorDetailAvis = [] 

    ListGlassdoorDetailAvis.append('"Clé";"colonne";"valeur"')
  
  #-- Boucle permettant de récupérer la date d'ingestion, le nom de l'entreprise et la note moyenne par entreprise

for myFileName in myListOfFile:
    myHTMLPathFileName = myPathHtml + myFileName
    myFilePtr2 = open(myFilePathName, "w", encoding = "utf-8")
    f = open(myHTMLPathFileName, "r", encoding="utf-8", errors='ignore')
    myHTMLContents = f.read()
    f.close()
    
    mySoup = BeautifulSoup(myHTMLContents, 'lxml')
    
    #-- utilisation des fonctions qui récupèrent le nom et la note moyenne de l'entreprise
    ListGlassdoorDetailAvis.append(myFileName[:14]+';"date ingestion";' +Get_datetime_ingestion_AVI())
    ListGlassdoorDetailAvis.append(myFileName[:14]+';"nom_entreprise";' +Get_nom_entreprise_AVI(mySoup))
    ListGlassdoorDetailAvis.append(myFileName[:14]+';"note moyenne";' +(Get_note_moy_entreprise_AVI(mySoup)))
    
    
    
    myTest = mySoup.find_all('li', attrs = {'class':'empReview'})
    
    if (myTest == []) : 
        print("NULL")
    else:
        myListTab=[[]]
   
   
    
    
    #-- Boucle qui sert à récupérer le detail des avis par entreprise
    for x in range(0, len(myTest)) :
          
           #--------------------------------------------------------------------------
           #-- 0 - ID de l'avis (arbitraire) incremental
           #--------------------------------------------------------------------------
          ListGlassdoorDetailAvis.append(myFileName[:14]+';"numero_avis";' +str(x+1))
          try : soup2 = BeautifulSoup(str(myTest[x]), 'lxml')#quelques fichiers posaient probléme donc utilsation de try
          except : continue     
           #--------------------------------------------------------------------------
           #-- 1 - Employe actuel
           #--------------------------------------------------------------------------
          myTest2 = soup2.find_all('span', attrs = {'class':'authorJobTitle middle reviewer'})
          for i in range(0, len(myTest2)): 
              if (myTest2 == []) :        
                  ListGlassdoorDetailAvis.append(myFileName[:14]+';"type_employe";"NULL"')
              else :
                  txtclean = re.sub(r'<span (.*)">(.*)</span>(.*)', r'\2', str(myTest2[i]))
                  ListGlassdoorDetailAvis.append(myFileName[:14]+';"Type_employe";'+txtclean)
               #myListTab[x].append('"' + txtclean + '"')
       
           #--------------------------------------------------------------------------
           #-- 2 - Ville de l'employe 
           #--------------------------------------------------------------------------
          myTest2 = soup2.find_all('span', attrs = {'class':'authorLocation'}) 
          for i in range(0, len(myTest2)): 
               if (myTest2 == []) :
                   ListGlassdoorDetailAvis.append(myFileName[:14]+';"ville_employe";"NULL"')
               else :
                   txtclean = re.sub(r'<span (.*)">(.*)</span>(.*)', r'\2', str(myTest2[i]))
                   #print(txtclean)
                   ListGlassdoorDetailAvis.append(myFileName[:14]+';"ville_employe";'+txtclean)
       
           #--------------------------------------------------------------------------
           #-- 3 - Commentaire texte libre employe sur entreprise
           #--------------------------------------------------------------------------
          myTest2= soup2.find_all('p', attrs = {'class':'mainText mb-0'}) 
          for i in range(0, len(myTest2)): 
              if (myTest2 == []) :        
                  ListGlassdoorDetailAvis.append(myFileName[:14]+';"commentaire";"NULL"')
              else :
                  txtclean = myTest2[i].text
                 # print(txtclean)
                  ListGlassdoorDetailAvis.append(myFileName[:14]+';"commentaire";'+txtclean)
     
    
   
    
  #-- Boucle d'écriture de chaque ligne de la liste d'éléments dans le fichier 
for myLigneAEcrire in ListGlassdoorDetailAvis:
      myFilePtr2.write(myLigneAEcrire+"\n")
      
myFilePtr2.close()
   
#--------------------------------------------------------------------------------------
#-- Récuperation des informartions sur les entreprises Glassdoor et création fichier csv
#---------------------------------------------------------------------------------------

#-- Path ou l'on souhaite mettre notre fichier csv
myPathLog = "/Users/brossathugo/Desktop/DATALAKE/2_CURATED_ZONE/GLASSDOOR/SOC/"

#-- Path ou l'on va chercher nos fichiers html
myPathHtml = "/Users/brossathugo/Desktop/DATALAKE/0_SOURCE_WEB/"

##Changement de ma liste de fichiers pour prendre les fichiers "INFO Glassdoor"

myListOfFile = []
myListOfFileTmp = []

#-- Recupere les noms longs  des fichiers dans le path
myListOfFileTmp = os.listdir(myPathHtml)

#-- Filtrer les fichiers concernés 
myPattern = "*INFO-SOC-GLASSDOOR*"

#-- Parcour de tous les fichiers trouvés
for myEntry in myListOfFileTmp :  
    #-- On n'ajoute que les fichiers concernés
    if fnmatch.fnmatch(myEntry, myPattern)==True:
        myListOfFile.append(myEntry)


#-- 1er CAS : Ouverture d'un fichier HTML sur le disque dur

myFilePathName = myPathLog + "GlassdoorInfo.csv"

#-- Ouverture du fichier en création (raz)
#------------------------------------------------------------------------------
myFilePtr3 = open(myFilePathName, "w", encoding = "utf-8")

#-- Ouverture du fichier en ajout (modification)
#------------------------------------------------------------------------------
myFilePtr3 = open(myFilePathName, "a", encoding = "utf-8")

ListGlassdoorInfo = [] 

ListGlassdoorInfo.append('"Clé";"colonne";"valeur"')


for myFileName in myListOfFile:
  myHTMLPathFileName = myPathHtml + myFileName
  myFilePtr3 = open(myFilePathName, "w", encoding = "utf-8")
  f = open(myHTMLPathFileName, "r", encoding="utf-8", errors='ignore')
  myHTMLContents = f.read()
  f.close()
  mySoup = BeautifulSoup(myHTMLContents, 'lxml')

#Récupération des fonctions créés précedemment pour ajouter entreprise par entreprise les informations
  ListGlassdoorInfo.append(myFileName[:14]+';"ville";' +Get_ville_entreprise_SOC(mySoup))
  ListGlassdoorInfo.append(myFileName[:14]+';"nom_entreprise";' +Get_nom_entreprise_SOC(mySoup))
  ListGlassdoorInfo.append(myFileName[:14]+';"taille";' +Get_taille_entreprise_SOC(mySoup))
 

  
#-- Boucle d'écriture de chaque ligne de la liste d'éléments dans le fichier 
for myLigneAEcrire in ListGlassdoorInfo:
    myFilePtr3.write(myLigneAEcrire+"\n")

#-- Fermeture du fichier    
myFilePtr3.close()


