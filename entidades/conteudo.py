# Classe Base: Conteúdo

class Conteudo:
    def __init__(self, id_conteudo, nome_conteudo):
        self._id_conteudo = id_conteudo
        self._nome_conteudo = nome_conteudo.strip()
        self._interacoes = []

    def adicionar_interacao(self, interacao):
        self._interacoes.append(interacao)

    def calcular_total_interacoes_engajamento(self):
        tipos_engajamento = ["like", "share", "comment"]
        return len([i for i in self._interacoes if i.tipo_interacao in tipos_engajamento])

    def contar_tipos_interacao(self):
        contagem = {}
        for i in self._interacoes:
            tipo = i.tipo_interacao.lower()
            contagem[tipo] = contagem.get(tipo, 0) + 1
        return contagem

    def calcular_tempo_total_consumo(self):
        return sum(
            i.watch_duration_seconds for i in self._interacoes
            if isinstance(i.watch_duration_seconds, (int, float)) and i.watch_duration_seconds > 0
        )

    def calcular_media_tempo_consumo(self):
        tempos = [
            i.watch_duration_seconds for i in self._interacoes
            if isinstance(i.watch_duration_seconds, (int, float)) and i.watch_duration_seconds > 0
        ]
        return sum(tempos) / len(tempos) if tempos else 0

    def listar_comentarios(self):
        return [i.comment_text for i in self._interacoes if i.tipo_interacao == "comment"]

    def contar_visualizacoes(self):
        tipos_visualizacao = ["view_start", "play"]
        return len([
            i for i in self._interacoes
            if i.tipo_interacao.lower() in tipos_visualizacao
        ])

    @property
    def id_conteudo(self):
        return self._id_conteudo

    @property
    def nome_conteudo(self):
        return self._nome_conteudo

    def __str__(self):
        return f"Conteúdo: {self._nome_conteudo}"

    def __repr__(self):
        return f"Conteudo(id={self._id_conteudo}, nome='{self._nome_conteudo}')"


# Subclasse: Vídeo

class Video(Conteudo):
    def __init__(self, id_conteudo, nome_conteudo, duracao_total):
        super().__init__(id_conteudo, nome_conteudo)
        self.duracao_total = duracao_total

    def calcular_percentual_medio_assistido(self):
        if not self._interacoes or not self.duracao_total:
            return 0

        tempo_por_usuario = {}
        for interacao in self._interacoes:
            usuario_id = interacao.id_usuario
            tempo = interacao.watch_duration_seconds
            if isinstance(tempo, (int, float)) and tempo > 0:
                tempo_por_usuario[usuario_id] = tempo_por_usuario.get(usuario_id, 0) + tempo

        percentuais = [(tempo / self.duracao_total) * 100 for tempo in tempo_por_usuario.values()]
        return round(sum(percentuais) / len(percentuais), 2) if percentuais else 0

    def __str__(self):
        return f"[VÍDEO] {self.nome_conteudo} ({self.id_conteudo})"

    def __repr__(self):
        return f"Video(id={self.id_conteudo}, nome='{self.nome_conteudo}', duracao_total={self.duracao_total})"


# Subclasse: Podcast

class Podcast(Conteudo):
    def __init__(self, id_conteudo, nome_conteudo, duracao_total_episodio_seg):
        super().__init__(id_conteudo, nome_conteudo)
        self.__duracao_total_episodio_seg = duracao_total_episodio_seg

    @property
    def duracao_total_episodio_seg(self):
        return self.__duracao_total_episodio_seg


# Subclasse: Artigo

class Artigo(Conteudo):
    def __init__(self, id_conteudo, nome_conteudo, tempo_leitura_estimado_seg):
        super().__init__(id_conteudo, nome_conteudo)
        self.__tempo_leitura_estimado_seg = tempo_leitura_estimado_seg

    @property
    def tempo_leitura_estimado_seg(self):
        return self.__tempo_leitura_estimado_seg
