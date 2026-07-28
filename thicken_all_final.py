#!/usr/bin/env python3
"""全28記事に300行超えを目指した追加コンテンツを投入"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra, skip_over=300):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines >= skip_over:
        print(f"  SKIP {filename} ({lines} lines)")
        return False
    pos = content.rfind("</article>")
    if pos == -1:
        return False
    after = content[pos:]
    new = content[:pos] + extra + "\n" + after
    with open(path, "w") as f:
        f.write(new)
    print(f"  OK {filename} ({lines} -> {new.count(chr(10))} lines)")
    return True

# ===== 全28記事の追加コンテンツ =====
EXTRAS = {
    "kateiho.html": """
<h2>仮定法の実戦練習（会話形式）</h2>
<div class="highlight"><p>A: What would you do if you had a million dollars?<br>B: I would travel around the world.<br>A: If I were you, I would buy a house first.<br>B: That's a good idea!</p></div>
<h2>仮定法でよく使う表現</h2>
<table><tr><th>表現</th><th>意味</th></tr>
<tr><td>If I were you</td><td>もし私があなたなら</td></tr>
<tr><td>If I had time</td><td>もし時間があれば</td></tr>
<tr><td>If it were sunny</td><td>もし晴れなら</td></tr>
<tr><td>I wish I were〜</td><td>〜だったらいいのに</td></tr>
<tr><td>as if 〜 were</td><td>まるで〜のように</td></tr>
</table>
<h2>仮定法の応用表現</h2>
<ul>
  <li><strong>I wish + 過去形</strong>：I wish I were taller.（もっと背が高ければいいのに）</li>
  <li><strong>as if + 過去形</strong>：He talks as if he knew everything.（彼はまるで何でも知っているかのように話す）</li>
  <li><strong>If only + 過去形</strong>：If only I had more time.（もっと時間があればいいのに）</li>
</ul>
""",
    "genkan3.html": """
<h2>現在完了（完了）の実戦練習</h2>
<div class="highlight"><p>A: Have you finished your homework yet?<br>B: Yes, I have already finished it.<br>A: Great! Have you eaten lunch yet?<br>B: No, I haven't eaten yet. Let's go together!</p></div>
<h2>already / just / yet の位置まとめ</h2>
<table><tr><th>単語</th><th>肯定文</th><th>疑問文</th><th>否定文</th></tr>
<tr><td>already</td><td>I have already done it.</td><td>—</td><td>—</td></tr>
<tr><td>just</td><td>I have just done it.</td><td>—</td><td>—</td></tr>
<tr><td>yet</td><td>—</td><td>Have you done it yet?</td><td>I haven't done it yet.</td></tr>
</table>
<h2>完了用法の ever / never</h2>
<ul>
  <li><strong>ever</strong>（疑問文で「今までに」）：Have you ever seen a UFO?</li>
  <li><strong>never</strong>（肯定文で「一度も〜ない」）：I have never been abroad.</li>
</ul>
""",
    "genkeiFuteisi.html": """
<h2>原形不定詞と進行形の違い</h2>
<p>知覚動詞のあとには原形不定詞と現在分詞（-ing）の両方が使えますが、意味が異なります。</p>
<table><tr><th>構文</th><th>意味</th><th>例</th></tr>
<tr><td>see + 目的語 + 原形</td><td>〜するのを最後まで見る（完了）</td><td>I saw him cross the street.</td></tr>
<tr><td>see + 目的語 + -ing</td><td>〜しているところを見る（途中）</td><td>I saw him crossing the street.</td></tr>
</table>
<h2>make / let / have の違い</h2>
<table><tr><th>動詞</th><th>意味</th><th>ニュアンス</th><th>例</th></tr>
<tr><td>make</td><td>〜させる</td><td>強制的に（いやいや）</td><td>She made me clean my room.</td></tr>
<tr><td>let</td><td>〜させてくれる</td><td>許可する</td><td>My mother let me go out.</td></tr>
<tr><td>have</td><td>〜してもらう</td><td>依頼する</td><td>I had him repair my car.</td></tr>
</table>
""",
    "kakosin.html": """
