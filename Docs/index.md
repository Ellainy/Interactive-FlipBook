# Livro Interativo 3D - TCC

##  INTRODUÇÃO

No IFRN – Campus São Paulo do Potengi, alunos de diferentes cursos desenvolvem projetos de extensão com o objetivo de aproximar a comunidade do ambiente escolar e promover ações de impacto social, ambiental e educativo. Um desses projetos resultou na criação do livro **“Um Festival de Mudanças”**, escrito por estudantes do curso técnico em Meio Ambiente e ilustrado por alunos de outros cursos, com foco na educação ambiental, nas experiências de intercâmbio e na internacionalização.

Apesar da relevância do conteúdo, o acesso ao livro ainda estava limitado ao formato físico e a apresentações pontuais. Pensando nisso, surgiu a proposta de transformar essa produção em uma **plataforma digital interativa**, que permitisse maior alcance e acessibilidade.

Nesse contexto, o projeto **Interactive FlipBook** surge como uma proposta inovadora para transformar o livro “Um Festival de Mudanças” em uma plataforma digital interativa, acessível e visualmente atraente. A ideia é proporcionar uma nova forma de leitura e interação, tornando o conteúdo do livro mais dinâmico, envolvente e acessível a diferentes públicos.

O projeto também integra conhecimentos adquiridos ao longo da formação técnica, unindo design, UI/UX, programação, usabilidade e compromisso social em uma solução inovadora. Dessa forma, busca-se **ampliar o alcance da mensagem ambiental do livro**, incentivando a reflexão e a conscientização sobre as mudanças climáticas e a importância das ações locais para o impacto global.

Além disso, o sistema também conta com uma aparência personalizável e administração por uma dashboard com layout simples e atraente proporcionando conforto, controle e facilidade para um usuários sem conhecimento técnico na área de tecnologia possa administrar o site livremente.

---

##  JUSTIFICATIVA
O livro “Um Festival de Mudanças”, desenvolvido por alunos do curso técnico em Meio Ambiente do IFRN – Campus São Paulo do Potengi, surgiu de um projeto de extensão que aborda mudanças climáticas e intercâmbio cultural. No entanto, há limitação a  seu alcance e a acessibilidade é limitada.
A proposta deste trabalho de Prática Profissional Integrada é desenvolver um site com efeito de livro 3D, responsivo e visualmente atrativo, utilizando tecnologias como Django, HTML, CSS, Bootstrap, Turn.js e jQuery. Essa plataforma permitirá o gerenciamento dinâmico do conteúdo por meio de um painel administrativo, facilitando atualizações e manutenção da obra digital.
Ao unir design, funcionalidade e tecnologia, o projeto promove a integração entre cursos e áreas do conhecimento, incentivando a divulgação científica e a educação ambiental de forma inovadora. A iniciativa também reforça a importância da extensão como espaço de formação crítica, criativa e cidadã, e demonstra, na prática, as competências desenvolvidas ao longo do curso técnico em Informática para Internet.

---

##  PÚBLICO-ALVO

Nosso principal público-alvo são os **estudantes do IFRN - Campus São Paulo do Potengi**, interessados em projetos acadêmicos e extracurriculares. Também contempla:

- Professores
- Alunos
- Usuários externos 

---

##  OBJETIVOS

No IFRN Campus São Paulo do Potengi, este projeto busca fortalecer a divulgação do conhecimento produzido por meio da extensão e promover a conexão entre estudantes, comunidade acadêmica e público em geral. A seguir, os objetivos deste trabalho:
- Desenvolver uma **plataforma digital interativa** para divulgação do livro “Um Festival de Mudanças”.
- Facilitar o acesso e a leitura do conteúdo de forma **dinâmica, atrativa e acessível**.
- Promover a integração entre os cursos de **Meio Ambiente** e **Informática para Internet**, estimulando a interdisciplinaridade.
- Estimular o uso de **tecnologias digitais** aplicadas à educação ambiental e à comunicação científica.
- Valorizar o trabalho dos estudantes e ampliar a visibilidade do projeto de extensão dentro e fora do campus..

---

##  ANÁLISE E PROJETO

###  VISÃO GERAL DO SISTEMA

