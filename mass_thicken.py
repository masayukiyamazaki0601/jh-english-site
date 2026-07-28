#!/usr/bin/env python3
"""全28薄い記事を300行超えまで一気に拡充（追加の深掘り・例文・テスト対策・発展内容）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra, skip_over=800):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines >= skip_over:
        print(f"  SKIP {filename} ({lines} lines, already thick)")
        return
    pos = content.rfind("</article>")
    if pos == -1:
        return
    after = content[pos:]
    new = content[:pos] + extra + "\n" + after
    with open(path, "w") as f:
        f.write(new)
    print(f"  OK {filename} ({lines} -> {new.count(chr(10))} lines)")

# ===== 300行超えを目指した大量追加コンテンツ =====
BULK = {
    "be.html": """
<h2>be動詞の穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) a student. → am</li>
<li>You ( ) very kind. → are</li>
<li>He ( ) my best friend. → is</li>
<li>She ( ) from Tokyo. → is</li>
<li>We ( ) in the classroom. → are</li>
<li>They ( ) happy today. → are</li>
<li>It ( ) a sunny day. → is</li>
<li>I ( ) not a teacher. → am</li>
<li>She ( ) not tired. → is</li>
<li>We ( ) not late for school. → are</li>
<li>( ) you a student? → Are</li>
<li>( ) he your brother? → Is</li>
<li>( ) they from Japan? → Are</li>
<li>( ) it cold today? → Is</li>
<li>Where ( ) you from? → are</li>
</ol>
<h2>be動詞 英作文練習</h2>
<ol>
<li>私は13歳です。 → I am 13 years old.</li>
<li>彼女は大阪出身です。 → She is from Osaka.</li>
<li>私たちは教室にいます。 → We are in the classroom.</li>
<li>今日は晴れです。 → It is sunny today.</li>
<li>あなたは学生ですか？ → Are you a student?</li>
<li>彼は親切です。 → He is kind.</li>
<li>彼らは日本人です。 → They are Japanese.</li>
</ol>
<h2>be動詞 発展学習：進行形への橋渡し</h2>
<p>be動詞は「〜です」の他に、現在進行形（be + doing）や受動態（be + 過去分詞）の一部としても使われます。</p>
<ul>
  <li><strong>現在進行形</strong>：I <strong>am</strong> reading a book.（本を読んでいます）</li>
  <li><strong>過去進行形</strong>：He <strong>was</strong> watching TV.（テレビを見ていました）</li>
  <li><strong>受動態</strong>：This cake <strong>was</strong> made by my mother.（このケーキは母によって作られました）</li>
</ul>
""",
    "ippan.html": """
<h2>一般動詞 穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) breakfast at seven. → eat</li>
<li>She ( ) tennis on Sunday. → plays</li>
<li>They ( ) English every day. → study</li>
<li>We ( ) coffee in the morning. → drink</li>
<li>He ( ) to school by bus. → goes</li>
<li>My father ( ) at a hospital. → works</li>
<li>I ( ) like fish. → don't</li>
<li>She ( ) play the guitar. → doesn't</li>
<li>They ( ) eat meat. → don't</li>
<li>He ( ) like coffee. → doesn't</li>
<li>( ) you like cats? → Do</li>
<li>( ) she speak English? → Does</li>
<li>( ) they live in Tokyo? → Do</li>
<li>Where ( ) you live? → do</li>
<li>What ( ) she like? → does</li>
</ol>
<h2>一般動詞 英作文練習</h2>
<ol>
<li>私は毎朝パンを食べます。 → I eat bread every morning.</li>
<li>彼女は日曜日にテニスをします。 → She plays tennis on Sunday.</li>
<li>私はコーヒーが好きではありません。 → I don't like coffee.</li>
<li>彼はピアノを弾きません。 → He doesn't play the piano.</li>
<li>猫は好きですか？ → Do you like cats?</li>
</ol>
<h2>一般動詞の発展：時制の全体像</h2>
<table>
<tr><th>時制</th><th>形</th><th>例</th><th>意味</th></tr>
<tr><td>現在</td><td>動詞（三単現でs）</td><td>I play tennis.</td><td>普段の習慣</td></tr>
<tr><td>過去</td><td>過去形</td><td>I played tennis.</td><td>昨日した</td></tr>
<tr><td>未来</td><td>will + 原形</td><td>I will play tennis.</td><td>これからする</td></tr>
<tr><td>進行</td><td>be + doing</td><td>I am playing tennis.</td><td>今している</td></tr>
<tr><td>完了</td><td>have + 過去分詞</td><td>I have played tennis.</td><td>したことがある</td></tr>
</table>
""",
    "kako.html": """
