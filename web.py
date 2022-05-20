# ライブラリをインポート
from selenium import webdriver
import time

# 繰り返し回数を設定
print('繰り返し回数を入力してください')
count = int(input())

while type(count) != int:
    print('エラー:整数を入力してください')
    count = int(input())

# Chromeの自動化
browser = webdriver.Chrome()
# browser = webdriver.Chrome(executable_path = \
# ‘C:\\Users\\KinoCode\\Desktop\\MyCode\\chromedriver.exe’) # Windows
browser.implicitly_wait(2)

# webページのデータを取得(html形式)
url_login = "https://jp.akinator.com"
browser.get(url_login)
time.sleep(2)

# 開始する
browser_from = browser.find_element_by_class_name('btn-play')
browser_from.click()
print('開始しました')
time.sleep(2)

# ゲームモード選択
browser_from = browser.find_element_by_link_text('キャラクター')
browser_from.click()
print('ゲームモードを選択しました')
time.sleep(2)

# 「はい」を選ぶべき質問
datasets_yes = ['年齢は20代ですか？', '25歳よりも若い?',
                'インターネットから有名になった?', '実際に存在する?', '日本人?',
                'ひらがなですか？', '個人的にあなたを知ってる?', '人間？',
                'スライムに関係していますか？', '男性？', '日本に住んでいますか?',
                '学校に通ってる?', '兄弟か姉妹がいる？', 'あなたと関係がある？',
                '現在、日本に住んでいる？', 'その人は20歳以上ですか？', '目はある？',
                '首は一つですか？', '実在する?', '足はある？', '肌の色は人間と同じ色をしている？',
                '口はついていますか？', '学校に通っていますか？', '大学にいった?'
                ]

# 「多分そう部分的にそう」を選ぶべき質問
datasets_maybe = [
    "音楽に関係してる?", "歌に関係ありますか？",
]

for i in range(count):
    print('\n\n' + str(i+1) + "回目")
    flag_answer = browser.find_elements_by_class_name('proposal-title')
    while not flag_answer:
        question_text = browser.find_element_by_class_name('question-text').text
        print(question_text)
        for yes in datasets_yes:
            flag_yes = question_text == yes
            if flag_yes:
                click_btn = browser.find_element_by_id('a_yes')
                click_btn.click()
                print('はいを選択しました')
                time.sleep(2)
                break
        else:

            for maybe in datasets_maybe:
                flag_maybe = question_text == maybe
                if flag_maybe:
                    click_btn = browser.find_element_by_id('a_probably')
                    click_btn.click()
                    print('多分そう部分的にそうを選択しました')
                    time.sleep(2)
                    break
            else:
                click_btn = browser.find_element_by_id('a_no')
                click_btn.click()
                print('いいえを選択しました')
                time.sleep(2)
        flag_answer = browser.find_elements_by_class_name('proposal-title')
    flag_answer = browser.find_element_by_class_name('proposal-title')
    print(flag_answer.text + 'を思い浮かべています')

    if flag_answer.text == 'ぽゅん':
        propose_yes = browser.find_element_by_id('a_propose_yes')
        propose_yes.click()
        print('はいを選択肢しました')
        time.sleep(2)
    else:
        propose_no = browser.find_element_by_id('a_propose_no')
        propose_no.click()
        print('いいえを選択肢しました')
        time.sleep(2)

    # もう一度遊ぶ
    browser_from = browser.find_element_by_link_text('もう一度遊ぶ')
    browser_from.click()
    print('もう一度遊ぶを選択しました')
    time.sleep(2)
