# Sesame RESTful webAPI Lock Unlock for MicroPython
Sesame RESTful webAPI Lock Unlock for MicroPython

## なにか
CANDY HOUSE の Sesame RESTful webAPI による施解錠を MircoPython に移植したもの

## 動作環境
* D1 mini(ESP8266)
* MicroPython 1.21

## D1 mini
https://www.wemos.cc/en/latest/d1/d1_mini.html

## candyhouse_webapi.py
https://doc.candyhouse.co/ja/SesameAPI
* Python から Micropython への移植

## aesEncrypt.py
https://github.com/gradoj/nanoserver
* nanoserver.py から関数のみ抽出、修正

## cmac.py
https://github.com/gradoj/nanoserver
* そのまま
