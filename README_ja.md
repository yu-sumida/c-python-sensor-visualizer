# センサーデータ可視化ツール（C × Python × Streamlit）

## 概要

本プロジェクトは、C言語で温度・湿度・加速度の3種類のセンサーデータを疑似生成し、  
CSVファイルとして出力します。  
そのデータをPython製のWebアプリ（Streamlit）で可視化することで、  
「組み込み開発×データサイエンス」両方のスキルをアピールできるポートフォリオです。

---

## 特徴

- C言語による複数センサーデータ（温度・湿度・加速度）の生成
- データをCSVファイルとして保存
- Python/Streamlitによるデータの可視化（折れ線グラフ等）
- 仮想環境とrequirements.txtによる簡単な再現性

---

## 使い方

### 1. C言語でCSVファイルを生成

C言語プログラムをコンパイル＆実行してください。

```sh
gcc main.c -o main
./main
```
### 2. Python仮想環境のセットアップとライブラリのインストール

```sh
python -m venv venv
venv\Scripts\activate (windows)
source venv/bin/activate (Mac/Linux)
```
必要なライブラリをインストールします。
```sh
pip install -r requirements.txt
```
### 3. Streamlitアプリの実行
```sh
streamlit run sensor_app.py
```