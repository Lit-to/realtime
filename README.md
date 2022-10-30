# 時間を取得するデータパック
## このレポジトリはMinecraft用**データパック**です！！！
Pythonのファイルで生成したloottableがあるため、Pythonと表示されていますが、データパックとしてご利用いただけます。
このデータパックは開発者向けです。
## 内容
サーバーの時間を取得します。

## 対応バージョン
-   1.19
1.19のバニラでのみ動作確認をしていますが、恐らく他バージョンでも動くと思います。
__ただし、最新バージョンはspigot環境などでは動かすことが出来ません__
→[spigotでも動かす裏技](#spigot環境で動かす裏技)
## 利用方法
1. データパックを導入する
2. ``/function realtime:get``を実行する
3. ``/data get storage realtime: hour``で時間
4. ``/data get storage realtime: minute``で分
5. ``/data get storage realtime: second``で秒をそれぞれ2のタイミングの時間の取得ができます。

## Spigot環境で動かす裏技
このデータパックはspigot環境で元々作成したため、頑張れば動かすこともできます。
releaseのv1.0はその当時のデータパックなので、その場合はv1.0を使うと良いです。


協力:[なお](https://twitter.com/nao2002_)
参考動画:https://youtu.be/rTCVKCxp84A
