import cv2
import numpy as np

path = "face.jpg"
emoji_path = "emoji.png"  # 絵文字の画像パス

# 画像の読み込み
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier(r"C:\Users\username\face_mosaic\haarcascade_frontalface_default.xml")

# 顔を検出
lists = cascade.detectMultiScale(img_gray, minSize=(100, 100))

if len(lists):
    # 絵文字画像を読み込み
    emoji = cv2.imread(emoji_path, cv2.IMREAD_UNCHANGED)
    print(emoji.shape)  # 形状を確認

    # RGBの場合はアルファチャンネルを追加
    if emoji.shape[2] == 3:
        alpha_channel = np.ones((emoji.shape[0], emoji.shape[1], 1), dtype=emoji.dtype) * 255
        emoji = np.concatenate((emoji, alpha_channel), axis=2)

    for (x, y, w, h) in lists:
        emoji_resized = cv2.resize(emoji, (w, h))

        for i in range(h):
            for j in range(w):
                if emoji_resized[i, j][3] != 0:  # アルファチャンネルを確認
                    img[y + i, x + j] = emoji_resized[i, j][:3]  # BGRチャンネルに書き込み

    # 完成した画像を表示
    cv2.imshow('img', img)

    # 画像を保存
    cv2.imwrite('output_image.jpg', img)

    cv2.waitKey(0)
else:
    print('Nothing')