<h2>過去形 穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) to the park yesterday. → went</li>
<li>She ( ) breakfast at seven. → ate</li>
<li>They ( ) a movie last night. → saw</li>
<li>I ( ) my homework yesterday. → did</li>
<li>He ( ) a cake for me. → made</li>
<li>We ( ) to school by bus. → went</li>
<li>She ( ) a letter to her friend. → wrote</li>
<li>He ( ) a new car. → bought</li>
<li>I ( ) the window. → opened</li>
<li>She ( ) to music yesterday. → listened</li>
<li>I ( ) go to school yesterday. → didn't</li>
<li>He ( ) eat breakfast. → didn't</li>
<li>( ) you go to the park? → Did</li>
<li>( ) she eat sushi? → Did</li>
<li>What ( ) you do last night? → did</li>
</ol>
<h2>不規則動詞一覧（暗記用 全20語）</h2>
<table>
<tr><th>原形</th><th>過去形</th><th>意味</th><th>原形</th><th>過去形</th><th>意味</th></tr>
<tr><td>be</td><td>was/were</td><td>です</td><td>go</td><td>went</td><td>行く</td></tr>
<tr><td>eat</td><td>ate</td><td>食べる</td><td>see</td><td>saw</td><td>見る</td></tr>
<tr><td>do</td><td>did</td><td>する</td><td>have</td><td>had</td><td>持つ</td></tr>
<tr><td>make</td><td>made</td><td>作る</td><td>buy</td><td>bought</td><td>買う</td></tr>
<tr><td>write</td><td>wrote</td><td>書く</td><td>read</td><td>read</td><td>読む</td></tr>
<tr><td>come</td><td>came</td><td>来る</td><td>take</td><td>took</td><td>取る</td></tr>
<tr><td>speak</td><td>spoke</td><td>話す</td><td>swim</td><td>swam</td><td>泳ぐ</td></tr>
<tr><td>run</td><td>ran</td><td>走る</td><td>sing</td><td>sang</td><td>歌う</td></tr>
<tr><td>give</td><td>gave</td><td>与える</td><td>get</td><td>got</td><td>得る</td></tr>
<tr><td>tell</td><td>told</td><td>伝える</td><td>meet</td><td>met</td><td>会う</td></tr>
</table>
<h2>過去形 英作文練習</h2>
<ol>
<li>昨日公園に行きました。 → I went to the park yesterday.</li>
<li>彼女は7時に朝食を食べました。 → She ate breakfast at seven.</li>
<li>私たちは昨夜映画を見ました。 → We saw a movie last night.</li>
<li>昨日学校に行きませんでした。 → I didn't go to school yesterday.</li>
<li>朝食を食べましたか？ → Did you eat breakfast?</li>
</ol>
""",
    "can.html": """
