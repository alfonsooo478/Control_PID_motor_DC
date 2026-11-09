"""Coordinación de un paso del lazo cerrado."""

from controlador_pid import ControladorPID
from planta_motor import PlantaMotor
from sensor import Sensor


class SistemaLazoCerrado:
    """Conecta el controlador, el motor y el sensor."""

    def __init__(
        self,
        controlador: ControladorPID,
        motor: PlantaMotor,
        sensor: Sensor,
    ) -> None:
        self.controlador = controlador
        self.motor = motor
        self.sensor = sensor
        self.velocidad_deseada = 0.0

    def set_velocidad_deseada(self, velocidad: float) -> None:
        """Establece la referencia de velocidad en RPM."""
        self.velocidad_deseada = velocidad

    def ejecutar_paso(self, paso_tiempo: float) -> dict:
        """Mide, calcula el voltaje y actualiza la velocidad del motor."""
        velocidad_medida = self.sensor.medir(
            self.motor.get_velocidad_actual()
        )
        voltaje = self.controlador.calcular_accion(
            self.velocidad_deseada,
            velocidad_medida,
            paso_tiempo,
        )
        nueva_velocidad = self.motor.aplicar_voltaje(
            voltaje, paso_tiempo
        )

        return {
            "velocidad_deseada": self.velocidad_deseada,
            "velocidad_medida": velocidad_medida,
            "voltaje": voltaje,
            "velocidad_motor": nueva_velocidad,
        }
