""" But : 
    - parcourir un fichier de log (Cassandra pour commencer) fourni en paramètre
    - compter les occurences de niveau d'erreur : INFO,WARN,ERROR, FATAL
    - afficher date de début et de fin  
    - grapher les données dans un histogramme simple : X = type, Y = nb d'erreur
    - résumer le tout dans un élégant bloc de texte. 
    - le tout en collant au PEP8 au plus près.
"""

"""Conventions :
naming variable = naming function = lowercase + underscore """

""" IMPORTS """
import sys    # pour récupérer le nom du fichier  
import os 
import re

""" VARIABLES """
file_2_parse = r"c:\Users\ldemontreuille\Downloads\DEV_PYTHON\wpya0254_server.log"
error_levels = ["INFO","WARN","ERROR","FATAL"] # liste des niveaux connus. Placeholder


""" FUNCTIONS """
def parse_file(file_2_parse):
    """Ouvre un fichier de log et compte des trucs"""
    nb_errors = nb_warnings = nb_infos = nb_fatals = nb_lines = 0 # tous les compteurs à zéro
    with open(file_2_parse,"r") as fh:                                # file handler 
        for line in fh:
            nb_lines += 1
            if ("INFO" in line) or ("WARN" in line) or ("ERROR" in line) or ("FATAL" in line) :
                line_pieces = line.split()
                error_level = line_pieces[0]
                if "INFO" in error_level:
                    nb_infos += 1
                if "WARN" in error_level:
                    nb_warnings += 1
                if "ERROR" in error_level:
                    nb_errors += 1           
                if "FATAL" in error_level:
                    nb_fatals += 1   
    return file_2_parse, nb_infos, nb_warnings, nb_errors, nb_fatals, nb_lines

def get_first_line(file_2_parse):
    """On récupère la date de la première ligne du ficher"""
    with open(file_2_parse,"r") as fh:
        for line in fh:
            if ("INFO" in line) or ("WARN" in line) or ("ERROR" in line) or ("FATAL" in line):
                first_line = fh.readlines()[0] # première ligne. Doit contenir une erreur
                break                        
    first_daytime = first_line.split()[2] #Récup champ date + suppression millisecondes
    first_hour = first_line.split()[3].split(",")[0] #Récup champ date + suppression millisecondes
    first_date = [first_line.split()[2],first_line.split()[3].split(",")[0]]
    return " ".join(first_date) 

def get_last_line(file_2_parse):
    """ lecture du fichier file_2_parse par la fin"""
    with open(file_2_parse,"r") as fh:
        for line in fh:
            if ("INFO" in line) or ("WARN" in line) or ("ERROR" in line) or ("FATAL" in line):
                last_line = fh.readlines()[-1] # première ligne. Doit contenir une erreur
                break                        
    last_daytime = last_line.split()[2] #Récup champ date + suppression millisecondes
    last_hour = last_line.split()[3].split(",")[0] #Récup champ date + suppression millisecondes
    last_date = [last_line.split()[2],last_line.split()[3].split(",")[0]]
    return " ".join(last_date)   

def print_header(res_tuple,f_date,l_date):  # a remplacer pour qu'elle admette un tuple
    """ Construit un résumé depuis le tuple retourné par parse_file"""
    # 1) on affecte les champs de paramètres aux bonnes variables : 
    file_2_parse = res_tuple[0]
    nb_infos = res_tuple[1]
    nb_warnings = res_tuple[2]
    nb_errors = res_tuple[3]
    nb_fatals = res_tuple[4]
    nb_lines = res_tuple[5]
    first_date = f_date
    last_date = l_date
    
    # 2) Un peu de calcul et de mise en forme
    info_percent = round((nb_infos/nb_lines)*100)
    warning_percent = round((nb_warnings/nb_lines)*100)
    error_percent = round((nb_errors/nb_lines)*100)
    fatal_percent = round((nb_fatals/nb_lines)*100)
    
    # 3) on construit le rapport, version texte
    print(f"In {file_2_parse}") 
    print(f"Start date : {first_date}\nEnd date :   {last_date}")
    print(f"Infos count = {nb_infos} ({info_percent} %)")
    print(f"Warnings count = {nb_warnings} ({warning_percent} %)")
    print(f"Errors count = {nb_errors} ({error_percent} %)")
    print(f"Fatals count = {nb_fatals} ({fatal_percent} %)")
    print("------------------------------")
    print(f"Total lines = {nb_lines}")
    
    

""" Main """
f_date=get_first_line(file_2_parse)
l_date=get_last_line(file_2_parse)
res = parse_file(file_2_parse)
print_header(res,f_date,l_date)



