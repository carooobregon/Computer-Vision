## Detección de Objetos via YOLO (Apples vs. Oranges)

### ¿Qué es este proyecto?

Con el modelo de detección de objetos **YOLO (You Only Look Once)**, hemos realizado un sistema de visión capaz de identificar y diferenciar entre objetos (en nuestro caso **manzanas y naranjas**) presentes en imágenes y videos por medio de un entrenamiento en el cual se le alimenta al sistema con datos de aprendizaje y prueba.

YOLO: https://pjreddie.com/darknet/yolo/

### ¿Cómo funciona?

Entrenando al sistema con 300 imágenes de aprendizaje y 50 de prueba, se desarrolla una capacidad alta para determinar si un objeto se encuentra presente. Para esto se descarga un dataset de la web, se cambia el formato del mismo para ser legible por YOLO y se juega con el repositorio **Darknet** para hacer uso de sus funciones auxiliares a la hora de guradar y leer datos.

### ¿Quién puede usar este repositorio?

Siendo esta una aplicación **Cloud y no local** de YOLO, quien quiera que esté interesado en probar el modelo se puede conectar al mismo por medio de una cuenta de Drive y desde ahí proporcionar imágenes o video a visualizar.

### ¿Cuál es el objetivo de este proyecto?

Verificar si el número de imágenes de aprendizaje y prueba recopilados y alimentados al sistema son suficientes para que se logre diferenciar con alta precisión entre diferentes tipos de manzanas y naranjas en cualquier escenario.
