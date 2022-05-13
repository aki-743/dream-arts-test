# 概要

以下の要件を満たすAPIの作成

- アラビア数字から大数表記の漢数字に変換
- 大字表記の漢数字からアラビア数字に変換

# エンドポイント

|用途|パス|
|---|---|
|漢数字へ変換|https://qos9g60lbc.execute-api.ap-northeast-1.amazonaws.com/v1/number2kanji/{arabian_figure}|
|アラビア数字へ変換|https://qos9g60lbc.execute-api.ap-northeast-1.amazonaws.com/v1/kanji2number/{kanji_figure}|

## リクエスト成功例

- 漢数字へ変換

https://qos9g60lbc.execute-api.ap-northeast-1.amazonaws.com/v1/number2kanji/1234

- アラビア数字へ変換

https://qos9g60lbc.execute-api.ap-northeast-1.amazonaws.com/v1/kanji2number/壱千九百四拾七

## リクエスト失敗例

- 漢数字へ変換

https://qos9g60lbc.execute-api.ap-northeast-1.amazonaws.com/v1/number2kanji/-1

- アラビア数字へ変換

https://qos9g60lbc.execute-api.ap-northeast-1.amazonaws.com/v1/kanji2number/壱京九百四拾七