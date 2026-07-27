#!/usr/bin/env python3
"""最終厚書: suryo(数量詞), kansi(冠詞), zensi(前置詞) を拡張"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    pos = content.rfind("</article>")
    if pos == -1:
        print(f"  SKIP {filename}")
        return
    lc = content.count("\n")
    if lc > 200:
        print(f"  SKIP {filename}: already {lc}")
        return
    new = content[:pos] + extra + "\n" + content[pos:]
    with open(path, "w") as f:
        f.write(new)
    print(f"  {filename}: {lc} -> {new.count(chr(10))}")

# === suryo.html（数量詞） ===
suryo = """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">There are many books on the desk.</span> <span class="example-jp">（机の上にたくさんの本がある）</span></li>
  <li><span class="example">I have some money.</span> <span class="example-jp">（いくらかお金を持っている）</span></li>
  <li><span class="example">There is little water in the glass.</span> <span class="example-jp">（コップに水がほとんどない）</span></li>
  <li><span class="example">She has few friends.</span> <span class="example-jp">（彼女には友達がほとんどいない）</span></li>
  <li><span class="example">I have a lot of homework.</span> <span class="example-jp">（たくさん宿題がある）</span></li>
</ul>
<div class="tip-box"><h3>💡 many / much / a lot of の使い分け</h3><p><strong>many</strong> = 可算名詞（数えられるもの）に使う。many books, many students<br><strong>much</strong> = 不可算名詞（数えられないもの）に使う。much water, much money<br><strong>a lot of</strong> = 両方に使える。カジュアルな表現。</p></div>
<div class="tip-box"><h3>💡 few / a few / little / a little の違い</h3><p><strong>few</strong> = 「ほとんどない」（否定的、可算名詞）<br><strong>a few</strong> = 「いくつかある」（肯定的、可算名詞）<br><strong>little</strong> = 「ほとんどない」（否定的、不可算名詞）<br><strong>a little</strong> = 「少しある」（肯定的、不可算名詞）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「many water」</strong> → water は不可算名詞なので much または a lot of を使う。</li>
  <li><strong>「few と a few の混同」</strong> → few = ほとんどない（否定）、a few = いくつかある（肯定）。</li>
  <li><strong>「much books」</strong> → books は可算名詞なので many を使う。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/be.html">練習問題を解く</a> か <a href="../test/be_test.html">確認テストに挑戦</a> しよう。</p></div>
"""

# === kansi.html（冠詞） ===
kansi = """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I have a cat. The cat is cute.</span> <span class="example-jp">（猫を飼っています。その猫はかわいいです）</span></li>
  <li><span class="example">She is an honest girl.</span> <span class="example-jp">（彼女は正直な女の子です）</span></li>
  <li><span class="example">The sun rises in the east.</span> <span class="example-jp">（太陽は東から昇る）</span></li>
  <li><span class="example">I play the piano.</span> <span class="example-jp">（ピアノを弾きます）</span></li>
  <li><span class="example">She goes to school by bus.</span> <span class="example-jp">（彼女はバスで学校に行きます）</span></li>
</ul>
<div class="tip-box"><h3>💡 a / an / the のルール</h3><p><strong>a</strong> = 子音の前（a book, a university ← 「ユ」は子音）<br><strong>an</strong> = 母音の前（an apple, an hour ← h が発音されない）<br><strong>a/an</strong> = 不特定（初めて出てくるもの）<br><strong>the</strong> = 特定（すでに話題に出たもの、唯一のもの）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「a apple」</strong> → apple は母音で始まるので an が正解。「an apple」。</li>
  <li><strong>「a hour」</strong> → hour は h が発音されないので母音扱い。「an hour」。</li>
  <li><strong>無冠詞でいいのに the をつける</strong> → 固有名詞（Tokyo, Japan）、曜日、言語（English）には基本的に冠詞不要。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/be.html">練習問題を解く</a> か <a href="../test/be_test.html">確認テストに挑戦</a> しよう。</p></div>
"""

# === zensi.html（前置詞） ===
zensi = """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">The cat is on the desk.</span> <span class="example-jp">（猫は机の上にいる）</span></li>
  <li><span class="example">She is in the classroom.</span> <span class="example-jp">（彼女は教室の中にいる）</span></li>
  <li><span class="example">The bank is between the post office and the hospital.</span> <span class="example-jp">（銀行は郵便局と病院の間にある）</span></li>
  <li><span class="example">I go to school by bus.</span> <span class="example-jp">（バスで学校に行く）</span></li>
  <li><span class="example">He is good at math.</span> <span class="example-jp">（彼は数学が得意です）</span></li>
</ul>
<div class="tip-box"><h3>💡 場所の前置詞まとめ</h3><p><strong>in</strong> = 〜の中に / <strong>on</strong> = 〜の上に（接触） / <strong>at</strong> = 〜の地点で（点）<br><strong>under</strong> = 〜の下に / <strong>by</strong> = 〜のそばに / <strong>between</strong> = 〜の間に（2つ）<br><strong>near</strong> = 〜の近くに / <strong>in front of</strong> = 〜の前に</p></div>
<div class="tip-box"><h3>💡 時間の前置詞まとめ</h3><p><strong>at</strong> = 時刻（at 7 o'clock） / <strong>in</strong> = 月・年・季節（in May）<br><strong>on</strong> = 曜日・日付（on Monday） / <strong>by</strong> = 〜までに<br><strong>for</strong> = 期間 / <strong>since</strong> = 起点</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「in the morning」と「on Monday morning」の使い分け</strong> → 曜日がつくときは on、そうでなければ in。</li>
  <li><strong>「at night」は慣用表現</strong> → in the night ではなく at night。</li>
  <li><strong>「by bus」に冠詞をつけない</strong> → by bus / by train / by car は無冠詞。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/be.html">練習問題を解く</a> か <a href="../test/be_test.html">確認テストに挑戦</a> しよう。</p></div>
"""

if __name__ == "__main__":
    print("=== 最終厚書 ===")
    thicken("suryo.html", suryo)
    thicken("kansi.html", kansi)
    thicken("zensi.html", zensi)
    print("=== 完了 ===")