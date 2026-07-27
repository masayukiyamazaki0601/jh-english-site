#!/usr/bin/env python3
"""主要3記事（不定詞・現在完了・関係代名詞）を教師品質に厚く書き換え"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def write_article(filename, title, grade, grade_class, html_content):
    header = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 中学英語学習サイト</title>
<meta name="description" content="中学英語の{title}をわかりやすく解説。肯定文・否定文・疑問文の作り方から応用まで完全網羅。練習問題と確認テストで実力チェック。">
<meta property="og:title" content="{title} | 中学英語学習サイト">
<meta property="og:type" content="article">
<meta property="og:locale" content="ja_JP">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="../index.html" class="header-logo">📚 中学英語<span>Lab</span></a>
    <nav class="header-nav">
      <a href="../index.html">ホーム</a>
      <a href="../index.html#grammar" class="active">文法解説</a>
      <a href="../practice/index.html">練習問題</a>
      <a href="../test/index.html">確認テスト</a>
    </nav>
    <div class="hamburger" onclick="document.getElementById('mobileNav').classList.toggle('open')">
      <span></span><span></span><span></span>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobileNav">
  <a href="../index.html">ホーム</a>
  <a href="../index.html#grammar">文法解説</a>
  <a href="../practice/index.html">練習問題</a>
  <a href="../test/index.html">確認テスト</a>
</div>
<div class="breadcrumb">
  <a href="../index.html">ホーム</a> > <a href="../index.html#grammar">文法解説</a> > {title}
</div>
<article class="grammar-detail">
  <span class="grade-badge badge {grade_class}">{grade}</span>
  <h1>{title}</h1>
  <p style="color: var(--gray-500); margin-bottom: 24px; font-size: 1.05rem;">
    {html_content.split('</h2>')[0].split('>')[-1] if '</h2>' in html_content else ''}
  </p>
  {html_content}
</article>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>
<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。英文法・練習問題・確認テストで英語力を確実にアップ。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a><a href="../grammar/genkan1.html">現在完了</a><a href="../grammar/kankeisi1.html">関係代名詞</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a><a href="../practice/futeisi.html">不定詞</a><a href="../practice/genkan.html">現在完了</a></div>
    <div><h3>確認テスト</h3><a href="../test/be_test.html">be動詞</a><a href="../test/futeisi_test.html">不定詞</a><a href="../test/genkan_test.html">現在完了</a></div>
    <div><h3>その他</h3><a href="../listening/index.html">リスニング</a><a href="../word/index.html">英単語帳</a><a href="../verb/index.html">不規則動詞</a><a href="../exam/index.html">入試対策</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "w") as f:
        f.write(header)
    print(f"  grammar/{filename}")

# === 不定詞（futeisi1.html） ===
write_article("futeisi1.html", "不定詞（3用法を完全マスター）", "中学2年", "g2", '''
<div class="tip-box">
  <h3>📑 このページで学ぶこと</h3>
  <ol style="margin:8px 0 0 20px;">
    <li>不定詞とは（to + 動詞の原形）</li>
    <li>名詞的用法（〜すること）</li>
    <li>副詞的用法（〜するために）</li>
    <li>形容詞的用法（〜するための）</li>
    <li>3用法の見分け方</li>
    <li>動名詞との違い</li>
    <li>よくある間違い</li>
  </ol>
</div>

<h2>1. 不定詞とは何か</h2>
<p>不定詞とは「<strong>to + 動詞の原形</strong>」の形をしたフレーズで、大きく分けて<strong>3つの用法</strong>があります。中学英語で最も重要な文法事項のひとつです。</p>
<div class="highlight">
  <p><strong>不定詞の3つの用法</strong><br>
  ✅ <strong>名詞的用法</strong>：「〜すること」（名詞の代わり）→ I want <strong>to go</strong>.<br>
  ✅ <strong>副詞的用法</strong>：「〜するために」（目的）→ I went <strong>to see</strong> him.<br>
  ✅ <strong>形容詞的用法</strong>：「〜するための」（名詞を修飾）→ I have <strong>to eat</strong> something.</p>
</div>

<h2>2. 名詞的用法：「〜すること」</h2>
<p>不定詞が文の中で<strong>主語・目的語・補語</strong>の役割をします。「〜すること」と訳します。</p>
<ul>
  <li><span class="example">To study English</span> is important. <span class="example-jp">（英語を勉強することは重要です）← 主語</span></li>
  <li><span class="example">I want to go</span> to Kyoto. <span class="example-jp">（京都に行きたいです）← 目的語</span></li>
  <li><span class="example">My dream is to be</span> a doctor. <span class="example-jp">（私の夢は医者になることです）← 補語</span></li>
</ul>
<div class="tip-box"><h3>💡 重要表現</h3>
<p><strong>want to〜</strong>（〜したい）が最もよく使われる。<br>
<strong>like to〜</strong>（〜することが好き）、<strong>need to〜</strong>（〜する必要がある）も頻出。</p></div>

<h2>3. 副詞的用法：「〜するために」</h2>
<p>文の中で<strong>目的</strong>を表します。「〜するために」と訳します。</p>
<div class="highlight"><p>【公式】 主語 + 動詞 + 〜 + <strong>to + 動詞の原形</strong><br>「〜するために...する」</p></div>
<ul>
  <li><span class="example">I went to the library to study.</span> <span class="example-jp">（勉強するために図書館に行った）</span></li>
  <li><span class="example">She came to Tokyo to see her friend.</span> <span class="example-jp">（彼女は友人に会うために東京に来た）</span></li>
  <li><span class="example">He woke up early to catch the train.</span> <span class="example-jp">（彼は電車に乗るために早く起きた）</span></li>
</ul>

<h2>4. 形容詞的用法：「〜するための」</h2>
<p>名詞の後ろに置いて、その名詞を修飾します。</p>
<div class="highlight"><p>【公式】 名詞 + <strong>to + 動詞の原形</strong><br>「〜するための名詞」「〜すべき名詞」</p></div>
<ul>
  <li><span class="example">I have something to eat.</span> <span class="example-jp">（何か食べるものがある）</span></li>
  <li><span class="example">She has a lot of homework to do.</span> <span class="example-jp">（彼女にはたくさんやるべき宿題がある）</span></li>
  <li><span class="example">I need a pen to write with.</span> <span class="example-jp">（書くためのペンが必要だ）</span></li>
</ul>
<div class="note"><strong>注意！</strong> 形容詞的用法は必ず<strong>名詞の直後</strong>に置く。日本語と語順が違うので要注意。</div>

<h2>5. 3用法の見分け方</h2>
<table>
  <tr><th>用法</th><th>ポイント</th><th>例文</th></tr>
  <tr><td>名詞的用法</td><td>主語・目的語・補語になっている</td><td>I want <strong>to go</strong></td></tr>
  <tr><td>副詞的用法</td><td>動詞を修飾。「〜するために」</td><td>went <strong>to study</strong></td></tr>
  <tr><td>形容詞的用法</td><td>直前の名詞を修飾</td><td>something <strong>to eat</strong></td></tr>
</table>
<div class="tip-box"><h3>💡 見分け方のコツ</h3><p>不定詞の前が<strong>動詞</strong>なら名詞的用法（目的語）、<strong>名詞</strong>なら形容詞的用法（修飾）、文全体にかかるなら副詞的用法（目的）。</p></div>

<h2>6. 動名詞との違い</h2>
<p>不定詞（to do）と動名詞（doing）はどちらも「〜すること」の意味を持ちますが、<strong>使える動詞が決まっている</strong>ものがあります。</p>
<table>
  <tr><th>不定詞だけを目的語に取る動詞</th><th>動名詞だけを目的語に取る動詞</th></tr>
  <tr><td>want（したい）, hope（希望する）<br>decide（決心する）, plan（計画する）</td><td>enjoy（楽しむ）, finish（終える）<br>stop（やめる）, give up（あきらめる）</td></tr>
</table>
<ul>
  <li><span class="example">I want to play</span> tennis. <span class="example-jp">（テニスをしたい）← 不定詞のみ</span></li>
  <li><span class="example">I enjoy playing</span> tennis. <span class="example-jp">（テニスを楽しむ）← 動名詞のみ</span></li>
</ul>

<div class="mistake-section"><h2>⚠️ よくある間違い</h2>
<ul>
  <li><strong>「I want go.」</strong> → 正しくは「I want <strong>to</strong> go.」 wantのあとのtoを忘れがち。</li>
  <li><strong>「to と for の混同」</strong> → 「〜するために」は to + 動詞。「〜のために」は for + 名詞。</li>
  <li><strong>「I enjoyed to play.」</strong> → enjoy のあとは動名詞。「I enjoyed playing.」が正解。</li>
</ul></div>

<div class="roadmap-box"><h2>🗺️ 学習の流れ</h2>
<div class="roadmap-links">
  <a href="futeisi2.html" class="roadmap-next">不定詞（応用）へ →</a>
  <a href="doumei.html" class="roadmap-next" style="background:#059669;">動名詞へ →</a>
</div></div>

<div class="related-articles"><h2>📚 関連する文法単元</h2>
<div class="related-grid">
  <a href="futeisi2.html" class="related-card"><span class="related-title">不定詞（応用）</span><span class="related-arrow">→</span></a>
  <a href="doumei.html" class="related-card"><span class="related-title">動名詞</span><span class="related-arrow">→</span></a>
  <a href="jyodosi.html" class="related-card"><span class="related-title">助動詞</span><span class="related-arrow">→</span></a>
</div></div>

<div class="practice-link-box"><p>
  ✅ <a href="../practice/futeisi.html">不定詞の練習問題を解く</a> か
  <a href="../test/futeisi_test.html">不定詞の確認テストに挑戦</a> しよう。
</p></div>
''')

# === 現在完了（genkan1.html） ===
write_article("genkan1.html", "現在完了（継続・経験・完了）", "中学3年", "g3", '''
<div class="tip-box">
  <h3>📑 このページで学ぶこと</h3>
  <ol style="margin:8px 0 0 20px;">
    <li>現在完了とは（have + 過去分詞）</li>
    <li>継続用法（ずっと〜している）</li>
    <li>経験用法（〜したことがある）</li>
    <li>完了・結果用法（〜したところだ）</li>
    <li>現在完了と過去形の違い</li>
    <li>現在完了進行形</li>
    <li>よくある間違い</li>
  </ol>
</div>

<h2>1. 現在完了とは</h2>
<p>現在完了は「<strong>have / has + 過去分詞</strong>」の形で、<strong>過去のある時点から現在まで</strong>をひとつなぎで表す時制です。3つの用法があります。</p>
<div class="highlight">
  <p><strong>現在完了の3つの用法</strong><br>
  ✅ <strong>継続</strong>：「ずっと〜している」→ I <strong>have lived</strong> here for 5 years.<br>
  ✅ <strong>経験</strong>：「〜したことがある」→ I <strong>have been</strong> to Kyoto.<br>
  ✅ <strong>完了・結果</strong>：「〜したところだ」→ I <strong>have just finished</strong> my homework.</p>
</div>

<h2>2. 継続用法：「ずっと〜している」</h2>
<p>過去のある時点から現在まで続いている状態を表します。<strong>for（期間）</strong>や<strong>since（起点）</strong>と一緒によく使われます。</p>
<div class="highlight"><p>【公式】 主語 + have/has + 過去分詞 + <strong>for / since</strong> + 〜</p></div>
<ul>
  <li><span class="example">I have lived</span> in Tokyo <strong>for five years.</strong> <span class="example-jp">（東京に5年間住んでいます）</span></li>
  <li><span class="example">She has studied</span> English <strong>since 2020.</strong> <span class="example-jp">（彼女は2020年から英語を勉強しています）</span></li>
  <li><span class="example">They have known</span> each other <strong>for a long time.</strong> <span class="example-jp">（彼らは長い間お互いを知っています）</span></li>
</ul>

<div class="note"><strong>for と since の違い</strong><br>
<strong>for</strong> + <strong>期間</strong>（for 3 years, for a week）← 「どのくらい」<br>
<strong>since</strong> + <strong>時点</strong>（since 2020, since last year）← 「いつから」</div>

<h2>3. 経験用法：「〜したことがある」</h2>
<p>今までの人生での経験を表します。<strong>ever（今までに）</strong>や<strong>never（一度もない）</strong>と一緒に使われます。</p>
<ul>
  <li><span class="example">I have been</span> to Kyoto twice. <span class="example-jp">（京都に2回行ったことがあります）</span></li>
  <li><span class="example">Have you ever seen</span> a lion? <span class="example-jp">（ライオンを見たことがありますか？）</span></li>
  <li><span class="example">She has never eaten</span> sushi. <span class="example-jp">（彼女は寿司を食べたことがありません）</span></li>
</ul>

<div class="tip-box"><h3>💡 「行ったことがある」は have been to</h3>
<p><strong>have been to</strong> = 「行ったことがある」（経験・行って帰ってきた）<br>
<strong>have gone to</strong> = 「行ってしまった」（今ここにいない）<br>
<strong>have been in</strong> = 「〜に住んでいる」（継続）<br>
この3つの違いをしっかり区別しましょう。</p></div>

<h2>4. 完了・結果用法：「〜したところだ」</h2>
<p>動作が<strong>ついさっき完了した</strong>ことや、その<strong>結果</strong>を表します。<strong>just（ちょうど）</strong>、<strong>already（もう）</strong>、<strong>yet（もう/まだ）</strong>と一緒に使われます。</p>
<ul>
  <li><span class="example">I have just finished</span> my homework. <span class="example-jp">（ちょうど宿題を終えたところです）</span></li>
  <li><span class="example">She has already eaten</span> lunch. <span class="example-jp">（彼女はもう昼食を食べました）</span></li>
  <li><span class="example">Have you finished</span> your homework <strong>yet</strong>? <span class="example-jp">（もう宿題を終えましたか？）</span></li>
  <li><span class="example">I haven't finished</span> my homework <strong>yet</strong>. <span class="example-jp">（まだ宿題を終えていません）</span></li>
</ul>

<div class="note"><strong>already / yet / just の位置</strong><br>
<strong>already</strong>（もう）→ 肯定文で使う。have + already + 過去分詞<br>
<strong>yet</strong>（もう？/まだ）→ 疑問文・否定文の<strong>文末</strong>に置く<br>
<strong>just</strong>（ちょうど）→ have + just + 過去分詞</div>

<h2>5. 現在完了 vs 過去形</h2>
<table>
  <tr><th></th><th>現在完了</th><th>過去形</th></tr>
  <tr><td>焦点</td><td>現在とのつながり</td><td>過去の事実だけ</td></tr>
  <tr><td>例</td><td>I <strong>have lost</strong> my key.（今も見つかっていない）</td><td>I <strong>lost</strong> my key yesterday.（昨日落としたけど今はあるかも）</td></tr>
  <tr><td>使えない表現</td><td>yesterday, last week など過去の特定時点とは使えない</td><td>yesterday, last year, ago と使える</td></tr>
</table>
<div class="tip-box"><h3>💡 過去形との使い分け</h3><p><strong>「いつ」が大切</strong>なときは過去形（I went to Kyoto last year.）<br>
<strong>「今どうか」が大切</strong>なときは現在完了（I have been to Kyoto.）</p></div>

<div class="mistake-section"><h2>⚠️ よくある間違い</h2>
<ul>
  <li><strong>「I have been to Kyoto yesterday.」</strong> → yesterday は現在完了と使えない！「I went to Kyoto yesterday.」が正解。</li>
  <li><strong>「have been to」と「have gone to」の混同</strong> → been toは「行ったことがある」、gone toは「行ってしまった」。</li>
  <li><strong>「for」と「since」の混同</strong> → for + 期間、since + 時点。</li>
</ul></div>

<div class="roadmap-box"><h2>🗺️ 学習の流れ</h2>
<div class="roadmap-links">
  <a href="genkan2.html" class="roadmap-next">現在完了（経験）詳細へ →</a>
  <a href="genkan3.html" class="roadmap-next" style="background:#059669;">現在完了（完了）詳細へ →</a>
</div></div>

<div class="related-articles"><h2>📚 関連する文法単元</h2>
<div class="related-grid">
  <a href="genkan2.html" class="related-card"><span class="related-title">現在完了（経験）</span><span class="related-arrow">→</span></a>
  <a href="genkan3.html" class="related-card"><span class="related-title">現在完了（完了）</span><span class="related-arrow">→</span></a>
  <a href="genkanSinkokei.html" class="related-card"><span class="related-title">現在完了進行形</span><span class="related-arrow">→</span></a>
  <a href="ukemi.html" class="related-card"><span class="related-title">受け身</span><span class="related-arrow">→</span></a>
</div></div>

<div class="practice-link-box"><p>
  ✅ <a href="../practice/genkan.html">現在完了の練習問題を解く</a> か
  <a href="../test/genkan_test.html">現在完了の確認テストに挑戦</a> しよう。
</p></div>
''')

# === 関係代名詞（kankeisi1.html） ===
write_article("kankeisi1.html", "関係代名詞（who, which, that）", "中学3年", "g3", '''
<div class="tip-box">
  <h3>📑 このページで学ぶこと</h3>
  <ol style="margin:8px 0 0 20px;">
    <li>関係代名詞とは何か</li>
    <li>主格の関係代名詞（who / which / that）</li>
    <li>目的格の関係代名詞</li>
    <li>関係代名詞の省略</li>
    <li>関係代名詞と間接疑問の違い</li>
    <li>よくある間違い</li>
  </ol>
</div>

<h2>1. 関係代名詞とは</h2>
<p>関係代名詞は、<strong>名詞を後ろから説明する</strong>ための文法です。2つの文を1つにつなぐ働きをします。高校入試でも頻出の最重要単元です。</p>
<div class="highlight">
  <p><strong>関係代名詞の種類</strong><br>
  ✅ <strong>who</strong> → <strong>人</strong>に使う（主格）<br>
  ✅ <strong>which</strong> → <strong>物・動物</strong>に使う（主格・目的格）<br>
  ✅ <strong>that</strong> → <strong>人・物</strong>両方に使える<br>
  ✅ <strong>whose</strong> → 「〜の」所有を表す</p>
</div>

<h2>2. 主格の関係代名詞（who / which / that）</h2>
<p>関係代名詞のあとに<strong>動詞</strong>が続くのが主格です。関係代名詞自身が主語の役割をします。</p>
<div class="highlight"><p>【公式】 先行詞（人） + <strong>who</strong> + 動詞 + 〜<br>【公式】 先行詞（物） + <strong>which/that</strong> + 動詞 + 〜</p></div>

<h3>who（人）の例</h3>
<ul>
  <li><span class="example">The boy who is running</span> is Taro. <span class="example-jp">（走っている男の子は太郎です）</span></li>
  <li><span class="example">I know a man who can speak</span> five languages. <span class="example-jp">（5ヶ国語を話せる男性を知っています）</span></li>
  <li><span class="example">The woman who lives next door</span> is a teacher. <span class="example-jp">（隣に住んでいる女性は先生です）</span></li>
</ul>

<h3>which（物）の例</h3>
<ul>
  <li><span class="example">The book which is on the desk</span> is mine. <span class="example-jp">（机の上にある本は私のです）</span></li>
  <li><span class="example">I like music which makes</span> me happy. <span class="example-jp">（私を幸せにする音楽が好きです）</span></li>
</ul>

<div class="tip-box"><h3>💡 that は万能</h3>
<p>that は人にも物にも使えます。who の代わりに that、which の代わりに that が使えます。<br>
ただし、<strong>who や which よりも that のほうがカジュアル</strong>な印象になります。</p></div>

<h2>3. 目的格の関係代名詞</h2>
<p>関係代名詞のあとに<strong>主語+動詞</strong>が続くのが目的格です。関係代名詞が目的語の役割をします。</p>
<div class="highlight"><p>【公式】 先行詞（人） + <strong>who(m)/that</strong> + 主語 + 動詞<br>【公式】 先行詞（物） + <strong>which/that</strong> + 主語 + 動詞</p></div>
<ul>
  <li><span class="example">The book which I bought</span> is interesting. <span class="example-jp">（私が買った本は面白いです）</span></li>
  <li><span class="example">The man who(m) I met yesterday</span> was kind. <span class="example-jp">（昨日会った男性は親切でした）</span></li>
  <li><span class="example">This is the car that I want to buy</span>. <span class="example-jp">（これが私が買いたい車です）</span></li>
</ul>

<div class="note"><strong>目的格の関係代名詞は省略できる</strong><br>
目的格の who(m) / which / that は<strong>省略可能</strong>です。<br>
例：The book <del>which</del> I bought is interesting. → 関係代名詞なしでもOK！</div>

<h2>4. whose（所有格）</h2>
<p>「〜の」という所有の意味を表します。人にも物にも使えます。</p>
<ul>
  <li><span class="example">The girl whose hair is long</span> is Mary. <span class="example-jp">（髪が長い女の子はメアリーです）</span></li>
  <li><span class="example">I know a person whose father is a doctor</span>. <span class="example-jp">（父親が医者である人を知っています）</span></li>
</ul>

<h2>5. 関係代名詞 vs 間接疑問</h2>
<table>
  <tr><th></th><th>関係代名詞</th><th>間接疑問</th></tr>
  <tr><td>役割</td><td>名詞を説明する</td><td>疑問文を文中に埋め込む</td></tr>
  <tr><td>例</td><td>I know the boy <strong>who</strong> is running.</td><td>I know <strong>who</strong> he is.</td></tr>
  <tr><td>違い</td><td>先行詞（the boy）がある</td><td>先行詞がない</td></tr>
</table>

<div class="mistake-section"><h2>⚠️ よくある間違い</h2>
<ul>
  <li><strong>「who」と「which」の混同</strong> → 人には who / 物には which。ただし that は両方OK。</li>
  <li><strong>「I know who is he?」</strong> → 間接疑問は疑問文の語順にならない。「I know who he is.」が正解。</li>
  <li><strong>主格と目的格の区別</strong> → 関係代名詞のあとに「主語+動詞」が来たら目的格で省略可能。</li>
</ul></div>

<div class="related-articles"><h2>📚 関連する文法単元</h2>
<div class="related-grid">
  <a href="kansetu.html" class="related-card"><span class="related-title">間接疑問</span><span class="related-arrow">→</span></a>
  <a href="kankeisi2.html" class="related-card"><span class="related-title">関係代名詞（続き）</span><span class="related-arrow">→</span></a>
  <a href="bunsi.html" class="related-card"><span class="related-title">分詞</span><span class="related-arrow">→</span></a>
</div></div>

<div class="practice-link-box"><p>
  ✅ <a href="../practice/kankeisi.html">関係代名詞の練習問題を解く</a> か
  <a href="../test/kankeisi_test.html">関係代名詞の確認テストに挑戦</a> しよう。
</p></div>
''')

if __name__ == "__main__":
    print("=== 記事を厚くしました ===")
    print("  grammar/futeisi1.html (不定詞)")
    print("  grammar/genkan1.html (現在完了)")
    print("  grammar/kankeisi1.html (関係代名詞)")