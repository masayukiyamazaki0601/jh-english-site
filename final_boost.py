#!/usr/bin/env python3
"""残り200行未満の14記事にさらに大量追加（300行目標）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra, skip_over=800):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines >= skip_over:
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

FINAL_CONTENT = {
    "doumei.html": """
<h2>動名詞の重要構文（5パターン）</h2>
<ul>
<li><strong>It is no use + 動名詞</strong>：It is no use crying.（泣いても無駄だ）</li>
<li><strong>There is no + 動名詞</strong>：There is no telling what will happen.（何が起こるかわからない）</li>
<li><strong>cannot help + 動名詞</strong>：I cannot help laughing.（笑わずにはいられない）</li>
<li><strong>be worth + 動名詞</strong>：This book is worth reading.（この本は読む価値がある）</li>
<li><strong>feel like + 動名詞</strong>：I feel like sleeping.（眠い気分だ）</li>
</ul>
<h2>動名詞 vs 不定詞 どちらをとるか診断</h2>
<p><strong>動名詞のみを目的語にとる動詞（暗記リスト）</strong></p>
<ul>
<li>enjoy, finish, stop, quit, give up, put off, avoid, miss, practice, suggest, consider, imagine, mind, keep (on)</li>
</ul>
<p><strong>不定詞のみを目的語にとる動詞（暗記リスト）</strong></p>
<ul>
<li>want, hope, wish, decide, plan, expect, promise, refuse, learn, fail, manage, offer</li>
</ul>
<p><strong>両方使える動詞（意味が変わる）</strong></p>
<ul>
<li>stop doing（やめる）/ stop to do（やめて〜する）</li>
<li>remember doing（したことを覚える）/ remember to do（することを覚える）</li>
<li>forget doing（したことを忘れる）/ forget to do（することを忘れる）</li>
<li>try doing（試しに〜する）/ try to do（〜しようとする）</li>
</ul>
""",
    "gimonsi.html": """
<h2>疑問詞 英作文練習（10問）</h2>
<ol>
<li>あなたの名前は何ですか？ → What is your name?</li>
<li>彼は誰ですか？ → Who is he?</li>
<li>どこから来ましたか？ → Where are you from?</li>
<li>誕生日はいつですか？ → When is your birthday?</li>
<li>なぜ遅刻したのですか？ → Why are you late?</li>
<li>お元気ですか？ → How are you?</li>
<li>何冊本を持っていますか？ → How many books do you have?</li>
<li>これはいくらですか？ → How much is this?</li>
<li>あなたは何歳ですか？ → How old are you?</li>
<li>昨日何が起こりましたか？ → What happened yesterday?</li>
</ol>
<h2>疑問詞の使い分けマスター表</h2>
<table>
<tr><th>質問したい内容</th><th>使う疑問詞</th><th>例文</th></tr>
<tr><td>物・事・行動</td><td>What</td><td>What is this? / What do you do?</td></tr>
<tr><td>人</td><td>Who</td><td>Who is that girl?</td></tr>
<tr><td>場所</td><td>Where</td><td>Where do you live?</td></tr>
<tr><td>時間</td><td>When</td><td>When does school start?</td></tr>
<tr><td>理由</td><td>Why</td><td>Why are you happy?</td></tr>
<tr><td>方法・状態</td><td>How</td><td>How do you go to school?</td></tr>
<tr><td>数量（数）</td><td>How many</td><td>How many pets do you have?</td></tr>
<tr><td>数量（量）</td><td>How much</td><td>How much water do you drink?</td></tr>
<tr><td>年齢</td><td>How old</td><td>How old is your sister?</td></tr>
<tr><td>頻度</td><td>How often</td><td>How often do you play tennis?</td></tr>
</table>
""",
    "jyodosi.html": """