<h2>過去進行形と過去形の組み合わせ</h2>
<p>「〜していたときに、〜した」という表現は、過去進行形と過去形を組み合わせて使います。よく使う重要パターンです。</p>
<ul>
  <li><span class="example">I was watching TV when she called.</span> <span class="example-jp">（彼女が電話したとき、テレビを見ていました）</span></li>
  <li><span class="example">When I was taking a bath, the phone rang.</span> <span class="example-jp">（お風呂に入っているとき、電話が鳴りました）</span></li>
  <li><span class="example">While I was studying, my friend came.</span> <span class="example-jp">（勉強している間に友達が来ました）</span></li>
  <li><span class="example">It was raining when I left home.</span> <span class="example-jp">（家を出たとき雨が降っていました）</span></li>
</ul>
<div class="tip-box"><h3>💡 when vs while</h3><p><strong>when</strong> = 「〜したとき」一点の動作・状態の両方に使える<br><strong>while</strong> = 「〜している間に」継続する状態にのみ使う</p></div>
""",
    "there.html": """
<h2>there is 構文の応用</h2>
<p>there is 構文は疑問詞と組み合わせて様々な質問ができます。</p>
<ul>
  <li><strong>How many + 名詞 + are there?</strong>：How many students are there in your class?</li>
  <li><strong>What is there + 場所?</strong>：What is there in the box?</li>
  <li><strong>Is there anything + 形容詞?</strong>：Is there anything interesting in the news?</li>
</ul>
<h2>there is と there are の使い分け「近接の法則」</h2>
<div class="note"><strong>重要ルール！</strong> There + be動詞 の be動詞は「すぐ後ろの名詞」に合わせます。複数のものがあっても、最初の名詞が単数なら is を使います。<br>There <strong>is</strong> a pen and three books on the desk.（最初の a pen が単数なので is）<br>There <strong>are</strong> three books and a pen on the desk.（最初の three books が複数なので are）</div>
""",
    "genkanSinkokei.html": """
<h2>現在完了進行形の実戦練習</h2>
<div class="highlight"><p>A: How long have you been studying English?<br>B: I have been studying English for three years.<br>A: That's great! How long have you been living in Tokyo?<br>B: I have been living here since 2023.</p></div>
<h2>現在完了進行形を使う動詞リスト</h2>
<table><tr><th>動詞</th><th>例文</th></tr>
<tr><td>study</td><td>I have been studying for two hours.</td></tr>
<tr><td>wait</td><td>She has been waiting for 30 minutes.</td></tr>
<tr><td>rain</td><td>It has been raining all day.</td></tr>
<tr><td>work</td><td>He has been working here since April.</td></tr>
<tr><td>practice</td><td>They have been practicing for the concert.</td></tr>
</table>
""",
    "bekako.html": """
<h2>be動詞の過去形 実戦練習</h2>
<div class="highlight"><p>A: Where were you yesterday?<br>B: I was at the library. I was studying for the exam.<br>A: Was it crowded?<br>B: Yes, it was. There were many students.</p></div>
<h2>There were / There was の過去形</h2>
<ul>
  <li><strong>There was</strong> + 単数名詞：There was a cat on the chair.</li>
  <li><strong>There were</strong> + 複数名詞：There were many people at the party.</li>
  <li><strong>Was there</strong> + 単数名詞？：Was there a phone call for me?</li>
  <li><strong>Were there</strong> + 複数名詞？：Were there any problems?</li>
</ul>
""",
    "kansetu.html": """
