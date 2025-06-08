class Plataforma:
    def __init__(self, nome_plataforma: str, id_plataforma: int = None):
        if not nome_plataforma or not nome_plataforma.strip():
            raise ValueError("O nome da plataforma não pode ser vazio.")

        self.__id_plataforma = id_plataforma
        self.__nome_plataforma = nome_plataforma.strip()

    @property
    def id_plataforma(self):
        return self.__id_plataforma

    @id_plataforma.setter
    def id_plataforma(self, novo_id: int):
        if novo_id is not None and not isinstance(novo_id, int):
            raise TypeError("O ID da plataforma deve ser um inteiro.")
        self.__id_plataforma = novo_id

    @property
    def nome_plataforma(self):
        return self.__nome_plataforma

    @nome_plataforma.setter
    def nome_plataforma(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome da plataforma não pode ser vazio.")
        self.__nome_plataforma = novo_nome.strip()

    def __str__(self):
        return self.__nome_plataforma

    def __repr__(self):
        return f"Plataforma(nome='{self.__nome_plataforma}')"

    def __eq__(self, other):
        if isinstance(other, Plataforma):
            return self.__nome_plataforma.lower() == other.__nome_plataforma.lower()
        return False

    def __hash__(self):
        return hash(self.__nome_plataforma.lower())
