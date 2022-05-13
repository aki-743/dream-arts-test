KANSUJI = {
  0: "零",
  1: "壱",
  2: "弐",
  3: "参",
  4: "四",
  5: "五",
  6: "六",
  7: "七",
  8: "八",
  9: "九",
  10: "拾",
  100: "百",
  1000: "千",
  10000: "万",
  100000000: "億",
  1000000000000: "兆"
}
UNIT = ["","拾","百","千"]
DIGIT = ["","万","億","兆"]

# アラビア数字から漢数字に変換
def number2kanji(num: str) -> str:
    NumList = []
    kanji = ""

    # 下位からから4桁ずつ区切る
    for _ in range(len(num)//4+1):
        tmp = num[-4:]

        NumList.append(tmp)

        # 末尾の文字列を削除
        # num = num.rstrip(tmp) # この場合同じ数字が連続していると全部消える
        num = num[:-4]

    # リストを逆順にする
    NumList = NumList[::-1]

    # 零の処理
    if len(NumList) == 1 and NumList[0] == "0":
        kanji = "零"

    else:
        # 4桁ずつ処理していく
        for index,fourDigit in enumerate(NumList):
            tmp = ""
            # 区切りを追加
            for i in range(len(fourDigit)):
                if fourDigit[i] == "0":
                    continue
                else:
                    tmp += KANSUJI[int(fourDigit[i])]
                    tmp += UNIT[len(fourDigit)-i-1]

            # 桁を追加
            if fourDigit != "":
                digit = len(NumList)-index-1
                tmp += DIGIT[digit] 
                kanji += tmp

    return kanji

# Lambdaハンドラー
def lambda_handler(event, context):
  try:
    path_parameters = event["pathParameters"]

    # パスパラメータからアラビア数字を取得
    arabian_figure = path_parameters["arabian_figure"]
    int_arabian_figure = int(arabian_figure)

    if int_arabian_figure >= 0 and int_arabian_figure <= 9999999999999999:
      # 漢数字に変換
      kanji_numeral = number2kanji(arabian_figure)

      return {
        "isBase64Encoded" : False,
        "statusCode": 200,
        "headers": {},
        "body": kanji_numeral
      }
    else:
      raise ValueError
  except ValueError:
    return {
      "isBase64Encoded" : False,
      "statusCode": 204,
      "headers": {},
      "body": "'{}' can`t convert kanji numeral".format(arabian_figure)
    }


# デバッグ用
def main():
  event = {
    "pathParameters": {
      "arabian_figure": "-1"
    },
  }

  response = lambda_handler(event, None)
  print(response)

if __name__ == "__main__":
  main()