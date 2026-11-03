"""Historial de los errores recientes de velocidad."""

from collections import deque


class BufferErrores:
    """Guarda las últimas muestras en una cola de capacidad fija."""

    def __init__(self, capacidad: int) -> None:
        # deque descarta automáticamente la muestra más antigua al llenarse.
        self._errores = deque(maxlen=capacidad)

    def agregar(self, error_velocidad: float) -> None:
        """Guarda un error nuevo al final de la cola."""
        self._errores.append(error_velocidad)

    def historial(self) -> tuple[float, ...]:
        """Entrega las muestras para calcular el promedio reciente."""
        return tuple(self._errores)

    def obtener_error_anterior(self) -> float | None:
        """Entrega la muestra previa para el término derivativo."""
        if len(self._errores) > 1:
            return self._errores[-2]
        return None