<h2>助動詞 英作文練習（10問）</h2>
<ol>
<li>もっと勉強しなければなりません。 → You must study harder.</li>
<li>今行かなければなりません。 → I have to go now.</li>
<li>入ってもいいですか？ → May I come in?</li>
<li>ここでは走ってはいけません。 → You must not run here.</li>
<li>休むべきです。 → You should rest.</li>
<li>行く必要はありません。 → You don't have to go.</li>
<li>お互いに助け合うべきです。 → We should help each other.</li>
<li>電話を使ってもいいですか？ → May I use your phone?</li>
<li>彼は気をつけなければなりません。 → He must be careful.</li>
<li>食べ過ぎるべきではありません。 → You should not eat too much.</li>
</ol>
<h2>助動詞 時制の変化表</h2>
<table>
<tr><th>現在形</th><th>意味</th><th>過去形</th><th>未来形</th></tr>
<tr><td>can</td><td>できる</td><td>could</td><td>will be able to</td></tr>
<tr><td>must</td><td>しなければならない</td><td>had to</td><td>will have to</td></tr>
<tr><td>may</td><td>してもよい</td><td>might</td><td>will be allowed to</td></tr>
<tr><td>should</td><td>すべきだ</td><td>should have</td><td>—</td></tr>
</table>
""",
    "kakosin.html": """
<h2>過去進行形 英作文練習（10問）</h2>
<ol>
<li>午後8時に本を読んでいました。 → I was reading a book at 8pm.</li>
<li>彼らは昨日サッカーをしていました。 → They were playing soccer yesterday.</li>
<li>彼女はその時夕食を作っていました。 → She was cooking dinner at that time.</li>
<li>彼はその時寝ていませんでした。 → He was not sleeping at that time.</li>
<li>真夜中に勉強していましたか？ → Were you studying at midnight?</li>
<li>その時何をしていましたか？ → What were you doing then?</li>
<li>電話したとき、私はテレビを見ていました。 → I was watching TV when you called.</li>
<li>雨が降っていたので、家にいました。 → It was raining, so I stayed home.</li>
<li>彼女が来たとき、私たちは食事をしていました。 → We were eating when she came.</li>
<li>彼は宿題をしているときに眠ってしまいました。 → He fell asleep while he was doing homework.</li>
</ol>
<h2>過去進行形 重要パターンまとめ</h2>
<p><strong>while + 過去進行形, 過去形</strong>：While I was watching TV, the phone rang.</p>
<p><strong>過去形 + when + 過去進行形</strong>：The phone rang when I was taking a bath.</p>
<p><strong>過去進行形 + when + 過去形</strong>：I was taking a bath when the phone rang.</p>
""",
    "kansetu.html": """
<h2>間接疑問 重要構文まとめ</h2>
<p><strong>【間接疑問の語順ルール】</strong></p>
<ul>
<li>疑問詞がある場合：Do you know + 疑問詞 + 主語 + 動詞？</li>
<li>疑問詞がない場合：Do you know + if/whether + 主語 + 動詞？</li>
</ul>
<p><strong>使える動詞リスト（間接疑問と一緒に使う）</strong></p>
<ul>
<li><strong>know</strong>：I know〜 / Do you know〜? / I don't know〜</li>
<li><strong>tell</strong>：Can you tell me〜? / Please tell me〜</li>
<li><strong>wonder</strong>：I wonder〜（〜か疑問だ）</li>
<li><strong>ask</strong>：He asked〜（彼は〜と尋ねた）</li>
<li><strong>understand</strong>：I don't understand〜（〜がわからない）</li>
<li><strong>be sure</strong>：I'm not sure〜（〜が確かでない）</li>
</ul>
""",
    "ukemi.html": """
<h2>受け身 重要ポイント：by以外の前置詞</h2>
<p>受け身では <strong>by</strong> が最も一般的ですが、以下の前置詞も使われます。</p>
<ul>
<li><strong>with</strong>（道具・材料）：The cake was filled <strong>with</strong> cream.</li>
<li><strong>to</strong>（知られている）：This fact is known <strong>to</strong> everyone.</li>
<li><strong>for</strong>（目的）：This room is used <strong>for</strong> meetings.</li>
</ul>
<h2>受け身 英作文練習（10問）</h2>
<ol>
<li>英語は多くの国で話されています。 → English is spoken in many countries.</li>
<li>この本は漱石によって書かれました。 → This book was written by Soseki.</li>
<li>窓はその少年によって壊されました。 → The window was broken by the boy.</li>
<li>これらのクッキーは母によって作られました。 → These cookies were made by my mother.</li>
<li>毎日部屋が掃除されます。 → The room is cleaned every day.</li>
<li>この寺は400年前に建てられました。 → This temple was built 400 years ago.</li>
<li>ドアは7時に開けられます。 → The door is opened at seven.</li>
<li>この車は日本で作られました。 → This car was made in Japan.</li>
<li>多くの木が公園に植えられました。 → Many trees were planted in the park.</li>
<li>この手紙は英語で書かれました。 → This letter was written in English.</li>
</ol>
""",
    "bekako.html": """
