class Interacao:
    _id_interacao_global = 1

    def __init__(self, conteudo_associado, id_usuario, timestamp_interacao, plataforma_interacao,
                 tipo_interacao, watch_duration_seconds=0, comment_text=""):

        if not conteudo_associado:
            raise ValueError("Conteúdo associado é obrigatório.")
        if not id_usuario:
            raise ValueError("ID de usuário é obrigatório.")
        if not timestamp_interacao:
            raise ValueError("Timestamp é obrigatório.")
        if not plataforma_interacao:
            raise ValueError("Plataforma é obrigatória.")
        if not tipo_interacao:
            raise ValueError("Tipo de interação é obrigatório.")

        self.__id_interacao = Interacao._id_interacao_global
        Interacao._id_interacao_global += 1

        self.__conteudo_associado = conteudo_associado
        self.__id_usuario = id_usuario
        self.__timestamp_interacao = timestamp_interacao
        self.__plataforma_interacao = plataforma_interacao
        self.__tipo_interacao = tipo_interacao.lower()
        self.__watch_duration_seconds = float(watch_duration_seconds) if watch_duration_seconds else 0
        self.__comment_text = comment_text.strip()

    @property
    def id_interacao(self):
        return self.__id_interacao

    @property
    def conteudo_associado(self):
        return self.__conteudo_associado

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def timestamp_interacao(self):
        return self.__timestamp_interacao

    @property
    def plataforma_interacao(self):
        return self.__plataforma_interacao

    @property
    def tipo_interacao(self):
        return self.__tipo_interacao

    @property
    def watch_duration_seconds(self):
        return self.__watch_duration_seconds

    @property
    def comment_text(self):
        return self.__comment_text

    def __str__(self):
        return f"Interação {self.__id_interacao} ({self.__tipo_interacao})"

    def __repr__(self):
        return f"Interacao(id={self.__id_interacao}, tipo='{self.__tipo_interacao}')"
