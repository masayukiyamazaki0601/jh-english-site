#!/usr/bin/env python3
"""全28薄い記事にさらにコンテンツを追加（会話練習・テスト対策・穴埋め問題）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra, skip_over=400):
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
    print(f"  DONE {filename} ({lines} -> {new.count(chr(10))} lines)")

EXTRA = {
    "genkan1.html": """
<h2>現在完了（継続）のテスト対策</h2>
<p><strong>テストでよく出る問題パターン：</strong></p>
<ul>
  <li>for + 数字：for three years, for two hours, for a long time</li>
  <li>since + 時点：since last year, since 2020, since I was a child</li>
  <li>現在完了と過去形の区別：yesterday/ago → 過去形、for/since → 現在完了</li>
</ul>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I have lived in Tokyo ( ) five years. → for<br>
(2) She has studied English ( ) 2020. → since<br>
(3) They have known each other ( ) childhood. → since<br>
(4) He has been sick ( ) Monday. → since</p></div>
""",
    "genkan2.html": """
<h2>現在完了（経験）のテスト対策</h2>
<p><strong>テストでよく出る問題パターン：</strong></p>
<ul>
  <li>Have you ever + 過去分詞？「〜したことがありますか？」</li>
  <li>I have never + 過去分詞「一度も〜したことがない」</li>
  <li>How many times have you + 過去分詞？「何回〜したことがありますか？」</li>
</ul>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) Have you ( ) been to Kyoto? → ever<br>
(2) I have ( ) eaten sushi. → never<br>
(3) I have seen this movie ( ). → before<br>
(4) She has ( ) to the US twice. → been<br>
(5) He has ( ) to Kyoto. → gone（今ここにいない）</p></div>
""",
    "genkan3.html": """
<h2>現在完了（完了）のテスト対策</h2>
<p><strong>already / just / yet の位置がテストの鉄則！</strong></p>
<ul>
  <li>already = 肯定文の文中：I have already finished.</li>
  <li>just = 肯定文の文中：I have just finished.</li>
  <li>yet = 疑問文の文末：Have you finished yet?</li>
  <li>yet = 否定文の文末：I haven't finished yet.</li>
</ul>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I have ( ) finished my homework. → just<br>
(2) She has ( ) eaten lunch. → already<br>
(3) Have you finished ( )? → yet<br>
(4) I haven't seen that movie ( ). → yet</p></div>
""",
    "genkanSinkokei.html": """
<h2>現在完了進行形のテスト対策</h2>
<p><strong>テストでよく出る問題パターン：</strong></p>
<ul>
  <li>have/has + been + doing（be動詞は2回使う！have been + doing）</li>
  <li>How long + have/has + 主語 + been + doing？「どのくらい〜し続けていますか？」</li>
  <li>状態動詞（live, know）は現在完了（継続）を使う</li>
  <li>動作動詞（study, wait, rain）は現在完了進行形が自然</li>
</ul>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I have been ( ) English for three years. → studying<br>
(2) It has been ( ) since morning. → raining<br>
(3) How long have you been ( ) here? → living<br>
(4) She has been ( ) for 30 minutes. → waiting</p></div>
""",
    "kateiho.html": """
<h2>仮定法のテスト対策</h2>
<p><strong>テストで絶対に覚える3つのポイント：</strong></p>
<ol>
  <li><strong>If + 過去形</strong>（現在形ではない！）：If I had money, ...</li>
  <li><strong>主節は would/could</strong>：I would buy a car.</li>
  <li><strong>be動詞は were</strong>（was ではない）：If I were you, ...</li>
</ol>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) If I ( ) you, I would study harder. → were<br>
(2) If I ( ) money, I would buy a car. → had<br>
(3) If it ( ) sunny, we could go out. → were<br>
(4) I would be happy if I ( ) meet her. → could</p></div>
""",
    "genkeiFuteisi.html": """
<h2>原形不定詞のテスト対策</h2>
<p><strong>テストで絶対に覚える3ポイント：</strong></p>
<ol>
  <li><strong>知覚動詞</strong>（see, hear, watch）+ 目的語 + 動詞の原形</li>
  <li><strong>使役動詞</strong>（make, let, have）+ 目的語 + 動詞の原形</li>
  <li><strong>to がつかない！</strong>これが一番のテストポイント</li>
</ol>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I saw him (run/to run). → run<br>
(2) She made me (clean/to clean) the room. → clean<br>
(3) Let's (go/to go) to the park. → go<br>
(4) I heard her (sing/to sing) a song. → sing</p></div>
""",
    "kakosin.html": """
