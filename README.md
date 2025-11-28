# Projeto Rota dos Tropeiros
## O que é? 
é um projeto realizado em curso com a finidade de desenvolver uma solução social
em que ajude as pessoas de alguma forma. Nosso grupo resolver criar uma solução para facilitar
o uso do transporte público local

(Hero do site)

<img width="1366" height="690" alt="Captura de tela de 2025-11-27 11-47-24" src="https://github.com/user-attachments/assets/87a9635a-8612-4d1b-bdf6-292f5a78f355" />


## Como funciona?
Simplificando, ele usa APIs como Open Street Map e Leaf Leet para mapa e roteamento, para criarmos 
as rotas é necessário termos as coordenadas geográficas dos pontos da cidade, que podem ser
retiradas através do Google Maps.

## Como posso testar? 
Você pode baixar os arquivos do repositório e executar em sua IDE ou pode abrir pelo Code Space(Recomendado).

Para ver o funcionamento primeiro, é recomendado criar um ambiente virtual usando o venv
"python (ou python3) -m venv .venv"

depois precisamos ativá-lo:
no CodeSpace / linux use o comando "source .venv/bin/activate"
no Windows ".\.venv\Scripts\activate" (era pra aparcer "\" antes do .venv)
 
Depois instale as dependencias com "pip install Django Pillow"

ele irá pedir usuário, e-mail e senha, pode inserir valores ficticios e qualquer senha, se a senha for muito curta aparecerá um prompt falando que a senha é muito fraca,
apenas confirme a senha com y.

agora execute os comando "python manage.py makemigrations" e depois "python manage.py migrate" para criar o arquivo do banco de dados

agora precisamos criar um super usuário para adicionarmos informações no banco de dados:
no terminal use o comando "python (ou python3) manage.py createsuperuser" (sem aspas)

e por fim rode o servidor "python manage.py runserver"

## Vamos adicionar informações:
Para acessarmos o Admin precisamos alter a barra de enederço, onde está escrito "127.0.0.1:8000" mude para "127.0.0.1:8000/admin" e insira os dados de login do super usuário.

Agora que entramos no admin, iremos adicionar uma Linha de Ônibus, clique em "+ Adicionar" ao lado de "Rotas", 
dê um nome, por exemplo: "Jardim Bonito / Bairro das Flores"

<img width="1078" height="426" alt="Captura de tela de 2025-11-27 12-08-08" src="https://github.com/user-attachments/assets/5709f864-29f5-4006-af44-45938753e1eb" />

por enquanto não temos nehum ponto cadastrado, então apenas clique em salvar.

agora vamos adicionar um ponto, clique em "+ Adicionar" ao lado de "Paradas".

<img width="1050" height="528" alt="Captura de tela de 2025-11-27 12-14-38" src="https://github.com/user-attachments/assets/7f9d41e9-9a2e-4e39-be55-1e1967618806" />

Insira um nome do ponto, e depois cole as coordenadas do ponto que podem ser pegas através do Google Maps

<img width="627" height="442" alt="Captura de tela de 2025-11-27 12-13-06" src="https://github.com/user-attachments/assets/5babbba1-edfa-481e-a896-5dae7481a9b2" />

clique em cima de "Rota" e depois o nome da Linha que você cadastrou nesse caso "Jardim Bonito / Bairro das Flores" 
adicione o Ponto que você acabou de cadastrar e o seu horário, pode ser qualquer horário, agora precisamos interligar essas duas informações, a linha e o ponto. 
 Não se esqueça que é preciso pelo menos de 2 pontos para ver a linha da rota no mapa, 

<img width="1045" height="382" alt="Captura de tela de 2025-11-27 12-25-41" src="https://github.com/user-attachments/assets/eec4d864-992e-4fd8-b4af-a39046f504f9" />

Salve tudo e retorne para a página incial apagando tudo menos "http://127.0.0.1:8000" e veja como ficou o site depois de adicionarmos as rotas, paradas e horários!

<img width="1295" height="624" alt="Captura de tela de 2025-11-27 13-04-34" src="https://github.com/user-attachments/assets/e9f7c722-2dcd-4119-aef5-c29832afe8dd" />