<h2>be動詞過去形 英作文練習（10問）</h2>
<ol>
<li>私は昨日幸せでした。 → I was happy yesterday.</li>
<li>彼らは昨夜家にいました。 → They were at home last night.</li>
<li>彼女は昨日忙しかったです。 → She was busy yesterday.</li>
<li>私たちは先週日曜日に公園にいました。 → We were in the park last Sunday.</li>
<li>彼は昨日病気でした。 → He was sick yesterday.</li>
<li>私は昨日家にいませんでした。 → I was not at home yesterday.</li>
<li>彼女は病気じゃなかった。 → She wasn't sick.</li>
<li>試合の後疲れていましたか？ → Were you tired after the game?</li>
<li>彼女はパーティーにいましたか？ → Was she at the party?</li>
<li>今朝は寒かったですか？ → Was it cold this morning?</li>
</ol>
<h2>過去形の短縮形まとめ</h2>
<table>
<tr><th>元の形</th><th>短縮形</th><th>発音</th></tr>
<tr><td>was not</td><td>wasn't</td><td>ワズント</td></tr>
<tr><td>were not</td><td>weren't</td><td>ワーント</td></tr>
<tr><td>I was</td><td>—</td><td>短縮形なし</td></tr>
<tr><td>you were</td><td>—</td><td>短縮形なし</td></tr>
</table>
""",
    "genkan2.html": """
<h2>現在完了（経験） 英作文練習（10問）</h2>
<ol>
<li>今までに京都に行ったことがありますか？ → Have you ever been to Kyoto?</li>
<li>寿司を食べたことがありません。 → I have never eaten sushi.</li>
<li>彼女はアメリカに2回行ったことがあります。 → She has been to the US twice.</li>
<li>この映画を以前見たことがあります。 → I have seen this movie before.</li>
<li>彼は海外に行ったことがありません。 → He has never been abroad.</li>
<li>京都に行ったことがあります。 → I have been to Kyoto.</li>
<li>彼女は京都に行ってしまいました。 → She has gone to Kyoto.</li>
<li>今までに納豆を食べたことがありますか？ → Have you ever eaten natto?</li>
<li>私は蛇を見たことがありません。 → I have never seen a snake.</li>
<li>彼は3回その映画を見ています。 → He has seen that movie three times.</li>
</ol>
<h2>現在完了（経験）よく出る副詞</h2>
<table>
<tr><th>副詞</th><th>意味</th><th>肯定文</th><th>疑問文</th><th>否定文</th></tr>
<tr><td>ever</td><td>今までに</td><td>—</td><td>⭕</td><td>—</td></tr>
<tr><td>never</td><td>一度も〜ない</td><td>⭕</td><td>—</td><td>—</td></tr>
<tr><td>before</td><td>以前に</td><td>⭕</td><td>⭕</td><td>—</td></tr>
<tr><td>once</td><td>1回</td><td>⭕</td><td>—</td><td>—</td></tr>
<tr><td>twice</td><td>2回</td><td>⭕</td><td>—</td><td>—</td></tr>
</table>
""",
    "genkanSinkokei.html": """
<h2>現在完了進行形 英作文練習（10問）</h2>
<ol>
<li>私は3年間英語を勉強し続けています。 → I have been studying English for three years.</li>
<li>朝から雨が降り続いています。 → It has been raining since morning.</li>
<li>どのくらい英語を勉強し続けていますか？ → How long have you been studying English?</li>
<li>彼女は30分待ち続けています。 → She has been waiting for 30 minutes.</li>
<li>彼らは2時間テニスをし続けています。 → They have been playing tennis for two hours.</li>
<li>最近よく眠れていません。 → I have not been sleeping well lately.</li>
<li>昨日から雨が降り続いていますか？ → Has it been raining since yesterday?</li>
<li>彼は4月からここで働いています。 → He has been working here since April.</li>
<li>彼女は1時間夕食を作っています。 → She has been cooking dinner for an hour.</li>
<li>赤ちゃんは20分泣き続けています。 → The baby has been crying for 20 minutes.</li>
</ol>
<h2>現在完了（継続）vs 現在完了進行形 選択問題</h2>
<ol>
<li>I ( ) here for 5 years. (live) → have lived / have been living</li>
<li>It ( ) since morning. (rain) → has been raining</li>
<li>She ( ) English for 3 years. (study) → has studied / has been studying</li>
<li>I ( ) him since childhood. (know) → have known（状態動詞）</li>
<li>They ( ) for 2 hours. (play) → have been playing</li>
</ol>
""",
    "futeisi2.html": """