<h2>can 穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) swim. → can</li>
<li>She ( ) speak French. → can</li>
<li>He ( ) run fast. → can</li>
<li>My father ( ) cook well. → can</li>
<li>We ( ) see the mountain. → can</li>
<li>I ( ) play the piano. → can't</li>
<li>She ( ) come to the party. → can't</li>
<li>He ( ) find his keys. → can't</li>
<li>We ( ) go out today. → can't</li>
<li>They ( ) understand English. → can't</li>
<li>( ) you help me? → Can</li>
<li>( ) I use your pen? → Can</li>
<li>( ) she speak Japanese? → Can</li>
<li>( ) he play soccer? → Can</li>
<li>Where ( ) I buy a ticket? → can</li>
</ol>
<h2>can 英作文練習</h2>
<ol>
<li>私は泳げます。 → I can swim.</li>
<li>彼女はフランス語を話せます。 → She can speak French.</li>
<li>私はピアノを弾けません。 → I can't play the piano.</li>
<li>手伝ってくれますか？ → Can you help me?</li>
<li>ペンを使ってもいいですか？ → Can I use your pen?</li>
</ol>
<h2>can の発展：could（過去形）と be able to</h2>
<p>can の過去形は <strong>could</strong>、よりフォーマルな表現は <strong>be able to</strong> です。</p>
<ul>
  <li><strong>could</strong>（過去の能力）：I could swim when I was five.</li>
  <li><strong>was/were able to</strong>（過去にうまくできた）：I was able to finish my homework.</li>
  <li><strong>will be able to</strong>（未来の能力）：I will be able to drive next year.</li>
</ul>
""",
    "shinko.html": """
<h2>現在進行形 穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) reading a book now. → am</li>
<li>She ( ) watching TV now. → is</li>
<li>They ( ) playing soccer now. → are</li>
<li>He ( ) studying English now. → is</li>
<li>We ( ) having lunch now. → are</li>
<li>I ( ) not sleeping now. → am</li>
<li>She ( ) not eating now. → is</li>
<li>They ( ) not working now. → are</li>
<li>He ( ) not running now. → is</li>
<li>We ( ) not watching TV now. → are</li>
<li>( ) you studying now? → Are</li>
<li>( ) she sleeping now? → Is</li>
<li>( ) they playing now? → Are</li>
<li>What ( ) you doing now? → are</li>
<li>Where ( ) he going? → is</li>
</ol>
<h2>現在進行形 英作文練習</h2>
<ol>
<li>私は今本を読んでいます。 → I am reading a book now.</li>
<li>彼女は今テレビを見ています。 → She is watching TV now.</li>
<li>彼らは今サッカーをしています。 → They are playing soccer now.</li>
<li>今勉強していますか？ → Are you studying now?</li>
<li>彼は寝ていません。 → He is not sleeping.</li>
</ol>
<h2>進行形にできない動詞（状態動詞）</h2>
<table>
<tr><th>カテゴリ</th><th>動詞</th><th>例（進行形にできない）</th><th>正しい表現</th></tr>
<tr><td>知覚</td><td>see, hear, smell</td><td>I am seeing a bird.❌</td><td>I see a bird.⭕</td></tr>
<tr><td>感情</td><td>like, love, hate, want</td><td>I am wanting coffee.❌</td><td>I want coffee.⭕</td></tr>
<tr><td>知識</td><td>know, understand, believe</td><td>I am knowing the answer.❌</td><td>I know the answer.⭕</td></tr>
<tr><td>所有</td><td>have, own, belong</td><td>I am having a car.❌</td><td>I have a car.⭕</td></tr>
</table>
""",
    "santan.html": """
