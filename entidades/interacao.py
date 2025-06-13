from datetime import datetime

class Interacao:
    """
    Representa uma única interação de um usuário com um conteúdo em uma plataforma.
    Ajustes para aceitar exatamente 'view_start' do CSV e tratar durações vazias ou não inteiras.
    """
    TIPOS_INTERACAO_VALIDOS = {'view_start', 'like', 'share', 'comment'}
    _id_interacao_global = 1

    def __init__(self,
                 conteudo_associado,
                 id_usuario,
                 timestamp_interacao,
                 plataforma_interacao,
                 tipo_interacao,
                 watch_duration_seconds=0,
                 comment_text=""):
        # valida conteúdo associado
        if conteudo_associado is None:
            raise ValueError("Conteúdo associado é obrigatório.")

        # converte e valida id de usuário
        try:
            id_usuario = int(id_usuario)
        except (TypeError, ValueError):
            raise ValueError("ID de usuário deve ser um inteiro.")

        # valida e converte timestamp
        if timestamp_interacao is None:
            raise ValueError("Timestamp é obrigatório.")
        if isinstance(timestamp_interacao, str):
            try:
                timestamp = datetime.fromisoformat(timestamp_interacao)
            except ValueError:
                raise ValueError("Timestamp inválido. Use formato ISO 8601.")
        elif isinstance(timestamp_interacao, datetime):
            timestamp = timestamp_interacao
        else:
            raise ValueError("Timestamp deve ser str ISO-8601 ou datetime.")
        
        # valida plataforma
        if plataforma_interacao is None:
            raise ValueError("Plataforma é obrigatória.")

        # normaliza e valida tipo de interação (exatamente 'view_start', 'like', 'share', 'comment')
        tipo_norm = tipo_interacao.strip().lower()
        if tipo_norm not in Interacao.TIPOS_INTERACAO_VALIDOS:
            raise ValueError(f"Tipo de interação inválido: '{tipo_interacao}'")

        # trata watch_duration_seconds faltante ou vazio como 0
        raw = watch_duration_seconds
        if isinstance(raw, str) and not raw.strip():
            raw = 0
        # tenta converter para número e depois para int
        try:
            duration = int(float(raw))
        except (TypeError, ValueError):
            duration = 0
        # garante não-negatividade
        if duration < 0:
            raise ValueError("watch_duration_seconds deve ser ≥ 0.")

        # atribuição de ID sequencial
        self.__id_interacao = Interacao._id_interacao_global
        Interacao._id_interacao_global += 1

        # atribuições finais
        self.__conteudo_associado = conteudo_associado
        self.__id_usuario = id_usuario
        self.__timestamp_interacao = timestamp
        self.__plataforma_interacao = plataforma_interacao
        self.__tipo_interacao = tipo_norm
        self.__watch_duration_seconds = duration
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
        return (f"Interacao(id={self.__id_interacao}, "
                f"tipo='{self.__tipo_interacao}', "
                f"duracao={self.__watch_duration_seconds}s)")
