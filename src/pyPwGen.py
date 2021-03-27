"""
pySimpleGUI サンプル - パスワードジェネレータ

        pwgen CLI コマンドを平易に GUI 化するため pySimpleGUI を利用する
"""

# インポート
import          PySimpleGUI         as          S

from            common.Log          import      SetupLog, Log, DEBUG

from            pyPwGenLayout       import      layout
from            pyPwGenValidate     import      validate
from            pyPwGenAction       import      action

# フォント
FONT            = ( 'Anito', 14, )

# パスワードジェネレータ主処理
def         pyPwGen( title : str ) -> None :
    """
    パスワードジェネレータ主処理

    pwgen コマンドを利用して GUI 版のフロントエンドとして動作します

    :param title:        ウィンドウのタイトル
    """

    # ロガー
    log         = Log( __name__ )

    # 主画面のレイアウトにより window を生成する
    screen          = '主画面'
    window          = S.Window( title = title, layout = layout( screen ), font = FONT, keep_on_top = True )

    # イベントループ
    while True :

        # window からのイベントを待ち、発生したイベントとフォーム (入力データの辞書) が返る
        event, values       = window.read()

        log.debug( '受信 : 画面 [ {} ] / イベント [ {} ]'.format( screen, event ) )
        log.debug( "受信フォーム : " + str( values ) )

        # イベント毎の処理を行う
        try :

            # イベントに応じたバリデーションを行う
            validate( screen, event, values )

            # イベントに応じたアクションを実行し、画面を更新するための結果を得る
            result          = action( screen, event, values )

            log.debug( '結果データ : ' + str( result ) )

            # None が返って来た時は終了する
            if result is None :
                break

            # 返ってきた結果で画面を更新する
            for key, val in result.items() :
                window[ key ].update( val )

        # バリデーションおよびアクションの例外は、エラーメッセージを表示する
        except Exception as e :
            window[ 'err' ].update( e )

    # ウィンドウを終了
    window.close()

# エントリポイント
if __name__ == '__main__':

    # ロガーのセットアップ
    SetupLog( DEBUG )

    # 主処理
    pyPwGen( 'パスワード ジェネレータ' )
