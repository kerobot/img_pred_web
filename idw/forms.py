from django import forms

class ImageForm(forms.Form):

    image = forms.ImageField(label="判定する画像を選択してください",  error_messages={'missing' : '画像が選択されていません',  'invalid' : '判定する画像を選択してください',  'invalid_image' : '画像ファイルではないようです'})
