from roboflow import Roboflow
from decouple import config

rf = Roboflow(api_key=config("API_KEY"))
project = rf.workspace().project("body-measurement-zmbgv")
model = project.version(1).model

# infer on a local image
print(
    model.predict(
        "/Users/anton/Downloads/Image-Based-Body-Measurement-Detection-Challenge-main/Dataset/test/arm_circumference_img_25-0_jpg.rf.eb6ea95d2c858075c07feac975b495ee.jpg",
        confidence=40,
        overlap=30,
    ).json()
)

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