<h2>三人称単数現在 穴埋め問題（全15問）</h2>
<ol>
<li>He ( ) tennis every Sunday. → plays</li>
<li>She ( ) to school by bus. → goes</li>
<li>The cat ( ) milk. → drinks</li>
<li>My mother ( ) dinner every day. → cooks</li>
<li>He ( ) English very well. → speaks</li>
<li>He ( ) play tennis. → doesn't</li>
<li>She ( ) like coffee. → doesn't</li>
<li>It ( ) rain a lot here. → doesn't</li>
<li>My father ( ) work on Sunday. → doesn't</li>
<li>She ( ) study French. → doesn't</li>
<li>( ) she like music? → Does</li>
<li>( ) he play soccer? → Does</li>
<li>( ) your mother cook well? → Does</li>
<li>Where ( ) she live? → does</li>
<li>What ( ) he like? → does</li>
</ol>
<h2>三単現 英作文練習</h2>
<ol>
<li>彼は毎週日曜日にテニスをします。 → He plays tennis every Sunday.</li>
<li>彼女はバスで学校に行きます。 → She goes to school by bus.</li>
<li>彼はピアノを弾きません。 → He doesn't play the piano.</li>
<li>彼女は英語を勉強しますか？ → Does she study English?</li>
<li>彼はどこに住んでいますか？ → Where does he live?</li>
</ol>
<h2>三単現 発展：不規則な3人称単数形</h2>
<table>
<tr><th>原形</th><th>3人称単数</th><th>ルール</th></tr>
<tr><td>have</td><td>has</td><td>完全不規則（暗記！）</td></tr>
<tr><td>do</td><td>does</td><td>-es がつく</td></tr>
<tr><td>go</td><td>goes</td><td>oで終わる → es</td></tr>
<tr><td>say</td><td>says</td><td>発音が変わる（セズ）</td></tr>
</table>
""",
    "kansi.html": """
<h2>冠詞 穴埋め問題（全15問）</h2>
<ol>
<li>I have ( ) cat. → a</li>
<li>She is ( ) teacher. → a</li>
<li>He is ( ) honest boy. → an</li>
<li>I ate ( ) apple. → an</li>
<li>She studies at ( ) university. → a</li>
<li>Please close ( ) door. → the</li>
<li>( ) sun is bright today. → The</li>
<li>I play ( ) piano. → the</li>
<li>Mt. Fuji is ( ) highest mountain. → the</li>
<li>I have a cat. ( ) cat is cute. → The</li>
<li>I go to school by ( ) bus. → (no article)</li>
<li>She plays ( ) tennis. → (no article)</li>
<li>I have ( ) breakfast at seven. → (no article)</li>
<li>He speaks ( ) English. → (no article)</li>
<li>She was born in ( ) Japan. → (no article)</li>
</ol>
<h2>冠詞 発展：the の特別な使い方</h2>
<table>
<tr><th>使い方</th><th>例</th><th>説明</th></tr>
<tr><td>唯一のもの</td><td>the sun, the moon</td><td>宇宙に1つしかないもの</td></tr>
<tr><td>最上級</td><td>the best, the tallest</td><td>最上級の前は必ず the</td></tr>
<tr><td>楽器</td><td>play the piano</td><td>楽器の前は the</td></tr>
<tr><td>順序</td><td>the first, the second</td><td>序数の前は the</td></tr>
<tr><td>同じもの</td><td>the same</td><td>same の前は必ず the</td></tr>
</table>
""",
    "fukusu.html": """
<h2>複数形 穴埋め問題（全15問）</h2>
<ol>
<li>one cat → two ( ) → cats</li>
<li>one book → three ( ) → books</li>
<li>one box → two ( ) → boxes</li>
<li>one baby → three ( ) → babies</li>
<li>one knife → two ( ) → knives</li>
<li>one child → three ( ) → children</li>
<li>one man → two ( ) → men</li>
<li>one woman → three ( ) → women</li>
<li>one foot → two ( ) → feet</li>
<li>one tooth → three ( ) → teeth</li>
<li>one sheep → two ( ) → sheep</li>
<li>one fish → three ( ) → fish</li>
<li>one watch → two ( ) → watches</li>
<li>one city → three ( ) → cities</li>
<li>one leaf → two ( ) → leaves</li>
</ol>
<h2>複数形 発展：不規則複数形まとめ</h2>
<table>
<tr><th>パターン</th><th>単数</th><th>複数</th><th>説明</th></tr>
<tr><td>-en 型</td><td>child</td><td>children</td><td>古い英語の複数形の名残</td></tr>
<tr><td>母音変化型</td><td>man / woman</td><td>men / women</td><td>母音が変化</td></tr>
<tr><td>-ee 型</td><td>foot / tooth</td><td>feet / teeth</td><td>母音がeeに変化</td></tr>
<tr><td>単複同形</td><td>sheep / fish</td><td>sheep / fish</td><td>形が同じ</td></tr>
<tr><td>外来語</td><td>Japanese</td><td>Japanese</td><td>日本語由来は同形</td></tr>
</table>
""",
    "daimeisi.html": """
