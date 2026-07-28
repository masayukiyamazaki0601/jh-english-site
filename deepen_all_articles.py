#!/usr/bin/env python3
"""全28薄い記事に深掘り解説・追加例文・間違いポイントを追加（300行目標）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken_article(filename, extra_content, max_skip=200):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines > max_skip:
        print(f"  SKIP {filename} ({lines} lines, already thick)")
        return False
    insert_pos = content.rfind("</article>")
    if insert_pos == -1:
        print(f"  SKIP {filename}: no article tag")
        return False
    before = content[:insert_pos]
    after = content[insert_pos:]
    new_content = before + extra_content + "\n" + after
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  THICKENED {filename} ({lines} -> {new_content.count(chr(10))} lines)")
    return True

# === 各記事の追加深掘りコンテンツ ===
DEEPEN_CONTENT = {
    "be.html": """
<h2>実践会話で覚えるbe動詞</h2>
<p>be動詞は日常会話で最も頻繁に使われる動詞です。以下の会話を練習しましょう。</p>
<div class="highlight"><p>A: Hi! How are you?<br>B: I'm fine, thanks. How about you?<br>A: I'm good. Are you a student?<br>B: Yes, I am. I'm a junior high school student.</p></div>
<p><strong>会話のポイント：</strong></p>
<ul>
  <li>「How are you?」に対する答えは「I'm fine.」や「I'm good.」が一般的。</li>
  <li>「Are you 〜？」の質問には「Yes, I am. / No, I'm not.」で答える。</li>
  <li>I'm = I am の短縮形。会話では必ず短縮形を使う。</li>
</ul>
<h2>be動詞を使ったよくある表現</h2>
<table>
<tr><th>表現</th><th>意味</th><th>例文</th></tr>
<tr><td>be good at 〜</td><td>〜が得意だ</td><td>I am good at tennis.</td></tr>
<tr><td>be interested in 〜</td><td>〜に興味がある</td><td>She is interested in music.</td></tr>
<tr><td>be afraid of 〜</td><td>〜を怖がる</td><td>He is afraid of dogs.</td></tr>
<tr><td>be fond of 〜</td><td>〜が好きだ</td><td>We are fond of Japanese food.</td></tr>
<tr><td>be proud of 〜</td><td>〜を誇りに思う</td><td>I am proud of my sister.</td></tr>
</table>
""",
    "ippan.html": """
<h2>一般動詞の活用パターン</h2>
<p>一般動詞は主語と時制によって形が変わります。以下の3つのパターンを覚えましょう。</p>
<table>
<tr><th>時制</th><th>主語</th><th>動詞の形</th><th>例</th></tr>
<tr><td rowspan="2">現在形</td><td>I / You / We / They</td><td>原形</td><td>I play tennis.</td></tr>
<tr><td>He / She / It</td><td>原形 + s/es</td><td>She plays tennis.</td></tr>
<tr><td rowspan="2">過去形</td><td>すべての主語</td><td>過去形（-ed/不規則）</td><td>I played tennis.</td></tr>
<tr><td>（否定・疑問）</td><td>did + 原形</td><td>Did you play tennis?</td></tr>
<tr><td rowspan="2">未来形</td><td>すべての主語</td><td>will + 原形</td><td>I will play tennis.</td></tr>
<tr><td>すべての主語</td><td>be going to + 原形</td><td>I am going to play tennis.</td></tr>
</table>
<h2>よく使う一般動詞リスト（暗記推奨）</h2>
<table>
<tr><th>動詞</th><th>意味</th><th>例文</th></tr>
<tr><td>get</td><td>得る、着く</td><td>I get up at six.</td></tr>
<tr><td>take</td><td>取る、かかる</td><td>It takes 10 minutes.</td></tr>
<tr><td>give</td><td>与える</td><td>She gave me a present.</td></tr>
<tr><td>tell</td><td>伝える</td><td>Tell me the truth.</td></tr>
<tr><td>think</td><td>思う</td><td>I think so.</td></tr>
<tr><td>know</td><td>知っている</td><td>I know the answer.</td></tr>
<tr><td>live</td><td>住む</td><td>I live in Tokyo.</td></tr>
<tr><td>work</td><td>働く</td><td>My father works at a hospital.</td></tr>
</table>
""",
    "kako.html": """
<h2>不規則動詞の効果的な覚え方</h2>
<p>不規則動詞は「ABパターン」「ABCパターン」「AAAパターン」に分類すると覚えやすいです。</p>
<table>
<tr><th>パターン</th><th>原形</th><th>過去形</th><th>過去分詞</th><th>特徴</th></tr>
<tr><td rowspan="3">ABA型</td><td>come</td><td>came</td><td>come</td><td rowspan="3">過去分詞が原形と同じ</td></tr>
<tr><td>run</td><td>ran</td><td>run</td></tr>
<tr><td>become</td><td>became</td><td>become</td></tr>
<tr><td rowspan="3">ABC型</td><td>go</td><td>went</td><td>gone</td><td rowspan="3">3つとも形が違う</td></tr>
<tr><td>eat</td><td>ate</td><td>eaten</td></tr>
<tr><td>write</td><td>wrote</td><td>written</td></tr>
<tr><td rowspan="3">AAA型</td><td>put</td><td>put</td><td>put</td><td rowspan="3">全部同じ形</td></tr>
<tr><td>read</td><td>read</td><td>read</td></tr>
<tr><td>cut</td><td>cut</td><td>cut</td></tr>
</table>
<h2>過去形の時を表す表現</h2>
<ul>
  <li><strong>yesterday</strong>：I went to the park yesterday.</li>
  <li><strong>last night / last week / last year</strong>：I saw a movie last night.</li>
  <li><strong>〜 ago</strong>：I came to Japan two years ago.</li>
  <li><strong>this morning</strong>：I ate breakfast this morning.</li>
  <li><strong>when I was young</strong>：I played soccer when I was young.</li>
</ul>
<div class="note"><strong>注意！</strong> yesterday, last〜, 〜ago がある文は必ず過去形を使います。</div>
""",
    "can.html": """
<h2>can't の発音と使い方</h2>
<p>can の否定形は cannot（1語）または can't（短縮形）です。発音に注意しましょう。</p>
<ul>
  <li><strong>cannot</strong>：フォーマルな書き言葉で使う（I cannot swim.）</li>
  <li><strong>can't</strong>：会話で使う（I can't swim.）カントゥ /kænt/ と発音</li>
  <li><strong>can</strong>：肯定文では弱く発音（キャン /kən/）</li>
  <li><strong>can't</strong>：否定文では強く発音（カントゥ /kænt/）</li>
</ul>
<h2>can の過去形 could</h2>
<p>can の過去形は <strong>could</strong>（クドゥ）です。過去の能力を表します。</p>
<ul>
  <li><span class="example">I could swim when I was five.</span> <span class="example-jp">（5歳の時泳げました）</span></li>
  <li><span class="example">She could speak English when she was ten.</span> <span class="example-jp">（彼女は10歳の時英語を話せました）</span></li>
  <li><span class="example">I couldn't play the piano last year.</span> <span class="example-jp">（去年はピアノを弾けませんでした）</span></li>
</ul>
""",
}

for fname, extra in DEEPEN_CONTENT.items():
    thicken_article(fname, extra)

print("=== 深掘り解説の追加が完了しました ===")