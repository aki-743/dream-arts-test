from urllib.parse import unquote

SUJI = {
  "零": 0,
  "壱": 1,
  "弐": 2,
  "参": 3,
  "四": 4,
  "五": 5,
  "六": 6,
  "七": 7,
  "八": 8,
  "九": 9
}

UNIT = {
  "拾": 10,
  "百": 100,
  "千": 1000
}

DIGIT = {
  "万": 10000,
  "億": 100000000,
  "兆": 1000000000000
}

def kanji2number(kansuji: str) -> int:
    number = 0
    tmp = 0
    for kanji in kansuji:
        if kanji in UNIT:
            number += tmp*UNIT[kanji]
            tmp = 0
        elif kanji in DIGIT:
            number += tmp
            number *= DIGIT[kanji]
            tmp = 0
        else:
            tmp += SUJI[kanji]

    number += tmp
    return number

# Lambdaハンドラー
def lambda_handler(event, context):
  try:
    path_parameters = event["pathParameters"]

    # パスパラメータから漢数字を取得
    kanji_figure = unquote(path_parameters["kanji_figure"])

    # アラビア数字に変換
    arabian_numeral = str(kanji2number(kanji_figure))

    return {
      "isBase64Encoded" : False,
      "statusCode": 200,
      "headers": {},
      "body": arabian_numeral
    }
  except KeyError:
    return {
      "isBase64Encoded" : False,
      "statusCode": 204,
      "headers": {},
      "body": "'{}' can`t convert arabian numeral".format(kanji_figure)
    }
  

# デバッグ用
def main():
  event = {
    "pathParameters": {
      "kanji_figure": "%E5%A3%B1%E5%8D%83%E4%B9%9D%E7%99%BE%E5%9B%9B%E6%8B%BE%E4%B8%83"
    },
  }

  response = lambda_handler(event, None)
  print(response)

if __name__ == "__main__":
  main()