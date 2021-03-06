# ライブラリをインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 繰り返し回数を設定
print('繰り返し回数を入力してください')
count = int(input())

while type(count) != int:
    print('エラー:整数を入力してください')
    count = int(input())

# Chromeの自動化
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome(executable_path = \
# ‘C:\\Users\\KinoCode\\Desktop\\MyCode\\chromedriver.exe’) # Windows
browser.implicitly_wait(3)

# webページのデータを取得(html形式)
url_login = "https://jp.akinator.com"
browser.get(url_login)
time.sleep(3)

# 開始する
btn_play = browser.find_element_by_class_name('btn-play')
btn_play.click()
print('開始しました')
time.sleep(3)

# ゲームモード選択
btn_character = browser.find_element_by_link_text('キャラクター')
btn_character.click()
print('ゲームモードを選択しました')
time.sleep(3)

# 「はい」を選ぶべき質問
datasets_yes = ['年齢は20代ですか？', '25歳よりも若い?',
                'インターネットから有名になった?', '実際に存在する?', '日本人?',
                'ひらがなですか？', '個人的にあなたを知ってる?', '人間？',
                'スライムに関係していますか？', '男性？', '日本に住んでいますか?',
                '学校に通ってる?', '兄弟か姉妹がいる？', 'あなたと関係がある？',
                '現在、日本に住んでいる？', 'その人は20歳以上ですか？', '目はある？',
                '首は一つですか？', '実在する?', '足はある？', '肌の色は人間と同じ色をしている？',
                '口はついていますか？', '学校に通っていますか？', '大学にいった?', '脚(足)がある?',
                'あなたに会ったことがある？', 'あなたは会ったことがありますか？',
                'その人は成人していますか', 'あなたの同じ学校ですか？' 'ネッ友を思い浮かべています',
                '一般的に見て清潔感がある？ ', 'あなたの友達ですか？', '理系ですか？', '男性?',
                '学校に通ってる？'
                ]

# 「多分そう部分的にそう」を選ぶべき質問
datasets_maybe = [
    "音楽に関係してる?", "歌に関係ありますか？", '様々な種類のクローンがいますか？'
]

# 処理開始
for i in range(count):
    print('\n\n' + str(i+1) + "回目")

    proposal_title = browser.find_elements_by_class_name('proposal-title')

    while not proposal_title:
        question_text = browser.find_element_by_class_name('question-text').text

        while question_text == '取り込み中・・・':
            question_text = browser.find_element_by_class_name(
                'question-text').text

        print(question_text)

        for yes in datasets_yes:
            flag_yes = question_text == yes

            if flag_yes:
                yes = browser.find_element_by_id('a_yes')
                yes.click()

                print('はいを選択しました')
                break

        else:

            for maybe in datasets_maybe:
                flag_maybe = question_text == maybe

                if flag_maybe:
                    probably = browser.find_element_by_id('a_probably')
                    probably.click()

                    print('多分そう部分的にそうを選択しました')
                    break

            else:
                no = browser.find_element_by_id('a_no')
                no.click()

                print('いいえを選択しました')

        proposal_title = browser.find_elements_by_class_name('proposal-title')

    proposal_title = browser.find_element_by_class_name('proposal-title')
    print(proposal_title.text + 'を思い浮かべています')

    if proposal_title.text == 'ぽゅん':
        propose_yes = browser.find_element_by_id('a_propose_yes')
        propose_yes.click()

        print('はいを選択肢しました')
    elif proposal_title.text == '技術的問題が発生しました。再度お試しください。':
        browser.refresh()
        i -= 1
    else:
        propose_no = browser.find_element_by_id('a_propose_no')
        propose_no.click()

        print('いいえを選択肢しました')

    # もう一度遊ぶ
    btn_again = browser.find_element_by_link_text('もう一度遊ぶ')
    btn_again.click()

    print('もう一度遊ぶを選択しました')
browser.close()
