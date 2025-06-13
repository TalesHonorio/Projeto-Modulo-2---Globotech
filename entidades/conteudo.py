from typing import List, Dict

class Conteudo:
    """
    Representa um item de conteúdo consumível, com lista de interações.
    """
    def __init__(self, id_conteudo, nome_conteudo):
        # validação de inputs
        try:
            id_conteudo = int(id_conteudo)
        except (TypeError, ValueError):
            raise ValueError("id_conteudo deve ser um inteiro.")
        
        nome = nome_conteudo.strip()
        if not nome:
            raise ValueError("nome_conteudo não pode ser vazio.")

        # atributos privados/protegidos
        self._id_conteudo: int = id_conteudo
        self._nome_conteudo: str = nome
        self._interacoes: List = []

    def adicionar_interacao(self, interacao):
        """Registra uma nova interação neste conteúdo."""
        self._interacoes.append(interacao)

    def calcular_total_interacoes_engajamento(self) -> int:
        """
        Retorna o total de interações de engajamento:
        soma dos tipos 'like', 'share' e 'comment' apenas.
        """
        tipos_engajamento = {"like", "share", "comment"}
        return sum(1 for i in self._interacoes if i.tipo_interacao in tipos_engajamento)


    def calcular_contagem_por_tipo_interacao(self) -> Dict[str, int]:
        """
        Retorna dicionário {tipo: quantidade} para cada tipo de interação.
        """
        contagem: Dict[str, int] = {}
        for i in self._interacoes:
            t = i.tipo_interacao
            contagem[t] = contagem.get(t, 0) + 1
        return contagem

    def calcular_tempo_total_consumo(self) -> int:
        """
        Soma watch_duration_seconds de todas as interações positivas.
        """
        return sum(
            i.watch_duration_seconds 
            for i in self._interacoes 
            if i.watch_duration_seconds > 0
        )

    def calcular_media_tempo_consumo(self) -> float:
        """
        Retorna a média de watch_duration_seconds > 0.
        """
        tempos = [
            i.watch_duration_seconds 
            for i in self._interacoes 
            if i.watch_duration_seconds > 0
        ]
        return (sum(tempos) / len(tempos)) if tempos else 0.0

    def listar_comentarios(self) -> List[str]:
        """
        Retorna lista com todos os comment_text de interações 'comment'.
        """
        return [i.comment_text for i in self._interacoes if i.tipo_interacao == "comment"]

    @property
    def id_conteudo(self) -> int:
        return self._id_conteudo

    @property
    def nome_conteudo(self) -> str:
        return self._nome_conteudo

    def __str__(self) -> str:
        return f"Conteúdo: {self._nome_conteudo}"

    def __repr__(self) -> str:
        return f"Conteudo(id={self._id_conteudo}, nome='{self._nome_conteudo}')"

    @classmethod
    def criar_por_tipo(cls, id_conteudo, nome_conteudo):
        """
        Fábrica que escolhe Video, Podcast ou Artigo
        com base em palavras-chave em nome_conteudo.
        """
        nome_lower = nome_conteudo.lower()
        # prioridade: podcast, artigo, senão vídeo
        if "podcast" in nome_lower:
            # duração inicial zero; pode ajustar depois
            return Podcast(id_conteudo, nome_conteudo, duracao_total_episodio_seg=0)
        elif "documentário" in nome_lower or "artigo" in nome_lower:
            return Artigo(id_conteudo, nome_conteudo, tempo_leitura_estimado_seg=0)
        else:
            return Video(id_conteudo, nome_conteudo, duracao_total_video_seg=0)

class Video(Conteudo):
    """
    Especialização de Conteudo para vídeos, com cálculo de percentual médio.
    """
    def __init__(self, id_conteudo, nome_conteudo, duracao_total_video_seg):
        super().__init__(id_conteudo, nome_conteudo)
        # validação
        try:
            d = int(duracao_total_video_seg)
        except (TypeError, ValueError):
            raise ValueError("duracao_total_video_seg deve ser inteiro.")
        if d < 0:
            raise ValueError("duracao_total_video_seg deve ser ≥ 0.")
        self.__duracao_total_video_seg = d

    @property
    def duracao_total_video_seg(self) -> int:
        return self.__duracao_total_video_seg

    def calcular_percentual_medio_assistido(self) -> float:
        """
        ((tempo médio por usuário) / duracao_total_video_seg) * 100.
        """
        if self.__duracao_total_video_seg == 0 or not self._interacoes:
            return 0.0

        por_usuario: Dict[int, int] = {}
        for it in self._interacoes:
            if it.watch_duration_seconds > 0:
                por_usuario[it.id_usuario] = por_usuario.get(it.id_usuario, 0) + it.watch_duration_seconds

        percentuais = [
            (tempo / self.__duracao_total_video_seg) * 100 
            for tempo in por_usuario.values()
        ]
        return round(sum(percentuais) / len(percentuais), 2) if percentuais else 0.0

    def __str__(self) -> str:
        return f"[VÍDEO] {self.nome_conteudo} (ID {self.id_conteudo})"

    def __repr__(self) -> str:
        return (
            f"Video(id={self.id_conteudo}, nome='{self.nome_conteudo}', "
            f"duracao_total={self.__duracao_total_video_seg})"
        )


class Podcast(Conteudo):
    """
    Especialização de Conteudo para podcasts, com duração de episódio.
    """
    def __init__(self, id_conteudo, nome_conteudo, duracao_total_episodio_seg):
        super().__init__(id_conteudo, nome_conteudo)
        try:
            d = int(duracao_total_episodio_seg)
        except (TypeError, ValueError):
            raise ValueError("duracao_total_episodio_seg deve ser inteiro.")
        if d < 0:
            raise ValueError("duracao_total_episodio_seg deve ser ≥ 0.")
        self.__duracao_total_episodio_seg = d

    @property
    def duracao_total_episodio_seg(self) -> int:
        return self.__duracao_total_episodio_seg


class Artigo(Conteudo):
    """
    Especialização de Conteudo para artigos, com tempo estimado de leitura.
    """
    def __init__(self, id_conteudo, nome_conteudo, tempo_leitura_estimado_seg):
        super().__init__(id_conteudo, nome_conteudo)
        try:
            t = int(tempo_leitura_estimado_seg)
        except (TypeError, ValueError):
            raise ValueError("tempo_leitura_estimado_seg deve ser inteiro.")
        if t < 0:
            raise ValueError("tempo_leitura_estimado_seg deve ser ≥ 0.")
        self.__tempo_leitura_estimado_seg = t

    @property
    def tempo_leitura_estimado_seg(self) -> int:
        return self.__tempo_leitura_estimado_seg