<h2>不定詞（応用） 英作文練習（10問）</h2>
<ol>
<li>私たちが英語を勉強することは重要です。 → It is important for us to study English.</li>
<li>彼女がこの問題を解くのは簡単です。 → It is easy for her to solve this problem.</li>
<li>この箱は重すぎて私には運べません。 → This box is too heavy for me to carry.</li>
<li>彼女は若すぎて車を運転できません。 → She is too young to drive a car.</li>
<li>彼は車を運転するのに十分な年齢です。 → He is old enough to drive a car.</li>
<li>その本を買うのに十分なお金があります。 → I have enough money to buy the book.</li>
<li>彼女はその箱を運ぶのに十分強いです。 → She is strong enough to carry the box.</li>
<li>疲れすぎて勉強できませんでした。 → I was too tired to study.</li>
<li>このコーヒーは熱すぎて飲めません。 → This coffee is too hot to drink.</li>
<li>私たちがテニスをするのは楽しいです。 → It is fun for us to play tennis.</li>
</ol>
<h2>too 〜 to 構文の応用</h2>
<div class="note"><strong>too 〜 to の言い換え</strong><br>
too + 形容詞 + to do = so + 形容詞 + that + 主語 + cannot + 動詞<br>
例：She is too young to drive. = She is so young that she cannot drive.</div>
""",
    "genkan3.html": """
<h2>現在完了（完了） 英作文練習（10問）</h2>
<ol>
<li>ちょうど宿題を終えたところです。 → I have just finished my homework.</li>
<li>彼女はもう昼食を食べました。 → She has already eaten lunch.</li>
<li>もう宿題を終えましたか？ → Have you finished your homework yet?</li>
<li>まだ終えていません。 → I haven't finished yet.</li>
<li>彼はもう学校に行きました。 → He has already left for school.</li>
<li>ちょうど駅に着きました。 → We have just arrived at the station.</li>
<li>電車はもう着きましたか？ → Has the train arrived yet?</li>
<li>その映画はまだ見ていません。 → I haven't seen that movie yet.</li>
<li>彼女はもうそのレストランに行ったことがあります。 → She has already been to that restaurant.</li>
<li>ちょうどそのニュースを聞きました。 → I have just heard the news.</li>
</ol>
<h2>現在完了（完了）時制の流れ図</h2>
<p><strong>過去</strong> → 動作が完了 → <strong>現在</strong>（結果が残っている）</p>
<ul>
<li>I have lost my key.（過去になくした → 今も持っていない）</li>
<li>She has finished her homework.（過去に終えた → 今は自由）</li>
<li>He has arrived.（過去に着いた → 今ここにいる）</li>
</ul>
""",
    "bunsi.html": """
<h2>分詞 英作文練習（10問）</h2>
<ol>
<li>眠っている赤ちゃんを見て。 → Look at the sleeping baby.</li>
<li>部屋で歌っている女の子を知っています。 → I know the girl singing in the room.</li>
<li>壊れた時計を持っています。 → I have a broken watch.</li>
<li>これは漱石によって書かれた本です。 → This is a book written by Soseki.</li>
<li>走っている少年は私の弟です。 → The boy running is my brother.</li>
<li>ソファで寝ている猫がいます。 → There is a cat sleeping on the sofa.</li>
<li>少年によって壊された窓は新品です。 → The window broken by the boy is new.</li>
<li>これは英語で書かれた手紙です。 → This is a letter written in English.</li>
<li>ピンクのドレスを着た女の子は私の妹です。 → The girl wearing a pink dress is my sister.</li>
<li>路上で落ちている財布を見つけました。 → I found a lost wallet on the street.</li>
</ol>
""",
    "suryo.html": """
