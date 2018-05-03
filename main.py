#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la MongoDB
#
# Perpetrados por: Oscar Corres y Viloria

from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')

# Ejercicio 1:
#
# Diseña un conjunto de colecciones que sean capaces de cumplir con los siguientes requisitos:
#
#     Será necesario tener un control de acceso para los usuarios de la plataforma
#     Los usuarios deberán tener al menos los siguientes campos: nombre de usuario, contraseña e email

db = client.Citas

usuarios = db.Usuarios

usuario = {'NombreUsuario': 'LonelyRanger', 'Clave': 'Silver', 'e-mail': 'away@kimosabit.com'}
result = usuarios.insert_one(usuario)
result = usuarios.insert_one({'NombreUsuario':'PoisonIvy',
                              'Clave':'Batman',
                              'e-mail':'Bruce@Wayne.com'})
print(result)

#     Queremos montar un servicio de citas por lo que tendremos que registrar los mensajes que se envíen los usuarios

mensajes = db.Mensajes
mensaje = { 'De': usuarios.find_one({'NombreUsuario': 'PoisonIvy'}, '_id')['_id'],
            'Para': usuarios.find_one({'NombreUsuario': 'LonelyRanger'}, '_id')['_id'],
            'Mensajes': "ipsum lipsum horeca",
            'Fecha': datetime.utcnow()
            }
result = mensajes.insert_one(mensaje)
pprint(mensaje)

#     Por lo tanto una de las consultas básicas ser´el dame los últimos 10 mensajes dirigidos a un usuario

result = mensajes.find({'De': usuarios.find_one(
                                                 {'NombreUsuario': 'PoisonIvy'},
                                                 '_id')
                                                ['_id']}
                       ).sort('Fecha', -1).limit(10)

for mensaje in result:
    pprint(mensaje)

#     Tenemos que almacenar también las medidas de cada usuario: altura peso, edad y color de ojos
result = usuarios.update_one({'NombreUsuario': 'LonelyRanger'},
                             {"$set": {'altura': 185,'peso', edad y color de ojos}},
                             upsert=False)


result = usuarios.update_one({'NombreUsuario': 'LonelyRanger'},
                             {"$set": {'Clave': 'Tonto'}},
                             upsert=False)
pprint(result)