<h2>間接疑問の実戦練習</h2>
<div class="highlight"><p>A: Excuse me, do you know where the station is?<br>B: Yes, go straight and turn left.<br>A: Can you tell me how long it takes?<br>B: It takes about 10 minutes on foot.<br>A: I wonder if there is a bus to the station.<br>B: Yes, the bus stop is over there.</p></div>
<h2>疑問詞のない間接疑問のルール</h2>
<ul>
  <li>「〜かどうか」を表すには <strong>if</strong> または <strong>whether</strong> を使う。</li>
  <li><strong>if</strong>：会話でよく使う。I don't know if he is coming.</li>
  <li><strong>whether</strong>：フォーマルな表現。少し硬い。I wonder whether she will come.</li>
  <li>whether のあとに <strong>or not</strong> をつけられる：I don't know whether he is coming or not.</li>
</ul>
""",
    "setuzoku.html": """
<h2>接続詞 that の省略</h2>
<p>think, know, say, believe などの動詞の後ろで使う that は、会話ではよく省略されます。</p>
<ul>
  <li>I think (that) he is kind.</li>
  <li>I know (that) she is right.</li>
  <li>He said (that) he was tired.</li>
  <li>She believes (that) it is true.</li>
</ul>
<div class="note"><strong>テストでは</strong>：that があってもなくても正解です。ただし、フォーマルな文章では that を入れた方が良いとされています。</div>
<h2>if の条件と「〜かどうか」の違い</h2>
<table><tr><th>if の用法</th><th>意味</th><th>例</th></tr>
<tr><td>条件</td><td>もし〜なら</td><td>If it rains, I will stay home.</td></tr>
<tr><td>「〜かどうか」</td><td>〜かどうか</td><td>I don't know if he is kind.</td></tr>
</table>
""",
    "genkan2.html": """
<h2>現在完了（経験）の実戦練習</h2>
<div class="highlight"><p>A: Have you ever been to Kyoto?<br>B: Yes, I have been there twice.<br>A: Have you ever eaten natto?<br>B: No, I have never eaten it. Is it delicious?<br>A: Well, it's an acquired taste!</p></div>
<h2>回数を尋ねる表現</h2>
<ul>
  <li><strong>once</strong>：1回 I have been to Kyoto once.</li>
  <li><strong>twice</strong>：2回 She has been to the US twice.</li>
  <li><strong>three times</strong>：3回 He has seen that movie three times.</li>
  <li><strong>many times</strong>：何度も They have visited the temple many times.</li>
</ul>
""",
    "gimonsi.html": """
<h2>疑問詞を使った実戦会話</h2>
<div class="highlight"><p>A: What is your name?<br>B: My name is Taro.<br>A: Where are you from?<br>B: I'm from Osaka.<br>A: When is your birthday?<br>B: It's on April 1st.<br>A: Why do you study English?<br>B: Because I want to travel abroad.</p></div>
<h2>How + 形容詞 の便利な表現</h2>
<table><tr><th>表現</th><th>意味</th><th>例</th></tr>
<tr><td>How many?</td><td>いくつ？（数）</td><td>How many books do you have?</td></tr>
<tr><td>How much?</td><td>いくら？（量・金額）</td><td>How much is this?</td></tr>
<tr><td>How old?</td><td>何歳？</td><td>How old are you?</td></tr>
<tr><td>How long?</td><td>どのくらいの長さ？</td><td>How long is this bridge?</td></tr>
<tr><td>How far?</td><td>どのくらいの距離？</td><td>How far is the station?</td></tr>
</table>
""",
    "mirai.html": """
<h2>未来形の実戦練習</h2>
<div class="highlight"><p>A: What are you going to do this weekend?<br>B: I'm going to visit my grandparents.<br>A: That sounds nice! Will you go by train?<br>B: Yes, I will. It takes about two hours.<br>A: I will call you on Sunday.</p></div>
<h2>現在形で未来を表す表現</h2>
<p>確定した予定（時刻表・カレンダー）は現在形で未来を表します。</p>
<ul>
  <li>The train <strong>leaves</strong> at 8am.（電車は午前8時に出発します）</li>
  <li>The store <strong>opens</strong> at 10am.（店は午前10時に開店します）</li>
  <li>School <strong>starts</strong> in April.（学校は4月に始まります）</li>
