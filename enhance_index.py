#!/usr/bin/env python3
"""index.htmlとguide/ページを拡充"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def inject_before(filename, marker, content, folder="."):
    path = os.path.join(BASE, folder, filename)
    with open(path, "r") as f:
        text = f.read()
    pos = text.find(marker)
    if pos == -1:
        print(f"  SKIP {folder}/{filename}: marker not found")
        return
    before = text[:pos]
    after = text[pos:]
    new = before + content + "\n" + after
    with open(path, "w") as f:
        f.write(new)
    print(f"  OK {folder}/{filename} ({text.count(chr(10))} -> {new.count(chr(10))} lines)")

# index.html に学習の流れセクションを追加
inject_before("index.html", '<footer class="footer">', """
<section class="page-section" id="how-to-study">
  <div class="container" style="text-align: left;">
    <h2>📖 学習の進め方</h2>
    <div class="step-box" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
      <div class="grammar-card" style="padding: 16px;">
        <h3>ステップ1 🎯</h3>
        <p><strong>文法解説を読む</strong><br>各単元の解説ページで基本ルールを理解しましょう。公式・表・例文でわかりやすく解説しています。</p>
      </div>
      <div class="grammar-card" style="padding: 16px;">
        <h3>ステップ2 ✏️</h3>
        <p><strong>練習問題を解く</strong><br>文法解説で理解した後は、練習問題で実践。全問正解できるまで繰り返しましょう。</p>
      </div>
      <div class="grammar-card" style="padding: 16px;">
        <h3>ステップ3 📝</h3>
        <p><strong>確認テストに挑戦</strong><br>制限時間5分のテストで実力をチェック。満点を目指しましょう！</p>
      </div>
      <div class="grammar-card" style="padding: 16px;">
        <h3>ステップ4 🔄</h3>
        <p><strong>復習を忘れずに</strong><br>翌日・1週間後・1ヶ月後に復習すると、長期記憶に定着します。</p>
      </div>
    </div>
  </div>
</section>
""")

# guide/ ページの拡充
for guide_file, extra_content in [
    ("how-to-study.html", """
<h2>中学英語をマスターするための年間計画</h2>
<table><tr><th>学年</th><th>学習内容</th><th>目標</th></tr>
<tr><td>中学1年</td><td>be動詞、一般動詞、疑問文、否定文、命令文、三人称単数、現在進行形、can、過去形、名詞の複数形、代名詞</td><td>英語の基礎を固める。簡単な日常会話ができる。</td></tr>
<tr><td>中学2年</td><td>未来形、動名詞、不定詞、助動詞、比較、受け身、接続詞、there is構文、前置詞</td><td>中間レベルの文法をマスター。自分の意見を言える。</td></tr>
<tr><td>中学3年</td><td>現在完了、現在完了進行形、関係代名詞、間接疑問、仮定法、分詞、不定詞（応用）、原形不定詞</td><td>高校入試に対応できる実力をつける。長文読解ができる。</td></tr>
</table>
<h2>1週間の学習スケジュール例</h2>
<table><tr><th>曜日</th><th>学習内容</th><th>時間</th></tr>
<tr><td>月曜日</td><td>新しい文法単元を1つ学ぶ</td><td>30分</td></tr>
<tr><td>火曜日</td><td>練習問題を解く・間違えた問題を復習</td><td>20分</td></tr>
<tr><td>水曜日</td><td>確認テストに挑戦</td><td>15分</td></tr>
<tr><td>木曜日</td><td>英単語を20語覚える</td><td>15分</td></tr>
<tr><td>金曜日</td><td>今週学んだ文法を復習</td><td>20分</td></tr>
<tr><td>土曜日</td><td>リスニング練習・英作文練習</td><td>30分</td></tr>
<tr><td>日曜日</td><td>今週の総復習・苦手分野の克服</td><td>30分</td></tr>
</table>
<h2>よくある学習の悩みと解決策</h2>
<div class="grammar-grid"><div class="grammar-card"><h3>❓ 単語が覚えられない</h3><p>→ 1日10語ずつ、例文ごと覚えましょう。単語帳アプリも活用して隙間時間に繰り返し見ることが大切です。</p></div>
<div class="grammar-card"><h3>❓ 文法が難しい</h3><p>→ まずは基本ルールをしっかり理解しましょう。このサイトの解説を読んでから練習問題を解くと効果的です。</p></div>
<div class="grammar-card"><h3>❓ リスニングが聞き取れない</h3><p>→ スピードを遅くして聞くことから始めましょう。シャドーイング練習もおすすめです。</p></div>
<div class="grammar-card"><h3>❓ 長文読解が苦手</h3><p>→ 設問から先に読んで、何を聞かれているか把握してから本文を読みましょう。</p></div></div>
"""),
    ("pronunciation.html", """
