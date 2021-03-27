"""
pyPwGenLayout.py

        画面ごとのレイアウトを返す
"""

# インポート
import          copy

from            common.Log          import      Log, abort
from            typing              import      List

import          PySimpleGUI         as          S

#
# デザインテーマの設定をする
#       レイアウトの定義より前にテーマを設定すること
#
S.theme( 'DarkGrey4' )

#
# 画面のレイアウト
#       レイアウトは window に描画される毎に「使い捨て」になるので注意
#       このため、定義したレイアウトの deepcopy() をレイアウトとして返す
#
LAYOUT          = {

    # 主画面のレイアウト
    '主画面' :

        [
            # 1 行目 - パスワード表示行
            [ S.Text( 'パスワードは', size = ( 12, 1 ), ),
              S.InputText( key = 'pwd', size = ( 65, 1 ) ), ],
            # 2 行目 - パスワード桁数とパスワードの種類の指定行
            [ S.Text( '桁数', size = ( 4, 1 ), ),
              S.InputText( key = 'col', size = ( 4, 1 ), default_text = '16', ),
              S.Text( '文字種', size = ( 6, 1 ), ),
              S.Radio( '大小文字混在', key = 'cap', default = True, group_id = 'char', ),
              S.Radio( '小文字のみ', default = False, group_id = 'char', ),
              S.Checkbox( '数字あり', key = 'num', default = True, ),
              S.Checkbox( '記号あり', key = 'sym', default = False, ), ],
            # 3 行目 - メッセージ表示行
            [ S.Text( '', size = ( 72, 1 ), key = 'err', text_color = '#DD5F5D' ), ],
            # 4 行目 - パスワード生成・終了ボタン表示行
            [ S.Button( 'パスワード生成', ),
              S.Button( '閉じる', ), ],
        ],
}

# 画面名に応じたレイアウトを返す
def             layout( screen : str ) -> List :
    """
    画面名に応じたレイアウトを返す

    :param screen:      画面名
    :return:            レイアウト
    """

    # ロガー
    _               = Log( __name__ )

    # 画面名に対応するレイアウトを返す
    try :

        # 画面に対応するレイアウトのディープコピーオブジェクトを返す
        return copy.deepcopy( LAYOUT[ screen ] )

    # 対応する画面がなければ異常終了
    except Exception :
        abort( '!!! 画面 {} が定義されていません'.format( screen ) )
