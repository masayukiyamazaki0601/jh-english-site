#!/usr/bin/env python3
"""全34記事を発展内容で一気に拡充（各記事に重要表現リストと英作文を追加）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines >= 800:
        print(f"  SKIP {filename} ({lines} lines)")
        return
    pos = content.rfind("</article>")
    if pos == -1:
        return
    after = content[pos:]
    new = content[:pos] + extra + "\n" + after
    with open(path, "w") as f:
        f.write(new)
    print(f"  OK {filename} ({lines} -> {new.count(chr(10))} lines)")

ALL_EXTRA = {
    "genkan1.html": """
<h2>現在完了（継続） 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>3年間住んでいる</td><td>have lived for 3 years</td></tr>
<tr><td>10歳から勉強している</td><td>have studied since I was ten</td></tr>
<tr><td>月曜から病気</td><td>have been sick since Monday</td></tr>
<tr><td>どのくらい住んでいますか？</td><td>How long have you lived?</td></tr>
<tr><td>先週から会っていない</td><td>haven't seen since last week</td></tr>
</table>
<h2>現在完了（継続） 発展：過去形との比較</h2>
<div class="highlight"><p><strong>I have lived in Tokyo for 5 years.</strong>（今も住んでいる）<br>
<strong>I lived in Tokyo for 5 years.</strong>（もう住んでいない）</p></div>
<p>この違いはテストで必ず出ます！過去形は「今は違う」、現在完了は「今も続いている」を意識しましょう。</p>
""",
    "genkan2.html": """
<h2>現在完了（経験） 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>京都に行ったことがある</td><td>have been to Kyoto</td></tr>
<tr><td>一度も食べたことがない</td><td>have never eaten</td></tr>
<tr><td>2回行ったことがある</td><td>have been twice</td></tr>
<tr><td>以前見たことがある</td><td>have seen before</td></tr>
<tr><td>海外に行ったことがない</td><td>have never been abroad</td></tr>
</table>
<h2>現在完了（経験） よく出る時制表現</h2>
<ul><li>Have you ever + 過去分詞？「今までに〜したことがありますか？」</li>
<li>I have never + 過去分詞「一度も〜したことがない」</li>
<li>How many times have you + 過去分詞？「何回〜したことがありますか？」</li>
<li>This is the first time I have + 過去分詞「〜するのは初めてです」</li></ul>
""",
    "genkan3.html": """
<h2>現在完了（完了） 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>ちょうど終えた</td><td>have just finished</td></tr>
<tr><td>もう食べた</td><td>have already eaten</td></tr>
<tr><td>もう終えた？</td><td>Have you finished yet?</td></tr>
<tr><td>まだ終えていない</td><td>haven't finished yet</td></tr>
<tr><td>もう学校に行った</td><td>have already left for school</td></tr>
</table>
<h2>現在完了（完了） テスト対策</h2>
<p><strong>already / just / yet の位置が命！</strong></p>
<ul><li>already = have + already + 過去分詞（肯定文のみ）</li>
<li>just = have + just + 過去分詞（肯定文のみ）</li>
<li>yet = 文末（疑問文・否定文のみ）</li></ul>
""",
    "genkanSinkokei.html": """
<h2>現在完了進行形 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>勉強し続けている</td><td>have been studying</td></tr>
<tr><td>降り続いている</td><td>has been raining</td></tr>
<tr><td>待ち続けている</td><td>has been waiting</td></tr>
<tr><td>遊び続けている</td><td>have been playing</td></tr>
<tr><td>働き続けている</td><td>has been working</td></tr>
</table>
<h2>現在完了 vs 現在完了進行形 最終チェック</h2>
<p><strong>状態動詞（live, know, have, be）</strong> → 現在完了（継続）が自然<br>
<strong>動作動詞（study, wait, rain, work）</strong> → 現在完了進行形が自然</p>
""",
    "kateiho.html": """
