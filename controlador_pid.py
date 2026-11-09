"""Controlador PID de velocidad."""

from buffer_errores import BufferErrores
from componente_control import ComponenteControl
from procesamiento_recursivo import suma_recursiva


class ControladorPID(ComponenteControl):
    """Calcula el voltaje a partir del error de velocidad."""

    def __init__(
        self,
        identificador: str,
        kp: float,
        ki: float,
        kd: float,
        voltaje_maximo: float,
        capacidad_historial: int = 10,
    ) -> None:
        super().__init__(identificador)
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.voltaje_maximo = voltaje_maximo
        self.error_acumulado = 0.0
        self.historial_errores = BufferErrores(capacidad_historial)

    def calcular_accion(
        self,
        velocidad_deseada: float,
        velocidad_medida: float,
        paso_tiempo: float,
    ) -> float:
        """Calcula el voltaje con P, I y D para un paso de tiempo."""
        error_velocidad = velocidad_deseada - velocidad_medida
        self.historial_errores.agregar(error_velocidad)

        historial = self.historial_errores.historial()
        error_medio = suma_recursiva(historial) / len(historial)
        self.error_acumulado += error_medio * paso_tiempo

        error_anterior = self.historial_errores.obtener_error_anterior()
        if error_anterior is None:
            error_anterior = 0.0
        derivada = (error_velocidad - error_anterior) / paso_tiempo

        voltaje_control = (
            self.kp * error_velocidad
            + self.ki * self.error_acumulado
            + self.kd * derivada
        )

        if voltaje_control > self.voltaje_maximo:
            voltaje_control = self.voltaje_maximo
        elif voltaje_control < -self.voltaje_maximo:
            voltaje_control = -self.voltaje_maximo

        return voltaje_control
