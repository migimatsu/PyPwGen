"""
pyPwGenAction.py

        画面・イベントごとにフォームのアクションを行い、その結果を返す
"""

# インポート
from            subprocess          import      run, PIPE

from            common.Log          import      Log, abort
from            typing              import      Dict

# pwgen コマンド
CMD             = '/opt/homebrew/bin/pwgen'

# 最大桁数
COL_MAX         = 48

# 画面・イベントごとにフォームのアクションを行い、結果を返す
def             action( screen : str, event : str, values : Dict ) -> Dict or None :
    """
    パスワードジェネレータのアクション処理

    イベントに対応するアクションを実行し、実行結果を更新データとして返す

    :param screen:      画面名
    :param event:       画面で発生するイベント名
    :param values:      受信したフォーム (辞書)
    :return:            結果としてのフォーム更新データ。None なら終了を示す
    """

    # ロガー
    _               = Log( __name__ )

    # 結果領域 - エラーメッセージはクリアする
    result          = { 'err' : '' }

    # 終了 - window close または 閉じる ボタンを押下した時は終了する
    if event is None :
        return None

    elif event == '閉じる' :
        return None

    # 主画面・パスワード生成 - pwgen を呼び出してパスワードを生成する
    elif screen == '主画面' and event == 'パスワード生成' :

        # pwgen コマンド引数をフォームの指定から生成する
        options = [ '-s', '-B' ]                                                # 必ず付加 : -s ランダム化 -B 難読除去
        options.append( '-c' ) if values[ 'cap' ] else options.append( '-A' )   # 大小文字混在・小文字のみ
        options.append( '-n' ) if values[ 'num' ] else options.append( '-0' )   # 数字あり・なし
        options.append( '-y' ) if values[ 'sym' ] else options                  # 記号あり・なし

        # pwgen コマンドから結果のパスワードを得る
        try :

            # pwgen コマンドを実行する
            #        実行結果を stdout, stderr で受ける
            res         = run( [ CMD, * options, values[ 'col' ], '1', ], stdout = PIPE, stderr = PIPE )

            # エラーメッセージが返って来た時
            #       一行目をエラーとして例外を送出する
            if res.stderr :
                raise Exception( str( res.stderr.split( b'\n' )[ 0 ] ) )

            # 生成したパスワードを結果に設定する
            #        返ってきたパスワードを更新データとする
            result[ 'pwd' ]         = res.stdout

        # コマンドの実行そのものができなかった時は異常終了
        except Exception as e :
            abort( '!!! コマンド {} が実行できません ( {} )'.format( CMD, e ) )

    # 対応するアクションがなければ異常終了
    else :
        abort( '!!! 画面 {} イベント {} が定義されていません'.format( screen, event ) )

    # 結果 (画面の更新データ) を返す
    #       None を返すと window は終了する
    return result
