# Livro Interativo 3D 
Este projeto faz parte de uma ação de extensão do IFRN – Campus São Paulo do Potengi. O livro, intitulado **“Um Festival de Mudanças”**, foi escrito por alunos do curso técnico em Meio Ambiente e ilustrado por estudantes de diferentes cursos. A proposta é promover a educação ambiental de forma acessível e interativa, com foco na internacionalização.

A proposta do sistema é criar uma versão digital do livro, proporcionando uma experiência interativa em 3D, com gerenciamento dinâmico de páginas e conteúdos através de um sistema web.

## Tecnologias Utilizadas
- **Frontend:** HTML, CSS, Bootstrap, JavaScript, jQuery, Turn.js
- **Backend:** Python, Django, Pillow
- **Banco de Dados:** SQLite 
- **Outros:** Flipbook com Turn.js

## Pré-requisitos
- Python 3.8 ou superior
- MySQL
- Git


## Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/Ellainy/projeto_livroDjango.git
cd projeto
```

### 2. Crie e ative um ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
Este comando irá instalar todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

### 5. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

### 6. (Opcional) Crie um superusuário

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

### 7. Execute o servidor
```bash
python manage.py runserver
```

Acesse: http://localhost:8000

## Estrutura do Projeto

```
projeto_livroDjango/
│
├── config/                      # Arquivos de configuração para aplicação do Django
│
├── docs/                        # Documentação
│   ├── imgs/                    # Imagens da engenharia de software
│   ├── index.md                 # Detalhes da engenharia de software
|
├── livro3d/                     # App principal do sistema
│   ├── templates/               # Páginas HTML
│   ├── __init__.py              # Arquivo de execução do django
│   ├── admin.py                 # Arquivo de execução do django admin
│   ├── apps.py                  # Arquivo de execução de app do django
│   ├── context_processors.py    # Funções que renderizam dados em todas as páginas do sistema
│   ├── forms.py                 # Configuração de formulários
│   ├── models.py                # Estrutura do banco de dados
│   ├── urls.py                  # Caminhos das páginas e funções
│   ├── views.py                 # Lógica, execução e renderização de dados das páginas e funções
|
├── static/                      # Arquivos estáticos do sistema (imagens, CSS e JS)
|
├── users/                       # App relativo aos usuários do sistema
│   ├── templates/               # Páginas HTML
│   ├── __init__.py              # Arquivo de execução do django
│   ├── admin.py                 # Arquivo de execução do django admin
│   ├── apps.py                  # Arquivo de execução de app do django
│   ├── forms.py                 # Configuração de formulários
│   ├── models.py                # Estrutura do banco de dados
│   ├── urls.py                  # Caminhos das páginas e funções
│   ├── views.py                 # Lógica, execução e renderização de dados das páginas e funções
|
├── .gitignore                   # Arquivos ignorados pelo Git
|
├── LICENSE                      # Licença do projeto
|
├── README.md                    # Este arquivo
|
├── manage.py                    # Script principal do Django
├── requirements.txt             # Dependências do projeto
│

```

---

## Funcionalidades
- Cadastro e gerenciamento de páginas do livro via Django Admin.
- Navegação interativa com efeito de livro 3D, utilizando **Turn.js** e **jQuery**..
- Layout responsivo para desktop e mobile.
- Personalização do sistema (Cores, textos da paginas e informações gerais do sistema).

## Autores
- Ellainy Nayara        
- Mateus Cosme