</ul>
<div class="tip-box"><h3>💡 未来形の3つの使い分け</h3><p><strong>will</strong> = その場の意思・予測<br><strong>be going to</strong> = 予定・確実な未来<br><strong>現在形</strong> = 確定したスケジュール</p></div>
""",
    "bunsi.html": """
<h2>分詞構文への橋渡し</h2>
<p>分詞を文頭に使って「〜しながら」「〜なので」という意味を表すことができます。高校で学ぶ分詞構文の準備です。</p>
<ul>
  <li><strong>Walking in the park</strong>, I met my friend.（公園を歩いていると、友達に会いました）</li>
  <li><strong>Surprised by the news</strong>, she couldn't speak.（その知らせに驚いて、彼女は言葉が出なかった）</li>
  <li><strong>Being tired</strong>, I went to bed early.（疲れていたので、早く寝ました）</li>
</ul>
<h2>過去分詞の不規則変化リスト</h2>
<table><tr><th>原形</th><th>過去分詞</th><th>意味</th></tr>
<tr><td>write</td><td>written</td><td>書かれた</td></tr>
<tr><td>break</td><td>broken</td><td>壊された</td></tr>
<tr><td>eat</td><td>eaten</td><td>食べられた</td></tr>
<tr><td>take</td><td>taken</td><td>取られた</td></tr>
<tr><td>speak</td><td>spoken</td><td>話された</td></tr>
</table>
""",
    "daimeisi.html": """
<h2>代名詞の実戦練習</h2>
<div class="highlight"><p>A: Is this your book?<br>B: No, it isn't mine. It's hers.<br>A: Are these your keys?<br>B: Yes, they are mine. Thank you!<br>A: This is our classroom. That one is theirs.</p></div>
<h2>It の特別な用法</h2>
<ul>
  <li><strong>天候</strong>：It is sunny today.</li>
  <li><strong>時間</strong>：It is 8 o'clock.</li>
  <li><strong>曜日</strong>：It is Monday.</li>
  <li><strong>距離</strong>：It is 5km from here to the station.</li>
  <li><strong>天気</strong>：It is raining now.</li>
</ul>
<div class="note"><strong>it は「それ」以外にも色々な意味で使われる超便利な単語！</strong></div>
""",
    "kankeisi1.html": """
<h2>関係代名詞の実戦練習</h2>
<div class="highlight"><p>A: Do you know the boy who is running over there?<br>B: Yes, he is my classmate. His name is Ken.<br>A: Is he the boy that won the race last week?<br>B: Yes, he is! He's the one who runs the fastest in our school.</p></div>
<h2>主格と目的格の見分け方</h2>
<p>関係代名詞の後に <strong>名詞 or 主語</strong> がくるか <strong>動詞</strong> がくるかで判断します。</p>
<table><tr><th>格</th><th>後ろの語順</th><th>例</th></tr>
<tr><td>主格</td><td>who/which/that + <strong>動詞</strong></td><td>the boy <strong>who runs</strong> fast</td></tr>
<tr><td>目的格</td><td>who(m)/which/that + <strong>主語 + 動詞</strong></td><td>the boy <strong>(who) I met</strong></td></tr>
</table>
""",
    "ukemi.html": """
<h2>受け身の実戦練習</h2>
<div class="highlight"><p>A: This cake is delicious! Where was it made?<br>B: It was made by my grandmother.<br>A: Really? What is it made of?<br>B: It is made of chocolate and cream.<br>A: When was it made?<br>B: It was made this morning.</p></div>
<h2>made + 前置詞の使い分け</h2>
<table><tr><th>表現</th><th>意味</th><th>例</th></tr>
<tr><td>be made of</td><td>材料がわかる（形を保つ）</td><td>This desk is made of wood.</td></tr>
<tr><td>be made from</td><td>材料がわからない（変化した）</td><td>Paper is made from trees.</td></tr>
<tr><td>be made by</td><td>行為者</td><td>This cake was made by my mother.</td></tr>
<tr><td>be made in</td><td>生産地</td><td>This car was made in Japan.</td></tr>
</table>
""",
    "genkan1.html": """