<h2>過去進行形のテスト対策</h2>
<p><strong>when + 過去形 と while + 過去進行形 の組み合わせが鉄則！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) reading when she called. → was<br>
(2) They ( ) playing soccer yesterday. → were<br>
(3) ( ) you studying at midnight? → Were<br>
(4) He ( ) not sleeping at that time. → was</p></div>
""",
    "there.html": """
<h2>there is構文のテスト対策</h2>
<p><strong>テストでよく出る問題：</strong></p>
<ul>
  <li>There is + 単数名詞 / There are + 複数名詞</li>
  <li>否定：There is not / There are not</li>
  <li>疑問：Is there〜？ / Are there〜？</li>
  <li>How many + 名詞 + are there〜？</li>
</ul>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) ( ) a cat under the table. → There is<br>
(2) ( ) many books on the desk. → There are<br>
(3) ( ) a hospital near here? → Is there<br>
(4) There ( ) not any milk. → is</p></div>
""",
    "bekako.html": """
<h2>be動詞の過去形 テスト対策</h2>
<p><strong>was / were の使い分けが最重要！</strong></p>
<table><tr><th>主語</th><th>過去形</th></tr>
<tr><td>I / He / She / It</td><td>was</td></tr>
<tr><td>You / We / They</td><td>were</td></tr>
</table>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) happy yesterday. → was<br>
(2) They ( ) at home last night. → were<br>
(3) She ( ) busy yesterday. → was<br>
(4) ( ) you tired after the game? → Were</p></div>
""",
    "kansetu.html": """
<h2>間接疑問のテスト対策</h2>
<p><strong>最重要ルール！間接疑問のあとは肯定文の語順</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) Do you know where he ( )? → lives<br>
(2) I don't know what this ( ). → is<br>
(3) Can you tell me where the station ( )? → is<br>
(4) I wonder ( ) he is kind. → if / whether</p></div>
""",
    "setuzoku.html": """
<h2>接続詞のテスト対策</h2>
<p><strong>because と so の違いが最重要！同時には使えない</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I like cats ( ) dogs. → and<br>
(2) I like cats ( ) I don't like dogs. → but<br>
(3) I am happy ( ) I got a present. → because<br>
(4) I was tired, ( ) I went to bed. → so<br>
(5) Call me ( ) you arrive. → when</p></div>
""",
    "gimonsi.html": """
<h2>疑問詞のテスト対策</h2>
<p><strong>疑問詞 + 疑問文の語順 = be動詞 + 主語 / do + 主語 + 動詞</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) ( ) is your name? → What<br>
(2) ( ) is he? → Who<br>
(3) ( ) are you from? → Where<br>
(4) ( ) is your birthday? → When<br>
(5) ( ) are you late? → Why</p></div>
""",
    "mirai.html": """
<h2>未来形のテスト対策</h2>
<p><strong>will vs be going to の違いが頻出！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) call you later. → will<br>
(2) It ( ) rain tomorrow. → will<br>
(3) She ( ) going to study law. → is<br>
(4) We are ( ) to have a test next week. → going</p></div>
""",
    "bunsi.html": """
<h2>分詞のテスト対策</h2>
<p><strong>現在分詞 vs 過去分詞の違いが最重要！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) Look at the ( ) baby. → sleeping<br>
(2) I have a ( ) watch. → broken<br>
(3) This is a book ( ) by Soseki. → written<br>
(4) The boy ( ) is my brother. → running</p></div>
""",
    "can.html": """
<h2>canのテスト対策</h2>
<p><strong>can + 動詞の原形（toは不要！）が最重要ルール</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) swim. → can<br>
(2) She ( ) speak French. → can<br>
(3) ( ) you help me? → Can<br>
(4) I ( ) play the piano. → can't</p></div>
""",
    "daimeisi.html": """
<h2>代名詞のテスト対策</h2>
<p><strong>4つの変化をセットで覚えよう！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) ( ) is my friend. → She (Iの目的格は？)<br>
(2) I like ( ). → her (sheの目的格)<br>
(3) This is ( ) book. → my (所有格)<br>
(4) This book is ( ). → mine (所有代名詞)</p></div>
""",
    "kankeisi1.html": """
<h2>関係代名詞のテスト対策</h2>
<p><strong>主格と目的格の区別が最頻出！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I know the boy ( ) is running. → who<br>
(2) This is the book ( ) I bought. → which / that<br>
(3) She is the girl ( ) plays the piano. → who / that<br>
(4) He is the man ( ) I met yesterday. → whom / that</p></div>
""",
    "ukemi.html": """