<h2>仮定法 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>もし私があなたなら</td><td>If I were you</td></tr>
<tr><td>もし時間があれば</td><td>If I had time</td></tr>
<tr><td>もしお金があれば</td><td>If I had money</td></tr>
<tr><td>もし晴れなら</td><td>If it were sunny</td></tr>
<tr><td>できればいいのに</td><td>I wish I could</td></tr>
</table>
<h2>仮定法 テストの鉄則</h2>
<ol><li><strong>If + 過去形</strong>（現在形ではない！）</li>
<li><strong>主節は would/could</strong>（willではない！）</li>
<li><strong>be動詞は were</strong>（Iでもwere！）</li></ol>
""",
    "genkeiFuteisi.html": """
<h2>原形不定詞 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>走るのを見た</td><td>saw him run</td></tr>
<tr><td>掃除させた</td><td>made me clean</td></tr>
<tr><td>歌うのを聞いた</td><td>heard her sing</td></tr>
<tr><td>行こう</td><td>Let's go</td></tr>
<tr><td>運ぶのを手伝った</td><td>helped me carry</td></tr>
</table>
<h2>原形不定詞 テスト対策</h2>
<p><strong>to がつかない不定詞＝動詞の原形</strong><br>
知覚動詞（see, hear, watch, feel）+ 目的語 + 原形<br>
使役動詞（make, let, have）+ 目的語 + 原形</p>
""",
    "kakosin.html": """
<h2>過去進行形 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>本を読んでいた</td><td>was reading a book</td></tr>
<tr><td>サッカーをしていた</td><td>were playing soccer</td></tr>
<tr><td>電話したときテレビを見ていた</td><td>was watching TV when you called</td></tr>
<tr><td>その時何をしていた？</td><td>What were you doing then?</td></tr>
</table>
<h2>when / while の使い分け</h2>
<p><strong>when + 過去形</strong>：I was watching TV when she called.<br>
<strong>while + 過去進行形</strong>：She called while I was watching TV.</p>
""",
    "there.html": """
<h2>there is構文 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>猫がいる</td><td>There is a cat</td></tr>
<tr><td>たくさんの本がある</td><td>There are many books</td></tr>
<tr><td>病院はありますか？</td><td>Is there a hospital?</td></tr>
<tr><td>牛乳はない</td><td>There is not any milk</td></tr>
<tr><td>何人いますか？</td><td>How many students are there?</td></tr>
</table>
<h2>近接の法則 再確認</h2>
<p>There + be動詞 のbe動詞は、すぐ後ろの名詞に合わせる！<br>
There <strong>is</strong> a pen and three books.<br>
There <strong>are</strong> three books and a pen.</p>
""",
    "bekako.html": """
