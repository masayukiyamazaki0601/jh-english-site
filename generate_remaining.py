#!/usr/bin/env python3
"""残りの練習問題・テストと英単語機能を追加生成"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

HEADER = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 中学英語学習サイト</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="../index.html" class="header-logo">📚 中学英語<span>Lab</span></a>
    <nav class="header-nav">
      <a href="../index.html">ホーム</a>
      <a href="../index.html#grammar">文法解説</a>
      <a href="../index.html#practice">練習問題</a>
      <a href="../test/index.html">確認テスト</a>
    </nav>
    <div class="hamburger" onclick="document.getElementById('mobileNav').classList.toggle('open')">
      <span></span><span></span><span></span>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobileNav">
  <a href="../index.html">ホーム</a>
  <a href="../index.html#grammar">文法解説</a>
  <a href="../index.html#practice">練習問題</a>
  <a href="../test/index.html">確認テスト</a>
  <a href="../word/index.html">英単語帳</a>
</div>'''

FOOTER = '''<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a><a href="../grammar/genkan1.html">現在完了</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a><a href="../practice/futeisi.html">不定詞</a></div>
    <div><h3>英単語</h3><a href="../word/index.html">単語帳</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''

# === 追加の練習問題データ ===
EXTRA_QUESTIONS = {
    "gimonhitei": [
        {"text":"Are you a student? に正しく答えなさい。", "options":["Yes, I am.","Yes, I do.","Yes, I are."], "answer":"Yes, I am.","explanation":"be動詞の疑問文には be動詞で答える"},
        {"text":"Do you like cats? に正しく答えなさい。", "options":["Yes, I like.","Yes, I do.","Yes, I am."], "answer":"Yes, I do.","explanation":"一般動詞の疑問文には do で答える"},
        {"text":"He ___ a teacher. (否定文に)", "options":["is not","does not","do not"], "answer":"is not","explanation":"be動詞の否定は be動詞+not"},
        {"text":"I ___ like coffee.", "options":["am not","don't","isn't"], "answer":"don't","explanation":"一般動詞の否定は don't"},
        {"text":"___ she a doctor?", "options":["Do","Is","Are"], "answer":"Is","explanation":"she のbe動詞疑問文は Is"},
        {"text":"___ they play soccer?", "options":["Do","Does","Are"], "answer":"Do","explanation":"they の一般動詞疑問文は Do"},
        {"text":"She ___ not a student.", "options":["do","does","is"], "answer":"is","explanation":"be動詞否定文"},
        {"text":"We ___ eat meat.", "options":["are not","don't","isn't"], "answer":"don't","explanation":"一般動詞否定文は don't"},
        {"text":"Is he kind? に正しく答えなさい。", "options":["Yes, he is.","Yes, he does.","Yes, he do."], "answer":"Yes, he is.","explanation":"be動詞の疑問文には be動詞で"},
        {"text":"___ you speak English?", "options":["Are","Do","Is"], "answer":"Do","explanation":"一般動詞の疑問文は Do"}
    ],
    "meirei": [
        {"text":"「座りなさい」", "options":["Sit down.","Sitting down.","Sat down."], "answer":"Sit down.","explanation":"命令文は動詞の原形で始める"},
        {"text":"「走ってはいけません」", "options":["Don't run.","Not run.","No run."], "answer":"Don't run.","explanation":"禁止文は Don't + 動詞の原形"},
        {"text":"「本を開きなさい」", "options":["Open your book.","Opening your book.","Opened your book."], "answer":"Open your book.","explanation":"命令文は動詞の原形"},
        {"text":"「遅れてはいけません」", "options":["Don't be late.","Not late.","Don't late."], "answer":"Don't be late.","explanation":"be動詞の命令文は Don't be"},
        {"text":"「大きい声で読みなさい」", "options":["Read aloud.","Reads aloud.","Reading aloud."], "answer":"Read aloud.","explanation":"命令文は動詞の原形"},
        {"text":"「教室で食べてはいけません」", "options":["Don't eat in class.","Not eat in class.","Eat not in class."], "answer":"Don't eat in class.","explanation":"禁止文は Don't + 動詞の原形"},
        {"text":"「こっちに来なさい」", "options":["Come here.","Came here.","Coming here."], "answer":"Come here.","explanation":"命令文は動詞の原形"},
        {"text":"「ドアを閉めなさい」", "options":["Close the door.","Closes the door.","Closed the door."], "answer":"Close the door.","explanation":"命令文は動詞の原形"},
        {"text":"「立ってください」の丁寧な表現", "options":["Stand up.","Please stand up.","Stood up."], "answer":"Please stand up.","explanation":"Please を付けると丁寧になる"},
        {"text":"「タバコを吸ってはいけません」", "options":["Don't smoke.","Not smoke.","Smoke not."], "answer":"Don't smoke.","explanation":"禁止文は Don't + 動詞の原形"}
    ],
    "bekako": [
        {"text":"I ___ happy yesterday.", "options":["was","were","am"], "answer":"was","explanation":"I のbe動詞過去形は was"},
        {"text":"They ___ at home last night.", "options":["was","were","are"], "answer":"were","explanation":"They には were"},
        {"text":"She ___ busy yesterday.", "options":["was","were","is"], "answer":"was","explanation":"She には was"},
        {"text":"___ you tired after the game?", "options":["Was","Were","Are"], "answer":"Were","explanation":"you の疑問文は Were"},
        {"text":"He ___ not at school yesterday.", "options":["was","were","is"], "answer":"was","explanation":"He の否定は was not"},
        {"text":"We ___ in the park last Sunday.", "options":["was","were","are"], "answer":"were","explanation":"We には were"},
        {"text":"___ she at the party?", "options":["Was","Were","Is"], "answer":"Was","explanation":"she の疑問文は Was"},
        {"text":"I ___ not sick yesterday.", "options":["was","were","am"], "answer":"was","explanation":"I の否定文は was not"},
        {"text":"My parents ___ at home yesterday.", "options":["was","were","are"], "answer":"were","explanation":"My parents は複数なので were"},
        {"text":"___ it cold this morning?", "options":["Was","Were","Is"], "answer":"Was","explanation":"it の疑問文は Was"}
    ],
    "kakosin": [
        {"text":"I ___ reading a book at that time.", "options":["was","were","am"], "answer":"was","explanation":"I の過去進行形は was + reading"},
        {"text":"They ___ playing soccer yesterday.", "options":["was","were","are"], "answer":"were","explanation":"They の過去進行形は were + playing"},
        {"text":"She ___ watching TV at 8pm.", "options":["was","were","is"], "answer":"was","explanation":"She には was + watching"},
        {"text":"___ you sleeping at midnight?", "options":["Was","Were","Are"], "answer":"Were","explanation":"you は Were"},
        {"text":"He ___ not studying at that time.", "options":["was","were","is"], "answer":"was","explanation":"否定文は was not"},
        {"text":"We ___ eating dinner at 7pm.", "options":["was","were","are"], "answer":"were","explanation":"We には were"},
        {"text":"What ___ you doing then?", "options":["was","were","are"], "answer":"were","explanation":"you の疑問文は Were"},
        {"text":"It ___ raining at that time.", "options":["was","were","is"], "answer":"was","explanation":"It には was"},
        {"text":"The children ___ playing in the park.", "options":["was","were","are"], "answer":"were","explanation":"children は複数なので were"},
        {"text":"___ he running in the park?", "options":["Was","Were","Is"], "answer":"Was","explanation":"he には Was"}
    ],
    "mirai": [
        {"text":"I ___ go to Tokyo tomorrow.", "options":["will","am","was"], "answer":"will","explanation":"未来は will + 動詞の原形"},
        {"text":"She ___ going to study law.", "options":["will","is","are"], "answer":"is","explanation":"be going to の主語に合わせて is"},
        {"text":"They ___ visit us next week.", "options":["will","are","were"], "answer":"will","explanation":"未来は will + 動詞の原形"},
        {"text":"___ you help me?", "options":["Will","Are","Do"], "answer":"Will","explanation":"未来の疑問文は Will を文頭に"},
        {"text":"It ___ rain tomorrow.", "options":["will","is","was"], "answer":"will","explanation":"未来の予測は will"},
        {"text":"I am ___ to visit Kyoto.", "options":["going","go","went"], "answer":"going","explanation":"be going to の形"},
        {"text":"He ___ not come to the party.", "options":["will","is","was"], "answer":"will","explanation":"否定文は will not (won't)"},
        {"text":"We ___ going to have a test.", "options":["are","is","am"], "answer":"are","explanation":"We には are going to"},
        {"text":"___ she going to buy a car?", "options":["Is","Are","Will"], "answer":"Is","explanation":"she の be going to 疑問文は Is"},
        {"text":"I think it ___ be sunny tomorrow.", "options":["will","am","was"], "answer":"will","explanation":"think のあとの未来は will"}
    ],
    "doumei": [
        {"text":"I like ___ books.", "options":["read","reading","reads"], "answer":"reading","explanation":"like + 動名詞（〜することが好き）"},
        {"text":"___ swimming is fun.", "options":["Go","Going","Goes"], "answer":"Going","explanation":"動名詞が主語になる"},
        {"text":"He enjoys ___ tennis.", "options":["play","playing","plays"], "answer":"playing","explanation":"enjoy + 動名詞"},
        {"text":"I finished ___ my homework.", "options":["do","doing","did"], "answer":"doing","explanation":"finish + 動名詞"},
        {"text":"___ is good for health.", "options":["Swim","Swimming","Swam"], "answer":"Swimming","explanation":"動名詞が主語になる"},
        {"text":"She stopped ___ coffee.", "options":["drink","drinking","drinks"], "answer":"drinking","explanation":"stop + 動名詞（〜するのをやめる）"},
        {"text":"I am good at ___ English.", "options":["speak","speaking","speaks"], "answer":"speaking","explanation":"at のあとは動名詞"},
        {"text":"He is interested in ___ history.", "options":["study","studying","studies"], "answer":"studying","explanation":"in のあとは動名詞"},
        {"text":"___ breakfast is important.", "options":["Eat","Eating","Ate"], "answer":"Eating","explanation":"動名詞が主語"},
        {"text":"They started ___ Japanese.", "options":["learn","learning","learns"], "answer":"learning","explanation":"start + 動名詞"}
    ],
    "jyodosi": [
        {"text":"You ___ study harder.", "options":["must","are","have"], "answer":"must","explanation":"must + 動詞の原形「〜しなければならない」"},
        {"text":"I ___ to go now.", "options":["must","have","has"], "answer":"have","explanation":"have to + 動詞の原形"},
        {"text":"She ___ to wear a uniform.", "options":["must","has","have"], "answer":"has","explanation":"She には has to"},
        {"text":"May I ___ in?", "options":["come","came","coming"], "answer":"come","explanation":"may + 動詞の原形"},
        {"text":"You ___ not run here.", "options":["must","have","are"], "answer":"must","explanation":"must not = 禁止"},
        {"text":"We ___ help each other.", "options":["should","are","have"], "answer":"should","explanation":"should + 動詞の原形「〜すべきだ」"},
        {"text":"You don't ___ to go.", "options":["must","have","has"], "answer":"have","explanation":"don't have to = 必要ない"},
        {"text":"He ___ be careful.", "options":["must","has","have"], "answer":"must","explanation":"must + 動詞の原形"},
        {"text":"___ I use your phone?", "options":["May","Must","Have"], "answer":"May","explanation":"許可を求める May I ~?"},
        {"text":"You ___ not tell anyone.", "options":["must","have","are"], "answer":"must","explanation":"must not = してはいけない"}
    ],
    "there": [
        {"text":"___ a cat under the table.", "options":["There is","There are","It is"], "answer":"There is","explanation":"単数名詞には There is"},
        {"text":"___ many books on the desk.", "options":["There is","There are","It is"], "answer":"There are","explanation":"複数名詞には There are"},
        {"text":"___ a pen on the desk?", "options":["Is there","Are there","There is"], "answer":"Is there","explanation":"単数の疑問文は Is there"},
        {"text":"There ___ not any water.", "options":["is","are","am"], "answer":"is","explanation":"water は不可算名詞なので is"},
        {"text":"___ any students in the room?", "options":["Is there","Are there","There are"], "answer":"Are there","explanation":"複数の疑問文は Are there"},
        {"text":"There ___ two cats in the garden.", "options":["is","are","am"], "answer":"are","explanation":"複数名詞には are"},
        {"text":"There ___ a book on the table.", "options":["is","are","am"], "answer":"is","explanation":"単数名詞には is"},
        {"text":"___ there a hospital near here?", "options":["Is","Are","Am"], "answer":"Is","explanation":"単数名詞の疑問文は Is"},
        {"text":"There ___ not any milk in the fridge.", "options":["is","are","am"], "answer":"is","explanation":"milk は不可算名詞なので is"},
        {"text":"There ___ three apples on the table.", "options":["is","are","am"], "answer":"are","explanation":"複数名詞には are"}
    ],
    "setuzoku": [
        {"text":"I like cats ___ dogs.", "options":["and","but","because"], "answer":"and","explanation":"and は「〜と〜」並列"},
        {"text":"I like cats ___ I don't like dogs.", "options":["and","but","because"], "answer":"but","explanation":"but は「しかし」逆接"},
        {"text":"I am happy ___ I got a present.", "options":["and","but","because"], "answer":"because","explanation":"because は「なぜなら」理由"},
        {"text":"Call me ___ you arrive.", "options":["when","but","and"], "answer":"when","explanation":"when は「〜するとき」"},
        {"text":"___ it rains, I will stay home.", "options":["When","If","But"], "answer":"If","explanation":"if は「もし〜なら」条件"},
        {"text":"I think ___ he is kind.", "options":["that","if","when"], "answer":"that","explanation":"that は「〜ということ」"},
        {"text":"She studied hard ___ she passed the exam.", "options":["and","but","because"], "answer":"and","explanation":"and で結果をつなぐ"},
        {"text":"I was tired, ___ I went to bed.", "options":["so","because","but"], "answer":"so","explanation":"so は「なので」結果"},
        {"text":"___ it is sunny, let's go out.", "options":["If","But","And"], "answer":"If","explanation":"条件を表す if"},
        {"text":"I know ___ she is honest.", "options":["that","if","when"], "answer":"that","explanation":"that 節で内容を説明"}
    ],
    "ukemi": [
        {"text":"English ___ spoken in many countries.", "options":["is","are","am"], "answer":"is","explanation":"受け身は be動詞 + 過去分詞"},
        {"text":"This book ___ written by Soseki.", "options":["was","were","is"], "answer":"was","explanation":"過去の受け身は was"},
        {"text":"The window ___ broken by the boy.", "options":["was","were","are"], "answer":"was","explanation":"単数主語の受け身は was"},
        {"text":"These cookies ___ made by my mother.", "options":["was","were","are"], "answer":"were","explanation":"複数主語の受け身は were"},
        {"text":"rice ___ eaten in Japan.", "options":["is","are","am"], "answer":"is","explanation":"rice は不可算名詞なので is"},
        {"text":"The car ___ repaired yesterday.", "options":["was","were","is"], "answer":"was","explanation":"過去の受け身は was"},
        {"text":"Many trees ___ planted in the park.", "options":["was","were","are"], "answer":"were","explanation":"複数主語の受け身は were"},
        {"text":"This song ___ sung by many people.", "options":["is","are","am"], "answer":"is","explanation":"受け身は be動詞 + 過去分詞"},
        {"text":"The letter ___ written in English.", "options":["was","were","is"], "answer":"was","explanation":"過去の受け身"},
        {"text":"The room ___ cleaned every day.", "options":["is","are","am"], "answer":"is","explanation":"現在の受け身は is"}
    ],
    "can": [
        {"text":"I ___ swim.", "options":["can","am","is"], "answer":"can","explanation":"can + 動詞の原形"},
        {"text":"She ___ speak French.", "options":["can","are","have"], "answer":"can","explanation":"can + 動詞の原形"},
        {"text":"___ you help me?", "options":["Can","Are","Do"], "answer":"Can","explanation":"疑問文は Can を文頭に"},
        {"text":"I ___ play the piano.", "options":["can't","am not","don't"], "answer":"can't","explanation":"否定文は can not (can't)"},
        {"text":"He ___ run fast.", "options":["can","is","has"], "answer":"can","explanation":"can + 動詞の原形"},
        {"text":"___ I use your pen?", "options":["Can","Am","Do"], "answer":"Can","explanation":"許可を求めるときも Can"},
        {"text":"We ___ see the mountain.", "options":["can","are","have"], "answer":"can","explanation":"can + 動詞の原形"},
        {"text":"She ___ cook well.", "options":["can","is","has"], "answer":"can","explanation":"can + 動詞の原形"},
        {"text":"___ he speak Japanese?", "options":["Can","Is","Does"], "answer":"Can","explanation":"疑問文は Can を文頭に"},
        {"text":"Yes, I ___.", "options":["can","am","do"], "answer":"can","explanation":"Can の疑問文には can で答える"}
    ],
    "kako": [
        {"text":"I ___ to the park yesterday.", "options":["went","go","going"], "answer":"went","explanation":"go の過去形は went"},
        {"text":"She ___ breakfast at seven.", "options":["eat","ate","eating"], "answer":"ate","explanation":"eat の過去形は ate"},
        {"text":"They ___ a movie last night.", "options":["see","saw","seeing"], "answer":"saw","explanation":"see の過去形は saw"},
        {"text":"I ___ my homework yesterday.", "options":["did","do","doing"], "answer":"did","explanation":"do の過去形は did"},
        {"text":"He ___ a good time at the party.", "options":["have","had","having"], "answer":"had","explanation":"have の過去形は had"},
        {"text":"She ___ a cake for me.", "options":["make","made","making"], "answer":"made","explanation":"make の過去形は made"},
        {"text":"We ___ to school by bus.", "options":["go","went","going"], "answer":"went","explanation":"go の過去形は went"},
        {"text":"I ___ a letter to my friend.", "options":["write","wrote","writing"], "answer":"wrote","explanation":"write の過去形は wrote"},
        {"text":"He ___ a new car.", "options":["buy","bought","buying"], "answer":"bought","explanation":"buy の過去形は bought"},
        {"text":"She ___ the window.", "options":["open","opened","opening"], "answer":"opened","explanation":"規則動詞 open の過去形は opened"}
    ],
    "shinko": [
        {"text":"I ___ reading a book now.", "options":["am","are","is"], "answer":"am","explanation":"現在進行形は be動詞 + doing"},
        {"text":"She ___ watching TV now.", "options":["am","are","is"], "answer":"is","explanation":"She には is + watching"},
        {"text":"They ___ playing soccer now.", "options":["am","are","is"], "answer":"are","explanation":"They には are + playing"},
        {"text":"___ you studying now?", "options":["Am","Are","Is"], "answer":"Are","explanation":"you の疑問文は Are"},
        {"text":"He ___ not sleeping now.", "options":["am","are","is"], "answer":"is","explanation":"He の否定文は is not"},
        {"text":"What ___ you doing now?", "options":["am","are","is"], "answer":"are","explanation":"you には are"},
        {"text":"The baby ___ crying.", "options":["am","are","is"], "answer":"is","explanation":"The baby (単数) には is"},
        {"text":"We ___ having lunch now.", "options":["am","are","is"], "answer":"are","explanation":"We には are"},
        {"text":"___ it raining now?", "options":["Am","Are","Is"], "answer":"Is","explanation":"it には Is"},
        {"text":"My mother ___ cooking dinner.", "options":["am","are","is"], "answer":"is","explanation":"My mother (単数) には is"}
    ],
    "santan2": [
        {"text":"He ___ tennis every Sunday.", "options":["play","plays","playing"], "answer":"plays","explanation":"He には plays"},
        {"text":"She ___ to school by bus.", "options":["go","goes","going"], "answer":"goes","explanation":"She には goes"},
        {"text":"___ she like music?", "options":["Do","Does","Is"], "answer":"Does","explanation":"she の疑問文は Does"},
        {"text":"He ___ play the piano.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"He の否定文は doesn't"},
        {"text":"The cat ___ milk.", "options":["drink","drinks","drinking"], "answer":"drinks","explanation":"The cat には drinks"},
        {"text":"___ he get up early?", "options":["Do","Does","Is"], "answer":"Does","explanation":"he の疑問文は Does"},
        {"text":"She ___ watch TV.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"She の否定文は doesn't"},
        {"text":"It ___ a lot in June.", "options":["rain","rains","raining"], "answer":"rains","explanation":"It には rains"},
        {"text":"___ your father drive a car?", "options":["Do","Does","Is"], "answer":"Does","explanation":"your father (単数) には Does"},
        {"text":"My sister ___ dance well.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"My sister (単数) には doesn't"}
    ]
}

# === 英単語データ ===
WORD_LIST = {
    "g1": {"grade":"中学1年","words":[
        {"en":"apple","ja":"りんご","example":"I like apples."},
        {"en":"book","ja":"本","example":"This is my book."},
        {"en":"cat","ja":"猫","example":"I have a cat."},
        {"en":"dog","ja":"犬","example":"The dog is cute."},
        {"en":"eat","ja":"食べる","example":"I eat breakfast."},
        {"en":"friend","ja":"友達","example":"She is my friend."},
        {"en":"good","ja":"良い","example":"This is a good book."},
        {"en":"happy","ja":"幸せな","example":"I am happy."},
        {"en":"interesting","ja":"面白い","example":"This book is interesting."},
        {"en":"Japanese","ja":"日本語","example":"I study Japanese."},
        {"en":"kind","ja":"親切な","example":"He is kind."},
        {"en":"like","ja":"好き","example":"I like music."},
        {"en":"music","ja":"音楽","example":"I listen to music."},
        {"en":"name","ja":"名前","example":"My name is Taro."},
        {"en":"old","ja":"古い","example":"This is an old house."},
        {"en":"play","ja":"遊ぶ","example":"I play tennis."},
        {"en":"read","ja":"読む","example":"I read books."},
        {"en":"school","ja":"学校","example":"I go to school."},
        {"en":"student","ja":"学生","example":"I am a student."},
        {"en":"teacher","ja":"先生","example":"She is a teacher."},
        {"en":"today","ja":"今日","example":"It is sunny today."},
        {"en":"under","ja":"〜の下に","example":"The cat is under the table."},
        {"en":"water","ja":"水","example":"I drink water."},
        {"en":"what","ja":"何","example":"What is this?"},
        {"en":"where","ja":"どこ","example":"Where is the station?"},
        {"en":"white","ja":"白い","example":"It is white."},
        {"en":"year","ja":"年","example":"I am 12 years old."},
        {"en":"young","ja":"若い","example":"She is young."},
        {"en":"zoo","ja":"動物園","example":"Let's go to the zoo."},
        {"en":"tennis","ja":"テニス","example":"I play tennis."},
        {"en":"soccer","ja":"サッカー","example":"He plays soccer."},
        {"en":"piano","ja":"ピアノ","example":"She plays the piano."},
        {"en":"sister","ja":"姉/妹","example":"I have a sister."},
        {"en":"brother","ja":"兄/弟","example":"My brother is tall."},
        {"en":"mother","ja":"母","example":"My mother is kind."},
    ]},
    "g2": {"grade":"中学2年","words":[
        {"en":"beautiful","ja":"美しい","example":"She is beautiful."},
        {"en":"become","ja":"〜になる","example":"I want to become a doctor."},
        {"en":"between","ja":"〜の間に","example":"The cat is between the boxes."},
        {"en":"breakfast","ja":"朝食","example":"I eat breakfast at seven."},
        {"en":"careful","ja":"注意深い","example":"Be careful."},
        {"en":"dangerous","ja":"危険な","example":"This is dangerous."},
        {"en":"delicious","ja":"美味しい","example":"This is delicious."},
        {"en":"different","ja":"異なる","example":"We are different."},
        {"en":"difficult","ja":"難しい","example":"This math is difficult."},
        {"en":"enjoy","ja":"楽しむ","example":"I enjoy music."},
        {"en":"everything","ja":"すべて","example":"Everything is OK."},
        {"en":"exciting","ja":"わくわくする","example":"This game is exciting."},
        {"en":"expensive","ja":"高い","example":"This bag is expensive."},
        {"en":"foreign","ja":"外国の","example":"I like foreign countries."},
        {"en":"important","ja":"重要な","example":"This is important."},
        {"en":"language","ja":"言語","example":"English is a language."},
        {"en":"library","ja":"図書館","example":"I go to the library."},
        {"en":"mountain","ja":"山","example":"Mt.Fuji is a mountain."},
        {"en":"necessary","ja":"必要な","example":"Water is necessary."},
        {"en":"outside","ja":"外","example":"Let's play outside."},
        {"en":"practice","ja":"練習","example":"Practice makes perfect."},
        {"en":"problem","ja":"問題","example":"This is a hard problem."},
        {"en":"remember","ja":"覚える","example":"Remember this word."},
        {"en":"restaurant","ja":"レストラン","example":"Let's go to a restaurant."},
        {"en":"sandwich","ja":"サンドイッチ","example":"I ate a sandwich."},
        {"en":"should","ja":"すべき","example":"You should study."},
        {"en":"stadium","ja":"スタジアム","example":"The game is at the stadium."},
        {"en":"tomorrow","ja":"明日","example":"See you tomorrow."},
        {"en":"university","ja":"大学","example":"I want to go to university."},
        {"en":"weather","ja":"天気","example":"The weather is nice."},
    ]},
    "g3": {"grade":"中学3年","words":[
        {"en":"achieve","ja":"達成する","example":"I achieved my goal."},
        {"en":"actually","ja":"実際に","example":"Actually, it's true."},
        {"en":"believe","ja":"信じる","example":"I believe you."},
        {"en":"century","ja":"世紀","example":"21st century."},
        {"en":"climate","ja":"気候","example":"The climate is warm."},
        {"en":"communicate","ja":"伝える","example":"Let's communicate."},
        {"en":"community","ja":"地域社会","example":"Our community is nice."},
        {"en":"completely","ja":"完全に","example":"I completely agree."},
        {"en":"conference","ja":"会議","example":"I have a conference."},
        {"en":"consider","ja":"考える","example":"Consider this problem."},
        {"en":"continue","ja":"続ける","example":"Continue your study."},
        {"en":"contribute","ja":"貢献する","example":"I want to contribute."},
        {"en":"culture","ja":"文化","example":"Japanese culture."},
        {"en":"decision","ja":"決断","example":"Make a decision."},
        {"en":"development","ja":"発展","example":"Economic development."},
        {"en":"disappear","ja":"消える","example":"It disappeared."},
        {"en":"discover","ja":"発見する","example":"I discovered it."},
        {"en":"economy","ja":"経済","example":"The economy is growing."},
        {"en":"education","ja":"教育","example":"Education is important."},
        {"en":"election","ja":"選挙","example":"The election is next month."},
        {"en":"employment","ja":"雇用","example":"Employment is stable."},
        {"en":"encourage","ja":"励ます","example":"She encouraged me."},
        {"en":"environment","ja":"環境","example":"Protect the environment."},
        {"en":"especially","ja":"特に","example":"I like fruit, especially apples."},
        {"en":"experience","ja":"経験","example":"This is a good experience."},
        {"en":"government","ja":"政府","example":"The government decided."},
        {"en":"independence","ja":"独立","example":"Independence Day."},
        {"en":"international","ja":"国際的な","example":"International relations."},
        {"en":"opportunity","ja":"機会","example":"This is a good opportunity."},
        {"en":"population","ja":"人口","example":"The population is large."},
    ]}
}

def gen_practice_page(key, questions, name):
    q_json = json.dumps(questions, ensure_ascii=False)
    html = HEADER.format(title=f"{name} 練習問題", desc=f"中学英語 {name} の練習問題")
    html += f'<div class="breadcrumb"><a href="../index.html">ホーム</a> > <a href="../index.html#practice">練習問題</a> > {name}</div>\n'
    html += f'<div class="page-header"><h1>{name} 練習問題</h1><p>全{len(questions)}問。</p></div>\n'
    html += f'''
<div class="container">
  <div class="practice-box" id="practiceApp">
    <div class="question-card" v-for="(q, i) in questions" :key="i">
      <div class="q-number">{{{{ i + 1 }}}}</div>
      <div class="q-text">{{{{ q.text }}}}</div>
      <div class="q-options">
        <div v-for="opt in q.options" :key="opt"
          class="q-option"
          :class="{{ '{' }} correct: answered[i] && opt === q.answer, wrong: answered[i] && selected[i] === opt && opt !== q.answer {{ '}' }}"
          @click="selectAnswer(i, opt)">
          {{{{ opt }}}}
        </div>
      </div>
      <div class="feedback" :class="{{ '{' }} show: answered[i], correct: answered[i] && selected[i] === q.answer, wrong: answered[i] && selected[i] !== q.answer {{ '}' }}">
        <template v-if="answered[i] && selected[i] === q.answer">✅ {{{{ q.explanation }}}}</template>
        <template v-else-if="answered[i]">❌ 正解は「{{{{ q.answer }}}}」 {{{{ q.explanation }}}}</template>
      </div>
    </div>
    <div style="text-align:center;margin:24px 0;">
      <button class="hero-btn primary" @click="resetAll" style="border:none;cursor:pointer;">🔄 やり直す</button>
    </div>
    <div class="test-result" v-if="allAnswered">
      <div class="score">{{{{ score }}}} / {len(questions)}</div>
      <div class="rank">{{{{ score === questions.length ? '🎉 満点！' : score >= 7 ? '👍 よくできました！' : '💪 もう一度！' }}}}</div>
    </div>
  </div>
</div>
'''
    html += '<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>\n'
    html += FOOTER
    html += f'''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const {{ createApp }} = Vue;
createApp({{
  data() {{ return {{ selected: {{}}, answered: {{}}, questions: {q_json} }}; }},
  computed: {{ allAnswered() {{ return this.questions.every((_, i) => this.answered[i]); }}, score() {{ return this.questions.filter((q, i) => this.selected[i] === q.answer).length; }} }},
  methods: {{ selectAnswer(i, opt) {{ if (this.answered[i]) return; this.selected[i] = opt; this.answered[i] = true; }}, resetAll() {{ this.selected = {{}}; this.answered = {{}}; }} }}
}}).mount('#practiceApp');
</script>
</body>
</html>'''
    path = os.path.join(BASE, "practice", f"{key}.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  practice/{key}.html")

def gen_test_page(key, questions, name):
    q_json = json.dumps(questions, ensure_ascii=False)
    html = HEADER.format(title=f"{name} 確認テスト", desc=f"中学英語 {name} の確認テスト")
    html += f'<div class="breadcrumb"><a href="../index.html">ホーム</a> > <a href="index.html">確認テスト</a> > {name}</div>\n'
    html += f'<div class="page-header"><h1>{name} 確認テスト</h1><p>制限時間5分。全{len(questions)}問。</p></div>\n'
    html += f'''
<div class="container">
  <div class="test-header">
    <div class="timer" id="timerDisplay">05:00</div>
    <div class="progress" id="progressDisplay">0 / {len(questions)} 問解答</div>
  </div>
  <div class="practice-box" id="testApp">
    <div class="question-card" v-for="(q, i) in questions" :key="i">
      <div class="q-number">{{{{ i + 1 }}}}</div>
      <div class="q-text">{{{{ q.text }}}}</div>
      <div class="q-options">
        <div v-for="opt in q.options" :key="opt"
          class="q-option"
          :class="{{ '{' }} correct: finished && opt === q.answer, wrong: finished && selected[i] === opt && opt !== q.answer {{ '}' }}"
          @click="selectAnswer(i, opt)">
          {{{{ opt }}}}
        </div>
      </div>
    </div>
    <div style="text-align:center;margin:24px 0;">
      <button class="hero-btn primary" @click="submitTest" :disabled="!allAnswered" style="border:none;cursor:pointer;">📊 採点する</button>
    </div>
    <div class="test-result" v-if="finished">
      <div class="score">{{{{ score }}}} / {len(questions)}</div>
      <div class="label">正答率 {{{{ Math.round(score / questions.length * 100) }}}}%</div>
      <div class="rank">{{{{ score === questions.length ? '🎉 満点！' : score >= 7 ? '👍 よくできました！' : '💪 もう一度！' }}}}</div>
      <div style="margin-top:16px;">
        <button class="hero-btn secondary" @click="retry" style="border:none;cursor:pointer;background:var(--gray-600);color:#fff;">🔄 もう一度</button>
      </div>
    </div>
  </div>
</div>
'''
    html += '<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>\n'
    html += FOOTER
    html += f'''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const {{ createApp }} = Vue;
createApp({{
  data() {{ return {{
    selected: {{}}, finished: false,
    timerMinutes: 5, timerSeconds: 0, timerInterval: null, timeUp: false,
    questions: {q_json}
  }}; }},
  computed: {{
    allAnswered() {{ return this.questions.every((_, i) => this.selected[i]); }},
    score() {{ return this.questions.filter((q, i) => this.selected[i] === q.answer).length; }}
  }},
  methods: {{
    selectAnswer(i, opt) {{ if (this.finished || this.timeUp) return; this.selected[i] = opt; document.getElementById('progressDisplay').textContent = `${{{{Object.keys(this.selected).length}}}} / ${{{{this.questions.length}}}} 問解答`; }},
    submitTest() {{ if (!this.allAnswered) return; this.finished = true; if (this.timerInterval) clearInterval(this.timerInterval); }},
    retry() {{ this.selected = {{}}; this.finished = false; this.timeUp = false; this.timerMinutes = 5; this.timerSeconds = 0; document.getElementById('timerDisplay').textContent = '05:00'; document.getElementById('progressDisplay').textContent = '0 / {len(questions)} 問解答'; this.startTimer(); }},
    startTimer() {{ this.timerInterval = setInterval(() => {{ if (this.timerSeconds === 0) {{ if (this.timerMinutes === 0) {{ clearInterval(this.timerInterval); this.timeUp = true; this.finished = true; return; }} this.timerMinutes--; this.timerSeconds = 59; }} else {{ this.timerSeconds--; }} document.getElementById('timerDisplay').textContent = `${{{{String(this.timerMinutes).padStart(2, '0')}}}}:${{{{String(this.timerSeconds).padStart(2, '0')}}}}`; }}, 1000); }}
  }},
  mounted() {{ this.startTimer(); }}
}}).mount('#testApp');
</script>
</body>
</html>'''
    path = os.path.join(BASE, "test", f"{key}_test.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  test/{key}_test.html")

def gen_word_page():
    """英単語帳ページを生成"""
    word_data_json = json.dumps(WORD_LIST, ensure_ascii=False)
    html = HEADER.format(title="英単語帳", desc="中学英語の英単語を学年別に学習。意味・例文付き。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > 英単語帳</div>
<div class="page-header">
  <h1>📖 英単語帳</h1>
  <p>中学英語で習う単語を学年別にチェック。タップ/クリックで意味を確認できます。</p>
</div>
<div class="container">
  <div class="grade-tabs" id="wordTabs">
    <button class="grade-tab active" data-grade="g1" onclick="showGrade('g1')">中学1年</button>
    <button class="grade-tab" data-grade="g2" onclick="showGrade('g2')">中学2年</button>
    <button class="grade-tab" data-grade="g3" onclick="showGrade('g3')">中学3年</button>
  </div>
  <div id="wordApp">
    <div class="grammar-grid">
      <div class="grammar-card" v-for="w in currentWords" :key="w.en" @click="w.show = !w.show">
        <h3>{{ w.en }}</h3>
        <p v-if="w.show" style="color:var(--primary);font-weight:700;font-size:1.2rem;">{{ w.ja }}</p>
        <p v-else style="color:var(--gray-400);">タップで意味を表示</p>
        <p style="color:var(--gray-500);font-size:0.85rem;margin-top:8px;">{{ w.example }}</p>
      </div>
    </div>
  </div>
</div>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>'''
    html += FOOTER
    html += f'''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const wordData = {word_data_json};
const {{ createApp }} = Vue;
const app = createApp({{
  data() {{ return {{ currentGrade: 'g1' }}; }},
  computed: {{
    currentWords() {{ 
      const words = wordData[this.currentGrade]?.words || [];
      return words.map(w => ({{ ...w, show: false }}));
    }}
  }}
}}).mount('#wordApp');

function showGrade(g) {{
  document.querySelectorAll('.grade-tab').forEach(t => t.classList.remove('active'));
  document.querySelector(`[data-grade="${{g}}"]`).classList.add('active');
  app.currentGrade = g;
}}
</script>
</body>
</html>'''
    os.makedirs(os.path.join(BASE, "word"), exist_ok=True)
    path = os.path.join(BASE, "word", "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  word/index.html")

if __name__ == "__main__":
    name_map = {
        "gimonhitei":"疑問文・否定文","meirei":"命令文","bekako":"be動詞の過去形","kakosin":"過去進行形",
        "mirai":"未来形","doumei":"動名詞","jyodosi":"助動詞","there":"there is 構文",
        "setuzoku":"接続詞","ukemi":"受け身","can":"can","kako":"一般動詞の過去形","shinko":"現在進行形","santan2":"三人称単数現在"
    }
    print("=== 追加練習問題生成 ===")
    for key, questions in EXTRA_QUESTIONS.items():
        name = name_map[key]
        gen_practice_page(key, questions, name)
    print("=== 追加確認テスト生成 ===")
    for key, questions in EXTRA_QUESTIONS.items():
        name = name_map[key]
        gen_test_page(key, questions, name)
    print("=== 英単語帳生成 ===")
    gen_word_page()
    print("=== 完了 ===")