"""Cálculo recursivo aplicado a las muestras recientes de error."""


def suma_recursiva(errores: tuple[float, ...], indice: int = 0) -> float:
    """Suma las muestras desde indice hasta el final del historial."""
    if indice == len(errores):
        return 0.0
    return errores[indice] + suma_recursiva(errores, indice + 1)