<h2>数量詞 重要ポイント：many / much の比較級・最上級</h2>
<table>
<tr><th>原級</th><th>比較級</th><th>最上級</th></tr>
<tr><td>many（たくさんの）</td><td>more（より多くの）</td><td>the most（最も多くの）</td></tr>
<tr><td>much（たくさんの）</td><td>more（より多くの）</td><td>the most（最も多くの）</td></tr>
<tr><td>few（少ししかない）</td><td>fewer（より少ない）</td><td>the fewest（最も少ない）</td></tr>
<tr><td>little（少ししかない）</td><td>less（より少ない）</td><td>the least（最も少ない）</td></tr>
</table>
<div class="note"><strong>注意！</strong> many も much も比較級は more。違いは名詞の種類だけ！</div>
<h2>数量詞 英作文練習（10問）</h2>
<ol>
<li>机の上にたくさんの本があります。 → There are many books on the desk.</li>
<li>あまりお金を持っていません。 → I don't have much money.</li>
<li>彼には友達がほとんどいません。 → He has few friends.</li>
<li>友達が数人います。 → I have a few friends.</li>
<li>残っている水はほとんどありません。 → There is little water left.</li>
<li>彼女は英語を少し話します。 → She speaks a little English.</li>
<li>いくらかお金を持っています。 → I have some money.</li>
<li>質問はありますか？ → Do you have any questions?</li>
<li>公園にたくさんの人がいます。 → There are a lot of people in the park.</li>
<li>質問がいくつかあります。 → I have a few questions.</li>
</ol>
""",
    "hikaku1.html": """
<h2>比較 英作文練習（10問）</h2>
<ol>
<li>太郎は次郎より背が高い。 → Taro is taller than Jiro.</li>
<li>彼女は私より美しい。 → She is more beautiful than me.</li>
<li>富士山は日本で一番高い山です。 → Mt. Fuji is the highest mountain in Japan.</li>
<li>彼女は日本で一番人気の歌手です。 → She is the most popular singer in Japan.</li>
<li>彼は私と同じくらい背が高い。 → He is as tall as me.</li>
<li>この本はあの本ほど面白くない。 → This book is not as interesting as that one.</li>
<li>彼はクラスで一番背が高い。 → He is the tallest in his class.</li>
<li>東京は大阪より大きい。 → Tokyo is bigger than Osaka.</li>
<li>彼は私より速く走る。 → He runs faster than me.</li>
<li>これは今まで食べた中で一番美味しいケーキです。 → This is the most delicious cake I've ever eaten.</li>
</ol>
<h2>比較級を強める表現まとめ</h2>
<ul>
<li><strong>much</strong> + 比較級：much bigger（はるかに大きい）</li>
<li><strong>a little</strong> + 比較級：a little taller（少し背が高い）</li>
<li><strong>even</strong> + 比較級：even more interesting（さらに面白い）</li>
<li><strong>far</strong> + 比較級：far better（はるかに良い）</li>
<li><strong>a lot</strong> + 比較級：a lot faster（ずっと速い）</li>
</ul>
""",
    "zensi.html": """
<h2>前置詞 重要イディオム（暗記リスト）</h2>
<table>
<tr><th>イディオム</th><th>意味</th><th>例文</th></tr>
<tr><td>at first</td><td>最初は</td><td>At first, I didn't like it.</td></tr>
<tr><td>at last</td><td>ついに</td><td>At last, we arrived.</td></tr>
<tr><td>at least</td><td>少なくとも</td><td>At least 10 people came.</td></tr>
<tr><td>in fact</td><td>実際は</td><td>In fact, he is kind.</td></tr>
<tr><td>in a hurry</td><td>急いで</td><td>She left in a hurry.</td></tr>
<tr><td>on time</td><td>時間通りに</td><td>The train arrived on time.</td></tr>
<tr><td>by the way</td><td>ところで</td><td>By the way, what is your name?</td></tr>
<tr><td>for example</td><td>例えば</td><td>For example, cats are cute.</td></tr>
</table>
<h2>前置詞 意味別分類表</h2>
<p><strong>位置・場所：</strong> in, on, at, under, behind, between, in front of, next to, near, above, below</p>
<p><strong>方向・移動：</strong> to, from, into, out of, toward, across, through, along</p>
<p><strong>時間：</strong> in, on, at, before, after, during, until, by, for, since</p>
<p><strong>手段・方法：</strong> by, with, without</p>
<p><strong>理由・目的：</strong> for, because of, due to</p>
""",
    "futeisi1.html": """
