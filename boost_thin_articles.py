#!/usr/bin/env python3
"""残り14の薄い記事（158-199行）に300行超えを目指した大量追加"""
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

# 残り14の薄い記事に特化した追加コンテンツ
EXTRAS = {
    "genkeiFuteisi.html": """
<h2>原形不定詞 穴埋め問題（全20問）</h2>
<ol>
<li>I saw him ( ) in the park. (run) → run</li>
<li>She made me ( ) the room. (clean) → clean</li>
<li>Let's ( ) to the park. (go) → go</li>
<li>I heard her ( ) a song. (sing) → sing</li>
<li>My father had me ( ) the car. (wash) → wash</li>
<li>We watched the sun ( ). (set) → set</li>
<li>He helped me ( ) the box. (carry) → carry</li>
<li>I felt something ( ) my shoulder. (touch) → touch</li>
<li>She let me ( ) her phone. (use) → use</li>
<li>The teacher made us ( ) the essay. (rewrite) → rewrite</li>
<li>I saw a dog ( ) across the street. (run) → run</li>
<li>We heard the baby ( ). (cry) → cry</li>
<li>They watched the game ( ). (begin) → begin</li>
<li>My mother let me ( ) out. (go) → go</li>
<li>I had my brother ( ) my room. (clean) → clean</li>
<li>She helped me ( ) the problem. (solve) → solve</li>
<li>I saw the cat ( ) the tree. (climb) → climb</li>
<li>We heard the bell ( ). (ring) → ring</li>
<li>He made me ( ) the truth. (tell) → tell</li>
<li>Let's not ( ) late. (be) → be</li>
</ol>
<h2>知覚動詞・使役動詞一覧（暗記用）</h2>
<table>
<tr><th>種類</th><th>動詞</th><th>意味</th><th>例文</th></tr>
<tr><td rowspan="3">知覚動詞</td><td>see</td><td>見る</td><td>I saw him run.</td></tr>
<tr><td>hear</td><td>聞く</td><td>I heard her sing.</td></tr>
<tr><td>watch</td><td>観察する</td><td>We watched the sun set.</td></tr>
<tr><td rowspan="3">使役動詞</td><td>make</td><td>〜させる（強制）</td><td>She made me clean my room.</td></tr>
<tr><td>let</td><td>〜させてくれる（許可）</td><td>My mother let me go.</td></tr>
<tr><td>have</td><td>〜してもらう（依頼）</td><td>I had him carry the box.</td></tr>
</table>
""",
    "kankeisi1.html": """
<h2>関係代名詞 穴埋め問題（全20問）</h2>
<ol>
<li>I know the boy ( ) is running. → who</li>
<li>This is the book ( ) I bought. → which / that</li>
<li>She is the girl ( ) plays the piano. → who / that</li>
<li>He is the man ( ) I met yesterday. → whom / that</li>
<li>I have a dog ( ) can run fast. → that / which</li>
<li>The book ( ) I read was interesting. → that / which</li>
<li>Do you know the girl ( ) is singing? → who</li>
<li>This is the car ( ) he bought. → which / that</li>
<li>The man ( ) lives next door is kind. → who</li>
<li>The cake ( ) she made was delicious. → that / which</li>
<li>I like the teacher ( ) teaches math. → who</li>
<li>This is the house ( ) my grandfather built. → which / that</li>
<li>The girl ( ) you met is my sister. → whom / that</li>
<li>I have a friend ( ) can speak five languages. → who</li>
<li>The movie ( ) we saw was scary. → that / which</li>
<li>She is the woman ( ) helped me. → who</li>
<li>This is the museum ( ) has many paintings. → which / that</li>
<li>The boy ( ) broke the window apologized. → who</li>
<li>That is the park ( ) I used to play in. → which / that</li>
<li>I know the student ( ) won the contest. → who</li>
</ol>
<h2>関係代名詞 英作文練習（5問）</h2>
<ol>
<li>走っている少年を知っています。 → I know the boy who is running.</li>
<li>これは私が買った本です。 → This is the book which I bought.</li>
<li>彼女はピアノが上手な女の子です。 → She is the girl that plays the piano well.</li>
<li>彼は昨日私が会った男性です。 → He is the man (whom) I met yesterday.</li>
<li>私は速く走れる犬を飼っています。 → I have a dog that can run fast.</li>
</ol>
""",
    "kansetu.html": """
<h2>間接疑問 穴埋め問題（全15問）</h2>
<ol>
<li>Do you know where he ( )? → lives</li>
<li>I don't know what this ( ). → is</li>
<li>Can you tell me where the station ( )? → is</li>
<li>I wonder ( ) he is kind. → if / whether</li>
<li>Do you know ( ) she will come? → if / whether</li>
<li>Please tell me when the movie ( ). → starts</li>
<li>I know ( ) she is. → who</li>
<li>Do you know how much it ( )? → costs</li>
<li>I'm not sure if he ( ) come. → will</li>
<li>Can you tell me what time it ( )? → is</li>
<li>I wonder why she ( ) crying. → is</li>
<li>Do you know how I ( ) get there? → can</li>
<li>Please tell me what I ( ) do. → should</li>
<li>I don't know where she ( ) born. → was</li>
<li>Can you tell me who ( ) man is? → that</li>
</ol>
<h2>間接疑問 英作文練習（5問）</h2>
<ol>
<li>彼がどこに住んでいるか知っていますか？ → Do you know where he lives?</li>
<li>これが何かわかりません。 → I don't know what this is.</li>
<li>駅への行き方を教えてくれますか？ → Can you tell me how to get to the station?</li>
<li>彼が親切かどうか疑問だ。 → I wonder if he is kind.</li>
<li>彼女が誰か知っています。 → I know who she is.</li>
</ol>
""",
    "genkanSinkokei.html": """
<h2>現在完了進行形 穴埋め問題（全15問）</h2>
<ol>
<li>I have been ( ) English for three years. → studying</li>
<li>It has been ( ) since morning. → raining</li>
<li>How long have you been ( ) here? → living</li>
<li>She has been ( ) for the bus for 30 minutes. → waiting</li>
<li>They have been ( ) tennis for two hours. → playing</li>
<li>I have not been ( ) well lately. → sleeping</li>
<li>Has it been ( ) since yesterday? → raining</li>
<li>How long have you been ( ) Japanese? → learning</li>
<li>He has been ( ) here since April. → working</li>
<li>We have been ( ) for the exam all week. → studying</li>
<li>She has been ( ) dinner for an hour. → cooking</li>
<li>The baby has been ( ) for 20 minutes. → crying</li>
<li>I have been ( ) to call you all day. → trying</li>
<li>They have been ( ) about the problem. → talking</li>
<li>How long has it been ( )? → snowing</li>
</ol>
<h2>現在完了（継続）vs 現在完了進行形 比較問題</h2>
<table>
<tr><th>文</th><th>意味</th><th>正しい？</th></tr>
<tr><td>I have lived here for 5 years.</td><td>5年間ここに住んでいる</td><td>⭕状態動詞は継続形</td></tr>
<tr><td>I have been living here for 5 years.</td><td>5年間住み続けている</td><td>⭕動作の強調</td></tr>
<tr><td>I have studied for 2 hours.</td><td>2時間勉強した</td><td>⭕現在完了（継続）</td></tr>
<tr><td>I have been studying for 2 hours.</td><td>2時間勉強し続けている</td><td>⭕現在完了進行形</td></tr>
</table>
""",
    "gimonsi.html": """
<h2>疑問詞 穴埋め問題（全15問）</h2>
<ol>
<li>( ) is your name? → What</li>
<li>( ) is he? → Who</li>
<li>( ) are you from? → Where</li>
<li>( ) is your birthday? → When</li>
<li>( ) are you late? → Why</li>
<li>( ) are you? → How</li>
<li>( ) many books do you have? → How</li>
<li>( ) much is this? → How</li>
<li>( ) old are you? → How</li>
<li>( ) happened yesterday? → What</li>
<li>( ) came to the party? → Who</li>
<li>( ) do you go to school? → How</li>
<li>( ) do you like dogs? → Why</li>
<li>( ) is the station? → Where</li>
<li>( ) time do you get up? → What</li>
</ol>
<h2>What vs Which の違い</h2>
<div class="note"><strong>What</strong> = 選択肢が決まっていないとき（What do you want to eat?）<br>
<strong>Which</strong> = 選択肢が決まっているとき（Which do you like, coffee or tea?）</div>
""",
    "genkan2.html": """
<h2>現在完了（経験） 穴埋め問題（全15問）</h2>
<ol>
<li>Have you ( ) been to Kyoto? → ever</li>
<li>I have ( ) eaten sushi. → never</li>
<li>She has been to the US ( ). → twice</li>
<li>I have seen this movie ( ). → before</li>
<li>He has ( ) been abroad. → never</li>
<li>Have you ( ) eaten Italian food? → ever</li>
<li>I have ( ) to Kyoto twice. → been</li>
<li>She has ( ) to Kyoto.（行って戻っていない）→ gone</li>
<li>How many times have you ( ) to the US? → been</li>
<li>I have never ( ) to Hokkaido. → been</li>
<li>Have you ever ( ) natto? → eaten</li>
<li>She has never ( ) a snake. → seen</li>
<li>I have been to the US three ( ). → times</li>
<li>He has never ( ) sushi. → tried</li>
<li>Have you ever ( ) to a concert? → been</li>
</ol>
<h2>been to / gone to 比較表</h2>
<ul>
<li><strong>I have been to Kyoto.</strong> = 京都に行ったことがある（今ここにいる）</li>
<li><strong>She has gone to Kyoto.</strong> = 彼女は京都に行った（今ここにいない）</li>
<li><strong>They have been to the US.</strong> = 彼らはアメリカに行ったことがある（今ここにいる）</li>
<li><strong>He has gone to the US.</strong> = 彼はアメリカに行った（今ここにいない）</li>
</ul>
""",
    "futeisi2.html": """
<h2>不定詞（応用） 穴埋め問題（全15問）</h2>
<ol>
<li>It is important ( ) us to study English. → for</li>
<li>This box is too heavy ( ) me to carry. → for</li>
<li>She is ( ) young to drive a car. → too</li>
<li>He is old ( ) to drive a car. → enough</li>
<li>It is easy ( ) her to solve. → for</li>
<li>I was ( ) tired to study. → too</li>
<li>I have ( ) money to buy the book. → enough</li>
<li>This problem is too difficult ( ) me. → for</li>
<li>She is tall ( ) to reach the shelf. → enough</li>
<li>It is important ( ) to be on time. → (no word needed)</li>
<li>The bag is too heavy ( ) her to carry. → for</li>
<li>He is strong ( ) to lift the box. → enough</li>
<li>It is dangerous ( ) children to play here. → for</li>
<li>The coffee is ( ) hot to drink. → too</li>
<li>She is not old ( ) to stay up late. → enough</li>
</ol>
<h2>too 〜 to / enough to 言い換え問題</h2>
<ol>
<li>too young to drive = so young ( ) he cannot drive. → that</li>
<li>too heavy to carry = so heavy ( ) I cannot carry it. → that</li>
<li>old enough to drive = so old ( ) he can drive. → that</li>
<li>tall enough to reach = so tall ( ) she can reach it. → that</li>
</ol>
""",
    "genkan3.html": """
<h2>現在完了（完了） 穴埋め問題（全15問）</h2>
<ol>
<li>I have ( ) finished my homework. → just</li>
<li>She has ( ) eaten lunch. → already</li>
<li>Have you finished your homework ( )? → yet</li>
<li>I haven't seen that movie ( ). → yet</li>
<li>He has ( ) left for school. → already</li>
<li>We have ( ) arrived at the station. → just</li>
<li>Has the train arrived ( )? → yet</li>
<li>Has she ( ) finished her report? → already</li>
<li>I have ( ) heard the news. → just</li>
<li>They haven't left ( ). → yet</li>
<li>She has ( ) been to that restaurant. → already</li>
<li>Have you ( ) seen the new movie? → already / yet</li>
<li>He has ( ) come back from school. → just</li>
<li>We haven't decided ( ). → yet</li>
<li>I have ( ) finished reading the book. → already</li>
</ol>
<h2>現在完了（完了）vs 過去形 比較問題（5問）</h2>
<ol>
<li>I ( ) my key. (lose) 今も見つからない → have lost</li>
<li>I ( ) my key yesterday. (lose) 昨日なくした → lost</li>
<li>She ( ) to Kyoto. (be) 今も京都 → has been</li>
<li>She ( ) to Kyoto last year. (go) 去年行った → went</li>
<li>He ( ) his homework already. (finish) → has finished</li>
</ol>
""",
    "bunsi.html": """
<h2>分詞 穴埋め問題（全15問）</h2>
<ol>
<li>Look at the ( ) baby. (sleep) → sleeping</li>
<li>I know the girl ( ) in the room. (sing) → singing</li>
<li>I have a ( ) watch. (break) → broken</li>
<li>This is a book ( ) by Soseki. (write) → written</li>
<li>The boy ( ) is my brother. (run) → running</li>
<li>There is a cat ( ) on the sofa. (sleep) → sleeping</li>
<li>The window ( ) by the boy is new. (break) → broken</li>
<li>This is a letter ( ) in English. (write) → written</li>
<li>I saw a ( ) bird in the tree. (sing) → singing</li>
<li>Please throw away the ( ) cup. (break) → broken</li>
<li>The girl ( ) a pink dress is my sister. (wear) → wearing</li>
<li>I found a ( ) wallet on the street. (lose) → lost</li>
<li>Look at the ( ) leaves on the ground. (fall) → fallen</li>
<li>The man ( ) a hat is my uncle. (wear) → wearing</li>
<li>I ate a ( ) egg for breakfast. (boil) → boiled</li>
</ol>
<h2>現在分詞 vs 過去分詞 比較問題（6問）</h2>
<ol>
<li>boiling water / boiled water → 沸騰している水 / 沸騰したお湯</li>
<li>a boring movie / a bored student → 退屈な映画 / 退屈している生徒</li>
<li>an exciting game / an excited child → わくわくする試合 / 興奮している子ども</li>
<li>a surprising news / a surprised man → 驚くべきニュース / 驚いている男性</li>
<li>a tiring day / a tired worker → 疲れる一日 / 疲れている労働者</li>
<li>a frightening story / a frightened girl → 怖い話 / 怖がっている少女</li>
</ol>
""",
    "suryo.html": """
<h2>数量詞 穴埋め問題（全15問）</h2>
<ol>
<li>There are ( ) books on the desk. → many</li>
<li>I don't have ( ) money. → much</li>
<li>He has ( ) friends. (almost none) → few</li>
<li>I have ( ) friends. (some) → a few</li>
<li>There is ( ) water left. (almost none) → little</li>
<li>She speaks ( ) English. (a small amount) → a little</li>
<li>I have ( ) money. → some</li>
<li>Do you have ( ) questions? → any</li>
<li>There are a ( ) of people in the park. → lot</li>
<li>I have ( ) interest in that. (almost none) → little</li>
<li>He has ( ) friends here. (several) → a few</li>
<li>She has ( ) patience. (almost none) → little</li>
<li>There are too ( ) people in the room. → many</li>
<li>I have too ( ) homework. → much</li>
<li>I need ( ) minutes to finish. → a few</li>
</ol>
<h2>可算名詞 vs 不可算名詞 追加リスト</h2>
<table>
<tr><th>可算名詞</th><th>不可算名詞</th><th>注意点</th></tr>
<tr><td>chair, table, desk</td><td>furniture（家具）</td><td>「家具」は不可算</td></tr>
<tr><td>dollar, yen, euro</td><td>money（お金）</td><td>「お金」全体は不可算</td></tr>
<tr><td>job, task, project</td><td>work（仕事）</td><td>「仕事」は不可算</td></tr>
<tr><td>suggestion, idea</td><td>advice（アドバイス）</td><td>「アドバイス」は不可算</td></tr>
<tr><td>lesson, class</td><td>homework（宿題）</td><td>「宿題」は不可算</td></tr>
</table>
""",
    "hikaku1.html": """
<h2>比較 穴埋め問題（全15問）</h2>
<ol>
<li>Taro is ( ) than Jiro. (tall) → taller</li>
<li>She is more ( ) than me. (beautiful) → beautiful</li>
<li>Mt. Fuji is ( ) highest mountain in Japan. → the</li>
<li>He is as ( ) as me. (tall) → tall</li>
<li>This book is not as ( ) as that one. (interesting) → interesting</li>
<li>She is the ( ) popular singer in Japan. → most</li>
<li>good → ( ) → best → better</li>
<li>bad → ( ) → worst → worse</li>
<li>many/much → ( ) → most → more</li>
<li>Tokyo is ( ) than Osaka. (big) → bigger</li>
<li>He runs ( ) than me. (fast) → faster</li>
<li>This is ( ) most difficult problem. → the</li>
<li>She is ( ) tallest in her class. → the</li>
<li>He is not so ( ) as his brother. (tall) → tall</li>
<li>This is the ( ) delicious cake I've ever eaten. → most</li>
</ol>
<h2>比較級・最上級 ルール一覧</h2>
<table>
<tr><th>語の長さ</th><th>比較級</th><th>最上級</th><th>例</th></tr>
<tr><td>1音節</td><td>-er</td><td>the + -est</td><td>tall / taller / the tallest</td></tr>
<tr><td>1音節（子音+y）</td><td>-ier</td><td>the + -iest</td><td>happy / happier / the happiest</td></tr>
<tr><td>2音節（yで終わる）</td><td>-ier</td><td>the + -iest</td><td>easy / easier / the easiest</td></tr>
<tr><td>2音節以上</td><td>more + 原級</td><td>the most + 原級</td><td>beautiful / more beautiful / the most beautiful</td></tr>
<tr><td>不規則</td><td>個別に暗記</td><td>個別に暗記</td><td>good / better / best</td></tr>
</table>
""",
    "zensi.html": """
<h2>前置詞 穴埋め問題（全20問）</h2>
<ol>
<li>I get up ( ) six every morning. → at</li>
<li>She was born ( ) April 1st. → on</li>
<li>It is hot ( ) summer. → in</li>
<li>The cat is ( ) the table. → under</li>
<li>I go to school ( ) bus. → by</li>
<li>I studied English ( ) two hours. → for</li>
<li>There is a bank ( ) the station. → behind</li>
<li>I live ( ) Tokyo. → in</li>
<li>He is interested ( ) history. → in</li>
<li>She is good ( ) math. → at</li>
<li>I go to school ( ) bus. → by</li>
<li>Let's meet ( ) 3pm. → at</li>
<li>She was born ( ) 2008. → in</li>
<li>I will come back ( ) an hour. → in</li>
<li>The cat is ( ) the sofa. → on</li>
<li>She is standing ( ) the door. → behind</li>
<li>I put the book ( ) my bag. → in</li>
<li>The park is ( ) the station and the hospital. → between</li>
<li>He goes to school ( ) foot. → on</li>
<li>I cut the paper ( ) scissors. → with</li>
</ol>
<h2>in / on / at 診断テスト（8問）</h2>
<ol>
<li>I wake up ( ) 7am. → at</li>
<li>I was born ( ) May. → in</li>
<li>My birthday is ( ) May 5th. → on</li>
<li>I do my homework ( ) the evening. → in</li>
<li>Let's meet ( ) Sunday. → on</li>
<li>School starts ( ) April. → in</li>
<li>I brush my teeth ( ) night. → at</li>
<li>She came ( ) 8 o'clock. → at</li>
</ol>
""",
    "futeisi1.html": """
<h2>不定詞（基本） 穴埋め問題（全20問）</h2>
<ol>
<li>I want ( ) study English. → to</li>
<li>I went to Kyoto ( ) see temples. → to</li>
<li>I have something ( ) do. → to</li>
<li>I enjoy ( ) tennis. → playing</li>
<li>To play tennis ( ) fun. → is</li>
<li>My dream is ( ) be a doctor. → to</li>
<li>She studied hard ( ) pass the exam. → to</li>
<li>I need ( ) buy a new bag. → to</li>
<li>I hope ( ) see you again. → to</li>
<li>I want something ( ) drink. → to</li>
<li>He decided ( ) study abroad. → to</li>
<li>I went to the library ( ) borrow books. → to</li>
<li>It is important ( ) study every day. → to</li>
<li>I have a lot of homework ( ) do. → to</li>
<li>She wants ( ) be a singer. → to</li>
<li>I plan ( ) visit Kyoto next year. → to</li>
<li>He went to the post office ( ) mail a letter. → to</li>
<li>I need a pen ( ) write with. → to</li>
<li>She tried ( ) solve the problem. → to</li>
<li>I want a book ( ) read. → to</li>
</ol>
<h2>3用法の見分け方クイズ</h2>
<ol>
<li>I want <strong>to study</strong> English. → 名詞的用法（wantの目的語）</li>
<li>I went to Kyoto <strong>to see</strong> temples. → 副詞的用法（目的）</li>
<li>I have something <strong>to do</strong>. → 形容詞的用法（名詞を修飾）</li>
<li>My dream is <strong>to be</strong> a doctor. → 名詞的用法（補語）</li>
<li>She studied hard <strong>to pass</strong> the exam. → 副詞的用法（目的）</li>
</ol>
""",
    "kateiho.html": """
<h2>仮定法 穴埋め問題（全20問）</h2>
<ol>
<li>If I ( ) you, I would study harder. → were</li>
<li>If it ( ) sunny, we could go swimming. → were</li>
<li>I would buy a car if I ( ) enough money. → had</li>
<li>If she ( ) here, she would help us. → were</li>
<li>We could win if we ( ) harder. → tried</li>
<li>If I ( ) a bird, I would fly to you. → were</li>
<li>He would pass if he ( ) more. → studied</li>
<li>What would you do if you ( ) a million dollars? → had</li>
<li>If I ( ) time, I would go with you. → had</li>
<li>She would be happy if she ( ) him. → met</li>
<li>If it ( ) not raining, we could go out. → were</li>
<li>I would travel if I ( ) more money. → had</li>
<li>If I ( ) you, I would say sorry. → were</li>
<li>He could win if he ( ) harder. → tried</li>
<li>If they ( ) here, they would help us. → were</li>
<li>I would be surprised if she ( ) come. → came</li>
<li>If I ( ) his number, I would call him. → had</li>
<li>She could do it if she ( ) to. → tried</li>
<li>If I ( ) taller, I would play basketball. → were</li>
<li>We would go if it ( ) not so cold. → were</li>
</ol>
<h2>仮定法 英作文練習（5問）</h2>
<ol>
<li>もし私があなたなら、もっと勉強するのに。 → If I were you, I would study harder.</li>
<li>もしお金があれば、車を買うのに。 → If I had money, I would buy a car.</li>
<li>もし晴れなら、出かけられるのに。 → If it were sunny, we could go out.</li>
<li>もし時間があれば、あなたと行くのに。 → If I had time, I would go with you.</li>
<li>もし彼女に会えれば嬉しいのに。 → I would be happy if I could meet her.</li>
</ol>
""",
}

for fname, extra in EXTRAS.items():
    thicken(fname, extra)

print("=== 残り14記事の追加拡充が完了しました ===")