"""
pyPwGenValidate.py

        画面・イベントごとにフォームのバリデーションを行う
"""

# インポート
from            common.Log          import      Log, abort

from            typing              import      Dict

# 最大桁数
COL_MAX         = 48

# 画面・イベントごとにフォームのバリデーションを行う
def             validate( screen : str, event : str, values : Dict ) -> None :
    """
    画面・イベントごとにフォームのバリデーションを行う

    バリデーションエラー時は例外を送出する

    :param screen:      画面名
    :param event:
    :param values:
    :return:
    """

    # ロガー
    _               = Log( __name__ )

    # 終了 - バリデーションなし
    if event is None :
        pass

    elif event == '閉じる' :
        pass

    # 主画面・パスワード生成
    elif screen == '主画面' and event == 'パスワード生成' :

        # フォームから桁数を得る
        col : str       = values[ 'col' ]

        # 桁数が数値であるかのチェックをする
        if not col.isdecimal() :
            raise Exception( '桁数は数値にしてください' )

        # 桁数が最大桁数以下かのチェックをする
        elif int( col ) > COL_MAX :
            raise Exception( '桁数は {} までにしてください'.format( COL_MAX ) )

    # 対応するイベントがなければ異常終了
    else :
        abort( '!!! 画面 {} イベント {} が定義されていません'.format( screen, event ) )

    return None