<h2>不定詞 3用法の見分け方（完全ガイド）</h2>
<p><strong>ステップ1：</strong> 不定詞の前に <strong>be動詞</strong> がある？→ 補語（名詞的用法）</p>
<p><strong>ステップ2：</strong> 不定詞の前に <strong>want/hope/decide</strong> などの動詞がある？→ 目的語（名詞的用法）</p>
<p><strong>ステップ3：</strong> 不定詞の前に <strong>名詞・something</strong> がある？→ 名詞を修飾（形容詞的用法）</p>
<p><strong>ステップ4：</strong> 上記以外 → 動詞を修飾（副詞的用法＝目的）</p>
<div class="highlight">
<p>例文で確認：<br>
・I want <strong>to study</strong> English. → 名詞的用法（wantの目的語）<br>
・I went to Kyoto <strong>to see</strong> temples. → 副詞的用法（目的）<br>
・I have something <strong>to do</strong>. → 形容詞的用法（somethingを修飾）<br>
・My dream is <strong>to be</strong> a doctor. → 名詞的用法（補語）</p></div>
<h2>不定詞 重要構文まとめ</h2>
<ul>
<li><strong>want to do</strong>：〜したい</li>
<li><strong>hope to do</strong>：〜したいと望む</li>
<li><strong>decide to do</strong>：〜することを決心する</li>
<li><strong>need to do</strong>：〜する必要がある</li>
<li><strong>try to do</strong>：〜しようとする</li>
<li><strong>tell 人 to do</strong>：人に〜するように言う</li>
<li><strong>ask 人 to do</strong>：人に〜するように頼む</li>
<li><strong>want 人 to do</strong>：人に〜してほしい</li>
</ul>
""",
    "kateiho.html": """
<h2>仮定法 英作文練習（10問）</h2>
<ol>
<li>もし私があなたなら、もっと勉強するのに。 → If I were you, I would study harder.</li>
<li>もしお金があれば、車を買うのに。 → If I had money, I would buy a car.</li>
<li>もし晴れなら、出かけられるのに。 → If it were sunny, we could go out.</li>
<li>もし時間があれば、あなたと行くのに。 → If I had time, I would go with you.</li>
<li>もし彼女に会えれば嬉しいのに。 → I would be happy if I could meet her.</li>
<li>もし私が鳥なら、あなたのところに飛んで行くのに。 → If I were a bird, I would fly to you.</li>
<li>もしもっと勉強すれば、合格できるのに。 → If he studied more, he would pass.</li>
<li>もし大金を持っていたら、世界旅行するのに。 → If I had a lot of money, I would travel around the world.</li>
<li>もし彼がここにいれば、助けてくれるのに。 → If he were here, he would help us.</li>
<li>もしあなただったら、どうしますか？ → What would you do if you were me?</li>
</ol>
<h2>仮定法 よく出るテスト問題パターン</h2>
<p><strong>パターン1：</strong> If + 主語 + were / 過去形, 主語 + would + 動詞の原形</p>
<p><strong>パターン2：</strong> I wish + 主語 + 過去形（「〜だったらいいのに」の後ろも仮定法）</p>
<p><strong>パターン3：</strong> If I were you, I would〜（「もし私があなたなら」の決まり文句）</p>
""",
    "setuzoku.html": """
<h2>接続詞 英作文練習（10問）</h2>
<ol>
<li>猫と犬が好きです。 → I like cats and dogs.</li>
<li>猫は好きですが犬は好きではありません。 → I like cats but I don't like dogs.</li>
<li>プレゼントをもらったので嬉しいです。 → I am happy because I got a present.</li>
<li>疲れたので寝ました。 → I was tired, so I went to bed.</li>
<li>着いたら電話してください。 → Call me when you arrive.</li>
<li>雨が降れば家にいます。 → If it rains, I will stay home.</li>
<li>彼は親切だと思います。 → I think (that) he is kind.</li>
<li>彼女は正直だと知っています。 → I know (that) she is honest.</li>
<li>雨が降っていたので、傘を持って行きました。 → Because it was raining, I took an umbrella.</li>
<li>家に着いたら電話します。 → I will call you when I get home.</li>
</ol>
<h2>接続詞 重要ルール一覧</h2>
<ol>
<li><strong>and</strong> = 並列：同じ種類のものをくっつける</li>
<li><strong>but</strong> = 逆接：反対のことをくっつける</li>
<li><strong>because</strong> = 理由：原因や理由を説明する</li>
<li><strong>so</strong> = 結果：結果や結論を述べる</li>
<li><strong>when</strong> = 時：時間や状況を表す</li>
<li><strong>if</strong> = 条件：仮定や条件を表す</li>
<li><strong>that</strong> = 内容：思ったことや言ったこと</li>
</ol>
""",
    "there.html": """
