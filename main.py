import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

if not firebase_admin._apps:
    cred = credentials.Certificate('obj_database.json')
    app = firebase_admin.initialize_app(cred)

db = firestore.client()


# Autenticação
def authentication(user='', password=''):
    users_db = db.collection("users").stream()
    for user_db in users_db:
        return user_db.id
        if user == user_db.id and password == user_db.get('senha'): return {'nome':user_db.get('nome'), 'nivel':user_db.get('nivel')}
    return False

# #Criar task
# def add_tasks(instructor, message, type, candidate, user):
#     #Procurando candidato
#     user_id= ''
#     colecs = db.collection('users').get()
#     for colec in colecs:
#         name_user = colec.get('nome')
#         if name_user == candidate:
#            user_id = colec.id

#     #Adicionando task no candidato
#     tasks_doc = db.collection("users").document(user_id)
#     task = tasks_doc.get().to_dict().get('tasks')
#     task.append(
#         {
#             'instrutor':instructor,
#             'mensagem':message,
#             'status':'aFazer',
#             'tipo':type
#         }
#     )
#     tasks_doc.update({'tasks':task})

#     # Adicionando task no instrutor
#     tasks_doc = db.collection("users").document(user)
#     task = tasks_doc.get().to_dict().get('tasks')
#     task.append(
#         {
#             'instrutor':candidate,
#             'mensagem':message,
#             'status':'aFazer',
#             'tipo':type
#         }
#     )
#     tasks_doc.update({'tasks':task})

# # Puxar candidatos
# def get_candidates():
#     candidates = []
#     colecs = db.collection('users').get()
#     for colec in colecs:
#         if colec.get('nivel') == 'candidato': candidates.append(colec.get('nome'))
#     return sorted(candidates)
        

# #Puxar informações de cards
# def get_cards(user):
#     cards = {
#         'aFazer': [],
#         'concluido':[],
#         'corrigido':[]
#     }
#     tasks_doc = db.collection("users").document(user)
#     tasks = tasks_doc.get().to_dict().get('tasks')
#     i = 0
#     for task in tasks:
#         if task['status'] == 'aFazer':
#             cards['aFazer'].insert(
#                 0,
#                 {
#                     'id':i,
#                     'instrutor':task['instrutor'],
#                     'mensagem':task['mensagem'],
#                     'tipo':task['tipo']
#                 }
#             )
#         elif task['status'] == 'concluido':
#             cards['concluido'].insert(
#                 0,
#                 {
#                     'id':i,
#                     'instrutor':task['instrutor'],
#                     'mensagem':task['mensagem'],
#                     'tipo':task['tipo']
#                 }
#             )
#         elif task['status'] == 'corrigido':
#             cards['corrigido'].insert(
#                 0,
#                 {
#                     'id':i,
#                     'instrutor':task['instrutor'],
#                     'mensagem':task['mensagem'],
#                     'tipo':task['tipo']
#                 }
#             )

#         i += 1
#     return cards

# # Concluir task
# def task_concluded(id, user):
#     tasks_doc = db.collection("users").document(user)
#     tasks = tasks_doc.get().to_dict().get('tasks')
#     tasks[id]['status'] = 'concluido'
#     tasks_doc.update({'tasks':tasks})

# # Cancelar task concluida
# def task_inconcluded(id, user):
#     tasks_doc = db.collection("users").document(user)
#     tasks = tasks_doc.get().to_dict().get('tasks')
#     tasks[id]['status'] = 'aFazer'
#     tasks_doc.update({'tasks':tasks})

# # Corrigir task
# def task_corrected(id, user):
#     tasks_doc = db.collection("users").document(user)
#     tasks = tasks_doc.get().to_dict().get('tasks')
#     tasks[id]['status'] = 'corrigido'
#     tasks_doc.update({'tasks':tasks})

# # Cancelar task corrigida
# def task_incorrected(id, user):
#     tasks_doc = db.collection("users").document(user)
#     tasks = tasks_doc.get().to_dict().get('tasks')
#     tasks[id]['status'] = 'concluido'
#     tasks_doc.update({'tasks':tasks})

# # Excluir Task
# def task_delete(id, user):
#     tasks_doc = db.collection("users").document(user)
#     tasks = tasks_doc.get().to_dict().get('tasks')
#     del tasks[id]
#     tasks_doc.update({'tasks':tasks})

# # Puxar informações de hinos
# def get_data_hymns(candidate):
#     forms_doc = db.collection("users").document(candidate).get()
#     forms = forms_doc.to_dict().get('ficha')['hinos']
#     return forms

# def truco():
#     tasks_doc = db.collection("users").document('isaiasvitorslva@gmail.com')
#     # task = tasks_doc.get().to_dict().get('ficha')
#     task = []
#     for i in range(1, 481):
#         n = ''
#         if i < 10: n = f'00{i}'
#         elif i < 100: n = f'0{i}'
#         else: n = f'{i}'
#         task.append(
#             {
#                 'alternativa':False,
#                 'numero':n,
#                 'principal':False,
#                 'nome': ''
#             }
#         )

#     tasks_doc.update({'ficha':{'hinos':task}})

# truco()


st.title(authentication())
