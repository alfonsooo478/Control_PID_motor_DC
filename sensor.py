"""Sensor ideal de velocidad del motor."""

from componente_control import ComponenteControl


class Sensor(ComponenteControl):
    """Conserva la última velocidad medida en RPM."""

    def __init__(self, identificador: str) -> None:
        super().__init__(identificador)
        self.ultima_medicion = 0.0

    def medir(self, velocidad_real: float) -> float:
        """Registra la velocidad real como medición ideal."""
        self.ultima_medicion = velocidad_real
        return self.ultima_medicion