<h2>there is構文 英作文練習（10問）</h2>
<ol>
<li>テーブルの下に猫がいます。 → There is a cat under the table.</li>
<li>机の上にたくさんの本があります。 → There are many books on the desk.</li>
<li>机の上にペンがありますか？ → Is there a pen on the desk?</li>
<li>部屋に学生はいますか？ → Are there any students in the room?</li>
<li>冷蔵庫に牛乳はありません。 → There is not any milk in the fridge.</li>
<li>テーブルの上に3つのリンゴがあります。 → There are three apples on the table.</li>
<li>この近くに病院はありますか？ → Is there a hospital near here?</li>
<li>あなたのクラスに何人の学生がいますか？ → How many students are there in your class?</li>
<li>コップの中にいくらか水があります。 → There is some water in the glass.</li>
<li>公園にたくさんの人がいます。 → There are a lot of people in the park.</li>
</ol>
<h2>There is 構文の注意ポイント</h2>
<ul>
<li><strong>日本語と語順が逆</strong>：日本語は「場所 + に + 物 + がある」、英語は「There is + 物 + 場所」</li>
<li><strong>there は「そこ」という意味ではない</strong>：There is a book. = 「本があります」（「そこ」ではない）</li>
<li><strong>be動詞は後ろの名詞で決まる</strong>：近接の法則（後ろの名詞が単数なら is、複数なら are）</li>
</ul>
""",
    "mirai.html": """
<h2>未来形 英作文練習（10問）</h2>
<ol>
<li>あとで電話します。 → I will call you later.</li>
<li>明日雨が降るでしょう。 → It will rain tomorrow.</li>
<li>彼女は法学を勉強する予定です。 → She is going to study law.</li>
<li>手伝ってくれますか？ → Will you help me?</li>
<li>窓を開けてくれますか？ → Will you open the window?</li>
<li>来月京都を訪れる予定です。 → I am going to visit Kyoto next month.</li>
<li>彼女は医者になるつもりです。 → She is going to be a doctor.</li>
<li>来週テストがあります。 → We are going to have a test next week.</li>
<li>あの雲を見て！雨が降りそうだ。 → Look at those clouds! It's going to rain.</li>
<li>私は行きません。 → I will not go. / I won't go.</li>
</ol>
<h2>will と be going to の使い分けクイック診断</h2>
<table>
<tr><th>シチュエーション</th><th>適切な表現</th><th>理由</th></tr>
<tr><td>電話がなって「私が出ます」</td><td>I'll get it.</td><td>その場の意思決定</td></tr>
<tr><td>「今週末の予定は？」</td><td>I'm going to visit my grandparents.</td><td>前から決めていた</td></tr>
<tr><td>黒い雲を見て「雨が降るね」</td><td>It's going to rain.</td><td>証拠がある予測</td></tr>
<tr><td>天気予報「明日は晴れ」</td><td>It will be sunny tomorrow.</td><td>単なる予測</td></tr>
</table>
""",
    "can.html": """
<h2>can 英作文練習（10問）</h2>
<ol>
<li>私は泳げます。 → I can swim.</li>
<li>彼女はフランス語を話せます。 → She can speak French.</li>
<li>彼は速く走れます。 → He can run fast.</li>
<li>私はピアノを弾けません。 → I can't play the piano.</li>
<li>手伝ってくれますか？ → Can you help me?</li>
<li>ペンを使ってもいいですか？ → Can I use your pen?</li>
<li>5歳の時泳げました。 → I could swim when I was five.</li>
<li>彼女は10歳の時英語を話せました。 → She could speak English when she was ten.</li>
<li>去年はピアノを弾けませんでした。 → I couldn't play the piano last year.</li>
<li>彼は日本語を話せますか？ → Can he speak Japanese?</li>
</ol>
<h2>can / could / be able to 時制の比較</h2>
<table>
<tr><th>時制</th><th>can</th><th>be able to</th></tr>
<tr><td>現在</td><td>I can swim.</td><td>I am able to swim.</td></tr>
<tr><td>過去</td><td>I could swim.</td><td>I was able to swim.</td></tr>
<tr><td>未来</td><td>—</td><td>I will be able to swim.</td></tr>
<tr><td>現在完了</td><td>—</td><td>I have been able to swim.</td></tr>
</table>
<div class="note"><strong>could vs was able to</strong>：could = 能力があった、was able to = 実際にうまくできた</div>
""",
    "daimeisi.html": """
