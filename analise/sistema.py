from entidades.plataforma import Plataforma
from entidades.usuario import Usuario

class SistemaAnaliseEngajamento:
    VERSAO_ANALISE = "2.0"

    def __init__(self):
        self.__plataformas_registradas = {}
        self.__conteudos_registrados = {}
        self.__usuarios_registrados = {}
        self.__proximo_id_plataforma = 1

    def cadastrar_plataforma(self, nome_plataforma):
        if nome_plataforma not in self.__plataformas_registradas:
            plataforma = Plataforma(nome_plataforma, id_plataforma=self.__proximo_id_plataforma)
            self.__plataformas_registradas[nome_plataforma] = plataforma
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome_plataforma]

    def obter_plataforma(self, nome_plataforma):
        return self.__plataformas_registradas.get(nome_plataforma) or self.cadastrar_plataforma(nome_plataforma)

    def listar_plataformas(self):
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, caminho_arquivo):
        import csv
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)

    def processar_interacoes_do_csv(self, caminho_arquivo):
        from entidades.conteudo import Video
        from entidades.interacao import Interacao

        dados = self._carregar_interacoes_csv(caminho_arquivo)
        for linha in dados:
            try:
                plataforma = self.obter_plataforma(linha["plataforma"])

                id_conteudo = linha["id_conteudo"]
                nome_conteudo = linha["nome_conteudo"]
                if id_conteudo not in self.__conteudos_registrados:
                    self.__conteudos_registrados[id_conteudo] = Video(id_conteudo, nome_conteudo, 300)
                conteudo = self.__conteudos_registrados[id_conteudo]

                id_usuario = linha["id_usuario"]
                if id_usuario not in self.__usuarios_registrados:
                    self.__usuarios_registrados[id_usuario] = Usuario(id_usuario)
                usuario = self.__usuarios_registrados[id_usuario]

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
            except Exception as e:
                print(f"Erro ao processar linha: {e}")

    def gerar_relatorio_engajamento_conteudos(self, top_n=None):
        conteudos = list(self.__conteudos_registrados.values())
        if top_n:
            conteudos = sorted(conteudos, key=lambda c: c.calcular_total_interacoes_engajamento(), reverse=True)[:top_n]
        for c in conteudos:
            print(f"{c.nome_conteudo} - {c.calcular_total_interacoes_engajamento()} interações")

    def gerar_relatorio_atividade_usuarios(self, top_n=None):
        usuarios = list(self.__usuarios_registrados.values())
        if top_n:
            usuarios = sorted(usuarios, key=lambda u: len(u._Usuario__interacoes_realizadas), reverse=True)[:top_n]
        for u in usuarios:
            print(f"{u.id_usuario} - {len(u._Usuario__interacoes_realizadas)} interações")

    def identificar_top_conteudos(self, metrica, n):
        metrica_func = {
            'tempo_total_consumo': lambda c: c.calcular_tempo_total_consumo(),
            'media_tempo_consumo': lambda c: c.calcular_media_tempo_consumo(),
            'visualizacoes': lambda c: c.contar_visualizacoes()
        }.get(metrica)

        if not metrica_func:
            print("Métrica inválida.")
            return

        conteudos = sorted(self.__conteudos_registrados.values(), key=metrica_func, reverse=True)[:n]
        print(f"\nTop {n} conteúdos por {metrica.replace('_', ' ')}:")
        for c in conteudos:
            print(f"{c.nome_conteudo}: {metrica_func(c)}")
