import csv
from entidades.plataforma import Plataforma
from entidades.usuario import Usuario
from entidades.conteudo import Conteudo, Video, Podcast, Artigo
from entidades.interacao import Interacao

class SistemaAnaliseEngajamento:
    """
    Orquestra Plataformas, Conteúdos, Usuários e Interações,
    processa o CSV e gera relatórios de engajamento.
    """
    VERSAO_ANALISE = "2.0"

    def __init__(self):
        self.__plataformas_registradas = {}    # {nome_plataforma: Plataforma}
        self.__conteudos_registrados = {}      # {id_conteudo: Conteudo}
        self.__usuarios_registrados = {}       # {id_usuario: Usuario}
        self.__proximo_id_plataforma = 1

    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        if nome_plataforma not in self.__plataformas_registradas:
            p = Plataforma(nome_plataforma, id_plataforma=self.__proximo_id_plataforma)
            self.__plataformas_registradas[nome_plataforma] = p
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome_plataforma]

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        return (self.__plataformas_registradas.get(nome_plataforma)
                or self.cadastrar_plataforma(nome_plataforma))

    def listar_plataformas(self) -> list[Plataforma]:
        return list(self.__plataformas_registradas.values())

    def listar_conteudos(self) -> list[Conteudo]:
        return list(self.__conteudos_registrados.values())

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.__usuarios_registrados.values())

    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> list[dict]:
        with open(caminho_arquivo, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def processar_interacoes_do_csv(self, caminho_arquivo: str) -> None:
        for linha in self._carregar_interacoes_csv(caminho_arquivo):
            try:
                # Plataforma
                plataforma = self.obter_plataforma(linha["plataforma"])

                # Conteúdo — fábrica na própria classe Conteudo
                id_conteudo = int(linha["id_conteudo"])
                nome_conteudo = linha["nome_conteudo"]
                if id_conteudo not in self.__conteudos_registrados:
                    conteudo = Conteudo.criar_por_tipo(id_conteudo, nome_conteudo)
                    self.__conteudos_registrados[id_conteudo] = conteudo
                conteudo = self.__conteudos_registrados[id_conteudo]

                # Usuário
                id_usuario = int(linha["id_usuario"])
                if id_usuario not in self.__usuarios_registrados:
                    self.__usuarios_registrados[id_usuario] = Usuario(id_usuario)
                usuario = self.__usuarios_registrados[id_usuario]

                # Interação
                interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=id_usuario,
                    timestamp_interacao=linha["timestamp_interacao"],
                    plataforma_interacao=plataforma,
                    tipo_interacao=linha["tipo_interacao"],
                    watch_duration_seconds=linha.get("watch_duration_seconds", 0),
                    comment_text=linha.get("comment_text", "")
                )

                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)

            except ValueError as e:
                print(f"Erro ao processar linha: {e}")
            except KeyError as e:
                print(f"Coluna faltando no CSV: {e}")

    def gerar_relatorio_engajamento_conteudos(self, top_n: int = None) -> None:
        conteudos = self.listar_conteudos()
        if top_n is not None:
            conteudos = sorted(
                conteudos,
                key=lambda c: c.calcular_total_interacoes_engajamento(),
                reverse=True
            )[:top_n]

        for c in conteudos:
            total = c.calcular_total_interacoes_engajamento()
            print(f"ID: {c.id_conteudo} | Nome: {c.nome_conteudo} | Interacoes: {total}")

    def gerar_relatorio_atividade_usuarios(self, top_n: int = None) -> None:
        usuarios = self.listar_usuarios()
        if top_n is not None:
            usuarios = sorted(
                usuarios,
                key=lambda u: len(u.interacoes_realizadas),
                reverse=True
            )[:top_n]

        for u in usuarios:
            total = len(u.interacoes_realizadas)
            print(f"ID: {u.id_usuario} | Interacoes: {total}")

    def listar_conteudos_por_tipo(self, tipo: str) -> list[Conteudo]:
        """
        Retorna apenas os Conteudo do tipo 'video', 'podcast' ou 'artigo'.
        """
        mapping = {
            'video': Video,
            'podcast': Podcast,
            'artigo': Artigo,
        }
        cls = mapping.get(tipo.lower())
        return [c for c in self.listar_conteudos() if isinstance(c, cls)] if cls else []

    def identificar_top_por_tipo(self, tipo: str, top_n: int = 5) -> None:
        """
        Exibe os top N conteúdos de um determinado tipo
        ordenados por engajamento.
        """
        conteudos = self.listar_conteudos_por_tipo(tipo)
        top = sorted(
            conteudos,
            key=lambda c: c.calcular_total_interacoes_engajamento(),
            reverse=True
        )[:top_n]

        print(f"\nTop {top_n} {tipo}s por interações:")
        for c in top:
            total = c.calcular_total_interacoes_engajamento()
            print(f"ID: {c.id_conteudo} | Nome: {c.nome_conteudo} | Interacoes: {total}")
