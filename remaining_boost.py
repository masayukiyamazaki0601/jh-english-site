#!/usr/bin/env python3
"""残り200行未満の3記事（genkan1, kankeisi1, genkeiFuteisi）を拡充"""
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

thicken("genkan1.html", """
<h2>現在完了（継続）の重要パターンまとめ</h2>
<p><strong>公式1：for + 期間</strong>（数字が入る）<br>
例：for three years, for two hours, for a long time, for five days</p>
<p><strong>公式2：since + 時点</strong>（具体的な時）<br>
例：since 2020, since last year, since Monday, since I was born</p>
<p><strong>公式3：How long + 現在完了？</strong>（期間を尋ねる）<br>
例：How long have you lived here?</p>
<h2>現在完了（継続）のテスト対策 追加問題（10問）</h2>
<ol>
<li>I have lived here ( ) 2018. → since</li>
<li>She has studied English ( ) three years. → for</li>
<li>I have known him ( ) childhood. → since</li>
<li>He has been sick ( ) last Monday. → since</li>
<li>They have been married ( ) 10 years. → for</li>
<li>How long have you ( ) in Tokyo? → lived</li>
<li>She has ( ) a teacher since 2020. → been</li>
<li>I have ( ) seen him since last week. → not</li>
<li>We ( ) known each other since elementary school. → have</li>
<li>He has worked here ( ) April. → since</li>
</ol>
<h2>現在完了（継続）のよくある間違い</h2>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have went to Tokyo.」</strong> → 過去分詞は gone。「I have gone to Tokyo.」または「I have been to Tokyo.」</li>
  <li><strong>「I have lived here since five years.」</strong> → since + 時点。「for five years」が正解。</li>
  <li><strong>「I lived here for 5 years.」で今も住んでいることを表す</strong> → 過去形は「もう住んでいない」意味になる。現在完了「I have lived here for 5 years.」を使う。</li>
  <li><strong>「for」と「since」の混同</strong> → for = 数字が入る、since = 時点。これがテストの鉄則！</li>
</ul></div>
""")

thicken("kankeisi1.html", """
<h2>関係代名詞 重要ポイント：前置詞 + 関係代名詞</h2>
<p>高校レベルの発展内容ですが、余裕がある人は覚えておきましょう。</p>
<ul>
<li><strong>The man about whom we talked</strong> → 私たちが話した男性（フォーマル）</li>
<li><strong>The man (who) we talked about</strong> → 私たちが話した男性（日常会話）</li>
<li><strong>The house in which I lived</strong> → 私が住んでいた家（フォーマル）</li>
<li><strong>The house (which) I lived in</strong> → 私が住んでいた家（日常会話）</li>
</ul>
<h2>関係代名詞 that しか使えない場合</h2>
<table>
<tr><th>状況</th><th>例</th><th>理由</th></tr>
<tr><td>先行詞に最上級</td><td>This is the best movie that I've seen.</td><td>最上級の後は that</td></tr>
<tr><td>先行詞に all/every</td><td>All that I have is yours.</td><td>all の後は that</td></tr>
<tr><td>先行詞に only</td><td>He is the only person that I can trust.</td><td>only の後は that</td></tr>
<tr><td>人と物が混在</td><td>I remember the people and the places that I visited.</td><td>混在時は that</td></tr>
</table>
<h2>関係代名詞 よくある間違い</h2>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「The boy who he is running.」</strong> → 関係代名詞のあとに同じ先行詞（he）を繰り返さない。</li>
  <li><strong>「The man who I met him yesterday.」</strong> → 目的格の先行詞を繰り返さない。</li>
  <li><strong>人に which を使ってしまう</strong> → 人には who/that。which は物・動物。</li>
  <li><strong>主格と目的格の語順を混同</strong> → 主格: who + 動詞、目的格: who + 主語 + 動詞</li>
</ul></div>
""")

