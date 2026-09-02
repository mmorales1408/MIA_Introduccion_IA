## Aplicaciones a analizar

Describe PEAS para cada una de estas aplicaciones:

1. **Asistente virtual de voz** (p. ej. Siri, Alexa o Google Assistant en un altavoz inteligente).
2. **Robot aspirador doméstico** (p. ej. Roomba u otro robot que limpia pisos de un departamento).
3. **Sistema de recomendación de streaming** (p. ej. Netflix o Spotify que sugiere películas o canciones).
4. **Vehículo autónomo en ciudad** (conducción sin conductor en calles urbanas con tráfico y peatones).
5. **Agente de trading algorítmico en bolsa** (compra y venta automática de acciones en mercados financieros).
6. **Sistema de diagnóstico médico asistido por IA** (apoya a un médico a interpretar síntomas e imágenes clínicas).
7. **Dron de inspección de infraestructura** (revisa grietas, corrosión o fugas en puentes, tuberías o líneas eléctricas).
8. **Agente jugador de ajedrez** (programa que compite contra un humano u otro agente en partidas completas).

## Criterios de calidad

Performance: incluye métricas concretas (precisión, tiempo, costo, satisfacción del usuario, ganancia, seguridad, etc.), no solo “hacerlo bien”.
Environment: menciona si es parcialmente observable o totalmente observable, si es estocástico o determinista, episódico o secuencial, estático o dinámico, y discreto o continuo (según aplique).
Actuators: lista acciones reales que el agente puede ejecutar, no capacidades vagas.
Sensors: lista percepciones concretas (cámara, micrófono, API, historial de usuario, cotizaciones de mercado, etc.).

***

***
### Asistente virtual de voz 
- **Performance:**  Tiempo de respuesta, Precisión de entendimiento de la tarea, Satisfacción del usuario. 

- **Environment:** Host del asistente de voz (AWS, GPC, Azure etc), APIs de servicios que el asistente pueda utilzar, host físico del asistente (una computadora, el hardware de Alexa, un teléfono).
El ambiente es parcialmente observable, ya que el asistente no conoce por ejemplo los resultados de las APIs sino hasta que la consulta. 
El ambiente es estocástico ya que es imposible que el asistente tenga certeza de todos las respuestas de servicios externos. Por ejemplo, la pregunta "¿a qué temperatura estamos?" hecha en días distintos muy probablemente tenga respuestas distintas.
El ambiente es secuencial, ya que la respuesta de un asistente puede directamente afectar a desiciones futuras. Por ejemplo, la respuesta al request "Pon música" condiciona totalmente al siguiente request de "pausa".
El ambiente es dinámico. Bajo la misma premisa del ejemplo de ayer del clima, si yo le pregunto a un asistente "¿Va a llover en la próxima hora?" y tarda dos horas en darme una respuesta, el ambiente (en este caso, la respuesta del API de clima) es distinta al momento en el que yo hice la pregunta.
El ambiente podría ser considerado como contínuo. En teoría, existe un número infinito de segundos de delay que pueden existir entre un request y la respuesta del asistente, así como hay teóricamente un numero infinito de modos en los que el usuario pudiera formular una pregunta independientemente de si el asistente puede o no dar una respuesta a la misma.

- **Actuators:** Bocinas del asistente de voz, una pantalla (si aplica), su WIFI integrado (al momento de actuar sobre dispositivos inteligentes)

- **Sensors:** Los micrófonos utilizados por el asistente, la red WIFI a la que esté conectada.

***
### Robot aspirador doméstico
- **Performance:** Tiempo que tarda en limpiar el espacio deseado, fuerza de aspirado, alcance del espacio de aspirado, autonomía de la batería.

- **Environment:** Espacio físico en el que la aspiradora se mueve (como una casa).
El ambiente es parcialmente observable porque el robot necesita moverse para ir "desbloqueando" espacios para aspirar sin saber de antemano qué obstáculos va a tener o dónde está limpio y dónde no.
El ambiente es estocástico ya que pueden haber obstáculos innesperados en el ambiente como una alfombra o unos calcetines tirados en el espacio donde el robot necesita pasar.
El ambiente es secuencial, porque el hecho de que el robot termine de aspirar una habitación condiciona totalmente a que no vuelva a pasar por ahí, porque ya no es necesario.
El ambiente es dinámico ya que el espacio puede tener obstaculos o condicionales que van cambiando mientras el robot limpia. Por ejemplo un perro que esté dentro de la casa.
El ambiente es continuo porque hay variables continuas como la velocidad del robot, la fuerza de succión, el angulo en el que avanza, etc.

- **Actuators:** Bocinas (como en las estaciones de carga), ruedas, cepillos, motor de succión.

- **Sensors:** Cámara o sensor infrarrojo, sensor de distancia (para evitar caidas), la red WIFI a la que esté conectada.

***
### Sistema de recomendación de streaming
- **Performance:** Tiempo que el usuario final terminó consumiendo una opción recomendada por el agente, calificación explícita del usuario sobre la opcion recomendada (como en Netflix que puedes poner si una película te gustó o en Spotify que le puedes dar like).

- **Environment:** Host del agente de recomendación y la plataforma misma en caso de que sean distintas.
El ambiente es parcialmente observable, porque aunque tiene contexto total de las interacciones previas del usuario y del historial del comportamiento, hay muchas condiciones del usuario mismo que interactúan con el agente de las que el agente no tiene conocimiento (quizá tiene ganas de ver algo que ya vió, quizá nada más está entrando a agregar cosas a la watchlist, etc)
El ambiente es no determinista. Por el mismo motivo de que el usuario cuenta con muchas condiciones no observables que impactan en elegir o no el contenido recomendado, el recomendar el mismo resultado en distintos momentos puede tener distintas respuestas.
El ambiente es secuencial, ya que dependiendo del performance de cada recomendación, el proximo batch de recomendaciones está condicionado al anterior. (Si el usuario calificó con 1/5 estrellas a una película de acción, afectará el próximo batch de recomendaciones)
El ambiente es semidinámico, ya que aunque el ambiente no cambia con el tiempo, la satisfacción del usuario sí se ve afectada.
El ambiente es discreto, ya que la lista de películas recomendadas, el historia, y la calificación del usuario sobre la película se mide de manera discreta.

- **Actuators:**
Interfaz de la plataforma

- **Sensors:**
Historial de contenido consumido por el usuario. Calificación dada al contenido consumido, metadata de navegación (dispositivo, hora, perfil, edad, etc).

***
### Vehículo autónomo en la ciudad

- **Performance:**

- **Environment:**

- **Actuators:**

- **Sensors:** Velocímetro, tacómetro, 