"""Componente común del lazo de control."""


class ComponenteControl:
    """Guarda el identificador de un componente."""

    def __init__(self, identificador: str) -> None:
        self.identificador = identificador
