
# Python 3.5.2 にて動作を確認
# MySQLdb をインポート
import MySQLdb

# データベース接続とカーソル生成
# 接続情報はダミーです。お手元の環境にあわせてください。
connection = MySQLdb.connect(
    host='nsc-jp.net', user='g1', passwd='nscnl001', db='g1_db', charset='utf8')
cursor = connection.cursor()

# エラー処理（例外処理）
try:
    # CREATE
    # id, name だけのシンプルなテーブルを作成。id を主キーに設定。
    cursor.execute("DROP TABLE IF EXISTS `sample`")
    cursor.execute("""CREATE TABLE IF NOT EXISTS `sample` (
    `id` serial NOT NULL,
    `date` timestamp not null,
    `price` varchar(255)  NOT NULL,
     PRIMARY KEY (id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8""")

    # # INSERT
    # cursor.execute("INSERT INTO sample (price) VALUES ()")

    # プレースホルダの使用例
    # 1つの場合には最後に , がないとエラー。('鈴木') ではなく ('鈴木',)
    # cursor.execute("INSERT INTO sample VALUES (2, %s)", ('鈴木',))
    # cursor.execute("INSERT INTO sample VALUES (%s, %s)", (3, '高橋'))
    # cursor.execute("INSERT INTO sample VALUES (%(id)s, %(name)s)", {'id': 4, 'name': '田中'})

    # # 複数レコードを一度に挿入 executemany メソッドを使用
    # persons = [
    #     (5, '伊藤'),
    #     (6, '渡辺'),
    # ]
    # cursor.executemany("INSERT INTO sample VALUES (%s, %s)", persons)

    # # わざと主キー重複エラーを起こして例外を発生させてみる
    # cursor.execute("INSERT INTO sample VALUES (1, '中村')")
except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)

# 保存を実行（忘れると保存されないので注意）
connection.commit()

# 接続を閉じる
connection.close()
