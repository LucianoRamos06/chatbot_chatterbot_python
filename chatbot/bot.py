#Importar a biblioteca do chatterbot 
from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
import os

maria = ['Maria','./maria.sqlite3', 'maria/']
joao = ['Joao','./joao.sqlite3', 'joao/']
selecionado = []

op = '0'
while(op != '1' and op != '2'):
    print('1 - Treinar')
    print('2 - Não Treinar')
    op = input("resposta: ")


sel = '0'
while(sel != '1' and sel != '2'):
    print('1 - Maria')
    print('2 - João')
    sel = input("resposta: ")



if (sel == '1'):
	selecionado = maria
else:	
	selecionado = joao



treinar = False
if (op == '1'):
	treinar = False
else:	
	treinar = True

#Criar uma instância do chatbot
#storage_adapter - utilizado para selecionar o tipo de banco que será utilizado pelo chatbot
chatbot = ChatBot(
    selecionado[0],
    read_only=treinar,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database=selecionado[1],
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
	

# Dados existentes ao instalar o ChatterBot, porém estes dados estão em ingles
chatbot.train('chatterbot.corpus.english')

#Treinar o bot Usando arquivos .yml
#Arquivos disponíveis no git: https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/portuguese 
chatbot.train('portuguese/')

#Treinar o bot de acordo com o perfil escolhido. Ex: joão ou maria
chatbot.train(selecionado[2])

while True: 
	#Pergunta feita pelo usuário	
	quest = input("Você: ")

	#Instância do chatbot busca a resposta mais que considera correta
	resposta = chatbot.get_response(quest)

	#A resposta selecionada possuí um grau de confiança, caso esse grau seja baixo podemos enviar outra resposta.
	if float(resposta.confidence) > 0.3:
		print('Bot: ', resposta)
	else:
		print('Bot: ', 'Não sei a resposta.')

