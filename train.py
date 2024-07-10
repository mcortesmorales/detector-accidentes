from pathlib import Path
from ultralytics import YOLO

# Cargar el modelo YOLO
model = YOLO('model-implementor\models\i1-yolov8s.pt')

# Entrenar el modelo con los conjuntos de datos de entrenamiento y validación
results = model.train(data="D:\escritorio\estudios D\mlops\Accident-Detection-Web-App-main\Datos\data.yaml", epochs=50, imgsz=640)