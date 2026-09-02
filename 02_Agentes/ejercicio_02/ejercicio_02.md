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

Performance: incluye métricas concretas (precisión, tiempo, costo, satisfacción del usuario, ganancia, seguridad, etc.), no solo “hacerlo bien".
Environment: menciona si es parcialmente observable o totalmente observable, si es estocástico o determinista, episódico o secuencial, estático o dinámico, y discreto o continuo (según aplique).
Actuators: lista acciones reales que el agente puede ejecutar, no capacidades vagas.
Sensors: lista percepciones concretas (cámara, micrófono, API, historial de usuario, cotizaciones de mercado, etc.).

***

***
### Asistente virtual de voz
- **Performance:** tiempo de respuesta, precisión de entendimiento de la tarea, satisfacción del usuario.

- **Environment:** host del asistente de voz (AWS, GCP, Azure, etc.), APIs de servicios que el asistente pueda utilizar, host físico del asistente (una computadora, el hardware de Alexa, un teléfono).
El ambiente es parcialmente observable, ya que el asistente no conoce, por ejemplo, los resultados de las APIs sino hasta que realiza la consulta.
El ambiente es estocástico, ya que es imposible que el asistente tenga certeza de todas las respuestas de servicios externos. Por ejemplo, la pregunta “¿a qué temperatura estamos?" hecha en días distintos probablemente tendrá respuestas distintas.
El ambiente es secuencial, ya que la respuesta de un asistente puede afectar directamente decisiones futuras. Por ejemplo, la respuesta a la solicitud “Pon música" condiciona totalmente la siguiente solicitud de “pausa".
El ambiente es dinámico. Bajo la misma premisa del ejemplo del clima, si le pregunto a un asistente “¿Va a llover en la próxima hora?" y tarda dos horas en darme una respuesta, el ambiente (en este caso, la respuesta de la API de clima) es distinto al momento en el que hice la pregunta.
El ambiente podría considerarse continuo. En teoría, existe un número infinito de segundos de retraso que pueden existir entre una solicitud y la respuesta del asistente, así como también hay un número infinito de formas en que el usuario podría formular una pregunta, independientemente de si el asistente puede o no responderla.

- **Actuators:** Bocinas del asistente de voz, una pantalla (si aplica), su WIFI integrado (al momento de actuar sobre dispositivos inteligentes)

- **Sensors:** Los micrófonos utilizados por el asistente, la red WIFI a la que esté conectada.

***
### Robot aspirador doméstico
- **Performance:** tiempo que tarda en limpiar el espacio deseado, fuerza de aspirado, alcance del espacio de aspirado, autonomía de la batería.

- **Environment:** espacio físico en el que la aspiradora se mueve (como una casa).
El ambiente es parcialmente observable porque el robot necesita moverse para ir “desbloqueando" espacios para aspirar sin saber de antemano qué obstáculos va a tener o dónde está limpio y dónde no.
El ambiente es estocástico, ya que pueden haber obstáculos inesperados en el ambiente, como una alfombra o unos calcetines tirados en el espacio donde el robot necesita pasar.
El ambiente es secuencial, porque el hecho de que el robot termine de aspirar una habitación condiciona totalmente que no vuelva a pasar por ahí, porque ya no es necesario.
El ambiente es dinámico, ya que el espacio puede tener obstáculos o condiciones que van cambiando mientras el robot limpia. Por ejemplo, un perro dentro de la casa.
El ambiente es continuo porque hay variables continuas como la velocidad del robot, la fuerza de succión, el ángulo en el que avanza, etc.

- **Actuators:** bocinas (como en las estaciones de carga), ruedas, cepillos, motor de succión.

- **Sensors:** Cámara o sensor infrarrojo, sensor de distancia (para evitar caidas), la red WIFI a la que esté conectada.

***
### Sistema de recomendación de streaming
- **Performance:** tiempo que el usuario final termina consumiendo una opción recomendada por el agente; calificación explícita del usuario sobre la opción recomendada (como en Netflix que puedes poner si una película te gustó o en Spotify que le puedes dar like).

- **Environment:** host del agente de recomendación y la plataforma misma, en caso de que sean distintas.
El ambiente es parcialmente observable, porque aunque tiene contexto total de las interacciones previas del usuario y del historial de comportamiento, hay muchas condiciones del usuario mismo que interactúan con el agente de las que este no tiene conocimiento (quizá tiene ganas de ver algo que ya vio, quizá nada más está entrando a agregar cosas a la watchlist, etc.).
El ambiente es no determinista. Por el mismo motivo de que el usuario cuenta con muchas condiciones no observables que impactan en elegir o no el contenido recomendado, recomendar el mismo resultado en distintos momentos puede tener distintas respuestas.
El ambiente es secuencial, ya que dependiendo del performance de cada recomendación, el próximo batch de recomendaciones está condicionado al anterior. (Si el usuario calificó con 1/5 estrellas a una película de acción, afectará el próximo batch de recomendaciones).
El ambiente es semidinámico, ya que aunque el ambiente no cambia con el tiempo, la satisfacción del usuario sí se ve afectada.
El ambiente es discreto, ya que la lista de películas recomendadas, el historial y la calificación del usuario sobre la película se miden de manera discreta.

- **Actuators:**
Interfaz de la plataforma.

- **Sensors:**
Historial de contenido consumido por el usuario, calificación dada al contenido consumido, metadata de navegación (dispositivo, hora, perfil, edad, etc.).

***
### Vehículo autónomo en la ciudad

- **Performance:** tiempo que tarda en llegar, confort, optimización de rutas en relación con el costo (de gasolina o uso de batería).