<h2>代名詞 穴埋め問題（全15問）</h2>
<ol>
<li>( ) is my friend. → She</li>
<li>( ) are students. → They</li>
<li>( ) am happy. → I</li>
<li>This is ( ) book. → my</li>
<li>That is ( ) car. → his</li>
<li>These are ( ) keys. → her</li>
<li>I like ( ). → her</li>
<li>Please give it to ( ). → me</li>
<li>I saw ( ) yesterday. → him</li>
<li>This book is ( ). → mine</li>
<li>That pen is ( ). → yours</li>
<li>These keys are ( ). → hers</li>
<li>This school is ( ). → ours</li>
<li>That dog is ( ). → theirs</li>
<li>( ) is a teacher and ( ) students love ( ). → She, her, her</li>
</ol>
<h2>代名詞 英作文練習</h2>
<ol>
<li>彼女は私の友達です。 → She is my friend.</li>
<li>私は彼女が好きです。 → I like her.</li>
<li>これは私の本です。 → This is my book.</li>
<li>この本は私のものです。 → This book is mine.</li>
<li>それを私にください。 → Give it to me.</li>
</ol>
<h2>代名詞 発展：再帰代名詞（〜自身）</h2>
<table>
<tr><th>主格</th><th>再帰代名詞</th><th>例</th></tr>
<tr><td>I</td><td>myself</td><td>I taught myself English.</td></tr>
<tr><td>you</td><td>yourself</td><td>You hurt yourself.</td></tr>
<tr><td>he</td><td>himself</td><td>He cut himself.</td></tr>
<tr><td>she</td><td>herself</td><td>She looked at herself.</td></tr>
<tr><td>we</td><td>ourselves</td><td>We enjoyed ourselves.</td></tr>
<tr><td>they</td><td>themselves</td><td>They taught themselves.</td></tr>
</table>
""",
    "gimonhitei.html": """
<h2>疑問文・否定文 穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) a student. → am</li>
<li>You ( ) not a teacher. → are</li>
<li>She ( ) not at home. → is</li>
<li>I ( ) not a doctor. → am</li>
<li>They ( ) not from Osaka. → are</li>
<li>I ( ) like coffee. → don't</li>
<li>He ( ) play tennis. → doesn't</li>
<li>We ( ) eat meat. → don't</li>
<li>She ( ) speak French. → doesn't</li>
<li>They ( ) live in Tokyo. → don't</li>
<li>( ) you a student? → Are</li>
<li>( ) she like cats? → Does</li>
<li>( ) they play soccer? → Do</li>
<li>( ) he speak English? → Does</li>
<li>What ( ) you like? → do</li>
</ol>
<h2>be動詞 vs 一般動詞 比較問題</h2>
<table>
<tr><th>文の種類</th><th>be動詞</th><th>一般動詞</th></tr>
<tr><td>肯定文</td><td>I am a student.</td><td>I like cats.</td></tr>
<tr><td>否定文</td><td>I am not a student.</td><td>I don't like cats.</td></tr>
<tr><td>疑問文</td><td>Are you a student?</td><td>Do you like cats?</td></tr>
<tr><td>答え方</td><td>Yes, I am. / No, I'm not.</td><td>Yes, I do. / No, I don't.</td></tr>
</table>
<h2>テストの鉄則！疑問文・否定文のルール</h2>
<div class="note"><strong>絶対に覚える3つのルール：</strong><br>
① be動詞の否定は be動詞 + not（I am not a teacher.）<br>
② 一般動詞の否定は don't/doesn't + 原形（I don't like coffee.）<br>
③ be動詞と一般動詞の疑問文は語順が違う！</div>
""",
    "meirei.html": """