<h2>代名詞 英作文練習（10問）</h2>
<ol>
<li>彼女は私の友達です。 → She is my friend.</li>
<li>私は彼女が好きです。 → I like her.</li>
<li>これは私の本です。 → This is my book.</li>
<li>この本は私のものです。 → This book is mine.</li>
<li>それを私にください。 → Give it to me.</li>
<li>彼は先生で、生徒たちは彼を愛しています。 → He is a teacher and students love him.</li>
<li>これは私たちの教室です。 → This is our classroom.</li>
<li>あの犬は彼らのものです。 → That dog is theirs.</li>
<li>私は彼を昨日見ました。 → I saw him yesterday.</li>
<li>これらは彼女の鍵です。 → These are her keys.</li>
</ol>
<h2>代名詞の格変化 完全暗記表</h2>
<table>
<tr><th>人称</th><th>主格（〜は）</th><th>所有格（〜の）</th><th>目的格（〜を）</th><th>所有代名詞（〜のもの）</th><th>再帰代名詞（〜自身）</th></tr>
<tr><td>1人称単数</td><td>I</td><td>my</td><td>me</td><td>mine</td><td>myself</td></tr>
<tr><td>2人称単数</td><td>you</td><td>your</td><td>you</td><td>yours</td><td>yourself</td></tr>
<tr><td>3人称単数（男）</td><td>he</td><td>his</td><td>him</td><td>his</td><td>himself</td></tr>
<tr><td>3人称単数（女）</td><td>she</td><td>her</td><td>her</td><td>hers</td><td>herself</td></tr>
<tr><td>3人称単数（物）</td><td>it</td><td>its</td><td>it</td><td>its</td><td>itself</td></tr>
<tr><td>1人称複数</td><td>we</td><td>our</td><td>us</td><td>ours</td><td>ourselves</td></tr>
<tr><td>2人称複数</td><td>you</td><td>your</td><td>you</td><td>yours</td><td>yourselves</td></tr>
<tr><td>3人称複数</td><td>they</td><td>their</td><td>them</td><td>theirs</td><td>themselves</td></tr>
</table>
""",
    "genkan1.html": """
<h2>現在完了（継続） 英作文練習（10問）</h2>
<ol>
<li>東京に5年間住んでいます。 → I have lived in Tokyo for five years.</li>
<li>彼女は10歳から英語を勉強しています。 → She has studied English since she was ten.</li>
<li>彼は月曜から病気です。 → He has been sick since Monday.</li>
<li>どのくらいここに住んでいますか？ → How long have you lived here?</li>
<li>彼女は10年間先生ですか？ → Has she been a teacher for 10 years?</li>
<li>先週から彼に会っていません。 → I have not seen him since last week.</li>
<li>彼らは子供の頃からお互いを知っています。 → They have known each other since childhood.</li>
<li>私は2020年からこの学校に通っています。 → I have gone to this school since 2020.</li>
<li>彼は3年間ここで働いています。 → He has worked here for three years.</li>
<li>私は朝からずっと忙しいです。 → I have been busy since this morning.</li>
</ol>
<h2>現在完了（継続）よく使う動詞リスト</h2>
<ul>
<li><strong>live</strong>：住んでいる I have lived here for 5 years.</li>
<li><strong>study</strong>：勉強している She has studied English for 2 years.</li>
<li><strong>work</strong>：働いている He has worked here since April.</li>
<li><strong>know</strong>：知っている We have known each other for 10 years.</li>
<li><strong>have</strong>：持っている I have had this car since 2020.</li>
<li><strong>be</strong>：〜である She has been a teacher for 5 years.</li>
</ul>
""",
}

for fname, extra in FINAL_CONTENT.items():
    thicken(fname, extra)

print("=== 最終追加拡充が完了しました ===")