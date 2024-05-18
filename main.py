import streamlit as st
import database as db

# Configurações da Página
st.set_page_config(
    layout='wide'
)

# CSS
st.write(
    '''
        <style>
            button[data-baseweb="tab"] {
                font-size: 24px;
                margin: 0;
                width: 100%;
            }
        </style>
    ''',
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>GEM Morrinhos</h1>", unsafe_allow_html=True)

st.subheader(':violet[Tarefas]')

tab_aFazer, tab_concluido, tab_corrigido = st.tabs(["A FAZER", "CONCLUÍDO", "CORRIGIDO"])

#Classe para criar cards
class Card_task:
    def __init__(self, id, instrutor, mensagem, tipo, status):
        self.id = id
        self.instrutor = instrutor
        self.mensagem = mensagem
        self.tipo = tipo
        self.status = status
        self.build()

    def build(self):
        card = st.container(border=True)
        card.write(f'{self.tipo} - {self.id}')
        card.write(f'{self.mensagem}')
        self.btn_card(card)

    def btn_card(self, card):
        if self.status == 'aFazer': return card.button('ESTUDEI', use_container_width=True, key=self.id, on_click=self.estudei)
        elif self.status == 'concluido': return card.button('CANCELAR', use_container_width=True, key=self.id, on_click=self.cancelar)
        elif self.status == 'confirmado': return None

    def estudei(self): db.task_concluded(self.id, 'claudiomarçola@gmail.com')
    def cancelar(self): db.task_inconcluded(self.id, 'claudiomarçola@gmail.com')


with tab_aFazer:
    tasks = db.get_cards('claudiomarçola@gmail.com')['aFazer']
    for task in tasks:
        Card_task(task['id'], task['instrutor'], task['mensagem'], task['tipo'], 'aFazer')
with tab_concluido:
    tasks = db.get_cards('claudiomarçola@gmail.com')['concluido']
    for task in tasks:
        Card_task(task['id'], task['instrutor'], task['mensagem'], task['tipo'], 'concluido')
with tab_corrigido:
    tasks = db.get_cards('claudiomarçola@gmail.com')['corrigido']
    for task in tasks:
        Card_task(task['id'], task['instrutor'], task['mensagem'], task['tipo'], 'corrigido')








