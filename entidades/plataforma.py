class Plataforma:
    """
    Representa uma plataforma onde o conteúdo é consumido ou a interação ocorre.
    """
    def __init__(self, nome_plataforma: str, id_plataforma: int = None):
        # Valida e atribui nome via setter
        self.nome_plataforma = nome_plataforma
        # Valida e atribui ID via setter (pode ser None)
        self.id_plataforma = id_plataforma

    @property
    def id_plataforma(self) -> int:
        return self.__id_plataforma

    @id_plataforma.setter
    def id_plataforma(self, novo_id: int):
        if novo_id is not None and not isinstance(novo_id, int):
            raise TypeError("O ID da plataforma deve ser um inteiro ou None.")
        self.__id_plataforma = novo_id

    @property
    def nome_plataforma(self) -> str:
        return self.__nome_plataforma

    @nome_plataforma.setter
    def nome_plataforma(self, novo_nome: str):
        if not novo_nome or not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome da plataforma não pode ser vazio.")
        self.__nome_plataforma = novo_nome.strip()

    def __str__(self) -> str:
        # Retorna apenas o nome, para apresentações amigáveis
        return self.__nome_plataforma

    def __repr__(self) -> str:
        # Inclui ID e nome para facilitar o debug
        return (
            f"Plataforma("
            f"id={self.__id_plataforma}, "
            f"nome='{self.__nome_plataforma}'"
            f")"
        )

    def __eq__(self, other) -> bool:
        # Compara pelo nome (case-insensitive)
        return (
            isinstance(other, Plataforma)
            and self.__nome_plataforma.lower() == other.__nome_plataforma.lower()
        )

    def __hash__(self) -> int:
        # Mesma lógica do eq()
        return hash(self.__nome_plataforma.lower())
