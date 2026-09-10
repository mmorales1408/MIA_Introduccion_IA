## Objetivo

Correr ambas notebooks en **Google Colab** con la arquitectura original,
**agregar dos capas** a cada red, volver a entrenar y **comparar** qué cambia
(curva de error/pérdida, velocidad, calidad de la clasificación).

***   
***

A continuación, [adjunto](Notebooks) la carpeta en donde se podrán encontrar las notebook en donde edité los modelos originales para poder agregarle dos capas a cada red. Para diferenciar, agregé un markdown debajo del modelo original para poder mostrar dónde empieza la edición del modelo que hice. Se ve de la siguiente manera:

![división de modelos](Imagenes/colab.png)

### Gráficas del loss 
| Multilayer perceptron (original) | Multilayer perceptron (editado) |
| :---: | :---: |
| ![ Multilayer perceptron (original)](Imagenes/Multilayer_ORIGINAL_loss.png) | ![Multilayer perceptron (editado)](Imagenes/Multilayer_EDITADO_loss.png) |
| Keras MLP (original)|  Keras MLP (editado) |
| ![Keras MLP (original)](Imagenes/Keras_ORIGINAL_loss.png) | ![Keras MLP (editado)](Imagenes//Keras_EDITADO_loss.png) |


Es bastante interesante que, después de ver las gráficas de loss para ambos modelos (editados), podemos ver que el error empeoró o directamente se estancó utilizando las redes más profundas tanto en Keras como en NumPy. 
En el modelo de NumPy, podemos ver un descenso muy drástico en las primeras épocas pero luego el error se estancó a un punto similar o mayor al de la red menos profunda. 
Con respecto a Keras, el modelo profundo tardó mucho más en reducir significativamente el error, y aún así, terminó con un error significativamente mayor al de la red menos profunda.

Para los modelos originales (sin las dos capas profundas agregadas) podemos ver una diferencia en las gráficas de loss aunque terminaron con un error relativamente similar. 
Las diferencias en las gráficas se deben a varios motivos:

- Inicialización: Para el modelo hecho con NumPy, en el código inicializamos los pesos con una selección aleatoria simple, mientras que Keras tiene inicializadores estándar en su core, por lo que ambos modelos empiezan desde puntos distintos. 

- Vectorización: Keras utiliza valores de menor precisión (32 bits) para sus operaciones de optimización, mientras que NumPy utiliza valores de 64 bits.

Para responder a la pregunta _Con sigmoides apiladas y MSE, ¿tiene sentido que una red más profunda no aprenda mejor en Iris?_, nos sirve recordar un tema visto en la introducción al perceptrón que es el desvanecimiento del gradiente.
Cuando pensamos en la retropropagación para el aprendizaje, tenemos que considerar que básicamente estamos concatenando multiplicaciones. Ya que el valor máximo de la derivada de la función sigmoidal es 0.25, cuando apilamos multiplicaciones en la retropropagación, los pesos se vuelven exponencialmente pequeños, tendiendo a 0, por lo que el loss se estanca y el modelo no puede aprender. 
Esto se relaciona directamente con el dataset de Iris: como los datos son casi linealmente separables, una red básica es suficiente para lograr un buen desempeño. Agregar capas profundas solo acelera el desvanecimiento del gradiente sin beneficio.

***
***
Adjunto [las evidencias](Evidencias) de haber corrido las redes en mi instancia de Colab.