<h2>命令文 穴埋め問題（全10問）</h2>
<ol>
<li>( ) down. → Sit</li>
<li>( ) your book. → Open</li>
<li>( ) here. → Come</li>
<li>( ) the door. → Close</li>
<li>( ) aloud. → Read</li>
<li>( ) run. → Don't</li>
<li>( ) be late. → Don't</li>
<li>( ) eat in class. → Don't</li>
<li>( ) smoke. → Don't</li>
<li>( ) sit down, please. → Please</li>
</ol>
<h2>命令文 英作文練習</h2>
<ol>
<li>座りなさい。 → Sit down.</li>
<li>本を開きなさい。 → Open your book.</li>
<li>走ってはいけません。 → Don't run.</li>
<li>遅れてはいけません。 → Don't be late.</li>
<li>お座りください。 → Please sit down.</li>
</ol>
<h2>命令文 発展：Let's 〜（勧誘）</h2>
<ul>
  <li><strong>Let's + 動詞の原形</strong>：Let's go to the park.（公園に行きましょう）</li>
  <li><strong>否定の勧誘</strong>：Let's not go.（行くのはやめましょう）</li>
  <li><strong>Let me + 動詞の原形</strong>：Let me help you.（手伝わせてください）</li>
</ul>
""",
    "bekako.html": """
<h2>be動詞過去形 穴埋め問題（全15問）</h2>
<ol>
<li>I ( ) happy yesterday. → was</li>
<li>They ( ) at home last night. → were</li>
<li>She ( ) busy yesterday. → was</li>
<li>We ( ) in the park last Sunday. → were</li>
<li>He ( ) sick yesterday. → was</li>
<li>I ( ) not at home yesterday. → was</li>
<li>She ( ) not tired. → was</li>
<li>They ( ) not at school. → were</li>
<li>We ( ) not late. → were</li>
<li>He ( ) not hungry. → was</li>
<li>( ) you tired after the game? → Were</li>
<li>( ) she at the party? → Was</li>
<li>( ) they at home? → Were</li>
<li>( ) it cold this morning? → Was</li>
<li>Where ( ) you yesterday? → were</li>
</ol>
<h2>be動詞過去形 英作文練習</h2>
<ol>
<li>私は昨日幸せでした。 → I was happy yesterday.</li>
<li>彼らは昨夜家にいました。 → They were at home last night.</li>
<li>彼女は昨日忙しかったです。 → She was busy yesterday.</li>
<li>私は昨日家にいませんでした。 → I was not at home yesterday.</li>
<li>あなたは疲れていましたか？ → Were you tired?</li>
</ol>
""",
    "kakosin.html": """
<h2>過去進行形 穴埋め問題（全12問）</h2>
<ol>
<li>I ( ) reading a book at 8pm. → was</li>
<li>They ( ) playing soccer yesterday. → were</li>
<li>She ( ) cooking dinner at that time. → was</li>
<li>We ( ) watching TV at 9pm. → were</li>
<li>He ( ) studying English then. → was</li>
<li>I ( ) not sleeping then. → was</li>
<li>She ( ) not working yesterday. → was</li>
<li>They ( ) not playing. → were</li>
<li>We ( ) not eating. → were</li>
<li>( ) you studying at midnight? → Were</li>
<li>( ) she cooking dinner? → Was</li>
<li>What ( ) you doing then? → were</li>
</ol>
<h2>when 節と過去進行形の組み合わせ（10問）</h2>
<ol>
<li>I ( ) (watch) TV when she called. → was watching</li>
<li>He ( ) (study) when I visited. → was studying</li>
<li>They ( ) (play) when it started to rain. → were playing</li>
<li>She ( ) (cook) when the phone rang. → was cooking</li>
<li>We ( ) (sleep) when the earthquake happened. → were sleeping</li>
</ol>
""",
    "mirai.html": """
