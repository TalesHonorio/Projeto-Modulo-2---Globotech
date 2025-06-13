class Usuario:
    """
    Representa um usuário da plataforma, com suas interações registradas.
    """
    def __init__(self, id_usuario):
        # Converte e valida id_usuario
        try:
            self.__id_usuario = int(id_usuario)
        except (TypeError, ValueError):
            raise ValueError("id_usuario deve ser um inteiro.")
        # Lista interna de Interacao
        self.__interacoes_realizadas = []

    @property
    def id_usuario(self) -> int:
        """ID único do usuário."""
        return self.__id_usuario

    @property
    def interacoes_realizadas(self) -> list:
        """Retorna cópia da lista de interações realizadas."""
        return list(self.__interacoes_realizadas)

    def registrar_interacao(self, interacao) -> None:
        """Adiciona uma interação à lista de interações realizadas."""
        self.__interacoes_realizadas.append(interacao)

    def obter_interacoes_por_tipo(self, tipo_desejado: str) -> list:
        """
        Filtra e retorna todas as interações cujo tipo coincide com tipo_desejado.
        """
        return [
            i for i in self.__interacoes_realizadas
            if i.tipo_interacao == tipo_desejado
        ]

    def obter_conteudos_unicos_consumidos(self) -> set:
        """
        Retorna um set de objetos Conteudo únicos consumidos por este usuário.
        """
        return {i.conteudo_associado for i in self.__interacoes_realizadas}

    def calcular_tempo_total_consumo_plataforma(self, plataforma) -> int:
        """
        Soma watch_duration_seconds de todas as interações feitas nesta plataforma.
        """
        return sum(
            i.watch_duration_seconds
            for i in self.__interacoes_realizadas
            if i.plataforma_interacao == plataforma
        )

    def plataformas_mais_frequentes(self, top_n=3) -> list:
        """
        Retorna as N plataformas (objetos Plataforma) mais utilizadas pelo usuário.
        """
        contagem = {}
        for i in self.__interacoes_realizadas:
            plat = i.plataforma_interacao
            contagem[plat] = contagem.get(plat, 0) + 1
        # Ordena por frequência decrescente e extrai apenas as plataformas
        ordenadas = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        return [plat for plat, _ in ordenadas[:top_n]]

    def __str__(self) -> str:
        return f"Usuário {self.__id_usuario}"

    def __repr__(self) -> str:
        return f"Usuario(id={self.__id_usuario})"