<h2>英語の発音ルール 基本8つ</h2>
<p>発音をマスターすると、リスニング力とスピーキング力が劇的に向上します。</p>
<h3>1. 母音（a, e, i, o, u）の発音</h3>
<table><tr><th>文字</th><th>短母音</th><th>長母音</th><th>例</th></tr>
<tr><td>a</td><td>ア（cat）</td><td>エイ（cake）</td><td>cat / cake</td></tr>
<tr><td>e</td><td>エ（bed）</td><td>イー（bee）</td><td>bed / bee</td></tr>
<tr><td>i</td><td>イ（big）</td><td>アイ（bike）</td><td>big / bike</td></tr>
<tr><td>o</td><td>オ（hot）</td><td>オウ（home）</td><td>hot / home</td></tr>
<tr><td>u</td><td>ア（cut）</td><td>ユー（cute）</td><td>cut / cute</td></tr>
</table>
<h3>2. 子音の発音で気をつけるポイント</h3>
<ul><li><strong>th [θ] [ð]</strong>：舌を前歯の間に挟んで発音（think, this）</li>
<li><strong>r [r]</strong>：舌を上あごに近づけて発音（red, run）※日本語の「ラ行」ではない</li>
<li><strong>l [l]</strong>：舌を上あごの前につけて発音（like, light）</li>
<li><strong>v [v]</strong>：下唇を上の歯に当てて発音（very, live）※日本語の「バ行」ではない</li>
<li><strong>f [f]</strong>：下唇を上の歯に当てて息だけ出す（fine, funny）</li>
<li><strong>sh [ʃ]</strong>：唇を丸くして発音（she, fish）</li>
<li><strong>ch [tʃ]</strong>：チュッと発音（child, watch）</li>
</ul>
<h3>3. アクセントのルール</h3>
<p><strong>名詞と動詞でアクセントが変わる単語</strong></p>
<table><tr><th>単語</th><th>名詞</th><th>動詞</th></tr>
<tr><td>record</td><td>RE-cord（記録）</td><td>re-CORD（記録する）</td></tr>
<tr><td>present</td><td>PRE-sent（プレゼント）</td><td>pre-SENT（発表する）</td></tr>
<tr><td>import</td><td>IM-port（輸入品）</td><td>im-PORT（輸入する）</td></tr>
</table>
<h3>4. リンキング（音のつながり）</h3>
<p>英語では単語と単語の音がつながることがよくあります。</p>
<ul><li>get up → ゲﾄｩｯﾌﾟ（getのtがupのuにつながる）</li>
<li>not at all → ノﾀﾄｫｰﾙ（tがaにつながる）</li>
<li>I am → アイマム（Iとamがつながる）</li>
<li>what is → ワティズ（tがiにつながる）</li>
<li>good idea → グダイディア（dがiにつながる）</li>
</ul>
""")
]:
    inject_before(guide_file, '<footer class="footer">', extra_content, "guide")

print("=== index.htmlとguide/の拡充完了 ===")