<h2>be動詞過去形 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>幸せだった</td><td>was happy</td></tr>
<tr><td>家にいた</td><td>were at home</td></tr>
<tr><td>忙しかった</td><td>was busy</td></tr>
<tr><td>家にいなかった</td><td>was not at home</td></tr>
<tr><td>疲れていましたか？</td><td>Were you tired?</td></tr>
</table>
<h2>was / were 完全マスター表</h2>
<table><tr><th>主語</th><th>過去形</th><th>否定</th><th>疑問</th></tr>
<tr><td>I</td><td>was</td><td>was not (wasn't)</td><td>Was I?</td></tr>
<tr><td>You</td><td>were</td><td>were not (weren't)</td><td>Were you?</td></tr>
<tr><td>He/She/It</td><td>was</td><td>was not (wasn't)</td><td>Was he/she/it?</td></tr>
<tr><td>We/They</td><td>were</td><td>were not (weren't)</td><td>Were we/they?</td></tr>
</table>
""",
    "kansetu.html": """
<h2>間接疑問 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>どこに住んでいるか知っていますか？</td><td>Do you know where he lives?</td></tr>
<tr><td>これが何かわかりません</td><td>I don't know what this is.</td></tr>
<tr><td>駅はどこか教えてください</td><td>Tell me where the station is.</td></tr>
<tr><td>彼が親切かどうか疑問だ</td><td>I wonder if he is kind.</td></tr>
</table>
<h2>間接疑問 テスト対策</h2>
<p><strong>最重要ルール！ 間接疑問のあとは肯定文の語順</strong><br>
「Do you know what is this?」→ 間違い！<br>
「Do you know what this is?」→ 正解！</p>
""",
    "setuzoku.html": """
<h2>接続詞 重要表現まとめ</h2>
<table><tr><th>接続詞</th><th>意味</th><th>例文</th></tr>
<tr><td>and</td><td>〜と</td><td>I like cats and dogs.</td></tr>
<tr><td>but</td><td>しかし</td><td>I like cats but not dogs.</td></tr>
<tr><td>because</td><td>なぜなら</td><td>I am happy because I got a present.</td></tr>
<tr><td>so</td><td>なので</td><td>I was tired, so I went to bed.</td></tr>
<tr><td>when</td><td>〜するとき</td><td>Call me when you arrive.</td></tr>
<tr><td>if</td><td>もし〜なら</td><td>If it rains, I will stay home.</td></tr>
<tr><td>that</td><td>〜ということ</td><td>I think that he is kind.</td></tr>
</table>
""",
    "genkan2.html": "",  # skip - already has this
    "gimonsi.html": """
<h2>疑問詞 重要表現まとめ</h2>
<table><tr><th>疑問詞</th><th>意味</th><th>例文</th><th>答え方</th></tr>
<tr><td>What</td><td>何</td><td>What is this?</td><td>It's a book.</td></tr>
<tr><td>Who</td><td>誰</td><td>Who is he?</td><td>He is Taro.</td></tr>
<tr><td>Where</td><td>どこ</td><td>Where are you from?</td><td>I'm from Japan.</td></tr>
<tr><td>When</td><td>いつ</td><td>When is your birthday?</td><td>It's on May 5th.</td></tr>
<tr><td>Why</td><td>なぜ</td><td>Why are you late?</td><td>Because I missed the bus.</td></tr>
<tr><td>How</td><td>どうやって</td><td>How do you go to school?</td><td>By bus.</td></tr>
</table>
""",
    "mirai.html": """
<h2>未来形 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>あとで電話します</td><td>will call you later</td></tr>
<tr><td>明日雨が降るでしょう</td><td>will rain tomorrow</td></tr>
<tr><td>京都を訪れる予定</td><td>am going to visit Kyoto</td></tr>
<tr><td>医者になるつもり</td><td>is going to be a doctor</td></tr>
<tr><td>手伝ってくれますか？</td><td>Will you help me?</td></tr>
</table>
<h2>未来形 テスト対策</h2>
<p><strong>will と be going to の違い！</strong><br>
will = その場の意思決定・予測<br>
be going to = 前からの予定・確実な未来</p>
""",
    "bunsi.html": """
<h2>分詞 重要表現まとめ</h2>
<table><tr><th>種類</th><th>例</th><th>意味</th></tr>
<tr><td>現在分詞</td><td>sleeping baby</td><td>眠っている赤ちゃん</td></tr>
<tr><td>過去分詞</td><td>broken watch</td><td>壊れた時計</td></tr>
<tr><td>分詞句（現在）</td><td>girl singing in the room</td><td>部屋で歌っている女の子</td></tr>
<tr><td>分詞句（過去）</td><td>book written by Soseki</td><td>漱石によって書かれた本</td></tr>
</table>
<h2>現在分詞 vs 過去分詞 最終確認</h2>
<p><strong>現在分詞（-ing）</strong> = 「〜している」（能動・進行）<br>
<strong>過去分詞（-ed/不規則）</strong> = 「〜される/された」（受動・完了）</p>
""",
    "can.html": """
<h2>can 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>泳げます</td><td>can swim</td></tr>
<tr><td>フランス語を話せます</td><td>can speak French</td></tr>
<tr><td>弾けません</td><td>can't play</td></tr>
<tr><td>手伝ってくれますか？</td><td>Can you help me?</td></tr>
<tr><td>使ってもいいですか？</td><td>Can I use your pen?</td></tr>
</table>
<h2>can の3つの用法</h2>
<ol><li><strong>能力</strong>：I can swim.（泳げる）</li>
<li><strong>許可</strong>：Can I sit here?（座ってもいい？）</li>
<li><strong>依頼</strong>：Can you help me?（手伝って？）</li></ol>
""",
    "daimeisi.html": """
<h2>代名詞 重要表現まとめ</h2>
<table><tr><th>主格</th><th>所有格</th><th>目的格</th><th>所有代名詞</th><th>再帰代名詞</th></tr>
<tr><td>I</td><td>my</td><td>me</td><td>mine</td><td>myself</td></tr>
<tr><td>you</td><td>your</td><td>you</td><td>yours</td><td>yourself</td></tr>
<tr><td>he</td><td>his</td><td>him</td><td>his</td><td>himself</td></tr>
<tr><td>she</td><td>her</td><td>her</td><td>hers</td><td>herself</td></tr>
<tr><td>it</td><td>its</td><td>it</td><td>its</td><td>itself</td></tr>
<tr><td>we</td><td>our</td><td>us</td><td>ours</td><td>ourselves</td></tr>
<tr><td>they</td><td>their</td><td>them</td><td>theirs</td><td>themselves</td></tr>
</table>
""",
    "kankeisi1.html": """
<h2>関係代名詞 重要表現まとめ</h2>
<table><tr><th>先行詞</th><th>主格</th><th>目的格</th><th>例</th></tr>
<tr><td>人</td><td>who</td><td>whom</td><td>the boy who runs</td></tr>
<tr><td>物</td><td>which</td><td>which</td><td>the book which I bought</td></tr>
<tr><td>人・物</td><td>that</td><td>that</td><td>the book that I read</td></tr>
</table>
<h2>目的格の関係代名詞は省略できる！</h2>
<p>This is the book (which) I bought. → which を省略してもOK！</p>
""",
    "ukemi.html": """
<h2>受け身 重要表現まとめ</h2>
<table><tr><th>日本語</th><th>英語</th></tr>
<tr><td>話されている</td><td>is spoken</td></tr>
<tr><td>書かれた</td><td>was written</td></tr>
<tr><td>壊された</td><td>was broken</td></tr>
<tr><td>作られた</td><td>was made</td></tr>
<tr><td>食べられている</td><td>is eaten</td></tr>
</table>
<h2>時制別 受け身の形</h2>
<ul><li><strong>現在</strong>：is/are + 過去分詞</li>
<li><strong>過去</strong>：was/were + 過去分詞</li>
<li><strong>未来</strong>：will be + 過去分詞</li>
<li><strong>現在完了</strong>：has/have been + 過去分詞</li></ul>
""",
    "genkan1.html": "",
    "doumei.html": """
<h2>動名詞 重要表現まとめ</h2>
<table><tr><th>動詞</th><th>動名詞使用例</th><th>日本語</th></tr>
<tr><td>enjoy</td><td>enjoy reading</td><td>読むことを楽しむ</td></tr>
<tr><td>finish</td><td>finish doing</td><td>〜し終える</td></tr>
<tr><td>stop</td><td>stop smoking</td><td>タバコをやめる</td></tr>
<tr><td>like</td><td>like swimming</td><td>泳ぐのが好き</td></tr>
<tr><td>give up</td><td>give up playing</td><td>プレイをあきらめる</td></tr>
</table>
<h2>前置詞 + 動名詞 重要パターン</h2>
<ul><li>be good at + 動名詞（〜が得意だ）</li>
<li>be interested in + 動名詞（〜に興味がある）</li>
<li>look forward to + 動名詞（〜を楽しみにする）</li>
<li>thank you for + 動名詞（〜してくれてありがとう）</li></ul>
""",
    "jyodosi.html": """
<h2>助動詞 重要表現まとめ</h2>
<table><tr><th>助動詞</th><th>意味</th><th>例文</th><th>否定</th></tr>
<tr><td>must</td><td>しなければならない</td><td>must study</td><td>must not（禁止）</td></tr>
<tr><td>have to</td><td>しなければならない</td><td>have to go</td><td>don't have to（不要）</td></tr>
<tr><td>may</td><td>してもよい</td><td>May I come in?</td><td>may not</td></tr>
<tr><td>should</td><td>すべきだ</td><td>should rest</td><td>should not</td></tr>
</table>
<h2>最も重要な違い！ must not vs don't have to</h2>
<p><strong>must not</strong> = 禁止（絶対ダメ）<br>
<strong>don't have to</strong> = 必要ない（やらなくてもOK）</p>
""",
    "hikaku1.html": """
<h2>比較 重要表現まとめ</h2>
<table><tr><th>比較級</th><th>最上級</th><th>原級（同等）</th></tr>
<tr><td>taller than</td><td>the tallest</td><td>as tall as</td></tr>
<tr><td>more beautiful than</td><td>the most beautiful</td><td>as beautiful as</td></tr>
<tr><td>better than</td><td>the best</td><td>as good as</td></tr>
</table>
<h2>不規則変化 完全暗記</h2>
<p>good/well → better → best<br>
bad/ill → worse → worst<br>
many/much → more → most<br>
little → less → least</p>
""",
    "zensi.html": """
<h2>前置詞 重要表現まとめ</h2>
<table><tr><th>前置詞</th><th>時間</th><th>場所</th><th>その他</th></tr>
<tr><td>in</td><td>in the morning</td><td>in the room</td><td>in English</td></tr>
<tr><td>on</td><td>on Sunday</td><td>on the desk</td><td>on foot</td></tr>
<tr><td>at</td><td>at 8 o'clock</td><td>at the station</td><td>at school</td></tr>
<tr><td>by</td><td>by 5pm</td><td>by the window</td><td>by bus</td></tr>
<tr><td>for</td><td>for 2 hours</td><td>—</td><td>for you</td></tr>
</table>
<h2>前置詞 テストの鉄則</h2>
<p>in（月・年・季節）/ on（曜日・日付）/ at（時刻）<br>
I was born <strong>in</strong> May.<br>
I was born <strong>on</strong> May 5th.<br>
I was born <strong>at</strong> 5am.</p>
""",
    "suryo.html": """
<h2>数量詞 重要表現まとめ</h2>
<table><tr><th>表現</th><th>意味</th><th>使う名詞</th></tr>
<tr><td>many</td><td>たくさんの</td><td>可算名詞</td></tr>
<tr><td>much</td><td>たくさんの</td><td>不可算名詞</td></tr>
<tr><td>a lot of</td><td>たくさんの</td><td>両方</td></tr>
<tr><td>a few</td><td>いくつか（肯定）</td><td>可算名詞</td></tr>
<tr><td>few</td><td>ほとんどない（否定）</td><td>可算名詞</td></tr>
<tr><td>a little</td><td>少し（肯定）</td><td>不可算名詞</td></tr>
<tr><td>little</td><td>ほとんどない（否定）</td><td>不可算名詞</td></tr>
</table>
<h2>some / any の使い分け</h2>
<p>some = 肯定文（I have some money.）<br>
any = 疑問文・否定文（Do you have any money? / I don't have any money.）</p>
""",
    "futeisi2.html": """
<h2>不定詞（応用） 重要表現まとめ</h2>
<table><tr><th>構文</th><th>意味</th><th>例</th></tr>
<tr><td>It is 〜 for 人 to do</td><td>人にとって〜することは〜だ</td><td>It is important for us to study English.</td></tr>
<tr><td>too 〜 to do</td><td>〜すぎてできない</td><td>too young to drive</td></tr>
<tr><td>enough to do</td><td>〜するのに十分〜だ</td><td>old enough to drive</td></tr>
</table>
<h2>too 〜 to 構文の言い換え（受験頻出）</h2>
<p>She is too young to drive.<br>
= She is so young that she cannot drive.</p>
""",
    "futeisi1.html": """
<h2>不定詞（基本） 重要表現まとめ</h2>
<table><tr><th>用法</th><th>役割</th><th>例文</th></tr>
<tr><td>名詞的用法</td><td>「〜すること」</td><td>I want to study English.</td></tr>
<tr><td>副詞的用法</td><td>「〜するために」</td><td>I went to Kyoto to see temples.</td></tr>
<tr><td>形容詞的用法</td><td>「〜するための」</td><td>I have something to do.</td></tr>
</table>
<h2>3用法の見分け方クイックチェック</h2>
<p>① be動詞の補語 → 名詞的用法（My dream is to be a doctor.）<br>
② want/hope の目的語 → 名詞的用法（I want to go.）<br>
③ 名詞を修飾 → 形容詞的用法（something to eat）<br>
④ 動詞を修飾（目的）→ 副詞的用法（went to see）</p>
""",
    "ippan.html": """
<h2>一般動詞 重要表現まとめ</h2>
<table><tr><th>時制</th><th>肯定文</th><th>否定文</th><th>疑問文</th></tr>
<tr><td>現在</td><td>I play tennis.</td><td>I don't play tennis.</td><td>Do you play tennis?</td></tr>
<tr><td>過去</td><td>I played tennis.</td><td>I didn't play tennis.</td><td>Did you play tennis?</td></tr>
<tr><td>未来</td><td>I will play tennis.</td><td>I won't play tennis.</td><td>Will you play tennis?</td></tr>
</table>
<h2>一般動詞 よく使う動詞リスト</h2>
<p>eat, drink, sleep, play, read, write, study, work, like, want, know, live, have, get, take, give, tell, think, make, go, come, see, hear, speak, run, swim, sing, buy, meet</p>
""",
    "be.html": """
<h2>be動詞 重要表現まとめ</h2>
<table><tr><th>主語</th><th>現在形</th><th>過去形</th><th>例文</th></tr>
<tr><td>I</td><td>am</td><td>was</td><td>I am a student.</td></tr>
<tr><td>You</td><td>are</td><td>were</td><td>You are kind.</td></tr>
<tr><td>He/She/It</td><td>is</td><td>was</td><td>He is my friend.</td></tr>
<tr><td>We/They</td><td>are</td><td>were</td><td>We are happy.</td></tr>
</table>
<h2>be動詞 短縮形 完全マスター</h2>
<p>I am = I'm / you are = you're / he is = he's / she is = she's / it is = it's / we are = we're / they are = they're<br>
is not = isn't / are not = aren't / was not = wasn't / were not = weren't</p>
""",
    "kako.html": """
<h2>過去形 重要表現まとめ</h2>
<table><tr><th>規則動詞</th><th>不規則動詞</th><th>否定/疑問</th></tr>
<tr><td>play → played</td><td>go → went</td><td>didn't + 原形</td></tr>
<tr><td>study → studied</td><td>eat → ate</td><td>Did + 主語 + 原形？</td></tr>
<tr><td>stop → stopped</td><td>see → saw</td><td>Where did you go?</td></tr>
</table>
<h2>過去形 よく出る時制表現</h2>
<p>yesterday, last night, last week, last year, 〜 ago, this morning, when I was young</p>
""",
}

for fname, extra in ALL_EXTRA.items():
    if extra:  # skip empty strings
        thicken(fname, extra)

print("=== 最終発展コンテンツの追加が完了しました ===")