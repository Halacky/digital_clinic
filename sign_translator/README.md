A model for classifying letters of the English alphabet in sign language was trained. 

YOLOv11-m was used as a pre-trained model.
https://docs.ultralytics.com/ru/tasks/classify/

The dataset was collected from different sources and will be combined into one.

According to the results of the training, it was revealed that the classifier is not ideal for solving such a task, since there are gestures that are shown in motion. 

Directions of development:
1) Use an action recognition model, for example, ActionRecognitionNet (https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/actionrecognitionnet)
2) Train an action recognition model for the Russian language (https://github.com/ai-forever/bukva)