O sistema **Livro Interativo 3D** é uma plataforma digital desenvolvida para disponibilizar de forma acessível e interativa o livro “Um Festival de Mudanças”.  

Funcionalidades principais:

- Leitura em PDF ou **formato flipbook 3D**
- Experiência responsiva (desktop e mobile)
- Personalização do site pelo administrador (cores, textos e livro)
- Página de internacionalização com **notícias e relatos de intercâmbio**

---

###  ATORES DO SISTEMA

| Ator                | Descrição                                                          |
| ------------------- | ------------------------------------------------------------------ |
| **Externos**        | Usuários não cadastrados com acesso ao conteúdo público do site.   |
| **Alunos**          | Usuários com registro no sistema e acesso ao próprio perfil.       |
| **Administradores** | Gerenciam conteúdo, visual do site e seção de internacionalização. |
| **Google**          | Sistema mediador de login.                                         |

---

## LEVANTAMENTO DE REQUISITOS

###  Requisitos Funcionais

| Código | Nome                        | Descrição                                                                    | Prioridade |
| ------ | --------------------------- | ---------------------------------------------------------------------------- | ---------- |
| RF01   | Cadastrar usuário           | Permitir que alunos de fora do IFRN se cadastrem com email.                  | Alta       |
| RF02   | Login                       | Usuários cadastrados poderão fazer login.                                    | Alta       |
| RF03   | Gerenciar conteúdo do livro | Administradores poderão adicionar, editar e excluir páginas.                 | Alta       |
| RF04   | Visualizar livro            | Usuários poderão acessar o livro em flipbook ou PDF.                         | Alta       |
| RF05   | Personalizar textos         | Administradores poderão adicionar e editar os textos das paginas do sistema. | Alta       |
| RF06   | Personalizar Sistema        | Administradores poderão adicionar e editar informações do site               | Alta       |
| RF07   | Personalizar tema           | Administradores poderão selecionar paletas de cores.                         | Média      |
| RF08   | Perfil do usuário           | Visualizar e editar informações pessoais.                                    | Média      |
| RF09   | Baixar PDF                  | Permitir o download do livro em PDF.                                         | Baixa      |

> Fonte: Elaboração própria (2025)

---

### Requisitos Não Funcionais

| Código | Descrição                                                                           | Categoria      |
| ------ | ----------------------------------------------------------------------------------- | -------------- |
| RNF01  | O sistema deve funcionar em ambiente web, compatível com navegadores modernos.      | Organizacional |
| RNF02  | Deve utilizar HTML, CSS, Python e JavaScript.                                       | Organizacional |
| RNF03  | Áreas administrativas devem ser restritas a usuários autenticados (incluindo SUAP). | Produto        |
| RNF04  | Senhas devem ser criptografadas com MD5.                                            | Produto        |
| RNF05  | O banco de dados utilizado será o SQLite.                                           | Organizacional |
| RNF06  | A interface deve ser responsiva e acessível.                                        | Produto        |

---
##  DIAGRAMAS DE CASO DE USO

O diagrama de casos de uso descreve o escopo do sistema projetado, além de especificar textualmente este escopo,
a técnica de casos de uso é uma excelente ferramenta para abstrair os requisitos funcionais e atores do sistema, mostrando quem
eles são e como interagem entre si. Dessa forma, levando em consideração os atores e os requisitos funcionais deste trabalho, 
foram definidos 15 (quinze) casos de uso, conforme ilustrado na Figura 1. 

---

Figura 1 - Diagrama de caso do projeto 

![Diagrama de casos de uso](imgs/DCU%20projeto%20livro.svg)

Fonte: Elaboração própria (2025)

## 2.5 EXPANSÃO DO CASO DE USO – GERENCIAR SISTEMA

O caso de uso **Gerenciar Sistema** é um dos casos de maior risco da aplicação, pois envolve operações críticas de administração e manutenção das informações do sistema. Nesta seção são especificadas as ações que o usuário **Administrador** pode executar no sistema com o objetivo de **cadastrar, editar e excluir os textos e cores padrão**, além de **editar informações gerais do sistema** com do site como nome do sistema, logo e contato.  
Somente usuários com permissão de administrador poderão acessar e executar este caso de uso.

