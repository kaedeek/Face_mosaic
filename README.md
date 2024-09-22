# Face mosaic
これは、真正面の顔を`emoji.png`で隠すコードです。

## ライブラリ
```
pip install opencv-python
```

## haarcascade_frontalface_default.xmlをダウンロード
download : [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)


## 使い方
```python
path = "face.jpg" # ここに隠したい画像のパスを入れる
```