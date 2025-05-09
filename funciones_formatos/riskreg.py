#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:34:39 2025

@author: javiermontanochiriboga
@coauthor: yerdna14
"""

import csv
import os
from datetime import datetime

def riskreg():
    num_riskreg = int(input('¿Cuántos riesgos vas a registrar hoy? '))
    # Revisar desde donde empezara a el nuevo id.
    file_exists = os.path.isfile('issuelog.csv')
    if file_exists:
        with open('issuelog.csv', 'r', encoding='utf-8') as arch:
            interx = csv.DictReader(arch)
            ids_exis = [int(fil['ID']) for fil in interx if fil['ID'].isdigit()]
            if ids_exis:
                sig_id = max(ids_exis) + 1
    else:
        sig_id = 1
    
    with open('riskreg.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribe headers si el archivo está vacío
        if csvfile.tell() == 0:
            writer.writerow(["ID", "Fecha de hallazgo", "WBS", "Rango", "Persona Asignada", "Descripción", "Impacto", "Probabilidad", "Estado"])
        
        for count in range(sig_id, num_riskreg + sig_id):
            print(f'\n--- Riesgo #{count} ---')
            writer.writerow([
                count,
                datetime.now().strftime('%Y-%m-%d'),
                input('Numero o ID de la WBS de la tarea(s) relacionada con el riesgo: '),
                input('Que tan importante es el riesgo de 1 a 5: '),
                input('Persona Asignada: '),
                input('Descripción: '),
                input('Impacto en el costo/tiempo de 1 a 5: '),
                input('Probabilidad de ocurrencia de 1 a 5: '),
                input('Estado en el changelog (P(Pendiente)/A(Aprovado)/R(Rechazado)): ').capitalize(),
                
            ])
    
    print(f'\n✅ Datos guardados en riskreg.csv ')

riskreg()