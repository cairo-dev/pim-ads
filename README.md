# Sistema de Gestão Educacional Simplificada

Este projeto foi desenvolvido como parte do PIM I (Projeto Integrado Multidisciplinar) do curso de Análise e Desenvolvimento de Sistemas da UNIP (1º semestre de 2025). O objetivo é aplicar os conhecimentos adquiridos nas disciplinas do semestre em um sistema funcional, construído em Python puro, utilizando arquivos JSON como banco de dados.

## 📌 Funcionalidades

- Cadastro de novos usuários com validação de senha e idade
- Login com controle de acessos
- Usuário comum:
  - Matricular-se em disciplinas
  - Visualizar suas matérias cadastradas
- Usuário administrador:
  - Cadastrar novas disciplinas
  - Gerar estatísticas:
    - Idade por disciplina
    - Quantidade de disciplinas por usuário
    - Quantidade de acessos por usuário

> 🔐 O acesso do administrador é feito com:
- Usuário: admin
- Senha: admin  
  - Essas credenciais devem ser usadas para acessar as funcionalidades de administração.

## 🛠 Tecnologias Utilizadas

- Python 3
- JSON para armazenamento de dados
- Bibliotecas padrão:
  - json
  - statistics

## 📁 Estrutura de Arquivos

- main.py → Arquivo principal do sistema
- usuarios.json → Armazena dados dos usuários
- materias.json → Armazena lista de disciplinas disponíveis
- README.md → Este arquivo

## 👨‍🏫 Disciplinas Integradas

- Pensamento Lógico Computacional com Python
- Infraestrutura Computacional
- Tecnologia da Informação e Comunicação
- Matemática e Estatística
- Ética, Cidadania e Sustentabilidade
- Cibersegurança
- LGPD (Lei Geral de Proteção de Dados)

## 🚀 Execução

Para rodar o sistema:

1. Instale o Python 3.x em seu computador
2. Clone este repositório:
   git clone https://github.com/cairo-dev/pim-ads
3. Execute o script:
   python main.py

(Ou, se estiver usando Linux/macOS: python3 main.py)
