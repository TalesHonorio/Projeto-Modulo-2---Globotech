# Classe Usuario

class Usuario:
    def __init__(self, id_usuario):
        self.__id_usuario = id_usuario
        self.__interacoes_realizadas = []

    @property
    def id_usuario(self):
        return self.__id_usuario

    def registrar_interacao(self, interacao):
        self.__interacoes_realizadas.append(interacao)

    def obter_interacoes_por_tipo(self, tipo_desejado: str):
        return [i for i in self.__interacoes_realizadas if i.tipo_interacao == tipo_desejado]

    def obter_conteudos_unicos_consumidos(self):
        return set(i.conteudo_associado for i in self.__interacoes_realizadas)

    def calcular_tempo_total_consumo_plataforma(self, plataforma):
        return sum([
            i.watch_duration_seconds for i in self.__interacoes_realizadas
            if i.plataforma_interacao == plataforma and isinstance(i.watch_duration_seconds, (int, float))
        ])

    def plataformas_mais_frequentes(self, top_n=3):
        contagem = {}
        for i in self.__interacoes_realizadas:
            nome = i.plataforma_interacao.nome_plataforma
            contagem[nome] = contagem.get(nome, 0) + 1
        ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        return ordenadas[:top_n]

    def __str__(self):
        return f"Usuário {self.__id_usuario}"

    def __repr__(self):
        return f"Usuario(id={self.__id_usuario})"
