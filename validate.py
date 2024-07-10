from ultralytics import YOLO

# Cargar el modelo YOLO previamente entrenado
model = YOLO('model-implementor\models\i1-yolov8s.pt')

# Validar el modelo con el conjunto de datos de validación
results = model.val(data="D:\escritorio\estudios D\mlops\Accident-Detection-Web-App-main\Datos\data.yaml", imgsz=640)

# Mostrar los resultados de la validación
print(results)