thicken("genkeiFuteisi.html", """
<h2>原形不定詞 よく出るテスト問題（追加10問）</h2>
<ol>
<li>I ( ) him cross the street. → saw</li>
<li>She ( ) me clean the room. → made</li>
<li>Let's ( ) to the park. → go</li>
<li>I ( ) her sing a beautiful song. → heard</li>
<li>My father ( ) me wash the car. → had</li>
<li>We ( ) the sun set. → watched</li>
<li>He ( ) me carry the box. → helped</li>
<li>I ( ) something touch my shoulder. → felt</li>
<li>She ( ) me use her phone. → let</li>
<li>The teacher ( ) us rewrite the essay. → made</li>
</ol>
<h2>原形不定詞の見分け方（クイックガイド）</h2>
<p><strong>公式1：see / hear / watch + 目的語 + 動詞の原形</strong> → 「〜が…するのを見る/聞く」</p>
<p><strong>公式2：make / let / have + 目的語 + 動詞の原形</strong> → 「〜に…させる」</p>
<p><strong>公式3：help + 目的語 + (to) + 動詞の原形</strong> → 「〜が…するのを手伝う」（to はあってもなくてもOK）</p>
<h2>原形不定詞 vs 現在分詞（-ing）の違い</h2>
<table>
<tr><th>構文</th><th>意味</th><th>ニュアンスの違い</th></tr>
<tr><td>I saw him run.</td><td>彼が走るのを見た</td><td>走るのを最後まで見た（動作の完了）</td></tr>
<tr><td>I saw him running.</td><td>彼が走っているのを見た</td><td>走っているところを目撃した（動作の途中）</td></tr>
<tr><td>I heard her sing.</td><td>彼女が歌うのを聞いた</td><td>歌を最後まで聞いた</td></tr>
<tr><td>I heard her singing.</td><td>彼女が歌っているのを聞いた</td><td>歌っている最中を聞いた</td></tr>
</table>
<div class="tip-box"><h3>💡 覚え方のコツ</h3><p>原形不定詞 = 動作の「全体・完了」を表す<br>現在分詞 = 動作の「途中・一部分」を表す</p></div>
<h2>原形不定詞 よくある間違い</h2>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I saw him to run.」</strong> → 知覚動詞のあとは to をつけない。「I saw him run.」</li>
  <li><strong>「I made him to clean.」</strong> → 使役動詞のあとも to 不要。「I made him clean.」</li>
  <li><strong>「Let's going.」</strong> → Let's のあとは動詞の原形。「Let's go.」</li>
  <li><strong>「He helped me to carried.」</strong> → 動詞は原形。「He helped me carry / to carry.」</li>
</ul></div>
""")

# さらにその他200〜210行台の記事も追加拡充
thicken("kansetu.html", """
<h2>間接疑問 テスト対策 追加問題（10問）</h2>
<ol>
<li>Do you know where she ( )? (live) → lives</li>
<li>I don't know what this ( ). (be) → is</li>
<li>Can you tell me when the store ( )? (open) → opens</li>
<li>I wonder ( ) he is honest. → if / whether</li>
<li>Do you know ( ) she will come? → if / whether</li>
<li>Please tell me how I ( ) get there. → can</li>
<li>I know ( ) she is. → who</li>
<li>Do you know how much it ( )? (cost) → costs</li>
<li>I'm not sure if he ( ) come. → will</li>
<li>Can you tell me what time it ( )? → is</li>
</ol>
<h2>間接疑問 英作文（5問）</h2>
<ol>
<li>彼がどこに住んでいるか知っていますか？ → Do you know where he lives?</li>
<li>これが何かわかりません。 → I don't know what this is.</li>
<li>駅への行き方を教えてくれますか？ → Can you tell me how to get to the station?</li>
<li>彼が親切かどうか疑問だ。 → I wonder if he is kind.</li>
<li>彼女が誰か知っています。 → I know who she is.</li>
</ol>
""")

thicken("kakosin.html", """
<h2>過去進行形 テスト対策 追加問題（10問）</h2>
<ol>
<li>I ( ) reading a book at 8pm. → was</li>
<li>They ( ) playing soccer yesterday. → were</li>
<li>She ( ) cooking dinner at that time. → was</li>
<li>( ) you studying at midnight? → Were</li>
<li>He ( ) not sleeping at that time. → was</li>
<li>What ( ) you doing then? → were</li>
<li>We ( ) watching TV when you called. → were</li>
<li>I ( ) taking a bath when the phone rang. → was</li>
<li>While I ( ) studying, my friend came. → was</li>
<li>It ( ) raining when I left home. → was</li>
</ol>
<h2>過去形 vs 過去進行形 比較問題（5問）</h2>
<ol>
<li>I (read) a book yesterday. → read（読み終えた）</li>
<li>I (read) a book at 8pm yesterday. → was reading（読んでいる途中）</li>
<li>She (call) me last night. → called（電話がかかってきた）</li>
<li>She (call) me when I was studying. → was calling（電話をかけていた）</li>
<li>We (have) dinner when the earthquake happened. → were having（食事中だった）</li>
</ol>
""")