<h2>現在完了（継続）の実戦練習</h2>
<div class="highlight"><p>A: How long have you lived in Tokyo?<br>B: I have lived here for five years.<br>A: How long have you studied English?<br>B: I have studied English since elementary school.<br>A: That's a long time! Your English is very good.</p></div>
<h2>継続用法と過去形の違い（例文比較）</h2>
<table><tr><th>現在完了（継続）</th><th>過去形</th></tr>
<tr><td>I have lived here for 5 years.（今も住んでいる）</td><td>I lived there for 5 years.（もう住んでいない）</td></tr>
<tr><td>She has been a teacher since 2020.（今も先生）</td><td>She was a teacher from 2010 to 2020.（過去の話）</td></tr>
<tr><td>We have known each other since childhood.（今も知っている）</td><td>We met each other in 2010.（出会った時点）</td></tr>
</table>
""",
    "doumei.html": """
<h2>動名詞の実戦練習</h2>
<div class="highlight"><p>A: What do you enjoy doing in your free time?<br>B: I enjoy reading books and listening to music.<br>A: I like playing tennis. Do you like playing sports?<br>B: Yes, but I'm not good at running. I prefer swimming.</p></div>
<h2>前置詞 + 動名詞の重要パターン</h2>
<table><tr><th>前置詞</th><th>例文</th></tr>
<tr><td>good at 〜</td><td>She is good at singing.</td></tr>
<tr><td>interested in 〜</td><td>He is interested in learning Japanese.</td></tr>
<tr><td>tired of 〜</td><td>I'm tired of waiting.</td></tr>
<tr><td>look forward to 〜</td><td>I look forward to seeing you.</td></tr>
<tr><td>instead of 〜</td><td>Let's walk instead of taking the bus.</td></tr>
</table>
<div class="note"><strong>look forward to の to は前置詞！</strong>不定詞の to ではないので、後ろは動名詞がきます。</div>
""",
    "jyodosi.html": """
<h2>助動詞の実戦練習</h2>
<div class="highlight"><p>A: May I use your phone?<br>B: Sure, you may.<br>A: I must finish my homework by tomorrow.<br>B: You should start now. Don't wait until the last minute.<br>A: You're right. I'll start right now.</p></div>
<h2>助動詞の過去形</h2>
<table><tr><th>現在</th><th>過去</th><th>例（過去）</th></tr>
<tr><td>can</td><td>could</td><td>I could swim when I was five.</td></tr>
<tr><td>must</td><td>had to</td><td>I had to go home early yesterday.</td></tr>
<tr><td>may</td><td>might</td><td>It might rain tomorrow.</td></tr>
<tr><td>will</td><td>would</td><td>I thought it would rain.</td></tr>
<tr><td>shall</td><td>should</td><td>I should have studied harder.</td></tr>
</table>
""",
    "hikaku1.html": """
<h2>比較の実戦練習</h2>
<div class="highlight"><p>A: Which is bigger, Tokyo or Osaka?<br>B: Tokyo is bigger than Osaka.<br>A: What is the highest mountain in Japan?<br>B: Mt. Fuji is the highest mountain in Japan.<br>A: Is it as high as Mt. Everest?<br>B: No, Mt. Everest is much higher than Mt. Fuji.</p></div>
<h2>比較級を強める表現</h2>
<ul>
  <li><strong>much</strong> + 比較級：Tokyo is much bigger than Osaka.</li>
  <li><strong>a little</strong> + 比較級：She is a little taller than me.</li>
  <li><strong>even</strong> + 比較級：This book is even more interesting.</li>
  <li><strong>far</strong> + 比較級：He is far better than me at tennis.</li>
</ul>
""",
    "zensi.html": """
