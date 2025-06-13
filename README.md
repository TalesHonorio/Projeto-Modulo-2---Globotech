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


## Estrutura do Repositório

```bash
Projeto-Modulo-2---Globotech/ # Pacote Principal
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
├── diagrama.mermaid # Diagrama de classes do sistema
└── README.md # Este arquivo de documentação

```


## Objetivos do Projeto

- Aplicar **princípios de POO** (Herança, Encapsulamento, Métodos Mágicos)  
- Tornar o sistema mais **robusto**, **modular**, **extensível**, **coeso** e **reutilizável**  
- Continuar as métricas da Fase 1 em um **menu interativo** com relatório de engajamento  


## Descrição Geral

O sistema simula a ingestão e análise de interações de usuários com conteúdos Globo (vídeos, podcasts, artigos). A partir de um arquivo CSV, ele:

1. **Carrega** cada linha como uma instância de `Interacao`.  
2. **Gerencia** em memória:
   - **Plataforma** (nome e ID incremental)
   - **Conteúdo** (`Conteudo` e subclasses)
   - **Usuário** e suas interações
3. **Gera** relatórios textuais:
   - Total de interações de engajamento (`like`, `share`, `comment`)
   - Contagem por tipo (`view_start`, `like`, `share`, `comment`)
   - Tempo total e médio de consumo
   - Listagem de comentários
   - Top-5 conteúdos por visualizações



## Principais Conceitos e Componentes

1. **Plataforma**
   - Guarda nome e ID  
   - `@property` para validação e acesso  
   - Métodos mágicos: `__str__`, `__repr__`, `__eq__`, `__hash__`

2. **Conteúdo & Subclasses**
   - **Conteudo**: ID, nome, lista de interações  
     - `adicionar_interacao()`  
     - `calcular_total_interacoes_engajamento()`  
     - `calcular_contagem_por_tipo_interacao()`  
     - `calcular_tempo_total_consumo()` / `calcular_media_tempo_consumo()`  
     - `listar_comentarios()`  
   - **Fábrica**: `@classmethod criar_por_tipo()` escolhe `Video`, `Podcast` ou `Artigo`  
   - **Video**: adiciona `duracao_total_video_seg` + `calcular_percentual_medio_assistido()`  
   - **Podcast**: adiciona `duracao_total_episodio_seg`  
   - **Artigo**: adiciona `tempo_leitura_estimado_seg`

3. **Interação**
   - Converte e valida `id_usuario`, `timestamp`, `watch_duration_seconds`  
   - Restringe tipos a `view_start`, `like`, `share`, `comment`  
   - Atributos privados + `@property`  
   - Métodos mágicos: `__str__`, `__repr__`

4. **Usuário**
   - Armazena `id_usuario` e lista de `Interacao`  
   - Métodos para registrar, filtrar por tipo e descobrir plataformas mais frequentes

5. **SistemaAnaliseEngajamento**
   - **CRUD em memória**: dicionários para plataformas, conteúdos e usuários  
   - **Processamento do CSV** → criação de objetos  
   - **Vinculação**: cada `Interacao` é registrada em `Conteudo` e `Usuario`  
   - **Relatórios**: métricas, rankings e listas detalhadas

## Exemplo de Saída

```text
=== MENU PRINCIPAL ===
1 – Métricas de Conteúdos
2 – Informações de Usuários
3 – Informações de Conteúdos
4 – Informações de Plataformas
5 – Listar Podcasts
0 – Sair
Escolha uma opção: 1

=== MENU DE MÉTRICAS ===
1 – Total de interações por conteúdo
2 – Contagem por tipo de interação
3 – Tempo total de visualização
4 – Tempo médio de visualização
5 – Listar comentários
6 – Top-5 conteúdos mais visualizados
```
---

### Autores
- André Carioca
- Diego Teixeira
- Marcelo Zilotti
- Mirra Bernardo
- Tales Honorio
- William Lopes