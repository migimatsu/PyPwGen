"""
pySimpleGUI サンプル
"""

# インポート
import          PySimpleGUI         as          S

# pySimpleGUI サンプル
def             simple() -> None :
    """
    pySimpleGUI サンプル
    """

    # 画面テーマ
    S.theme( 'DarkGrey4' )

    # 画面レイアウト
    layout          = [
        # 1 行目 - 表示行
        [ S.Text( '結果 : ', ), S.Text( '', key = 'out', size = ( 32, 1 ), ), ],
        # 2 行目 - 入力行
        [ S.Text( '入力 : ', ), S.InputText( 'Hello world !', key = 'in', size = ( 32, 1 ), ), ],
        # 3 行目 - ボタン
        [ S.Button( '表示', ), S.Button( '閉じる', ), ],
    ]

    # レイアウトにより画面を作る
    window          = S.Window( title = 'サンプル', layout = layout, font = ( 'anito', 16 ), )

    # イベントループ
    while True :

        # window からのイベントを待つ
        event, values       = window.read()

        # イベントに応じて処理を行う
        # - window のクローズまたは 閉じる ボタン押下
        if event is None or event == '閉じる' :
            break

        # - 表示 ボタン押下なら入力内容を表示する
        elif event == '表示' :
            window[ 'out' ].update( values[ 'in' ] )

    # ウィンドウを終了
    window.close()

# エントリポイント
if __name__ == '__main__':

    # 主処理
    simple()
