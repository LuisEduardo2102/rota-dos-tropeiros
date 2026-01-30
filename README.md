# 🗺️ Projeto Rota dos Tropeiros

## 📝 Sobre o Projeto

O Rota dos Tropeiros é um projeto desenvolvido academicamente com a finalidade de criar uma solução social que ajude as pessoas a facilitarem o uso do transporte público local.

<img width="1366" height="690" alt="Hero do site" src="https://github.com/user-attachments/assets/87a9635a-8612-4d1b-bdf6-292f5a78f355" />

### ⚙️ Como funciona?

A aplicação utiliza as seguintes ferramentas para gerar os mapas e trajetos:

    APIs de Mapa: Open Street Map e Leaflet para renderização e roteamento.

    Coordenadas: Para criar as rotas, utilizamos as coordenadas geográficas dos pontos da cidade, que podem ser extraídas via Google Maps.

### 🚀 Como posso testar?

Você pode baixar os arquivos do repositório ou executar via Code Space (Recomendado).
### 1. Configurar Ambiente Virtual

Recomenda-se criar um ambiente isolado:
```Bash

python -m venv .venv
```
Ativação:

    Linux/CodeSpace: source .venv/bin/activate

    Windows: .\.venv\Scripts\activate

#### 2. Instalar Dependências
```Bash

pip install Django Pillow
```
#### 3. Migrar Banco de Dados
```Bash

python manage.py makemigrations
```
```
python manage.py migrate
```
#### 4. Criar Super Usuário

Para gerenciar os dados, crie um acesso administrativo:
```Bash
python manage.py createsuperuser
```
   **Insira os dados solicitados. Se a senha for curta, confirme com y.**

#### 5. Rodar o Servidor
```Bash
python manage.py runserver
```
### 🛠️ Adicionando Informações (Passo a Passo)
#### Passo 1: Acesso ao Admin

Acesse ```http://127.0.0.1:8000/admin``` e faça login com seu super usuário.

#### Passo 2: Cadastrar Linha de Ônibus

No menu, clique em "+ Adicionar" ao lado de Rotas e dê um nome à linha. <img width="1078" height="426" alt="Adicionar Rota" src="https://github.com/user-attachments/assets/5709f864-29f5-4006-af44-45938753e1eb" />
#### Passo 3: Cadastrar Pontos e Coordenadas

Clique em "+ Adicionar" ao lado de Paradas. Insira o nome e as coordenadas obtidas no Google Maps. <img width="627" height="442" alt="Pegar Coordenadas" src="https://github.com/user-attachments/assets/5babbba1-edfa-481e-a896-5dae7481a9b2" />

Vincule o ponto à Rota desejada e defina o horário. <img width="1050" height="528" alt="Configurar Parada" src="https://github.com/user-attachments/assets/7f9d41e9-9a2e-4e39-be55-1e1967618806" />

   **Nota: É necessário cadastrar pelo menos 2 pontos para que a linha da rota seja desenhada no mapa.**

# 🏁 Resultado Final

Após salvar, volte para ```http://127.0.0.1:8000``` para visualizar as rotas e horários integrados.

<img width="1295" height="624" alt="Site funcionando" src="https://github.com/user-attachments/assets/e9f7c722-2dcd-4119-aef5-c29832afe8dd" />