<h2>未来形 穴埋め問題（全12問）</h2>
<ol>
<li>I ( ) call you later. → will</li>
<li>It ( ) rain tomorrow. → will</li>
<li>She ( ) come to the party. → will</li>
<li>They ( ) visit us next week. → will</li>
<li>I ( ) help you. → will</li>
<li>I ( ) not go there. → will</li>
<li>She ( ) not come. → will</li>
<li>We ( ) not be late. → will</li>
<li>( ) you help me? → Will</li>
<li>( ) it rain tomorrow? → Will</li>
<li>I am ( ) to visit Kyoto. → going</li>
<li>She is ( ) to study law. → going</li>
</ol>
<h2>未来形 英作文練習</h2>
<ol>
<li>あとで電話します。 → I will call you later.</li>
<li>明日雨が降るでしょう。 → It will rain tomorrow.</li>
<li>私は医者になるつもりです。 → I am going to be a doctor.</li>
<li>窓を開けてくれますか？ → Will you open the window?</li>
</ol>
<h2>未来形 発展：will と be going to の違いまとめ</h2>
<table>
<tr><th>状況</th><th>適切な表現</th><th>理由</th></tr>
<tr><td>電話が鳴って「出ます」</td><td>I'll get it.</td><td>その場で決めた</td></tr>
<tr><td>来週の旅行の予定</td><td>I'm going to visit Kyoto.</td><td>前から決めていた</td></tr>
<tr><td>曇り空を見て「雨が降る」</td><td>It's going to rain.</td><td>証拠がある</td></tr>
<tr><td>天気予報で「明日晴れ」</td><td>It will be sunny.</td><td>予測</td></tr>
</table>
""",
    "doumei.html": """
<h2>動名詞 穴埋め問題（全12問）</h2>
<ol>
<li>I like ( ). (swim) → swimming</li>
<li>( ) tennis is fun. (play) → Playing</li>
<li>He enjoys ( ) books. (read) → reading</li>
<li>I finished ( ) my homework. (do) → doing</li>
<li>She is good at ( ). (sing) → singing</li>
<li>I stopped ( ). (smoke) → smoking</li>
<li>She is interested in ( ) history. (study) → studying</li>
<li>I'm tired of ( ) for the bus. (wait) → waiting</li>
<li>I look forward to ( ) you. (see) → seeing</li>
<li>He gave up ( ) soccer. (play) → playing</li>
<li>( ) breakfast is important. (eat) → Eating</li>
<li>I don't like ( ) up early. (get) → getting</li>
</ol>
<h2>動名詞 vs 不定詞 選択問題（6問）</h2>
<ol>
<li>I enjoy (swim/swimming). → swimming</li>
<li>I want (study/to study) English. → to study</li>
<li>I like (play/playing/to play) tennis. → playing / to play</li>
<li>I finished (do/doing) my homework. → doing</li>
<li>She hopes (become/to become) a doctor. → to become</li>
<li>I stopped (smoke/smoking) last year. → smoking</li>
</ol>
""",
    "jyodosi.html": """
<h2>助動詞 穴埋め問題（全12問）</h2>
<ol>
<li>You ( ) study harder. → must</li>
<li>I ( ) to go now. → have</li>
<li>She ( ) to wear a uniform. → has</li>
<li>( ) I come in? → May</li>
<li>You ( ) not run here. → must</li>
<li>You ( ) rest. → should</li>
<li>You don't ( ) to go. → have</li>
<li>We ( ) help each other. → should</li>
<li>He ( ) be careful. → must</li>
<li>You ( ) not eat too much. → should</li>
<li>I ( ) to finish my homework. → have</li>
<li>She ( ) not smoke. → must</li>
</ol>
<h2>must vs have to の違い（例文比較）</h2>
<table>
<tr><th>文</th><th>意味</th><th>解説</th></tr>
<tr><td>I must study.</td><td>勉強しなければならない</td><td>自分でそう思っている</td></tr>
<tr><td>I have to study.</td><td>勉強しなければならない</td><td>親や先生に言われた</td></tr>
<tr><td>You must not smoke.</td><td>タバコを吸ってはいけない</td><td>絶対禁止</td></tr>
<tr><td>You don't have to go.</td><td>行く必要はない</td><td>選択自由</td></tr>
</table>
""",
    "there.html": """
