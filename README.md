# Livro Interativo 3D 
Este projeto faz parte de uma ação de extensão do IFRN – Campus São Paulo do Potengi. O livro, intitulado **“Um Festival de Mudanças”**, foi escrito por alunos do curso técnico em Meio Ambiente e ilustrado por estudantes de diferentes cursos. A proposta é promover a educação ambiental de forma acessível e interativa, com foco na internacionalização.

A proposta do sistema é criar uma versão digital do livro, proporcionando uma experiência interativa em 3D, com gerenciamento dinâmico de páginas e conteúdos através de um sistema web.
## Funcionalidades
- Cadastro e gerenciamento de páginas do livro via Django Admin.
- Navegação interativa com efeito de livro 3D, utilizando **Turn.js** e **jQuery**..
- Layout responsivo para desktop e mobile.

## Tecnologias Utilizadas
- **Frontend:** HTML, CSS, Bootstrap, JavaScript, jQuery, Turn.js
- **Backend:** Python, Django, Pillow
- **Banco de Dados:** SQLite 
- **Outros:** Flipbook com Turn.js

# Para usar o sistema, siga esses passos:
### 1 - Clone este repositório, ative a venv e instale as dependências:
    pip install -r requirements.txt

### 2 - Aplique as migrações:
    python .\manage.py migrate

### 3 - Por fim, rode o sistema:
    python .\manage.py runserver

