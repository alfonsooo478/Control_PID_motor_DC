# Control PID de velocidad para un motor DC — Hito 2

Proyecto de EL4203 Programación Avanzada, opción B. El programa mide la
velocidad de un motor DC, calcula un voltaje con un controlador PID y actualiza
la velocidad en pasos de tiempo. Conserva el modelo sencillo del Hito 1.

## Archivos

| Archivo | Función |
|---|---|
| `componente_control.py` | Clase base con el identificador común. |
| `controlador_pid.py` | Calcula el voltaje proporcional, integral y derivativo. |
| `planta_motor.py` | Mantiene privada la velocidad y la actualiza gradualmente. |
| `sensor.py` | Mide la velocidad del motor. |
| `sistema_lazo_cerrado.py` | Conecta sensor, controlador y motor. |
| `buffer_errores.py` | Guarda los últimos errores en una cola FIFO. |
| `procesamiento_recursivo.py` | Suma recursivamente los errores recientes. |
| `main.py` | Crea los objetos y ejecuta la simulación. |

## Ejecución

Se necesita Python 3.10 o posterior. No hay paquetes externos que instalar.
Desde esta carpeta:

```powershell
python main.py
```

La simulación conserva los parámetros del `main.py` local del Hito 1: motor de
3000 RPM y 24 V, referencia de 1500 RPM, `kp=0.02`, `ki=0.03`, `kd=0.0001`,
1000 pasos de 0.01 s y un historial de 10 errores. La salida verificada es:

```text
Simulación terminada
Referencia: 1500.00 RPM
Velocidad: 1500.00 RPM
Voltaje: 12.00 V
```

## Cambios del Hito 2

Las clases del Hito 1 se separaron en archivos. `BufferErrores` usa
`collections.deque(maxlen=10)`: cada error nuevo entra al final y, cuando la
cola está llena, se descarta el más antiguo. El controlador toma de allí el
error anterior para la derivada. También calcula el promedio de los errores
recientes mediante `suma_recursiva()` y lo integra en cada paso. El caso base de
la recursión es un historial vacío, cuya suma es cero.

La herencia desde `ComponenteControl`, la composición del sistema, el límite
de voltaje y la velocidad privada del motor se conservan. `control_pid.py`
permanece en la rama `main` como versión original del Hito 1.

## Complejidad Big-O

Sea `n` la cantidad de muestras guardadas, `N` la capacidad del buffer y `P`
la cantidad de pasos de simulación. Siempre se cumple `n ≤ N`.

| Operación | `deque` | `list` |
|---|---:|---:|
| Agregar al final | O(1) | O(1) amortizado |
| Quitar la más antigua | O(1) | O(n) con `pop(0)` |
| Recorrer o copiar el historial | O(n) | O(n) |
| Memoria para `N` muestras | O(N) | O(N) |

`list.pop(0)` desplaza los elementos restantes; `deque` evita ese costo. La
suma recursiva realiza una llamada por muestra: `T(n) = T(n-1) + O(1)`, por lo
que usa O(n) tiempo y O(n) memoria de pila. Cada paso del control copia y suma
el historial en O(n), y la simulación completa cuesta O(PN) en el peor caso.
Aquí `N=10`, por lo que la recursión tiene una profundidad pequeña.

## Siguiente etapa

El Hito 3 queda pendiente: ruido de medición con NumPy, respuesta al escalón
y gráfico solicitado por la pauta.