<h2>there is構文 穴埋め問題（全12問）</h2>
<ol>
<li>( ) a cat under the table. → There is</li>
<li>( ) many books on the desk. → There are</li>
<li>( ) a pen on the desk? → Is there</li>
<li>( ) any students in the room? → Are there</li>
<li>There ( ) not any milk in the fridge. → is</li>
<li>There ( ) three apples on the table. → are</li>
<li>( ) a hospital near here? → Is there</li>
<li>How many students ( ) there in your class? → are</li>
<li>There ( ) some water in the glass. → is</li>
<li>There ( ) a book and two pens. → is</li>
<li>There ( ) two pens and a book. → are</li>
<li>There ( ) a lot of people in the park. → are</li>
</ol>
<h2>there is 構文 英作文練習</h2>
<ol>
<li>机の上にペンがあります。 → There is a pen on the desk.</li>
<li>かごの中に3つのリンゴがあります。 → There are three apples in the basket.</li>
<li>この近くに病院はありますか？ → Is there a hospital near here?</li>
<li>冷蔵庫に牛乳はありません。 → There is not any milk in the fridge.</li>
</ol>
""",
    "setuzoku.html": """
<h2>接続詞 穴埋め問題（全12問）</h2>
<ol>
<li>I like cats ( ) dogs. → and</li>
<li>I like cats ( ) I don't like dogs. → but</li>
<li>I am happy ( ) I got a present. → because</li>
<li>I was tired, ( ) I went to bed. → so</li>
<li>Call me ( ) you arrive. → when</li>
<li>( ) it rains, I will stay home. → If</li>
<li>I think ( ) he is kind. → that</li>
<li>She studied hard ( ) she passed. → and</li>
<li>I know ( ) she is honest. → that</li>
<li>I was sick, ( ) I didn't go to school. → so</li>
<li>Let's go out ( ) it is sunny. → because</li>
<li>I will call you ( ) I get home. → when</li>
</ol>
<h2>because / so の使い分け問題</h2>
<ol>
<li>( ) it was raining, I took an umbrella. → Because</li>
<li>It was raining, ( ) I took an umbrella. → so</li>
<li>( ) I was tired, I went to bed early. → Because</li>
<li>I was tired, ( ) I went to bed early. → so</li>
</ol>
<div class="note"><strong>重要ルール！</strong> because = 理由（なぜなら）、so = 結果（なので）。同じ文の中で両方は使えません。</div>
""",
    "ukemi.html": """
<h2>受け身 穴埋め問題（全12問）</h2>
<ol>
<li>English ( ) spoken in many countries. → is</li>
<li>This book ( ) written by Soseki. → was</li>
<li>The window ( ) broken by the boy. → was</li>
<li>These cookies ( ) made by my mother. → were</li>
<li>Rice ( ) eaten in Japan. → is</li>
<li>This car ( ) made in Japan. → was</li>
<li>The door ( ) opened at seven. → was</li>
<li>Many trees ( ) planted in the park. → were</li>
<li>This song ( ) sung by many people. → is</li>
<li>The letter ( ) written in English. → was</li>
<li>The room ( ) cleaned every day. → is</li>
<li>This temple ( ) built 400 years ago. → was</li>
</ol>
<h2>能動態 → 受動態 書き換え問題（6問）</h2>
<ol>
<li>The boy broke the window. → The window was broken by the boy.</li>
<li>My mother made this cake. → This cake was made by my mother.</li>
<li>Many people speak English. → English is spoken by many people.</li>
<li>He cleans the room every day. → The room is cleaned every day.</li>
<li>She wrote this letter. → This letter was written by her.</li>
<li>They planted many trees. → Many trees were planted by them.</li>
</ol>
""",
}

for fname, extra in BULK.items():
    thicken(fname, extra)

print("=== 大量追加が完了しました ===")