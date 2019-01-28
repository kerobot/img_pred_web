# img_pred_web

学習モデルをもとにアップロードした画像ファイルから特定の顔を認識します。

事前に OpenCV の haarcascade_frontalface_default.xml を用意しておくこと。
事前に keras のモデルファイルを用意しておくこと。

## 環境

* Windows 10 x64 1809
* Python 3.6.5 x64
* Power Shell 6 x64
* Visual Studio Code x64
* Git for Windows x64
* OpenCV 3.4.4

## 構築

プロジェクトを clone してディレクトリに移動します。

```powershell
> git clone https://github.com/kerobot/img_pred_web.git img_pred_web
> cd img_pred_web
```

プロジェクトのための仮想環境を作成して有効化します。

```powershell
> python -m venv venv
> .\venv\Scripts\activate.ps1
```

念のため、仮想環境の pip をアップグレードします。

```powershell
> python -m pip install --upgrade pip
```

依存するパッケージをインストールします。

```powershell
> pip install -r requirements.txt
```

環境変数を設定します。

> CASCADE_FILE_PATH を設定  
> MODEL_FILE_PATH を設定

```powershell
> copy .\.env.sample .\.env
> code .\.env
```

Djangoのマイグレートを行います。

```powershell
> python manage.py migrate
```

## 実行

ルートにモデルファイル（例：model.h5）を配置し、Webアプリを起動します。

> Webアプリの起動

```powershell
> python manage.py runserver
```
