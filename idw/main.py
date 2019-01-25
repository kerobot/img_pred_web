from django.conf import settings
import base64
import io
from PIL import Image
import cv2
import keras
import numpy as np

def detect(upload_image):
    result_name = upload_image.name
    result_list = []
    result_img = ''

    cascade_file_path = settings.CASCADE_FILE_PATH
    model_file_path = settings.MODEL_FILE_PATH

    model = keras.models.load_model(model_file_path)

    image = np.asarray(Image.open(upload_image))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_gs = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    cascade = cv2.CascadeClassifier(cascade_file_path)
    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(64,64))

    # 顔が１つ以上検出できた場合
    if len(face_list) > 0:
        count = 1
        for rect in face_list:
            # 認識した顔の座標とサイズ
            x, y, width, height = rect
            # 認識した顔の切り抜き
            face_image = image_rgb[y:y+height, x:x+width]
            if face_image.shape[0] < 64 or face_image.shape[1] < 64:
                continue
            # 認識した顔のサイズ縮小
            face_image = cv2.resize(face_image,(64,64))
            # 認識した顔のまわりを赤枠で囲む
            cv2.rectangle(image_rgb, (x, y), (x+width, y+height), (0, 0, 255), thickness=2)

            # 認識した顔を1枚の画像を含む配列に変換
            face_image = np.expand_dims(face_image, axis=0)
            # 認識した顔から名前を特定
            name, result = detect_who(model, face_image)
            # 認識した顔に名前を描画
            cv2.putText(image_rgb, f"{count}. {name}", (x, y+height+20), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255) , 2)
            # 結果をリストに格納
            result_list.append(result)
            count = count + 1

    is_success, img_buffer = cv2.imencode(".png", image_rgb)
    if is_success:
        io_buffer = io.BytesIO(img_buffer)
        result_img = base64.b64encode(io_buffer.getvalue()).decode().replace("'", "")

    return (result_list, result_name, result_img)

def detect_who(model, face_image):
    # 予測
    predicted = model.predict(face_image)
    # 結果
    name = ""
    result = f"本田 翼 の可能性:{predicted[0][0]*100:.3f}% / 佐倉 綾音 の可能性:{predicted[0][1]*100:.3f}%"
    name_number_label = np.argmax(predicted)
    if name_number_label == 0:
        name = "Honda Tsubasa"
    elif name_number_label == 1:
        name = "Sakura Ayane"
    return (name, result)