### 2.5.1 Atores
- Administrador

### 2.5.2 Pré-condição
O usuário deve estar autenticado no sistema e possuir permissão de administrador, concedida pelo administrador principal do sistema.

### 2.5.3 Pós-condição
O sistema exibe o **dashboard administrativo**, refletindo as alterações realizadas pelo administrador.

### 2.5.4 Requisitos Funcionais
- **RF03** – Gerenciar conteúdo do livro   
- **RF05** – Personalizar textos 
- **RF06** – Personalizar Sistema  
- **RF07** – Personalizar tema  

### 2.5.5 Requisitos Não Funcionais
- **RNF003** – Acesso restrito a usuários com perfil de administrador.

---

### 2.5.6 Fluxo Principal 01 – Gerenciar conteúdo do livro   

1. **[EV]** Na tela do dashboard administrativo, o administrador clica na opção **“Gerenciar paginas”** logo após em Gerenciamneto do livro.
2. **[RS]** O sistema exibe o formulário de cadastro do livro.
3. **[EV]** O administrador informa os dados do livro, como título, descrição, capa, imagens, páginas do livro e demais informações necessárias.
4. **[RS]** O sistema valida os dados informados.
5. **[RS]** O sistema salva as informações no banco de dados.
6. **[RS]** O sistema exibe uma mensagem de sucesso e apresenta o livro cadastrado no painel administrativo.

---

### 2.5.7 Fluxo Principal 02 – Excluir Livro

1. **[EV]** Na tela do dashboard administrativo, o administrador seleciona o livro desejado e clica na opção **“Excluir”**.
2. **[RS]** O sistema solicita a confirmação da exclusão.
3. **[EV]** O administrador confirma a exclusão.
4. **[RS]** O sistema remove os dados do livro do banco de dados.
5. **[RS]** O sistema exibe uma mensagem confirmando a exclusão do livro.

---

### 2.5.8 Fluxo Principal 03 – Editar Livro

1. **[EV]** Na tela do dashboard administrativo, o administrador seleciona o livro e clica na opção **“Editar”**.
2. **[RS]** O sistema apresenta o formulário de edição com os dados previamente cadastrados do livro.
3. **[EV]** O administrador modifica os campos desejados (título, descrição, imagens, páginas do livro, idioma ou outras informações).
4. **[RS]** O sistema valida as alterações realizadas.
5. **[RS]** O sistema salva as alterações no banco de dados.
6. **[RS]** O sistema exibe o livro atualizado no painel administrativo.

---

### 2.5.9 Fluxos Alternativos

**1a. Administrador deseja editar um livro existente**

1. O administrador seleciona o livro desejado.
2. O sistema carrega os dados do livro.
3. O administrador realiza as alterações necessárias.
4. O administrador confirma as alterações.
5. O sistema salva os dados atualizados.
6. O fluxo retorna ao passo final do **Fluxo Principal 03**.

---

### 2.5.10 Fluxos de Exceção

**3a. Campo obrigatório não preenchido**  
- O sistema informa que os campos obrigatórios devem ser preenchidos para concluir a operação.

**4a. Duplicidade de livro**  
- O sistema informa que já existe um livro cadastrado com o mesmo título.

**4b. Formato de arquivo inválido**  
- O sistema informa que o formato do arquivo enviado não é permitido, indicando o formato correto aceito pelo sistema.

## DIAGRAMA DE CLASSES
	O diagrama de classes representa a estrutura de um sistema mostrando suas classes, atributos, métodos e os relacionamentos entre elas. É usado para modelar a arquitetura de um sistema orientado a objetos.

#a imagen irá aqui

Fonte: Elaboração própria (2025)


## Prototipos de tela
Protótipos de tela desenvolvidos no Figma, com foco em um layout simples, intuitivo e confortável para o usuário, utilizando bordas arredondadas e elementos visuais de maior destaque para facilitar a navegação e a usabilidade.

#aqui vou colocar as imagens


## REFERÊNCIAS BIBLIOGRÁFICAS CONSULTADAS:












> Projeto em *desenvolvimento* - IFRN-SPP |  2025 