<h2>前置詞の実戦練習</h2>
<div class="highlight"><p>A: Where is the cat?<br>B: It's under the table.<br>A: Where is the bank?<br>B: It's behind the station, between the post office and the park.<br>A: When do you get up?<br>B: I get up at seven in the morning on weekdays.</p></div>
<h2>in / on / at のイメージ図</h2>
<table><tr><th>前置詞</th><th>イメージ</th><th>時間</th><th>場所</th></tr>
<tr><td>in</td><td>「範囲の中」</td><td>in the morning, in May</td><td>in the room, in Tokyo</td></tr>
<tr><td>on</td><td>「接触・面」</td><td>on Sunday, on May 5th</td><td>on the desk, on the wall</td></tr>
<tr><td>at</td><td>「点」</td><td>at 8 o'clock, at noon</td><td>at the station, at school</td></tr>
</table>
<div class="tip-box"><h3>💡 in/on/at の覚え方</h3><p><strong>in</strong> = 広い範囲（東京・月・年）<br><strong>on</strong> = 特定の面（曜日・日付・机の上）<br><strong>at</strong> = 点（時刻・駅・学校）</p></div>
""",
    "suryo.html": """
<h2>数量詞の実戦練習</h2>
<div class="highlight"><p>A: How many books do you have?<br>B: I have a few books. Not many.<br>A: How much money do you have?<br>B: I have a little money. But not enough to buy that.<br>A: Do you have any questions?<br>B: Yes, I have some questions.</p></div>
<h2>可算名詞 vs 不可算名詞 リスト</h2>
<table><tr><th>可算名詞（数えられる）</th><th>不可算名詞（数えられない）</th></tr>
<tr><td>book / books</td><td>water（水）</td></tr>
<tr><td>cat / cats</td><td>money（お金）</td></tr>
<tr><td>apple / apples</td><td>information（情報）</td></tr>
<tr><td>student / students</td><td>time（時間）</td></tr>
<tr><td>idea / ideas</td><td>news（ニュース）</td></tr>
<tr><td>friend / friends</td><td>advice（アドバイス）</td></tr>
</table>
""",
    "futeisi2.html": """
<h2>不定詞の応用構文 実戦練習</h2>
<div class="highlight"><p>A: Is it difficult for you to run 10km?<br>B: Yes, it's too difficult for me to run that far.<br>A: I see. Is it easy for you to swim?<br>B: Yes, I'm strong enough to swim for an hour.</p></div>
<h2>too 〜 to 構文の言い換え</h2>
<p>too 〜 to 構文は so 〜 that 〜 cannot で言い換えられます。</p>
<table><tr><th>too 〜 to</th><th>so 〜 that 〜 cannot</th></tr>
<tr><td>too young to drive</td><td>so young that he cannot drive</td></tr>
<tr><td>too heavy to carry</td><td>so heavy that I cannot carry</td></tr>
<tr><td>too tired to study</td><td>so tired that I cannot study</td></tr>
</table>
<div class="note"><strong>高校入試頻出！</strong> too 〜 to = so 〜 that の言い換えは受験の定番問題です。</div>
""",
    "futeisi1.html": """
<h2>不定詞の3用法 実戦練習</h2>
<div class="highlight"><p>A: What do you want to do this weekend?<br>B: I want to go shopping. I have something to buy.<br>A: I went to the library to study yesterday.<br>B: My dream is to become a doctor.</p></div>
<h2>不定詞をとる動詞リスト</h2>
<table><tr><th>動詞</th><th>意味</th><th>例</th></tr>
<tr><td>want</td><td>〜したい</td><td>I want to be a teacher.</td></tr>
<tr><td>hope</td><td>〜を望む</td><td>I hope to see you again.</td></tr>
<tr><td>plan</td><td>〜を計画する</td><td>I plan to visit Kyoto.</td></tr>
<tr><td>decide</td><td>〜を決心する</td><td>I decided to study harder.</td></tr>
<tr><td>need</td><td>〜する必要がある</td><td>I need to buy a new bag.</td></tr>
<tr><td>try</td><td>〜しようとする</td><td>I will try to solve this problem.</td></tr>
</table>
""",
}

for fname, extra in EXTRAS.items():
    thicken(fname, extra)

print("=== 最終拡充が完了しました ===")