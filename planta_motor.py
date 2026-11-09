"""Modelo simplificado de la velocidad de un motor DC."""

from componente_control import ComponenteControl


class PlantaMotor(ComponenteControl):
    """Actualiza gradualmente la velocidad al recibir un voltaje."""

    def __init__(
        self,
        identificador: str,
        velocidad_maxima: float,
        voltaje_maximo: float,
        constante_tiempo: float,
    ) -> None:
        super().__init__(identificador)
        self.velocidad_maxima = velocidad_maxima
        self.voltaje_maximo = voltaje_maximo
        self.constante_tiempo = constante_tiempo
        self.__velocidad_actual = 0.0

    def get_velocidad_actual(self) -> float:
        """Permite leer la velocidad privada en RPM."""
        return self.__velocidad_actual

    def aplicar_voltaje(self, voltaje: float, paso_tiempo: float) -> float:
        """Acerca la velocidad actual a la objetivo durante el paso dado."""
        if voltaje > self.voltaje_maximo:
            voltaje = self.voltaje_maximo
        elif voltaje < -self.voltaje_maximo:
            voltaje = -self.voltaje_maximo

        velocidad_objetivo = (
            voltaje / self.voltaje_maximo * self.velocidad_maxima
        )
        factor_inercia = paso_tiempo / self.constante_tiempo

        if factor_inercia > 0.5:
            factor_inercia = 0.5

        cambio = factor_inercia * (
            velocidad_objetivo - self.__velocidad_actual
        )
        self.__velocidad_actual += cambio
        return self.__velocidad_actual