- **Environment:** el ambiente incluye todo lo relacionado con el lugar donde el vehículo se va a estar manejando: tráfico, peatones, calles, autopistas, clima, señalamientos de tránsito, etc.
El ambiente es parcialmente observable porque el vehículo no puede saber lo que hay más allá de lo que su “rango de visión" le permite. No sabe si va a haber o no un semáforo a un kilómetro de distancia.
El ambiente es estocástico, ya que (en una calle promedio) hay demasiado ruido que impacta en el resultado del agente. Por ejemplo, independientemente de la orden que le des al vehículo, si hay un señalamiento de tránsito adelante o si se atraviesa una persona influye totalmente en el resultado del agente.
El ambiente es secuencial, ya que dependiendo de si doblas a la izquierda o si tomas la glorieta, el siguiente paso se ve totalmente afectado por esto.
El ambiente es dinámico. Precisamente por el ruido que hay (personas, animales de la calle, etc.), el ambiente cambia en cada momento, independientemente del tiempo de respuesta del agente.
El ambiente es continuo. Hay demasiadas métricas del agente que son continuas, como la velocidad, el tiempo que se ha tomado en ir al lugar, etc.

- **Actuators:** los actuadores son casi todos los elementos del coche que interactúan con el ambiente: el volante, el claxon, la palanca de cambios, los pedales, las llantas, etc.

- **Sensors:** velocímetro, tacómetro, cámaras, GPS, etc.

***
### Agente de trading algorítmico en bolsa

- **Performance:** ROI calculado por el día (ganancias o pérdidas), número de transacciones hechas, velocidad de ejecución, precio promedio por transacción. También podría interactuar con los estados de cuenta de las principales empresas mundiales.

- **Environment:** el ambiente básicamente será el ámbito en el que el agente se desarrolle; por ejemplo, podría ser la bolsa de valores mexicana, NASDAQ, etc.
El ambiente es parcialmente observable, ya que no es posible tener un panorama completo de muchas acciones y empresas sin tener “inside traders", así como tampoco es posible que el agente esté al tanto de absolutamente todos los escenarios sociales que puedan o no impactar en la bolsa.
El ambiente es estocástico, ya que hay demasiados factores externos que impactan en el precio de las acciones y, por tanto, en el rendimiento del agente, como por ejemplo una publicación de Donald Trump.
El ambiente es secuencial, ya que la decisión de comprar o vender una acción condiciona el dinero que hay disponible para más transacciones.
El ambiente es dinámico. Ya sea day trading o con un enfoque más cauteloso, como lo que se busca es un rendimiento variable, hay demasiado ruido que afecta segundo a segundo el precio de las acciones e impacta en el performance del agente.
El ambiente es continuo, ya que se pueden comprar “partes" de acciones de empresas, así como sus costos no son necesariamente discretos.

- **Actuators:** creo que el único actuator sería la API de consultas para poder realizar compras o ventas de acciones.

- **Sensors:** APIs de consultas en tiempo real para conocer los precios de las acciones; API de redes sociales con consulta a cuentas de noticias económicas.

***
### Dron de inspección de infraestructura

- **Performance:** tiempo que tarda el dron en inspeccionar toda la infraestructura, precisión de la inspección, autonomía de la batería, alcance del control remoto, calidad de la cámara.

- **Environment:** el ambiente es totalmente dependiente de la infraestructura que se vaya a inspeccionar. Puede ser un edificio, una escuela, una casa, etc.
El ambiente es parcialmente observable ya que el dron solamente tiene visión del ambiente hasta el rango que sus sensores le permiten.
El ambiente puede ser estocástico, ya que si la infraestructura no es cerrada puede haber mucho ruido o interferencia en la inspección, como que un pájaro se meta o algo similar.
El ambiente es secuencial, muy similar al caso del coche: un giro a la izquierda o a la derecha afecta directamente decisiones futuras del agente.
El ambiente es dinámico (dependiendo de la infraestructura que se esté inspeccionando) porque puede haber mucho ruido interfiriendo en las inspecciones; por ejemplo, puede haber una araña en una esquina moviéndose y afectando las lecturas del dron.
El ambiente es continuo. Muy seguramente habrá mediciones de paredes o partes que den resultados continuos.

- **Actuators:** cámaras del dron, motores, hélices, pantallas (si aplica en el control remoto).

- **Sensors:** cámaras del dron, sistemas infrarrojos, giroscopios, GPS.

***
### Agente jugador de ajedrez

- **Performance:** Promedio de partidas ganadas y tiempo de respuesta (sobre todo si es una partida contrareloj)

- **Environment:** El ambiente en este caso es únicamente referente al tablero con sus respectivas piezas de ambas partes.
El ambiente es totalmente observable, ya que el agente tiene acceso a la información de todas las posiciones de las piezas y de la totalidad del tablero.
El ambiente es determinista. Como hay un conjunto de reglas fijo y posiciones determinadas de las piezas, no hay elementos que puedan quedar al azar.
El ambiente es secuencial, ya que la posición y los movimientos de las piezas afectan directamente el desarrollo del juego y las posiciones posibles.
El ambiente es semidinámico, ya que las posiciones de las piezas no cambian, pero mientras más tarda el agente, afecta su performance y el resultado del juego (por ejemplo, en un juego contra reloj).
El ambiente es discreto, ya que hay una posición determinada y finita en el tablero, y las piezas solamente pueden estar en una única posición al momento.

- **Actuators:** Depende de cómo sea el agente, podría ser una pantalla que muestre la posición recomendada por el agente, o un brazo robótico que mueva las piezas, o una interfaz que mueva directamente las piezas digitalmente.

- **Sensor:** Puede ser una cámara que visualice el tablero en caso de que sea físico, o incluso la misma interfaz que "vea" el estado actual del tablero.
