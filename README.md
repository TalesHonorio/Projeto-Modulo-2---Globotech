# Projeto Módulo 2 - Globotech

*Fase 2 do projeto unificado "Análise de Engajamento de Mídias Globo com Orientação a Objetos"*

## Dependências

Este projeto foi desenvolvido utilizando apenas **Python puro**, sem bibliotecas externas.  
Todas as funcionalidades utilizam exclusivamente módulos da **biblioteca padrão** do Python.

- **Versão recomendada do Python:** 3.8 ou superior

**Ferramentas utilizadas no desenvolvimento:**
- **Editor de código:** Visual Studio Code (VSCode)
- **Controle de versão e colaboração:** Git e GitHub

>**Observação:**  
Para executar o projeto, basta ter o Python instalado.  
Não é necessário rodar `pip install` ou utilizar qualquer gerenciador de pacotes.

---

## Estrutura do Repositório

```bash
projeto_engajamento_fase2/ # Pacote Principal
│__init__.py
├── entidades/ # Sub-pacote
│   ├── plataforma.py # Classe Plataforma
│   ├── conteudo.py # Classe Conteudo e subclasses (Video, Podcast, Artigo)
│   ├── interacao.py # Classe Interacao
│   ├── usuario.py # Classe Usuario
│
├── analise/ # Sub-pacote
│   └── sistema.py # Classe SistemaAnaliseEngajamento (orquestradora)
│
├── main.py # Script principal de execução
├── interacoes_globo.csv # Arquivo de dados de entrada
└── README.md # Este arquivo de documentação

```

## Objetivos do Projeto

Nesta segunda fase, o foco principal foi aplicar os **princípios da Programação Orientada a Objetos (POO)** sobre a base lógica desenvolvida na fase anterior, garantindo um sistema mais:

- Robusto
- Modular
- Extensível
- Coeso e reutilizável

---

## Componentes e Funcionalidades

### Modelagem Orientada a Objetos

As principais entidades do sistema foram representadas por classes:

- **Plataforma**: Representa o local de interação (ex: G1, Globoplay)
- **Conteudo (e subclasses)**: 
  - `Video`: com duração total do vídeo
  - `Podcast`: com duração do episódio
  - `Artigo`: com tempo estimado de leitura
- **Interacao**: Modela cada interação do usuário (view, like, share, comment)
- **Usuario**: Representa o usuário e suas interações

Cada classe foi construída com:
- Atributos encapsulados
- Validação de dados com `property`
- Métodos específicos de cálculo
- Métodos mágicos `__str__`, `__repr__`, `__eq__`, `__hash__`

---

### Sistema de Análise

A classe `SistemaAnaliseEngajamento` centraliza o gerenciamento e análise:

- **Gerenciamento interno ("CRUD")** de plataformas, conteúdos e usuários
- **Processamento de interações via CSV** e transformação em objetos
- **Vinculação lógica** entre usuários, conteúdos e plataformas
- **Geração de relatórios**, incluindo:
  - Total de interações
  - Contagem por tipo
  - Tempo total e médio de consumo
  - Comentários por conteúdo
  - Top conteúdos por engajamento

---

### Autores
- André Carioca
- Diego Teixeira
- Marcelo Zilotti
- Mirra Bernardo
- Tales Honorio
- William Lopes