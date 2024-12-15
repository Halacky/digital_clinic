from clearml import Task
from ultralytics import YOLO

task = Task.init(project_name="digital_clinic", task_name="sign_translator")

# Step 2: Selecting the YOLO11 Model
model_variant = "yolo11m-cls"
task.set_parameter("model_variant", model_variant)

# Step 3: Loading the YOLO11 Model
model = YOLO(f"/home/kirill/project/digital_clinic/weight/{model_variant}.pt")

# Step 4: Setting Up Training Arguments
args = dict(
    data="/home/kirill/project/digital_clinic/dataset/eng_alphabet", 
    epochs=100, 
    device='cuda',
    imgsz=64, 
    augment= True,  # Включение базовой аугментации
    hsv_h= 0.015,  # Сдвиг оттенка
    hsv_s= 0.7,    # Сдвиг насыщенности
    hsv_v= 0.4,    # Сдвиг яркости
    degrees= 0.0,  # Вращение изображений
    translate= 0.1, # Сдвиг изображений
    scale= 0.5,    # Масштабирование изображений
    shear= 0.0,    # Сдвиг (shear)
    flipud= 0.0,   # Вертикальный переворот
    fliplr= 0.5,   # Горизонтальный переворот
    mosaic= 1.0,   # Использование mosaic аугментации
    mixup= 0.0     # Использование mixup аугментации
)
task.connect(args)

# Step 5: Initiating Model Training
results = model.train(**args)