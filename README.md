# Montecarlo Galaxie Population (MGP)

## Descripción
Este programa en Python simula la evolución de estrellas basado en su masa inicial. Utiliza un enfoque probabilístico para modelar el nacimiento y la muerte de estrellas, categorizándolas en diferentes estados finales: Enanas Blancas (WD), Estrellas de Neutrones (NS) y Agujeros Negros (BH).

## Uso
Para ejecutar esta simulación, ejecutar la función `Main` con el número deseado de estrellas como argumento. Ejemplo: `Main(1000000)` para simular un millón de estrellas.

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Funciones

### Main(num)
Se encarga de todo el proceso de simulación de las estrellas asignandoles una edad y masa para luego clasificarlas segun secuencia principal y remanente.
- `num`: Número de estrellas a simular.
- El código cuenta con un sistema de clasificación mediante el uso de la función `np.where()` que se encarga de filtrar los datos.

## Salidas
El programa genera:
- Gráfico de la función de masa inicial (IMF) guardado como `imf.png`.
- Histograma de la tasa de formación estelar guardado como `timebirth.png`.
- Histograma de la masa final guardado como `masafinal.png`.
- Histogramas del tiempo guardados como `time.png` y `timezoom.png`.

## Resultados
Imprime la fracción de estrellas que terminan como estrellas de neutrones, agujeros negros, enanas blancas y aquellas que permanecen en la secuencia principal.

