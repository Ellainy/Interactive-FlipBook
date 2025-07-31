# Livro Interativo 3D - TCC

## 📘 INTRODUÇÃO

No IFRN – Campus São Paulo do Potengi, alunos de diferentes cursos desenvolvem projetos de extensão com o objetivo de aproximar a comunidade do ambiente escolar e promover ações de impacto social, ambiental e educativo. Um desses projetos resultou na criação do livro **“Um Festival de Mudanças”**, escrito por estudantes do curso técnico em Meio Ambiente e ilustrado por alunos de outros cursos, com foco na educação ambiental, nas experiências de intercâmbio e na internacionalização.

Apesar da relevância do conteúdo, o acesso ao livro ainda estava limitado ao formato físico e a apresentações pontuais. Pensando nisso, surgiu a proposta de transformar essa produção em uma **plataforma digital interativa**, que permitisse maior alcance e acessibilidade.

Nesse contexto, o projeto **Livro Interativo 3D** surge como uma proposta inovadora para transformar o livro “Um Festival de Mudanças” em uma plataforma digital interativa, acessível e visualmente atraente. A ideia é proporcionar uma nova forma de leitura e interação, tornando o conteúdo do livro mais dinâmico, envolvente e acessível a diferentes públicos.

O projeto também integra conhecimentos adquiridos ao longo da formação técnica, unindo design, UI/UX, programação, usabilidade e compromisso social em uma solução inovadora. Dessa forma, busca-se **ampliar o alcance da mensagem ambiental do livro**, incentivando a reflexão e a conscientização sobre as mudanças climáticas e a importância das ações locais para o impacto global.

---

## 🧩 JUSTIFICATIVA

O livro “Um Festival de Mudanças”, desenvolvido por alunos do curso técnico em Meio Ambiente do IFRN – Campus São Paulo do Potengi, surgiu de um projeto de extensão que aborda mudanças climáticas e intercâmbio cultural. No entanto, há limitação ao seu alcance e sua acessibilidade é reduzida.

A proposta deste trabalho de **Prática Profissional Integrada** é desenvolver um site com efeito de **livro 3D**, responsivo e visualmente atrativo, utilizando tecnologias como:

- Django  
- HTML  
- CSS  
- Bootstrap  
- Turn.js  
- jQuery  

Essa plataforma permitirá o **gerenciamento dinâmico do conteúdo** por meio de um painel administrativo, facilitando atualizações e manutenção da obra digital.

Ao unir design, funcionalidade e tecnologia, o projeto promove a integração entre cursos e áreas do conhecimento, incentivando a divulgação científica e a educação ambiental de forma inovadora. A iniciativa também reforça a importância da extensão como espaço de formação **crítica, criativa e cidadã**.

---

## 🎯 PÚBLICO-ALVO

Nosso principal público-alvo são os **estudantes do IFRN - Campus São Paulo do Potengi**, interessados em projetos acadêmicos e extracurriculares. Também contempla:

- Professores
- Representantes externos
- Parceiros em potencial para estágios e projetos acadêmico-profissionais

---

## 🎯 OBJETIVOS

Este projeto busca fortalecer a divulgação do conhecimento produzido por meio da extensão e promover a conexão entre estudantes, comunidade acadêmica e público em geral. A seguir, os objetivos principais:

- Desenvolver uma **plataforma digital interativa** para divulgação do livro “Um Festival de Mudanças”.
- Facilitar o acesso e a leitura do conteúdo de forma **dinâmica, atrativa e acessível**.
- Promover a integração entre os cursos de **Meio Ambiente** e **Informática para Internet**, estimulando a interdisciplinaridade.
- Estimular o uso de **tecnologias digitais** aplicadas à educação ambiental e à comunicação científica.
- Valorizar o trabalho dos estudantes e ampliar a visibilidade do projeto de extensão.

---

## 🧠 ANÁLISE E PROJETO

### 🔍 VISÃO GERAL DO SISTEMA

O sistema **Livro Interativo 3D** é uma plataforma digital desenvolvida para disponibilizar de forma acessível e interativa o livro “Um Festival de Mudanças”.  

Funcionalidades principais:

- Leitura em PDF ou **formato flipbook 3D**
- Experiência responsiva (desktop e mobile)
- Página de internacionalização com **notícias e relatos de intercâmbio**

---

### 👤 ATORES DO SISTEMA

| Ator | Descrição |
|------|-----------|
| **Externos** | Usuários não cadastrados com acesso ao conteúdo público do site. |
| **Alunos** | Usuários com registro no sistema e acesso ao próprio perfil. |
| **Administradores** | Gerenciam conteúdo, visual do site e seção de internacionalização. |
| **SUAP** | Sistema mediador de login por credenciais IFRN. |

---

## ✅ LEVANTAMENTO DE REQUISITOS

### 📌 Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
|--------|------|-----------|------------|
| RF01 | Cadastrar usuário | Permitir que alunos de fora do IFRN se cadastrem com email. | Alta |
| RF02 | Login | Usuários cadastrados poderão fazer login. | Alta |
| RF03 | Gerenciar conteúdo do livro | Administradores poderão adicionar, editar e excluir páginas. | Alta |
| RF04 | Visualizar livro | Usuários poderão acessar o livro em flipbook ou PDF. | Alta |
| RF05 | Gerenciar internacionalização | Adição/edição de relatos e notícias por administradores. | Alta |
| RF06 | Personalizar tema | Administradores poderão selecionar paletas de cores. | Média |
| RF07 | Perfil do usuário | Visualizar e editar informações pessoais. | Média |
| RF08 | Baixar PDF | Permitir o download do livro em PDF. | Baixa |

> Fonte: Elaboração própria (2025)

---

### ⚙️ Requisitos Não Funcionais

| Código | Descrição | Categoria |
|--------|-----------|-----------|
| RNF01 | O sistema deve funcionar em ambiente web, compatível com navegadores modernos. | Organizacional |
| RNF02 | Deve utilizar HTML, CSS, Python e JavaScript. | Organizacional |
| RNF03 | Áreas administrativas devem ser restritas a usuários autenticados (incluindo SUAP). | Produto |
| RNF04 | Senhas devem ser criptografadas com MD5. | Produto |
| RNF05 | O banco de dados utilizado será o SQLite. | Organizacional |
| RNF06 | A interface deve ser responsiva e acessível. | Produto |

---

**🚧 Projeto em desenvolvimento - IFRN-SPP | TCC 2025**