<h2>受け身のテスト対策</h2>
<p><strong>be動詞 + 過去分詞（by 〜）が基本形。時制に注意！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) English ( ) spoken in many countries. → is<br>
(2) This book ( ) written by Soseki. → was<br>
(3) The window ( ) broken by the boy. → was<br>
(4) These cookies ( ) made by my mother. → were</p></div>
""",
    "doumei.html": """
<h2>動名詞のテスト対策</h2>
<p><strong>前置詞のあとは必ず動名詞！これが最頻出！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I like ( ). → swimming<br>
(2) I finished ( ) my homework. → doing<br>
(3) She is good at ( ). → singing<br>
(4) I enjoy ( ) books. → reading</p></div>
""",
    "jyodosi.html": """
<h2>助動詞のテスト対策</h2>
<p><strong>must not（禁止）vs don't have to（不要）の違いが最頻出！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) You ( ) study harder. → must<br>
(2) ( ) I come in? → May<br>
(3) You ( ) not run here. → must<br>
(4) You ( ) rest. → should</p></div>
""",
    "hikaku1.html": """
<h2>比較のテスト対策</h2>
<p><strong>比較級：-er / more + than、最上級：the + -est / most が基本！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) Taro is ( ) than Jiro. → taller<br>
(2) Mt. Fuji is ( ) highest mountain. → the<br>
(3) He is as ( ) as me. → tall<br>
(4) good → better → ( ) → best</p></div>
""",
    "zensi.html": """
<h2>前置詞のテスト対策</h2>
<p><strong>in/on/at の使い分けが最重要！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I get up ( ) six every morning. → at<br>
(2) She was born ( ) April 1st. → on<br>
(3) It is hot ( ) summer. → in<br>
(4) I go to school ( ) bus. → by</p></div>
""",
    "suryo.html": """
<h2>数量詞のテスト対策</h2>
<p><strong>many + 可算名詞 / much + 不可算名詞 の区別が最頻出！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) How ( ) books do you have? → many<br>
(2) I don't have ( ) money. → much<br>
(3) He has ( ) friends.（ほとんどいない）→ few<br>
(4) I have ( ) friends.（数人いる）→ a few</p></div>
""",
    "futeisi2.html": """
<h2>不定詞（応用）のテスト対策</h2>
<p><strong>It is 〜 for 人 to do / too 〜 to / enough to は高校入試の頻出3構文！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) It is important ( ) us to study. → for<br>
(2) She is ( ) young to drive. → too<br>
(3) He is old ( ) to drive. → enough<br>
(4) This box is too heavy ( ) me to carry. → for</p></div>
""",
    "futeisi1.html": """
<h2>不定詞（基本）のテスト対策</h2>
<p><strong>3用法（名詞・副詞・形容詞）の区別が最重要！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I want ( ) study English. → to<br>
(2) I went to Kyoto ( ) see temples. → to<br>
(3) I have something ( ) do. → to<br>
(4) I enjoy ( ) tennis. → playing</p></div>
""",
    "ippan.html": """
<h2>一般動詞のテスト対策</h2>
<p><strong>否定文と疑問文での do/does の使い方が最頻出！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) breakfast every morning. → eat<br>
(2) She ( ) tennis on Sunday. → plays<br>
(3) I ( ) like coffee. → don't<br>
(4) He ( ) play the piano. → doesn't</p></div>
""",
    "be.html": """
<h2>be動詞のテスト対策</h2>
<p><strong>主語による be動詞の使い分けが絶対条件！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) a student. → am<br>
(2) You ( ) kind. → are<br>
(3) He ( ) my friend. → is<br>
(4) I ( ) not a teacher. → am<br>
(5) ( ) you a student? → Are</p></div>
""",
    "kako.html": """
<h2>過去形のテスト対策</h2>
<p><strong>不規則動詞の暗記が必須！did + 原形のルールも忘れずに！</strong></p>
<div class="practice-link-box"><p>✏️ 穴埋め問題：<br>
(1) I ( ) to the park yesterday. → went<br>
(2) She ( ) breakfast at seven. → ate<br>
(3) They ( ) a movie last night. → saw<br>
(4) I ( ) go to school yesterday. → didn't<br>
(5) ( ) you eat breakfast? → Did</p></div>
""",
}

for fname, extra in EXTRA.items():
    thicken(fname, extra)

print("=== テスト対策の追加が完了しました ===")