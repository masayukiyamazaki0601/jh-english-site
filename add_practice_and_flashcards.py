#!/usr/bin/env python3
"""全28薄い記事に練習問題・暗記カード・学習コツを追加"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken_article(filename, extra_content):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines > 200:
        print(f"  SKIP {filename} ({lines} lines)")
        return
    insert_pos = content.rfind("</article>")
    if insert_pos == -1:
        print(f"  SKIP {filename}: no article tag")
        return
    before = content[:insert_pos]
    after = content[insert_pos:]
    new_content = before + extra_content + "\n" + after
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  THICKENED {filename} ({lines} -> {new_content.count(chr(10))} lines)")

# 練習問題データ
PRACTICE = {
    "kateiho": [
        ("If I ( ) you, I would study harder.", "were"),
        ("If it ( ) sunny, we could go swimming.", "were"),
        ("I would buy a car if I ( ) enough money.", "had"),
        ("If she ( ) here, she would help us.", "were"),
        ("We could win if we ( ) harder.", "tried"),
    ],
    "genkan3": [
        ("I have ( ) finished my homework.", "just"),
        ("She has ( ) eaten lunch.", "already"),
        ("Have you finished your homework ( )?", "yet"),
        ("I haven't seen that movie ( ).", "yet"),
        ("He has ( ) left for school.", "already"),
    ],
    "genkeiFuteisi": [
        ("I saw him (run/running/to run) in the park.", "run"),
        ("She made me (clean/to clean/cleaning) the room.", "clean"),
        ("Let's (go/to go/going) to the park.", "go"),
        ("I heard her (sing/singing/to sing) a song.", "sing"),
        ("My father had me (wash/to wash/washing) the car.", "wash"),
    ],
    "kakosin": [
        ("I ( ) reading a book at 8pm last night.", "was"),
        ("They ( ) playing soccer yesterday.", "were"),
        ("She ( ) cooking dinner at that time.", "was"),
        ("( ) you studying at midnight?", "Were"),
        ("He ( ) not sleeping at that time.", "was"),
    ],
    "there": [
        ("( ) a cat under the table.", "There is"),
        ("( ) many books on the desk.", "There are"),
        ("( ) a pen on the desk?", "Is there"),
        ("( ) any students in the room?", "Are there"),
        ("There ( ) not any milk in the fridge.", "is"),
    ],
    "genkanSinkokei": [
        ("I have been ( ) English for three years.", "studying"),
        ("It has been ( ) since morning.", "raining"),
        ("How long have you been ( ) here?", "living"),
        ("She has been ( ) for 30 minutes.", "waiting"),
        ("They have been ( ) tennis for 2 hours.", "playing"),
    ],
    "bekako": [
        ("I ( ) happy yesterday.", "was"),
        ("They ( ) at home last night.", "were"),
        ("She ( ) busy yesterday.", "was"),
        ("( ) you tired after the game?", "Were"),
        ("He ( ) not at school yesterday.", "was"),
    ],
    "kansetu": [
        ("Do you know where he ( )?", "lives"),
        ("I don't know what this ( ).", "is"),
        ("Can you tell me where the station ( )?", "is"),
        ("I wonder ( ) he is kind.", "if / whether"),
        ("Do you know ( ) she will come?", "if / whether"),
    ],
    "setuzoku": [
        ("I like cats ( ) dogs.", "and"),
        ("I like cats ( ) I don't like dogs.", "but"),
        ("I am happy ( ) I got a present.", "because"),
        ("I was tired, ( ) I went to bed.", "so"),
        ("Call me ( ) you arrive.", "when"),
    ],
    "genkan2": [
        ("Have you ( ) been to Kyoto?", "ever"),
        ("I have ( ) eaten sushi.", "never"),
        ("She has been to the US ( ).", "twice"),
        ("I have seen this movie ( ).", "before"),
        ("He has ( ) been abroad.", "never"),
    ],
    "gimonsi": [
        ("( ) is your name?", "What"),
        ("( ) is he?", "Who"),
        ("( ) are you from?", "Where"),
        ("( ) is your birthday?", "When"),
        ("( ) are you late?", "Why"),
    ],
    "mirai": [
        ("I ( ) call you later.", "will"),
        ("It ( ) rain tomorrow.", "will"),
        ("She ( ) going to study law.", "is"),
        ("We are ( ) to have a test next week.", "going"),
        ("Will you ( ) the window?", "open"),
    ],
    "bunsi": [
        ("Look at the ( ) baby.", "sleeping"),
        ("I know the girl ( ) in the room.", "singing"),
        ("I have a ( ) watch.", "broken"),
        ("This is a book ( ) by Soseki.", "written"),
        ("The boy ( ) is my brother.", "running"),
    ],
    "can": [
        ("I ( ) swim.", "can"),
        ("She ( ) speak French.", "can"),
        ("( ) you help me?", "Can"),
        ("I ( ) play the piano.", "can't"),
        ("( ) I use your pen?", "Can"),
    ],
    "daimeisi": [
        ("( ) is my friend. (she/her)", "She"),
        ("I like ( ). (she/her)", "her"),
        ("This is ( ) book. (my/mine)", "my"),
        ("Give it to ( ). (I/me)", "me"),
        ("This book is ( ). (my/mine)", "mine"),
    ],
    "kankeisi1": [
        ("I know the boy ( ) is running.", "who"),
        ("This is the book ( ) I bought.", "which / that"),
        ("She is the girl ( ) plays the piano.", "who / that"),
        ("He is the man ( ) I met yesterday.", "whom / that"),
        ("I have a dog ( ) can run fast.", "that / which"),
    ],
    "ukemi": [
        ("English ( ) spoken in many countries.", "is"),
        ("This book ( ) written by Soseki.", "was"),
        ("The window ( ) broken by the boy.", "was"),
        ("These cookies ( ) made by my mother.", "were"),
        ("Rice ( ) eaten in Japan.", "is"),
    ],
    "genkan1": [
        ("I have lived in Tokyo ( ) five years.", "for"),
        ("She has studied English ( ) 2020.", "since"),
        ("I have ( ) seen him since last week.", "not"),
        ("How long have you ( ) here?", "lived"),
        ("( ) she been a teacher for 10 years?", "Has"),
    ],
    "doumei": [
        ("I like ( ). (swim)", "swimming"),
        ("( ) tennis is fun. (play)", "Playing"),
        ("He enjoys ( ) books. (read)", "reading"),
        ("I finished ( ) my homework. (do)", "doing"),
        ("She is good at ( ). (sing)", "singing"),
    ],
    "jyodosi": [
        ("You ( ) study harder.", "must"),
        ("I ( ) to go now.", "have"),
        ("She ( ) to wear a uniform.", "has"),
        ("( ) I come in?", "May"),
        ("You ( ) not run here.", "must"),
    ],
    "hikaku1": [
        ("Taro is ( ) than Jiro. (tall)", "taller"),
        ("She is more ( ) than me. (beautiful)", "beautiful"),
        ("Mt. Fuji is ( ) highest mountain in Japan.", "the"),
        ("He is as ( ) as me. (tall)", "tall"),
        ("This book is not as ( ) as that one. (interesting)", "interesting"),
    ],
    "zensi": [
        ("I get up ( ) six every morning.", "at"),
        ("She was born ( ) April 1st.", "on"),
        ("It is hot ( ) summer.", "in"),
        ("The cat is ( ) the table.", "under"),
        ("I go to school ( ) bus.", "by"),
    ],
    "suryo": [
        ("There are ( ) books on the desk.", "many"),
        ("I don't have ( ) money.", "much"),
        ("He has ( ) friends. (almost none)", "few"),
        ("I have ( ) friends. (some)", "a few"),
        ("There is ( ) water left. (almost none)", "little"),
    ],
    "futeisi2": [
        ("It is important ( ) us to study English.", "for"),
        ("This box is too heavy ( ) me to carry.", "for"),
        ("She is ( ) young to drive a car.", "too"),
        ("He is old ( ) to drive a car.", "enough"),
        ("It is easy ( ) her to solve.", "for"),
    ],
    "futeisi1": [
        ("I want ( ) study English.", "to"),
        ("I went to Kyoto ( ) see temples.", "to"),
        ("I have something ( ) do.", "to"),
        ("I enjoy ( ) tennis.", "playing"),
        ("To play tennis ( ) fun.", "is"),
    ],
    "ippan": [
        ("I ( ) breakfast every morning.", "eat"),
        ("She ( ) tennis on Sunday.", "plays"),
        ("I ( ) like coffee.", "don't"),
        ("He ( ) play the piano.", "doesn't"),
        ("( ) you like cats?", "Do"),
    ],
    "be": [
        ("I ( ) a student.", "am"),
        ("You ( ) kind.", "are"),
        ("He ( ) my friend.", "is"),
        ("I ( ) not a teacher.", "am"),
        ("She ( ) not tired.", "is"),
    ],
    "kako": [
        ("I ( ) to the park yesterday.", "went"),
        ("She ( ) breakfast at seven.", "ate"),
        ("They ( ) a movie last night.", "saw"),
        ("I ( ) my homework yesterday.", "did"),
        ("He ( ) a cake for me.", "made"),
    ],
}

ALL_TITLES = {
    "kateiho": "仮定法", "genkan3": "現在完了（完了）", "genkeiFuteisi": "原形不定詞",
    "kakosin": "過去進行形", "there": "there is構文", "genkanSinkokei": "現在完了進行形",
    "bekako": "be動詞の過去形", "kansetu": "間接疑問", "setuzoku": "接続詞",
    "genkan2": "現在完了（経験）", "gimonsi": "疑問詞", "mirai": "未来形", "bunsi": "分詞",
    "can": "can", "daimeisi": "代名詞", "kankeisi1": "関係代名詞", "ukemi": "受け身",
    "genkan1": "現在完了（継続）", "doumei": "動名詞", "jyodosi": "助動詞",
    "hikaku1": "比較", "zensi": "前置詞", "suryo": "数量詞",
    "futeisi2": "不定詞（応用）", "futeisi1": "不定詞（基本）", "ippan": "一般動詞",
    "be": "be動詞", "kako": "一般動詞の過去形",
}

for key, questions in PRACTICE.items():
    title = ALL_TITLES.get(key, key)
    
    # 練習問題セクション
    extra = '\n<h2>✏️ Practice！ 練習問題</h2>\n'
    extra += '<p>以下の問題を解いて、理解を確認しましょう。</p>\n<ol>\n'
    for q_text, q_answer in questions:
        extra += f'  <li>{q_text}<br><span style="color:var(--gray-500);font-size:0.9rem;">→ 答え: {q_answer}</span></li>\n'
    extra += '</ol>\n'
    
    # 暗記カード
    flashcard_data = {
        "kateiho": [("If + 過去形, would + 動詞の原形","仮定法の基本公式"),("If I were you","「もし私があなたなら」"),("were は主語が I でも使う","仮定法の鉄則")],
        "genkan3": [("have + just + 過去分詞","「ちょうど〜したところ」"),("have + already + 過去分詞","「もう〜した」"),("yet = 疑問文・否定文で使う","もう？ / まだ〜ない")],
        "genkeiFuteisi": [("知覚動詞 + 目的語 + 原形","see, hear, watch"),("使役動詞 + 目的語 + 原形","make, let, have"),("help は原形でもto不定詞でもOK","He helped me (to) carry.")],
        "kakosin": [("was/were + 動詞のing形","過去進行形の公式"),("単数主語 = was","I/He/She/It + was"),("複数主語 = were","You/We/They + were")],
        "there": [("There is + 単数名詞","「〜がある」"),("There are + 複数名詞","「〜がある」"),("否定: There is not / are not","「〜がない」")],
        "genkanSinkokei": [("have/has + been + doing","現在完了進行形"),("「ずっと〜し続けている」","動作の継続を強調"),("状態動詞は進行形にできない","live, know など")],
        "bekako": [("am/is → was","be動詞過去形"),("are → were","be動詞過去形"),("wasn't / weren't","否定短縮形")],
        "kansetu": [("間接疑問のあとは肯定文の語順","最重要ルール！"),("Do you know + 疑問詞 + 主語 + 動詞","よく使うパターン"),("if/whether = 「〜かどうか」","疑問詞がない場合")],
        "setuzoku": [("and = 並列「〜と」","I like cats and dogs."),("but = 逆接「しかし」","I like cats but not dogs."),("because = 理由「なぜなら」","I am happy because I got a present.")],
        "genkan2": [("Have you ever + 過去分詞？","「〜したことがありますか？」"),("I have never + 過去分詞","「〜したことがありません」"),("been to vs gone to","行って戻った vs 行ったまま")],
        "gimonsi": [("What = 何","What is this?"),("Who = 誰","Who is he?"),("Where = どこ","Where are you from?"),("When = いつ","When is your birthday?")],
        "mirai": [("will + 動詞の原形","未来形（その場の意思）"),("be going to + 動詞の原形","未来形（予定）"),("will not = won't","否定形")],
        "bunsi": [("現在分詞（-ing）","「〜している」能動"),("過去分詞（-ed/不規則）","「〜される/された」受動"),("boiling vs boiled","boiling water vs boiled water")],
        "can": [("can + 動詞の原形","canの基本公式"),("cannot = can't","否定形"),("Can + 主語 + 動詞の原形？","疑問形")],
        "daimeisi": [("I / my / me / mine","代名詞の4変化"),("you / your / you / yours","代名詞の4変化"),("he / his / him / his","代名詞の4変化")],
        "kankeisi1": [("who = 人（主格）","who + 動詞"),("which = 物（主格）","which + 動詞"),("that = 人・物両方","that + 動詞")],
        "ukemi": [("be動詞 + 過去分詞","受け身の基本形"),("by + 行為者","「〜によって」"),("時制によってbe動詞が変わる","is/was/will be/has been")],
        "genkan1": [("have/has + 過去分詞","現在完了の基本形"),("for + 期間（数字）","for 3 years"),("since + 時点","since 2020")],
        "doumei": [("動詞 + ing = 動名詞","「〜すること」"),("enjoy + 動名詞","「〜することを楽しむ」"),("finish + 動名詞","「〜するのを終える」")],
        "jyodosi": [("must + 動詞の原形","「〜しなければならない」"),("must not = 禁止","「〜してはいけない」"),("don't have to = 不要","「〜する必要はない」")],
        "hikaku1": [("比較級: -er / more","「より〜」"),("最上級: the + -est / most","「一番〜」"),("原級: as + 原級 + as","「〜と同じくらい」")],
        "zensi": [("in: 月・年・季節","in May, in 2024"),("on: 曜日・日付","on Sunday, on May 5th"),("at: 時刻","at 8 o'clock")],
        "suryo": [("many + 可算名詞","many books"),("much + 不可算名詞","much water"),("a few = 肯定的 / few = 否定的","いくつかある vs ほとんどない")],
        "futeisi2": [("It is 〜 for 人 to do","「人にとって〜することは〜だ」"),("too 〜 to do","「〜すぎてできない」"),("enough to do","「〜するのに十分〜だ」")],
        "futeisi1": [("to + 動詞の原形 = 不定詞","3つの用法がある"),("want to + 動詞","「〜したい」"),("名詞的用法 = 「〜すること」","主語・目的語・補語になる")],
        "ippan": [("否定文: don't/doesn't + 動詞の原形","does を使ったら s を取る"),("疑問文: Do/Does + 主語 + 動詞の原形？","Yes, I do. / No, I don't."),("三人称単数には s がつく","he/she/it + plays")],
        "be": [("I = am","主語とbe動詞の対応"),("you/we/they = are","主語とbe動詞の対応"),("he/she/it = is","主語とbe動詞の対応")],
        "kako": [("規則動詞: 原形 + ed","play→played"),("不規則動詞: 個別に暗記","go→went, eat→ate"),("did + 動詞の原形","否定文・疑問文では動詞は原形！")],
    }
    if key in flashcard_data:
        extra += '<h2>📌 重要ポイント暗記カード</h2>\n<table class="grammar-table" style="width:100%;">\n<tr><th>覚えること</th><th>補足</th></tr>\n'
        for term, defn in flashcard_data[key]:
            extra += f'<tr><td><strong>{term}</strong></td><td>{defn}</td></tr>\n'
        extra += '</table>\n'
    
    extra += '<div class="note"><strong>学習のコツ</strong> 間違えた問題はチェックしておいて、何度も繰り返し練習しましょう。1日5分でも毎日続けることが大切です。</div>\n'
    
    thicken_article(key + ".html", extra)

print("=== 練習問題・暗記カードの追加が完了しました ===")