thicken("jyodosi.html", """
<h2>助動詞 テスト対策 追加問題（10問）</h2>
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
</ol>
<h2>助動詞 意味の強さ比較</h2>
<table>
<tr><th>強さ</th><th>助動詞</th><th>意味</th><th>例</th></tr>
<tr><td>最強</td><td>must</td><td>〜しなければならない</td><td>You must stop.</td></tr>
<tr><td>強</td><td>have to</td><td>〜しなければならない</td><td>I have to go.</td></tr>
<tr><td>中</td><td>should</td><td>〜すべきだ</td><td>You should try.</td></tr>
<tr><td>弱</td><td>may</td><td>〜してもよい</td><td>You may go.</td></tr>
<tr><td>最弱</td><td>can</td><td>〜できる</td><td>I can help.</td></tr>
</table>
""")

thicken("ukemi.html", """
<h2>受け身 テスト対策 追加問題（10問）</h2>
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
</ol>
<h2>能動態 → 受動態 書き換え（5問）</h2>
<ol>
<li>The boy broke the window. → The window was broken by the boy.</li>
<li>My mother made this cake. → This cake was made by my mother.</li>
<li>Many people speak English. → English is spoken by many people.</li>
<li>He cleans the room every day. → The room is cleaned every day.</li>
<li>She wrote this letter. → This letter was written by her.</li>
</ol>
""")

thicken("doumei.html", """
<h2>動名詞 テスト対策 追加問題（10問）</h2>
<ol>
<li>I like ( ). (swim) → swimming</li>
<li>Playing tennis ( ) fun. → is</li>
<li>He enjoys ( ) books. (read) → reading</li>
<li>I finished ( ) my homework. (do) → doing</li>
<li>She is good at ( ). (sing) → singing</li>
<li>I stopped ( ). (smoke) → smoking</li>
<li>She is interested in ( ) history. (study) → studying</li>
<li>I'm tired of ( ) for the bus. (wait) → waiting</li>
<li>I look forward to ( ) you. (see) → seeing</li>
<li>He gave up ( ) soccer. (play) → playing</li>
</ol>
<h2>動名詞 vs 不定詞 暗記リスト（完全版）</h2>
<p><strong>動名詞のみ：</strong> enjoy, finish, stop, quit, give up, avoid, miss, practice, suggest, consider, imagine, mind, keep, put off</p>
<p><strong>不定詞のみ：</strong> want, hope, wish, decide, plan, expect, promise, refuse, learn, fail, manage, offer, afford</p>
<p><strong>両方可（意味はほぼ同じ）：</strong> like, love, hate, prefer, start, begin, continue</p>
<p><strong>両方可（意味が変わる）：</strong> stop, remember, forget, try</p>
""")

thicken("bekako.html", """
<h2>be動詞の過去形 テスト対策 追加問題（10問）</h2>
<ol>
<li>I ( ) happy yesterday. → was</li>
<li>They ( ) at home last night. → were</li>
<li>She ( ) busy yesterday. → was</li>
<li>We ( ) in the park last Sunday. → were</li>
<li>He ( ) sick yesterday. → was</li>
<li>I ( ) not at home yesterday. → was</li>
<li>She ( ) not tired. → was</li>
<li>They ( ) not at school. → were</li>
<li>( ) you tired? → Were</li>
<li>( ) she at the party? → Was</li>
</ol>
<h2>There was / There were の過去形（5問）</h2>
<ol>
<li>There ( ) a cat on the chair. → was</li>
<li>There ( ) many people at the party. → were</li>
<li>( ) there a phone call for me? → Was</li>
<li>( ) there any problems? → Were</li>
<li>There ( ) not enough chairs. → were</li>
</ol>
""")

print("=== 全記事の完全拡充が完了しました ===")