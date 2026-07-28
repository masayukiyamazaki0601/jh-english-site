#!/usr/bin/env python3
"""全34記事を300行以上に拡充（既に厚い6記事はスキップ）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def write_full_article(filename, title, grade, grade_class, sections):
    """完全な記事を書き出す（300行超え）"""
    toc_items = ""
    for i, (heading, _) in enumerate(sections, 1):
        toc_items += f"      <li>{heading}</li>\n"
    
    body = ""
    for heading, content in sections:
        body += f"  <h2>{heading}</h2>\n"
        body += content + "\n"
    
    related_links_map = {
        "be.html": "be動詞", "ippan.html": "一般動詞", "gimonhitei.html": "疑問文・否定文",
        "gimonsi.html": "疑問詞", "meirei.html": "命令文", "santan.html": "三人称単数現在",
        "shinko.html": "現在進行形", "can.html": "can", "kako.html": "一般動詞の過去形",
        "fukusu.html": "名詞の複数形", "daimeisi.html": "代名詞", "bekako.html": "be動詞の過去形",
        "kakosin.html": "過去進行形", "mirai.html": "未来形", "doumei.html": "動名詞",
        "futeisi1.html": "不定詞（基本）", "jyodosi.html": "助動詞", "hikaku1.html": "比較",
        "there.html": "there is構文", "setuzoku.html": "接続詞", "ukemi.html": "受け身",
        "genkan1.html": "現在完了（継続）", "genkan2.html": "現在完了（経験）", "genkan3.html": "現在完了（完了）",
        "genkanSinkokei.html": "現在完了進行形", "futeisi2.html": "不定詞（応用）", "bunsi.html": "分詞",
        "kansetu.html": "間接疑問", "kankeisi1.html": "関係代名詞", "kateiho.html": "仮定法",
        "genkeiFuteisi.html": "原形不定詞", "suryo.html": "数量詞", "zensi.html": "前置詞",
        "kansi.html": "冠詞",
    }
    related_html = '<div class="related-articles"><h2>📚 関連する文法単元</h2><div class="related-grid">\n'
    count = 0
    for f, n in related_links_map.items():
        if f != filename and count < 6:
            related_html += f'      <a href="{f}" class="related-card"><span class="related-title">{n}</span><span class="related-arrow">→</span></a>\n'
            count += 1
    related_html += '</div></div>\n'
    
    practice_file = filename.replace(".html", "")
    practice_link = f'<div class="practice-link-box"><p>✅ 理解を深めたら <a href="../practice/{practice_file}.html">練習問題を解く</a> か <a href="../test/{practice_file}_test.html">確認テストに挑戦</a> しよう。</p></div>\n'
    
    full_html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 中学英語学習サイト</title>
<meta name="description" content="中学英語の{title}をわかりやすく解説。例文・表・練習問題で完全マスター。">
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
    中学英語の{title}をわかりやすく解説します。このページで基礎から応用まで完全マスターしましょう。
  </p>

  <div class="tip-box">
    <h3>📑 このページで学ぶこと</h3>
    <ol style="margin: 8px 0 0 20px;">
{toc_items}    </ol>
  </div>

{body}
  {related_html}
  {practice_link}
</article>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>
<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。英文法・練習問題・確認テストで英語力を確実にアップ。</p></div>
    <div><h3>文法解説</h3><a href="be.html">be動詞</a><a href="futeisi1.html">不定詞</a><a href="genkan1.html">現在完了</a><a href="kankeisi1.html">関係代名詞</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a><a href="../practice/futeisi.html">不定詞</a><a href="../practice/genkan.html">現在完了</a></div>
    <div><h3>確認テスト</h3><a href="../test/be_test.html">be動詞</a><a href="../test/futeisi_test.html">不定詞</a><a href="../test/genkan_test.html">現在完了</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''
    
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "w") as f:
        f.write(full_html)
    lines = full_html.count("\n")
    print(f"  WRITTEN {filename} ({lines} lines)")

# ===== 既に厚い記事はスキップ =====
THICK_ARTICLES = {
    "kansi.html",    # 548 lines
    "santan.html",   # 515
    "gimonhitei.html", # 495
    "shinko.html",   # 480
    "fukusu.html",   # 470
    "meirei.html",   # 448
}

# ===== 全記事のセクション定義 =====
ALL_SECTIONS = {
"kateiho.html": {
    "title": "仮定法", "grade": "中学3年", "class": "g3",
    "sections": [
        ("仮定法とは", """
<p>仮定法（かていほう）は、<strong>現実と違うこと</strong>を仮定する表現です。「もし〜なら（実際はそうじゃないけど）」という意味を表します。</p>
<div class="highlight"><p>【公式】 If + 主語 + <strong>過去形</strong>, 主語 + <strong>would/could</strong> + 動詞の原形</p></div>
<div class="note"><strong>最重要ルール</strong>：仮定法では be動詞は常に <strong>were</strong> を使います。主語が I でも were です。</div>
"""),
        ("仮定法過去の形と意味", """
<p>仮定法過去は「現在の事実と違うこと」を仮定します。過去形を使いますが、<strong>過去の話ではありません</strong>。</p>
<div class="highlight"><p>【公式】 If + 主語 + 過去形, 主語 + <strong>would</strong> + 動詞の原形<br>If + 主語 + 過去形, 主語 + <strong>could</strong> + 動詞の原形（〜できるのに）</p></div>
<ul>
  <li><span class="example">If I were you, I would study harder.</span> <span class="example-jp">（もし私があなたなら、もっと勉強するのに）</span></li>
  <li><span class="example">If I had money, I would buy a car.</span> <span class="example-jp">（もしお金があれば、車を買うのに）</span></li>
  <li><span class="example">If it were sunny, we could go out.</span> <span class="example-jp">（もし晴れなら、出かけられるのに）</span></li>
  <li><span class="example">I would be happy if I could meet her.</span> <span class="example-jp">（彼女に会えれば嬉しいのに）</span></li>
</ul>
"""),
        ("仮定法と条件文の違い", """
<table>
<tr><th></th><th>条件文（if + 現在形）</th><th>仮定法（if + 過去形）</th></tr>
<tr><td>形</td><td>If + 現在形, 主語 + will</td><td>If + 過去形, 主語 + would</td></tr>
<tr><td>現実性</td><td>実現する可能性あり</td><td>現実とは違う（仮定）</td></tr>
<tr><td>例</td><td>If it rains, I will stay home.</td><td>If it rained, I would stay home.</td></tr>
<tr><td>日本語</td><td>雨が降れば家にいる</td><td>雨が降れば家にいるのに（実際は降っていない）</td></tr>
</table>
"""),
        ("would と could の使い分け", """
<table>
<tr><th>助動詞</th><th>意味</th><th>例</th></tr>
<tr><td>would</td><td>〜するだろう（意志）</td><td>I would go if I had time.（時間があれば行くのに）</td></tr>
<tr><td>could</td><td>〜できるだろう（可能）</td><td>I could help if I were there.（そこにいれば手伝えるのに）</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「If I was you」</strong> → 仮定法では「If I <strong>were</strong> you」が正解。</li>
  <li><strong>「would」のあとに「to」をつける</strong> → would + 動詞の原形。「would to go」は間違い。</li>
  <li><strong>仮定法の文中に「will」を使う</strong> → If節の中では will は使わない。If I will have → If I had。</li>
</ul></div>
"""),
        ("仮定法の練習問題", """
<div class="practice-link-box"><p>✏️ 仮定法の練習：<br>
(1) If I ( ) you, I would study harder. → were<br>
(2) If it ( ) sunny, we could go swimming. → were<br>
(3) I would buy a car if I ( ) enough money. → had<br>
(4) If she ( ) here, she would help us. → were<br>
(5) We could win if we ( ) harder. → tried</p></div>
"""),
    ]
},
"genkan3.html": {
    "title": "現在完了（完了・結果用法）", "grade": "中学3年", "class": "g3",
    "sections": [
        ("完了・結果用法とは", """
<p>現在完了の完了・結果用法は、「<strong>〜したところだ</strong>」「<strong>もう〜した</strong>」という意味を表します。動作がついさっき完了したことや、その結果が今も続いていることを示します。</p>
<div class="highlight"><p>【公式】 主語 + have/has + (just/already) + 過去分詞<br>疑問文: Have/Has + 主語 + (ever) + 過去分詞 + yet?<br>否定文: 主語 + haven't/hasn't + 過去分詞 + yet</p></div>
"""),
        ("already / just / yet の使い分け", """
<table>
<tr><th>単語</th><th>意味</th><th>使う文</th><th>位置</th></tr>
<tr><td><strong>already</strong></td><td>もう、すでに</td><td>肯定文</td><td>have + already + 過去分詞</td></tr>
<tr><td><strong>just</strong></td><td>ちょうど</td><td>肯定文</td><td>have + just + 過去分詞</td></tr>
<tr><td><strong>yet</strong></td><td>もう？ / まだ〜ない</td><td>疑問文・否定文</td><td>文末</td></tr>
</table>
<ul>
  <li><span class="example">I have just finished my homework.</span> <span class="example-jp">（ちょうど宿題を終えたところです）</span></li>
  <li><span class="example">She has already eaten lunch.</span> <span class="example-jp">（彼女はもう昼食を食べました）</span></li>
  <li><span class="example">Have you finished yet?</span> <span class="example-jp">（もう終えましたか？）</span></li>
  <li><span class="example">I haven't finished yet.</span> <span class="example-jp">（まだ終えていません）</span></li>
</ul>
"""),
        ("現在完了 vs 過去形（完了用法）", """
<table>
<tr><th></th><th>現在完了（完了）</th><th>過去形</th></tr>
<tr><td>焦点</td><td>現在の状態（今どうか）</td><td>過去の事実（いつしたか）</td></tr>
<tr><td>例</td><td>I have lost my key.（今も見つからない）</td><td>I lost my key yesterday.（今はあるかも）</td></tr>
<tr><td>共起語</td><td>already, just, yet, ever, never</td><td>yesterday, last〜, 〜ago</td></tr>
</table>
<div class="note"><strong>テストの鉄則</strong><br>yesterday / last night / ago があったら → 過去形<br>already / just / yet があったら → 現在完了</div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have already finished it yet.」</strong> → already と yet は同時に使わない。</li>
  <li><strong>「I have already finished yet.」</strong> → already は肯定文、yet は疑問文・否定文。</li>
  <li><strong>現在完了と過去形を混同</strong> → 「I have seen him yesterday」は間違い。「I saw him yesterday」が正解。</li>
</ul></div>
"""),
    ]
},
"genkeiFuteisi.html": {
    "title": "原形不定詞", "grade": "中学3年", "class": "g3",
    "sections": [
        ("原形不定詞とは", """
<p>原形不定詞（げんけいふていし）は、<strong>to のつかない不定詞</strong>、つまり<strong>動詞の原形</strong>のことです。主に知覚動詞（see, hear, watch）と使役動詞（make, let, have）のあとで使います。</p>
<div class="highlight"><p>【公式】 知覚動詞 + 目的語 + <strong>動詞の原形</strong><br>【公式】 使役動詞 + 目的語 + <strong>動詞の原形</strong></p></div>
"""),
        ("知覚動詞（see, hear, watch）", """
<p>「〜が…するのを見る/聞く」という意味。動作の<strong>完了・全体</strong>を表します。</p>
<ul>
  <li><span class="example">I saw him run.</span> <span class="example-jp">（彼が走るのを最後まで見ました）</span></li>
  <li><span class="example">I heard her sing.</span> <span class="example-jp">（彼女が歌うのを聞きました）</span></li>
  <li><span class="example">We watched the sun set.</span> <span class="example-jp">（太陽が沈むのを見ました）</span></li>
  <li><span class="example">I felt something touch my shoulder.</span> <span class="example-jp">（何かが肩に触れるのを感じました）</span></li>
</ul>
<div class="tip-box"><h3>💡 原形不定詞 vs 現在分詞</h3><p><strong>I saw him run.</strong> = 走るのを最後まで見た（動作の完了）<br><strong>I saw him running.</strong> = 走っているのを目撃した（動作の途中）</p></div>
"""),
        ("使役動詞（make, let, have）", """
<p>「〜に…させる」という意味。</p>
<ul>
  <li><span class="example">My mother made me clean my room.</span> <span class="example-jp">（母は私に部屋を掃除させました）</span></li>
  <li><span class="example">Let's go to the park.</span> <span class="example-jp">（公園に行きましょう）</span></li>
  <li><span class="example">I had him carry the box.</span> <span class="example-jp">（彼に箱を運ばせました）</span></li>
</ul>
<div class="note"><strong>help は特殊</strong>：help のあとは原形不定詞でも to 不定詞でもOK。<br>He helped me (to) carry the box.</div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I saw him to run.」</strong> → 知覚動詞のあとは to をつけない。「I saw him run.」が正解。</li>
  <li><strong>「I made him to clean.」</strong> → 使役動詞のあとも to 不要。「I made him clean.」が正解。</li>
  <li><strong>「Let's going.」</strong> → Let's のあとは動詞の原形。「Let's go.」が正解。</li>
</ul></div>
"""),
    ]
},
"kakosin.html": {
    "title": "過去進行形", "grade": "中学2年", "class": "g2",
    "sections": [
        ("過去進行形とは", """
<p>過去進行形は「<strong>was/were + 動詞のing形</strong>」で表し、「その時まさに〜していた」という意味です。現在進行形の過去版です。</p>
<div class="highlight"><p>【公式】 主語 + was/were + 動詞のing形<br>「（その時）〜していた」</p></div>
"""),
        ("肯定文の作り方", """
<table>
<tr><th>主語</th><th>be動詞</th><th>例文</th></tr>
<tr><td>I / He / She / It</td><td>was</td><td>I was reading a book.</td></tr>
<tr><td>You / We / They</td><td>were</td><td>They were playing soccer.</td></tr>
</table>
<ul>
  <li><span class="example">I was reading a book at 8pm.</span> <span class="example-jp">（午後8時に本を読んでいました）</span></li>
  <li><span class="example">She was cooking dinner at that time.</span> <span class="example-jp">（彼女はその時夕食を作っていました）</span></li>
  <li><span class="example">They were playing soccer yesterday.</span> <span class="example-jp">（彼らは昨日サッカーをしていました）</span></li>
</ul>
"""),
        ("否定文・疑問文", """
<ul>
  <li><span class="example">He was not sleeping at that time.</span> <span class="example-jp">（彼はその時寝ていませんでした）</span></li>
  <li><span class="example">Were you studying at midnight?</span> <span class="example-jp">（真夜中に勉強していましたか？）</span></li>
  <li><span class="example">What were you doing then?</span> <span class="example-jp">（その時何をしていましたか？）</span></li>
  <li><span class="example">I wasn't watching TV.</span> <span class="example-jp">（テレビを見ていませんでした）</span></li>
</ul>
"""),
        ("過去形 vs 過去進行形", """
<table>
<tr><th></th><th>過去形</th><th>過去進行形</th></tr>
<tr><td>焦点</td><td>「〜した」（完了した行為）</td><td>「〜していた」（進行中の行為）</td></tr>
<tr><td>例1</td><td>I read a book.（読み終えた）</td><td>I was reading a book.（読んでいる途中）</td></tr>
<tr><td>例2</td><td>She called me.（電話がかかってきた）</td><td>She was calling me.（電話をかけていた）</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I was read a book.」</strong> → 進行形は be動詞 + 動詞のing形。「I was reading」が正解。</li>
  <li><strong>「We was playing.」</strong> → We は複数なので were。「We were playing」が正解。</li>
  <li><strong>過去進行形と過去形を混同</strong> → 継続中の動作には過去進行形を使う。</li>
</ul></div>
"""),
    ]
},
"there.html": {
    "title": "there is 構文", "grade": "中学2年", "class": "g2",
    "sections": [
        ("there is 構文とは", """
<p>「〜がある/いる」という存在を表す構文です。日本語の「机の上に本があります」のような表現に使います。</p>
<div class="highlight"><p>【公式】 <strong>There is/are</strong> + 名詞 + 場所<br>「〜に…がある/いる」</p></div>
<div class="note"><strong>注意！</strong> 日本語の語順と逆です。日本語は「場所 + に + 物 + がある」、英語は「There is + 物 + 場所」。</div>
"""),
        ("単数と複数の使い分け", """
<table>
<tr><th>名詞の数</th><th>be動詞</th><th>例</th></tr>
<tr><td>単数名詞</td><td>There is</td><td>There is a cat under the table.</td></tr>
<tr><td>複数名詞</td><td>There are</td><td>There are many books on the desk.</td></tr>
<tr><td>不可算名詞</td><td>There is</td><td>There is some water in the glass.</td></tr>
<tr><td>数えられない物</td><td>There is</td><td>There is a lot of traffic.</td></tr>
</table>
<ul>
  <li><span class="example">There is a pen on the desk.</span> <span class="example-jp">（机の上にペンがあります）</span></li>
  <li><span class="example">There are three apples in the basket.</span> <span class="example-jp">（かごの中に3つのリンゴがあります）</span></li>
</ul>
"""),
        ("否定文・疑問文", """
<ul>
  <li><span class="example">There is not any milk in the fridge.</span> <span class="example-jp">（冷蔵庫に牛乳はありません）</span></li>
  <li><span class="example">Is there a hospital near here?</span> <span class="example-jp">（この近くに病院はありますか？）</span></li>
  <li><span class="example">Are there any students in the room?</span> <span class="example-jp">（部屋に学生はいますか？）</span></li>
  <li><span class="example">How many books are there on the desk?</span> <span class="example-jp">（机の上に何冊本がありますか？）</span></li>
</ul>
"""),
        ("There is と It is の違い", """
<table>
<tr><th></th><th>There is</th><th>It is</th></tr>
<tr><td>役割</td><td>「存在」を表す</td><td>「それ」を指す</td></tr>
<tr><td>例1</td><td>There is a cat.（猫がいる）</td><td>It is a cat.（それは猫です）</td></tr>
<tr><td>例2</td><td>There is a book on the desk.（本がある）</td><td>It is on the desk.（それは机の上にある）</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「There has a cat.」</strong> → there構文は have ではなく、There is/are。</li>
  <li><strong>「There is many people.」</strong> → people は複数なので「There are many people.」。</li>
  <li><strong>there と it を混同</strong> → 「There is a book.」= 本が存在する / 「It is a book.」= それは本だ。</li>
</ul></div>
"""),
    ]
},
"genkanSinkokei.html": {
    "title": "現在完了進行形", "grade": "中学3年", "class": "g3",
    "sections": [
        ("現在完了進行形とは", """
<p>現在完了進行形は「<strong>have/has + been + 動詞のing形</strong>」で表します。「ずっと〜し続けている」という動作の継続を強調します。</p>
<div class="highlight"><p>【公式】 主語 + have/has + <strong>been</strong> + 動詞のing形<br>「ずっと〜し続けている」</p></div>
<ul>
  <li><span class="example">I have been studying English for three years.</span> <span class="example-jp">（3年間英語を勉強し続けています）</span></li>
  <li><span class="example">It has been raining since morning.</span> <span class="example-jp">（朝から雨が降り続いています）</span></li>
  <li><span class="example">She has been waiting for 30 minutes.</span> <span class="example-jp">（彼女は30分待ち続けています）</span></li>
  <li><span class="example">They have been playing tennis for two hours.</span> <span class="example-jp">（彼らは2時間テニスをし続けています）</span></li>
</ul>
"""),
        ("現在完了（継続）との違い", """
<table>
<tr><th></th><th>現在完了（継続）</th><th>現在完了進行形</th></tr>
<tr><td>形</td><td>have/has + 過去分詞</td><td>have/has + been + doing</td></tr>
<tr><td>焦点</td><td>状態の継続</td><td>動作の継続（強調）</td></tr>
<tr><td>例</td><td>I have lived here for 5 years.</td><td>I have been living here for 5 years.</td></tr>
<tr><td>ニュアンス</td><td>事実として「住んでいる」</td><td>「住み続けている」と動作感</td></tr>
</table>
<div class="tip-box"><h3>💡 使い分けのポイント</h3><p>状態動詞（live, know, like, want）は現在完了（継続）が自然。<br>動作動詞（study, wait, rain, work）は現在完了進行形が自然。</p></div>
"""),
        ("否定文・疑問文", """
<ul>
  <li><span class="example">I have not been sleeping well lately.</span> <span class="example-jp">（最近よく眠れていません）</span></li>
  <li><span class="example">Has it been raining since yesterday?</span> <span class="example-jp">（昨日から雨が降り続いていますか？）</span></li>
  <li><span class="example">How long have you been studying English?</span> <span class="example-jp">（どのくらい英語を勉強し続けていますか？）</span></li>
</ul>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have been study.」</strong> → have + been + doing。studying が必要。</li>
  <li><strong>「I am studying for 2 hours.」</strong> → 現在進行形は「今している」だけ。継続には現在完了進行形。</li>
  <li><strong>been を忘れる</strong> → have + been + doing。been が必須。</li>
</ul></div>
"""),
    ]
},
"bekako.html": {
    "title": "be動詞の過去形", "grade": "中学2年", "class": "g2",
    "sections": [
        ("be動詞の過去形とは", """
<p>be動詞の過去形は、現在の am/are/is が <strong>was/were</strong> に変わります。過去の状態や存在を表します。</p>
<div class="highlight"><p><strong>am/is → was</strong>（I, he, she, it）<br><strong>are → were</strong>（you, we, they）</p></div>
<table>
<tr><th>現在形</th><th>過去形</th><th>例</th></tr>
<tr><td>I am</td><td>I was</td><td>I was happy yesterday.</td></tr>
<tr><td>You are</td><td>You were</td><td>You were late for school.</td></tr>
<tr><td>He/She/It is</td><td>was</td><td>She was busy last night.</td></tr>
<tr><td>We/They are</td><td>were</td><td>They were at the park.</td></tr>
</table>
"""),
        ("否定文の作り方", """
<p>否定文は was/were のあとに not を置きます。短縮形は wasn't / weren't。</p>
<div class="highlight"><p>【公式】 主語 + was/were + <strong>not</strong> + 〜</p></div>
<ul>
  <li><span class="example">I was not at home yesterday.</span> <span class="example-jp">（昨日家にいませんでした）</span></li>
  <li><span class="example">She wasn't sick. She was just tired.</span> <span class="example-jp">（彼女は病気じゃなかった。ただ疲れていただけです）</span></li>
  <li><span class="example">They weren't at school last Monday.</span> <span class="example-jp">（彼らは先週月曜日に学校にいませんでした）</span></li>
</ul>
"""),
        ("疑問文の作り方", """
<p>疑問文は was/were を文頭に置きます。</p>
<div class="highlight"><p>【公式】 Was/Were + 主語 + 〜？</p></div>
<ul>
  <li><span class="example">Were you tired after the game?</span> <span class="example-jp">（試合の後疲れていましたか？）</span></li>
  <li><span class="example">Was she at the party?</span> <span class="example-jp">（彼女はパーティーにいましたか？）</span></li>
  <li><span class="example">Was it cold this morning?</span> <span class="example-jp">（今朝は寒かったですか？）</span></li>
</ul>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I were happy.」</strong> → I には was を使います。仮定法以外では I were は使いません。</li>
  <li><strong>「There was many people.」</strong> → people は複数なので「There were many people.」が正解。</li>
  <li><strong>was と were の混同</strong> → 単数（I, he, she, it）は was / 複数（we, you, they）は were。</li>
</ul></div>
"""),
    ]
},
"kansetu.html": {
    "title": "間接疑問", "grade": "中学3年", "class": "g3",
    "sections": [
        ("間接疑問とは", """
<p>間接疑問（かんせつぎもん）は、「<strong>疑問文が文の中に埋め込まれた形</strong>」です。「〜か知っていますか」「〜かわかりません」のように使います。</p>
<div class="highlight"><p><strong>【最重要ルール】</strong> 間接疑問のあとは<strong>肯定文の語順</strong>（主語 + 動詞）になる！</p></div>
"""),
        ("疑問詞を使う間接疑問", """
<ul>
  <li><span class="example">Do you know where he lives?</span> <span class="example-jp">（彼がどこに住んでいるか知っていますか？）</span></li>
  <li><span class="example">I don't know what this is.</span> <span class="example-jp">（これが何かわかりません）</span></li>
  <li><span class="example">Can you tell me how to get to the station?</span> <span class="example-jp">（駅への行き方を教えてくれますか？）</span></li>
  <li><span class="example">I know who she is.</span> <span class="example-jp">（彼女が誰か知っています）</span></li>
  <li><span class="example">Please tell me when the movie starts.</span> <span class="example-jp">（映画がいつ始まるか教えてください）</span></li>
</ul>
"""),
        ("疑問詞のない間接疑問（whether/if）", """
<ul>
  <li><span class="example">I wonder if he is kind.</span> <span class="example-jp">（彼が親切かどうか疑問だ）</span></li>
  <li><span class="example">Do you know whether she will come?</span> <span class="example-jp">（彼女が来るかどうか知っていますか？）</span></li>
  <li><span class="example">I'm not sure if I can go.</span> <span class="example-jp">（行けるかどうかわかりません）</span></li>
</ul>
"""),
        ("間接疑問 vs 関係代名詞", """
<table>
<tr><th></th><th>間接疑問</th><th>関係代名詞</th></tr>
<tr><td>役割</td><td>疑問文を埋め込む</td><td>名詞を説明する</td></tr>
<tr><td>先行詞</td><td>なし</td><td>あり</td></tr>
<tr><td>例</td><td>I know <strong>who</strong> he is.</td><td>I know the boy <strong>who</strong> is running.</td></tr>
</table>
<div class="tip-box"><h3>💡 見分け方のコツ</h3><p>直前が<strong>名詞</strong>なら関係代名詞、<strong>動詞</strong>なら間接疑問。これでほぼ判別できます。</p></div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「Do you know what is this?」</strong> → 間接疑問のあとは肯定文の語順。「Do you know what this is?」が正解。</li>
  <li><strong>「Tell me where is the station.」</strong> → 「Tell me where the station is.」が正解。</li>
  <li><strong>間接疑問に？をつけてしまうケース</strong> → I don't know what this is.（文末はピリオド）</li>
</ul></div>
"""),
    ]
},
"setuzoku.html": {
    "title": "接続詞", "grade": "中学2年", "class": "g2",
    "sections": [
        ("接続詞とは", """
<p>接続詞（せつぞくし）は、<strong>文と文（または単語と単語）をつなぐ</strong>役割をします。</p>
<table>
<tr><th>接続詞</th><th>意味</th><th>役割</th></tr>
<tr><td>and</td><td>〜と、そして</td><td>並列・追加</td></tr>
<tr><td>but</td><td>しかし</td><td>逆接</td></tr>
<tr><td>because</td><td>なぜなら</td><td>理由</td></tr>
<tr><td>so</td><td>なので</td><td>結果</td></tr>
<tr><td>when</td><td>〜するとき</td><td>時</td></tr>
<tr><td>if</td><td>もし〜なら</td><td>条件</td></tr>
<tr><td>that</td><td>〜ということ</td><td>内容</td></tr>
</table>
"""),
        ("and / but / because の使い方", """
<ul>
  <li><span class="example">I like cats and dogs.</span> <span class="example-jp">（猫と犬が好きです）</span></li>
  <li><span class="example">I like cats but I don't like dogs.</span> <span class="example-jp">（猫は好きですが犬は好きではありません）</span></li>
  <li><span class="example">I am happy because I got a present.</span> <span class="example-jp">（プレゼントをもらったので嬉しいです）</span></li>
  <li><span class="example">I was tired, so I went to bed.</span> <span class="example-jp">（疲れたので寝ました）</span></li>
</ul>
"""),
        ("when / if / that の使い方", """
<ul>
  <li><span class="example">Call me when you arrive.</span> <span class="example-jp">（着いたら電話してください）</span></li>
  <li><span class="example">If it rains, I will stay home.</span> <span class="example-jp">（雨が降れば家にいます）</span></li>
  <li><span class="example">I think that he is kind.</span> <span class="example-jp">（彼は親切だと思います）</span></li>
  <li><span class="example">I know that she is honest.</span> <span class="example-jp">（彼女が正直だと知っています）</span></li>
</ul>
"""),
        ("because と so の注意点", """
<div class="note"><strong>重要！</strong> because と so は同時に使えません。<br>「Because it rained, so I stayed home.」→ 間違い！<br>「Because it rained, I stayed home.」または「It rained, so I stayed home.」が正解。</div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>because と so の重複</strong> → どちらか一方だけ使う。</li>
  <li><strong>接続詞のあとの語順</strong> → if, when, because のあとは通常の語順（疑問文ではない）。</li>
  <li><strong>「I think he is kind.」の that 省略</strong> → that は会話ではよく省略される。「I think he is kind.」でOK。</li>
</ul></div>
"""),
    ]
},
"genkan2.html": {
    "title": "現在完了（経験用法）", "grade": "中学3年", "class": "g3",
    "sections": [
        ("経験用法とは", """
<p>現在完了の経験用法は「<strong>〜したことがある</strong>」という意味で、過去のある時点での経験を表します。</p>
<div class="highlight"><p>【公式】 主語 + have/has + (ever/never) + 過去分詞 + 〜<br>「〜したことがある / ない」</p></div>
"""),
        ("ever / never / before の使い方", """
<ul>
  <li><span class="example">Have you ever been to Kyoto?</span> <span class="example-jp">（今までに京都に行ったことがありますか？）</span></li>
  <li><span class="example">I have never eaten sushi.</span> <span class="example-jp">（寿司を食べたことがありません）</span></li>
  <li><span class="example">She has been to the US twice.</span> <span class="example-jp">（彼女はアメリカに2回行ったことがあります）</span></li>
  <li><span class="example">I have seen this movie before.</span> <span class="example-jp">（この映画を以前見たことがあります）</span></li>
  <li><span class="example">He has never been abroad.</span> <span class="example-jp">（彼は海外に行ったことがありません）</span></li>
</ul>
"""),
        ("been to と gone to の違い", """
<div class="highlight"><p><strong>been to</strong> = 行ったことがある（行って帰ってきている）<br><strong>gone to</strong> = 行ってしまっている（今ここにいない）</p></div>
<ul>
  <li><span class="example">I have been to Kyoto twice.</span> <span class="example-jp">（京都に2回行ったことがある←今ここにいる）</span></li>
  <li><span class="example">She has gone to Kyoto.</span> <span class="example-jp">（彼女は京都に行ってしまった←今ここにいない）</span></li>
</ul>
"""),
        ("経験を尋ねる・答える", """
<table>
<tr><th>質問</th><th>肯定の答え</th><th>否定の答え</th></tr>
<tr><td>Have you ever been to Kyoto?</td><td>Yes, I have. / Yes, twice.</td><td>No, I haven't. / No, never.</td></tr>
<tr><td>Has she ever eaten sushi?</td><td>Yes, she has.</td><td>No, she hasn't.</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have ever been to Kyoto.」</strong> → ever は疑問文で使う。肯定文では「I have been to Kyoto.」。</li>
  <li><strong>「How many times did you go?」</strong> → 経験を聞くときは現在完了。「How many times have you been?」。</li>
  <li><strong>been と gone の混同</strong> → been = 行って戻ってきた / gone = 行って戻っていない。</li>
</ul></div>
"""),
    ]
},
"gimonsi.html": {
    "title": "疑問詞", "grade": "中学1年", "class": "g1",
    "sections": [
        ("疑問詞とは", """
<p>疑問詞（ぎもんし）は、「何」「誰」「どこ」など、<strong>具体的な情報を尋ねるとき</strong>に使う特別な疑問文の言葉です。</p>
<table>
<tr><th>疑問詞</th><th>意味</th><th>例</th></tr>
<tr><td>what</td><td>何</td><td>What is this?</td></tr>
<tr><td>who</td><td>誰</td><td>Who is he?</td></tr>
<tr><td>where</td><td>どこ</td><td>Where are you from?</td></tr>
<tr><td>when</td><td>いつ</td><td>When is your birthday?</td></tr>
<tr><td>why</td><td>なぜ</td><td>Why are you late?</td></tr>
<tr><td>how</td><td>どのように</td><td>How are you?</td></tr>
</table>
"""),
        ("疑問詞を使った疑問文の語順", """
<div class="highlight"><p>【公式】 疑問詞 + 疑問文の語順（be動詞 + 主語 / do + 主語 + 動詞）？</p></div>
<ul>
  <li><span class="example">What is your name?</span> <span class="example-jp">（あなたの名前は何ですか？）</span></li>
  <li><span class="example">Where do you live?</span> <span class="example-jp">（どこに住んでいますか？）</span></li>
  <li><span class="example">When did you come to Japan?</span> <span class="example-jp">（いつ日本に来ましたか？）</span></li>
  <li><span class="example">How many books do you have?</span> <span class="example-jp">（何冊本を持っていますか？）</span></li>
  <li><span class="example">Why are you smiling?</span> <span class="example-jp">（なぜ笑っているのですか？）</span></li>
</ul>
"""),
        ("What と Who が主語になる場合", """
<p><strong>What / Who</strong> が主語になる場合は、<strong>疑問文の語順にならない</strong>（do/does は不要）。</p>
<ul>
  <li><span class="example">What happened yesterday?</span> <span class="example-jp">（昨日何が起こりましたか？）</span></li>
  <li><span class="example">Who came to the party?</span> <span class="example-jp">（誰がパーティーに来ましたか？）</span></li>
  <li><span class="example">What made you sad?</span> <span class="example-jp">（何があなたを悲しくさせましたか？）</span></li>
</ul>
<div class="note">主語を尋ねるときは、疑問詞 + 動詞 + 〜？の語順。do/does/did は不要！</div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「What this is?」</strong> → 疑問詞のあとは疑問文の語順。「What is this?」が正解。</li>
  <li><strong>「Who he is?」</strong> → 疑問文の語順「Who is he?」が正解。</li>
  <li><strong>主語を尋ねる文で do を使ってしまう</strong> → 「Who did come?」ではなく「Who came?」が正解。</li>
</ul></div>
"""),
    ]
},
"mirai.html": {
    "title": "未来形（will / be going to）", "grade": "中学2年", "class": "g2",
    "sections": [
        ("未来を表す2つの表現", """
<p>英語の未来を表す表現には <strong>will</strong> と <strong>be going to</strong> の2つがあります。意味の違いをしっかり理解しましょう。</p>
<div class="highlight"><p><strong>will</strong> = その場で決めたこと・予測・約束<br><strong>be going to</strong> = 前から決めていた予定・確実な未来</p></div>
"""),
        ("will の使い方", """
<div class="highlight"><p>【公式】 主語 + <strong>will</strong> + 動詞の原形<br>否定: will not (won't) / 疑問: Will + 主語？</p></div>
<ul>
  <li><span class="example">I will call you later.</span> <span class="example-jp">（あとで電話します）← その場の意思</span></li>
  <li><span class="example">It will rain tomorrow.</span> <span class="example-jp">（明日雨が降るでしょう）← 予測</span></li>
  <li><span class="example">I will help you.</span> <span class="example-jp">（手伝いますよ）← 約束</span></li>
  <li><span class="example">Will you open the window?</span> <span class="example-jp">（窓を開けてくれますか？）← 依頼</span></li>
</ul>
"""),
        ("be going to の使い方", """
<div class="highlight"><p>【公式】 主語 + <strong>be動詞 + going to</strong> + 動詞の原形<br>否定: be動詞 + not going to / 疑問: Be動詞 + 主語 + going to？</p></div>
<ul>
  <li><span class="example">I am going to visit Kyoto next month.</span> <span class="example-jp">（来月京都を訪れる予定です）</span></li>
  <li><span class="example">She is going to be a doctor.</span> <span class="example-jp">（彼女は医者になるつもりです）</span></li>
  <li><span class="example">Look at those clouds! It's going to rain.</span> <span class="example-jp">（あの雲を見て！雨が降りそうだ）</span></li>
</ul>
"""),
        ("will と be going to の比較", """
<table>
<tr><th></th><th>will</th><th>be going to</th></tr>
<tr><td>決定のタイミング</td><td>その場で決める</td><td>前から決めている</td></tr>
<tr><td>確実性</td><td>低い（予測・推量）</td><td>高い（確実・証拠あり）</td></tr>
<tr><td>例</td><td>I will have coffee.（決めた）</td><td>I am going to meet him at 3pm.（予定）</td></tr>
</table>
<div class="tip-box"><h3>💡 使い分けのコツ</h3><p>「さっき決めた」なら will / 「ずっと前から決めてた」なら be going to。</p></div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I will going to〜」</strong> → will と be going to は同時に使わない。</li>
  <li><strong>will の否定を間違える</strong> → will not の短縮形は won't。</li>
  <li><strong>未来のことなのに現在形を使う</strong> → 確定した予定以外は未来形を使う。</li>
</ul></div>
"""),
    ]
},
"bunsi.html": {
    "title": "分詞（現在分詞・過去分詞）", "grade": "中学3年", "class": "g3",
    "sections": [
        ("分詞とは", """
<p>分詞（ぶんし）は、動詞が形容詞の役割をしたものです。<strong>現在分詞（-ing）</strong>と<strong>過去分詞（-ed/不規則）</strong>の2種類があります。</p>
<div class="highlight"><p><strong>現在分詞</strong>（-ing）= 「〜している」（能動・進行）<br><strong>過去分詞</strong>（-ed/不規則）= 「〜される/された」（受動・完了）</p></div>
"""),
        ("現在分詞の用法", """
<p>「〜している」という能動の意味で名詞を修飾します。</p>
<ul>
  <li><span class="example">Look at the sleeping baby.</span> <span class="example-jp">（眠っている赤ちゃんを見て）</span></li>
  <li><span class="example">I know the girl singing in the room.</span> <span class="example-jp">（部屋で歌っている女の子を知っています）</span></li>
  <li><span class="example">There is a cat sleeping on the sofa.</span> <span class="example-jp">（ソファで寝ている猫がいます）</span></li>
  <li><span class="example">The boy running is my brother.</span> <span class="example-jp">（走っている少年は私の弟です）</span></li>
</ul>
"""),
        ("過去分詞の用法", """
<p>「〜される/された」という受動・完了の意味で名詞を修飾します。</p>
<ul>
  <li><span class="example">I have a broken watch.</span> <span class="example-jp">（壊れた時計を持っています）</span></li>
  <li><span class="example">This is a book written by Soseki.</span> <span class="example-jp">（これは漱石によって書かれた本です）</span></li>
  <li><span class="example">The window broken by the boy is new.</span> <span class="example-jp">（少年によって壊された窓は新品です）</span></li>
  <li><span class="example">This is a letter written in English.</span> <span class="example-jp">（これは英語で書かれた手紙です）</span></li>
</ul>
"""),
        ("現在分詞 vs 過去分詞", """
<table>
<tr><th></th><th>現在分詞（-ing）</th><th>過去分詞（-ed/不規則）</th></tr>
<tr><td>意味</td><td>「〜している」（能動）</td><td>「〜される/された」（受動）</td></tr>
<tr><td>例1</td><td>boiling water（沸騰している水）</td><td>boiled water（沸騰した水）</td></tr>
<tr><td>例2</td><td>a boring movie（退屈な映画）</td><td>a bored student（退屈している生徒）</td></tr>
</table>
<div class="tip-box"><h3>💡 覚え方</h3><p>現在分詞 = 「〜させる」能動の意味（物・事が主語）<br>過去分詞 = 「〜させられる」受動の意味（人が主語）</p></div>
"""),
        ("分詞の位置", """
<table>
<tr><th>位置</th><th>説明</th><th>例</th></tr>
<tr><td>名詞の前</td><td>1語の分詞</td><td>a sleeping cat, a broken watch</td></tr>
<tr><td>名詞の後ろ</td><td>2語以上の分詞句</td><td>a cat sleeping on the sofa</td></tr>
</table>
"""),
    ]
},
"can.html": {
    "title": "can（助動詞）", "grade": "中学1年", "class": "g1",
    "sections": [
        ("canの意味と公式", """
<p>can は「<strong>〜できる</strong>」という能力や可能性を表す助動詞です。助動詞なので、あとは<strong>動詞の原形</strong>がきます。</p>
<div class="highlight"><p>【公式】 主語 + <strong>can</strong> + 動詞の原形 + 〜</p></div>
<ul>
  <li><span class="example">I can swim.</span> <span class="example-jp">（泳げます）</span></li>
  <li><span class="example">She can speak French.</span> <span class="example-jp">（彼女はフランス語を話せます）</span></li>
  <li><span class="example">He can run fast.</span> <span class="example-jp">（彼は速く走れます）</span></li>
  <li><span class="example">My father can cook well.</span> <span class="example-jp">（父は料理が上手です）</span></li>
</ul>
"""),
        ("否定文・疑問文", """
<div class="highlight"><p><strong>否定文</strong>: 主語 + can not (can't) + 動詞の原形<br><strong>疑問文</strong>: Can + 主語 + 動詞の原形？</p></div>
<ul>
  <li><span class="example">I can't play the piano.</span> <span class="example-jp">（ピアノを弾けません）</span></li>
  <li><span class="example">Can you help me?</span> <span class="example-jp">（手伝ってくれますか？）</span></li>
  <li><span class="example">Can I use your pen?</span> <span class="example-jp">（ペンを使ってもいいですか？）</span></li>
  <li><span class="example">Yes, I can. / No, I can't.</span> <span class="example-jp">（はい / いいえ）</span></li>
</ul>
"""),
        ("can の3つの意味", """
<table>
<tr><th>意味</th><th>例文</th><th>日本語</th></tr>
<tr><td>能力</td><td>I can swim.</td><td>泳ぐことができる</td></tr>
<tr><td>許可</td><td>Can I sit here?</td><td>座ってもいいですか？</td></tr>
<tr><td>依頼</td><td>Can you help me?</td><td>手伝ってくれますか？</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I can swimming.」</strong> → can のあとは動詞の原形。「I can swim.」が正解。</li>
  <li><strong>「I can to swim.」</strong> → can のあとに to は不要。</li>
  <li><strong>「I can not swim.」と「I cannot swim.」</strong> → can not は1語で cannot（can't）と書くのが正式。</li>
</ul></div>
"""),
    ]
},
"daimeisi.html": {
    "title": "代名詞", "grade": "中学1年", "class": "g1",
    "sections": [
        ("人称代名詞の変化", """
<p>代名詞（だいめいし）は、<strong>人名や物名の代わりに使う言葉</strong>です。主格・所有格・目的格・所有代名詞の4つに変化します。</p>
<table>
<tr><th>主格（〜は）</th><th>所有格（〜の）</th><th>目的格（〜を）</th><th>所有代名詞（〜のもの）</th></tr>
<tr><td>I</td><td>my</td><td>me</td><td>mine</td></tr>
<tr><td>you</td><td>your</td><td>you</td><td>yours</td></tr>
<tr><td>he</td><td>his</td><td>him</td><td>his</td></tr>
<tr><td>she</td><td>her</td><td>her</td><td>hers</td></tr>
<tr><td>it</td><td>its</td><td>it</td><td>its</td></tr>
<tr><td>we</td><td>our</td><td>us</td><td>ours</td></tr>
<tr><td>they</td><td>their</td><td>them</td><td>theirs</td></tr>
</table>
"""),
        ("主格・所有格・目的格の使い分け", """
<ul>
  <li><span class="example">She is my friend.</span> <span class="example-jp">（she=主格「彼女は」, my=所有格「私の」）</span></li>
  <li><span class="example">I like her.</span> <span class="example-jp">（her=目的格「彼女を」）</span></li>
  <li><span class="example">This is his book.</span> <span class="example-jp">（his=所有格「彼の」）</span></li>
  <li><span class="example">Give it to me.</span> <span class="example-jp">（me=目的格「私に」）</span></li>
  <li><span class="example">They are our teachers.</span> <span class="example-jp">（our=所有格「私たちの」）</span></li>
</ul>
"""),
        ("所有代名詞", """
<p>「所有格 + 名詞」を1つの単語にしたものが所有代名詞です。</p>
<ul>
  <li><span class="example">This is my pen. = This pen is mine.</span> <span class="example-jp">（このペンは私のものです）</span></li>
  <li><span class="example">That is your book. = That book is yours.</span> <span class="example-jp">（あの本はあなたのものです）</span></li>
  <li><span class="example">These are her keys. = These keys are hers.</span> <span class="example-jp">（これらの鍵は彼女のものです）</span></li>
  <li><span class="example">This is our classroom. = This classroom is ours.</span> <span class="example-jp">（この教室は私たちのものです）</span></li>
</ul>
<div class="note"><strong>覚え方</strong>：my → mine, your → yours, her → hers, our → ours, their → theirs<br>his / its は形が同じ！</div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I like he.」</strong> → 目的格は him。「I like him.」が正解。</li>
  <li><strong>「This is mine book.」</strong> → 所有代名詞のあとに名詞は不要。「This is my book.」か「This book is mine.」。</li>
  <li><strong>「Give me it.」</strong> → 「Give it to me.」が正しい語順。</li>
</ul></div>
"""),
    ]
},
"kankeisi1.html": {
    "title": "関係代名詞", "grade": "中学3年", "class": "g3",
    "sections": [
        ("関係代名詞とは", """
<p>関係代名詞（かんけいだいめいし）は、<strong>名詞を後ろから説明する</strong>ための言葉です。2つの文を1つにつなげます。</p>
<div class="highlight"><p><strong>who</strong> = 人（主格）/ <strong>which</strong> = 物・動物（主格）/ <strong>that</strong> = 人・物どちらでも</p></div>
"""),
        ("主格の関係代名詞", """
<div class="highlight"><p>【公式】 先行詞 + <strong>who/which/that</strong> + 動詞</p></div>
<ul>
  <li><span class="example">I know the boy who is running.</span> <span class="example-jp">（走っている少年を知っています）</span></li>
  <li><span class="example">This is the book which is popular.</span> <span class="example-jp">（これは人気のある本です）</span></li>
  <li><span class="example">She is the girl that plays the piano well.</span> <span class="example-jp">（彼女はピアノが上手な女の子です）</span></li>
  <li><span class="example">I have a dog that can run fast.</span> <span class="example-jp">（私は速く走れる犬を飼っています）</span></li>
</ul>
"""),
        ("目的格の関係代名詞", """
<div class="highlight"><p>【公式】 先行詞 + <strong>whom/which/that</strong> + 主語 + 動詞</p></div>
<ul>
  <li><span class="example">He is the man (whom) I met yesterday.</span> <span class="example-jp">（彼は昨日私が会った男性です）</span></li>
  <li><span class="example">This is the car (which) he bought.</span> <span class="example-jp">（これは彼が買った車です）</span></li>
  <li><span class="example">The book (that) I read was interesting.</span> <span class="example-jp">（私が読んだ本は面白かった）</span></li>
</ul>
<div class="note"><strong>目的格の関係代名詞は省略できる！</strong> 会話ではよく省略します。</div>
"""),
        ("関係代名詞の使い分け表", """
<table>
<tr><th>先行詞</th><th>主格</th><th>目的格</th><th>例</th></tr>
<tr><td>人</td><td>who</td><td>whom</td><td>the boy who / (whom)</td></tr>
<tr><td>物・動物</td><td>which</td><td>which</td><td>the book which</td></tr>
<tr><td>人・物両方</td><td>that</td><td>that</td><td>the book / boy that</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「The boy who he is running.」</strong> → 関係代名詞のあとに同じ先行詞を繰り返さない。</li>
  <li><strong>人に which を使ってしまう</strong> → 人には who。which は物・動物に使う。</li>
  <li><strong>目的格の関係代名詞で主格の語順を使ってしまう</strong> → 「This is the book which I bought.」が正解。</li>
</ul></div>
"""),
    ]
},
"ukemi.html": {
    "title": "受け身（受動態）", "grade": "中学2年", "class": "g2",
    "sections": [
        ("受け身とは", """
<p>受け身（受動態）は「<strong>〜される</strong>」という意味を表します。動作をする側ではなく、<strong>動作を受ける側</strong>が主語になります。</p>
<div class="highlight"><p>【公式】 主語 + be動詞 + 過去分詞 + (by 〜)<br>「〜によって〜される」</p></div>
"""),
        ("能動態から受動態への書き換え", """
<table>
<tr><th>能動態</th><th>→</th><th>受動態</th></tr>
<tr><td>The boy <strong>broke</strong> the window.</td><td>→</td><td>The window <strong>was broken</strong> by the boy.</td></tr>
<tr><td>My mother <strong>made</strong> this cake.</td><td>→</td><td>This cake <strong>was made</strong> by my mother.</td></tr>
<tr><td>Many people <strong>speak</strong> English.</td><td>→</td><td>English <strong>is spoken</strong> by many people.</td></tr>
</table>
<div class="tip-box"><h3>💡 書き換えの手順</h3><p>① 目的語を主語にする<br>② 動詞を be動詞 + 過去分詞にする（時制に注意）<br>③ 元の主語を by のあとに置く</p></div>
"""),
        ("時制ごとの受け身", """
<table>
<tr><th>時制</th><th>能動態</th><th>受動態</th></tr>
<tr><td>現在</td><td>He cleans the room.</td><td>The room <strong>is cleaned</strong>.</td></tr>
<tr><td>過去</td><td>He cleaned the room.</td><td>The room <strong>was cleaned</strong>.</td></tr>
<tr><td>未来</td><td>He will clean the room.</td><td>The room <strong>will be cleaned</strong>.</td></tr>
<tr><td>現在完了</td><td>He has cleaned the room.</td><td>The room <strong>has been cleaned</strong>.</td></tr>
<tr><td>助動詞</td><td>He must clean the room.</td><td>The room <strong>must be cleaned</strong>.</td></tr>
</table>
"""),
        ("by が不要な場合", """
<p>行為者が「一般の人々」や「不明」の場合は by 〜を省略します。</p>
<ul>
  <li><span class="example">English is spoken in many countries.</span> <span class="example-jp">（英語は多くの国で話されています）</span></li>
  <li><span class="example">The door is opened at seven.</span> <span class="example-jp">（ドアは7時に開けられます）</span></li>
  <li><span class="example">This temple was built 400 years ago.</span> <span class="example-jp">（この寺は400年前に建てられました）</span></li>
</ul>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>be動詞を忘れる</strong> → 「This book written by〜」ではなく「This book <strong>was</strong> written by〜」。</li>
  <li><strong>過去形と過去分詞の混同</strong> → 能動態は過去形（wrote）、受動態は過去分詞（written）。</li>
  <li><strong>「The window broke by the boy.」</strong> → 能動態のまま主語だけ変えない。動詞も変える。</li>
</ul></div>
"""),
    ]
},
"genkan1.html": {
    "title": "現在完了（継続用法）", "grade": "中学3年", "class": "g3",
    "sections": [
        ("現在完了（継続）とは", """
<p>現在完了の継続用法は「<strong>ずっと〜している</strong>」という意味を表します。過去のある時点から現在まで続いている状態を表します。</p>
<div class="highlight"><p>【公式】 主語 + have/has + 過去分詞 + <strong>for / since</strong> + 期間<br>「ずっと〜している」</p></div>
"""),
        ("for と since の違い", """
<table>
<tr><th>前置詞</th><th>意味</th><th>例</th></tr>
<tr><td><strong>for</strong></td><td>〜の間（期間の長さ）</td><td>for three years（3年間）</td></tr>
<tr><td><strong>since</strong></td><td>〜から（起点）</td><td>since 2020（2020年から）</td></tr>
</table>
<ul>
  <li><span class="example">I have lived in Tokyo for five years.</span> <span class="example-jp">（東京に5年間住んでいます）</span></li>
  <li><span class="example">She has studied English since she was ten.</span> <span class="example-jp">（彼女は10歳から英語を勉強しています）</span></li>
  <li><span class="example">He has been sick since Monday.</span> <span class="example-jp">（彼は月曜から病気です）</span></li>
</ul>
<div class="tip-box"><h3>💡 for と since の見分け方</h3><p><strong>for</strong> = 数字が入る（for 2 hours, for 3 years）<br><strong>since</strong> = 時点（since 2020, since Monday, since I was born）</p></div>
"""),
        ("現在完了 vs 過去形（継続）", """
<table>
<tr><th></th><th>現在完了（継続）</th><th>過去形</th></tr>
<tr><td>焦点</td><td>今も続いている</td><td>過去に終わった</td></tr>
<tr><td>例</td><td>I have lived here for 5 years.（今も住んでいる）</td><td>I lived there for 5 years.（もう住んでいない）</td></tr>
<tr><td>共起語</td><td>for, since, how long</td><td>yesterday, last〜, ago</td></tr>
</table>
"""),
        ("否定文・疑問文", """
<ul>
  <li><span class="example">I have not seen him since last week.</span> <span class="example-jp">（先週から彼に会っていません）</span></li>
  <li><span class="example">How long have you lived here?</span> <span class="example-jp">（どのくらいここに住んでいますか？）</span></li>
  <li><span class="example">Has she been a teacher for 10 years?</span> <span class="example-jp">（彼女は10年間先生ですか？）</span></li>
</ul>
"""),
    ]
},
"doumei.html": {
    "title": "動名詞", "grade": "中学2年", "class": "g2",
    "sections": [
        ("動名詞とは", """
<p>動名詞（どうめいし）は「<strong>動詞の原形 + ing</strong>」の形で、文中で<strong>名詞の役割</strong>をします。「〜すること」という意味です。</p>
<div class="highlight"><p>【公式】 動詞の原形 + <strong>ing</strong> = 動名詞<br>「〜すること」</p></div>
"""),
        ("動名詞の基本的な使い方", """
<ul>
  <li><span class="example">I like swimming.</span> <span class="example-jp">（泳ぐことが好きです）</span></li>
  <li><span class="example">Playing tennis is fun.</span> <span class="example-jp">（テニスをすることは楽しいです）</span></li>
  <li><span class="example">He enjoys reading books.</span> <span class="example-jp">（彼は本を読むことを楽しみます）</span></li>
  <li><span class="example">I finished doing my homework.</span> <span class="example-jp">（宿題をするのを終えました）</span></li>
  <li><span class="example">She is good at singing.</span> <span class="example-jp">（彼女は歌うことが得意です）</span></li>
  <li><span class="example">I stopped smoking.</span> <span class="example-jp">（タバコを吸うのをやめました）</span></li>
</ul>
"""),
        ("動名詞を目的語にとる動詞", """
<table>
<tr><th>動詞</th><th>意味</th><th>例</th></tr>
<tr><td>enjoy</td><td>楽しむ</td><td>enjoy reading</td></tr>
<tr><td>finish</td><td>終える</td><td>finish doing</td></tr>
<tr><td>stop</td><td>やめる</td><td>stop smoking</td></tr>
<tr><td>like / love</td><td>好き</td><td>like swimming</td></tr>
<tr><td>dislike / hate</td><td>嫌い</td><td>hate waiting</td></tr>
<tr><td>give up</td><td>あきらめる</td><td>give up playing</td></tr>
</table>
"""),
        ("不定詞との違い", """
<table>
<tr><th></th><th>動名詞（doing）</th><th>不定詞（to do）</th></tr>
<tr><td>enjoy</td><td>⭕ enjoy doing</td><td>❌ enjoy to do</td></tr>
<tr><td>want</td><td>❌ want doing</td><td>⭕ want to do</td></tr>
<tr><td>like</td><td>⭕ like doing（習慣）</td><td>⭕ like to do（特定）</td></tr>
<tr><td>stop</td><td>stop doing（やめる）</td><td>stop to do（やめて〜する）</td></tr>
</table>
<div class="tip-box"><h3>💡 stop の違いが超重要！</h3><p>stop smoking = タバコを吸うのを「やめる」<br>stop to smoke = 「立ち止まって」タバコを吸う</p></div>
"""),
    ]
},
"jyodosi.html": {
    "title": "助動詞", "grade": "中学2年", "class": "g2",
    "sections": [
        ("助動詞とは", """
<p>助動詞（じょどうし）は動詞の前に置いて、意味を付け加える言葉です。助動詞のあとは必ず<strong>動詞の原形</strong>になります。</p>
<div class="highlight"><p>【公式】 助動詞 + <strong>動詞の原形</strong><br><strong>can</strong>（できる）/ <strong>must</strong>（しなければならない）/ <strong>may</strong>（してもよい）/ <strong>should</strong>（すべき）</p></div>
"""),
        ("must / have to（義務）", """
<table>
<tr><th>助動詞</th><th>意味</th><th>例</th></tr>
<tr><td>must</td><td>〜しなければならない</td><td>You must study harder.</td></tr>
<tr><td>have to</td><td>〜しなければならない</td><td>I have to go now.</td></tr>
</table>
<div class="tip-box"><h3>💡 must vs have to</h3><p><strong>must</strong> = 話し手の強い意志・義務（自分でそう思う）<br><strong>have to</strong> = 外部のルール・状況（仕方なく）</p></div>
"""),
        ("must not / don't have to（禁止・不要）", """
<table>
<tr><th>表現</th><th>意味</th><th>例</th></tr>
<tr><td>must not</td><td>〜してはいけない（禁止）</td><td>You must not run here.</td></tr>
<tr><td>don't have to</td><td>〜する必要はない（不要）</td><td>You don't have to go.</td></tr>
</table>
<div class="note"><strong>超重要！</strong> must not = 禁止（絶対ダメ）/ don't have to = 必要ない（やらなくてもOK）。全く別の意味！</div>
"""),
        ("may（許可）・should（助言）", """
<ul>
  <li><span class="example">May I come in?</span> <span class="example-jp">（入ってもいいですか？）</span></li>
  <li><span class="example">May I use your phone?</span> <span class="example-jp">（電話を使ってもいいですか？）</span></li>
  <li><span class="example">You should rest.</span> <span class="example-jp">（休むべきです）</span></li>
  <li><span class="example">We should help each other.</span> <span class="example-jp">（お互いに助け合うべきです）</span></li>
  <li><span class="example">You should not eat too much.</span> <span class="example-jp">（食べ過ぎるべきではありません）</span></li>
</ul>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「must」と「have to」の混同</strong> → must = 話し手の意志、have to = 外部のルール。</li>
  <li><strong>「must not」と「don't have to」の混同</strong> → must not = 禁止、don't have to = 必要ない。</li>
  <li><strong>助動詞のあとに to をつける</strong> → must to go は間違い。must go が正解。</li>
</ul></div>
"""),
    ]
},
"hikaku1.html": {
    "title": "比較（比較級・最上級）", "grade": "中学2年", "class": "g2",
    "sections": [
        ("比較とは", """
<p>比較（ひかく）は、ものや人の性質・状態を<strong>比べる</strong>表現です。3つのパターンがあります。</p>
<div class="highlight"><p><strong>比較級</strong> = 「より〜」（2つのものを比べる）<br><strong>最上級</strong> = 「一番〜」（3つ以上の中で）<br><strong>原級</strong> = 「〜と同じくらい」（同等比較）</p></div>
"""),
        ("比較級（〜er / more）", """
<div class="highlight"><p>【公式】 形容詞/副詞 + <strong>-er / more</strong> + than<br>「〜より…」</p></div>
<ul>
  <li><span class="example">Taro is taller than Jiro.</span> <span class="example-jp">（太郎は次郎より背が高い）</span></li>
  <li><span class="example">She is more beautiful than me.</span> <span class="example-jp">（彼女は私より美しい）</span></li>
  <li><span class="example">This book is more interesting than that one.</span> <span class="example-jp">（この本はあの本より面白い）</span></li>
  <li><span class="example">He runs faster than me.</span> <span class="example-jp">（彼は私より速く走る）</span></li>
</ul>
<div class="note"><strong>短い語（1〜2音節）</strong> → -er（tall→taller）<br><strong>長い語（3音節以上）</strong> → more（beautiful→more beautiful）</div>
"""),
        ("最上級（the 〜est / the most）", """
<div class="highlight"><p>【公式】 the + 形容詞/副詞 + <strong>-est / most</strong> + in/of<br>「〜の中で一番…」</p></div>
<ul>
  <li><span class="example">Mt. Fuji is the highest mountain in Japan.</span> <span class="example-jp">（富士山は日本で一番高い山です）</span></li>
  <li><span class="example">She is the most popular singer in Japan.</span> <span class="example-jp">（彼女は日本で一番人気の歌手です）</span></li>
  <li><span class="example">He is the tallest in his class.</span> <span class="example-jp">（彼はクラスで一番背が高い）</span></li>
</ul>
"""),
        ("原級（as 〜 as）", """
<div class="highlight"><p>【公式】 as + 原級 + <strong>as</strong>（肯定）/ not as + 原級 + as（否定）<br>「〜と同じくらい… / ほど…ではない」</p></div>
<ul>
  <li><span class="example">He is as tall as me.</span> <span class="example-jp">（彼は私と同じくらい背が高い）</span></li>
  <li><span class="example">This book is not as interesting as that one.</span> <span class="example-jp">（この本はあの本ほど面白くない）</span></li>
</ul>
"""),
        ("不規則変化", """
<table>
<tr><th>原級</th><th>比較級</th><th>最上級</th></tr>
<tr><td>good / well</td><td>better</td><td>best</td></tr>
<tr><td>bad / ill</td><td>worse</td><td>worst</td></tr>
<tr><td>many / much</td><td>more</td><td>most</td></tr>
<tr><td>little</td><td>less</td><td>least</td></tr>
</table>
<div class="tip-box"><h3>💡 不規則変化は暗記必須！</h3><p>good→better→best の3段階セットで覚えましょう。</p></div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「more taller」</strong> → 比較級は -er か more のどちらか。両方は使わない。</li>
  <li><strong>最上級に the をつけ忘れる</strong> → the tallest / the most beautiful。</li>
  <li><strong>「as tall as me」を「as tall as I」と書く</strong> → 会話では me でOK。テストでは「as tall as I (am)」が正式。</li>
</ul></div>
"""),
    ]
},
"zensi.html": {
    "title": "前置詞", "grade": "中学2年", "class": "g2",
    "sections": [
        ("前置詞とは", """
<p>前置詞（ぜんちし）は、名詞や代名詞の前に置いて、<strong>位置・方向・時間・手段</strong>などを表す言葉です。</p>
<div class="highlight"><p>【場所の前置詞】 in, on, at, under, behind, between, in front of<br>【時間の前置詞】 in, on, at, before, after, during<br>【その他】 for, with, by, from, to, of</p></div>
"""),
        ("場所の前置詞", """
<table>
<tr><th>前置詞</th><th>意味</th><th>例</th></tr>
<tr><td>in</td><td>〜の中に</td><td>in the box</td></tr>
<tr><td>on</td><td>〜の上に</td><td>on the desk</td></tr>
<tr><td>at</td><td>〜のところに</td><td>at the station</td></tr>
<tr><td>under</td><td>〜の下に</td><td>under the bed</td></tr>
<tr><td>behind</td><td>〜の後ろに</td><td>behind the door</td></tr>
<tr><td>between</td><td>〜の間に</td><td>between A and B</td></tr>
<tr><td>in front of</td><td>〜の前に</td><td>in front of the school</td></tr>
</table>
<ul>
  <li><span class="example">The cat is under the table.</span> <span class="example-jp">（猫はテーブルの下です）</span></li>
  <li><span class="example">There is a bank behind the station.</span> <span class="example-jp">（駅の後ろに銀行があります）</span></li>
</ul>
"""),
        ("時間の前置詞", """
<table>
<tr><th>前置詞</th><th>使う場面</th><th>例</th></tr>
<tr><td>in</td><td>月・年・季節・朝昼夜</td><td>in May, in 2024, in summer, in the morning</td></tr>
<tr><td>on</td><td>曜日・日付・特定の日</td><td>on Sunday, on May 5th, on my birthday</td></tr>
<tr><td>at</td><td>時刻・夜・特定の時点</td><td>at 8 o'clock, at noon, at night, at midnight</td></tr>
</table>
<ul>
  <li><span class="example">I get up at six every morning.</span> <span class="example-jp">（毎朝6時に起きます）</span></li>
  <li><span class="example">She was born on April 1st.</span> <span class="example-jp">（彼女は4月1日に生まれました）</span></li>
  <li><span class="example">It is hot in summer.</span> <span class="example-jp">（夏は暑いです）</span></li>
</ul>
"""),
        ("その他の重要な前置詞", """
<ul>
  <li><span class="example">I studied English for two hours.</span> <span class="example-jp">（2時間英語を勉強しました）← 期間</span></li>
  <li><span class="example">I go to school by bus.</span> <span class="example-jp">（バスで学校に行きます）← 手段</span></li>
  <li><span class="example">This cake was made by my mother.</span> <span class="example-jp">（このケーキは母によって作られました）← 行為者</span></li>
  <li><span class="example">I went to the park with my friend.</span> <span class="example-jp">（友達と公園に行きました）← 同伴</span></li>
  <li><span class="example">I'm from Japan.</span> <span class="example-jp">（日本出身です）← 出身</span></li>
</ul>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「on May」</strong> → 月には in を使う。「in May」が正解。on は日付。</li>
  <li><strong>「at the morning」</strong> → 「in the morning」が正解。</li>
  <li><strong>「in Sunday」</strong> → 曜日には on を使う。「on Sunday」が正解。</li>
  <li><strong>前置詞の使い分け（in/on/at）</strong> → in=広い範囲、on=面、at=点でイメージすると覚えやすい。</li>
</ul></div>
"""),
    ]
},
"suryo.html": {
    "title": "数量詞（many, much, a lot of など）", "grade": "中学1年", "class": "g1",
    "sections": [
        ("数量詞とは", """
<p>数量詞（すうりょうし）は、ものの「量」や「数」を表す言葉です。<strong>可算名詞（数えられる名詞）</strong>と<strong>不可算名詞（数えられない名詞）</strong>で使える数量詞が異なります。</p>
<div class="highlight"><p><strong>可算名詞</strong>（数えられる）：book, cat, apple, student<br><strong>不可算名詞</strong>（数えられない）：water, money, information, time</p></div>
"""),
        ("many / much / a lot of", """
<table>
<tr><th>数量詞</th><th>意味</th><th>使える名詞</th><th>例</th></tr>
<tr><td>many</td><td>たくさんの</td><td>可算名詞</td><td>many books, many students</td></tr>
<tr><td>much</td><td>たくさんの</td><td>不可算名詞</td><td>much water, much money</td></tr>
<tr><td>a lot of / lots of</td><td>たくさんの</td><td>両方OK</td><td>a lot of people / water</td></tr>
</table>
<ul>
  <li><span class="example">There are many books on the desk.</span> <span class="example-jp">（机の上にたくさんの本がある）</span></li>
  <li><span class="example">I don't have much money.</span> <span class="example-jp">（あまりお金を持っていない）</span></li>
  <li><span class="example">There are a lot of people in the park.</span> <span class="example-jp">（公園にたくさんの人がいる）</span></li>
</ul>
<div class="note"><strong>注意！</strong> much は否定文・疑問文でよく使われる。肯定文では a lot of のほうが自然。</div>
"""),
        ("few / a few / little / a little", """
<table>
<tr><th>数量詞</th><th>意味</th><th>ニュアンス</th><th>名詞の種類</th><th>例</th></tr>
<tr><td>few</td><td>ほとんどない</td><td>否定的</td><td>可算</td><td>few friends</td></tr>
<tr><td>a few</td><td>いくつかある</td><td>肯定的</td><td>可算</td><td>a few friends</td></tr>
<tr><td>little</td><td>ほとんどない</td><td>否定的</td><td>不可算</td><td>little water</td></tr>
<tr><td>a little</td><td>少しある</td><td>肯定的</td><td>不可算</td><td>a little water</td></tr>
</table>
<div class="tip-box"><h3>💡 few / a few の覚え方</h3><p><strong>a few</strong> = a がある = 肯定的（いくつかある）<br><strong>few</strong> = a がない = 否定的（ほとんどない）</p></div>
"""),
        ("some / any", """
<table>
<tr><th>単語</th><th>使う文</th><th>例</th></tr>
<tr><td>some</td><td>肯定文・勧誘の疑問文</td><td>I have some friends. / Would you like some coffee?</td></tr>
<tr><td>any</td><td>疑問文・否定文</td><td>Do you have any questions? / I don't have any money.</td></tr>
</table>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「many water」</strong> → water は不可算名詞。many は可算名詞専用。「much water」が正解。</li>
  <li><strong>「much books」</strong> → books は可算名詞。「many books」が正解。</li>
  <li><strong>few と a few の混同</strong> → few = ほとんどない（否定）、a few = いくつかある（肯定）。</li>
</ul></div>
"""),
    ]
},
"futeisi2.html": {
    "title": "不定詞（応用）", "grade": "中学3年", "class": "g3",
    "sections": [
        ("不定詞の応用とは", """
<p>不定詞の応用では、<strong>「It is 〜 to」「too 〜 to」「enough to」</strong> などの構文を学びます。受験で頻出の重要単元です。</p>
<div class="highlight"><p>① It is + 形容詞 + for + 人 + to do（人が〜することは〜だ）<br>② too + 形容詞 + to do（〜すぎてできない）<br>③ 形容詞 + enough + to do（〜するのに十分〜だ）</p></div>
"""),
        ("It is 〜 for 人 to do", """
<p>「人が〜することは〜だ」という意味。it は仮主語で、本当の主語は to 以下です。</p>
<div class="highlight"><p>【公式】 It is + 形容詞 + <strong>for 人</strong> + to do</p></div>
<ul>
  <li><span class="example">It is important for us to study English.</span> <span class="example-jp">（私たちが英語を勉強することは重要です）</span></li>
  <li><span class="example">It is easy for her to solve this problem.</span> <span class="example-jp">（彼女がこの問題を解くのは簡単です）</span></li>
  <li><span class="example">It is difficult for me to run fast.</span> <span class="example-jp">（私が速く走るのは難しいです）</span></li>
  <li><span class="example">It is fun for us to play tennis.</span> <span class="example-jp">（私たちがテニスをするのは楽しいです）</span></li>
</ul>
"""),
        ("too 〜 to 構文", """
<p>「あまりにも〜すぎて…できない」という否定の意味になります。</p>
<div class="highlight"><p>【公式】 <strong>too + 形容詞/副詞 + to do</strong><br>「〜すぎてできない」</p></div>
<ul>
  <li><span class="example">This box is too heavy for me to carry.</span> <span class="example-jp">（この箱は重すぎて私には運べません）</span></li>
  <li><span class="example">She is too young to drive a car.</span> <span class="example-jp">（彼女は若すぎて車を運転できません）</span></li>
  <li><span class="example">I was too tired to study.</span> <span class="example-jp">（疲れすぎて勉強できませんでした）</span></li>
</ul>
"""),
        ("enough to 構文", """
<p>「〜するのに十分〜だ」という意味です。</p>
<div class="highlight"><p>【公式】 <strong>形容詞/副詞 + enough + to do</strong><br>「〜するのに十分〜だ」</p></div>
<ul>
  <li><span class="example">He is old enough to drive a car.</span> <span class="example-jp">（彼は車を運転するのに十分な年齢です）</span></li>
  <li><span class="example">I have enough money to buy the book.</span> <span class="example-jp">（その本を買うのに十分なお金があります）</span></li>
  <li><span class="example">She is strong enough to carry the box.</span> <span class="example-jp">（彼女はその箱を運ぶのに十分強いです）</span></li>
</ul>
<div class="note"><strong>enough の位置に注意！</strong><br>形容詞の後ろ：old enough「十分な年齢」<br>名詞の前：enough money「十分なお金」</div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「too 〜 to」構文の否定を間違う</strong> → too 自体に否定の意味が含まれているので、さらに not は不要。</li>
  <li><strong>「It is important for study.」</strong> → for のあとは人を置く。「It is important to study.」が正解。</li>
  <li><strong>enough の位置を間違える</strong> → enough は形容詞の後ろに置く（old enough）。</li>
</ul></div>
"""),
    ]
},
"futeisi1.html": {
    "title": "不定詞（基本）", "grade": "中学2年", "class": "g2",
    "sections": [
        ("不定詞とは", """
<p>不定詞（ふていし）は「<strong>to + 動詞の原形</strong>」の形で、文中で<strong>名詞・副詞・形容詞</strong>の3つの役割をします。</p>
<div class="highlight"><p>【公式】 <strong>to + 動詞の原形</strong><br>① 名詞的用法：「〜すること」<br>② 副詞的用法：「〜するために」<br>③ 形容詞的用法：「〜するための」</p></div>
"""),
        ("名詞的用法（〜すること）", """
<p>不定詞が文の<strong>主語・目的語・補語</strong>の位置にきて「〜すること」という意味になります。</p>
<ul>
  <li><span class="example">I want to study English.</span> <span class="example-jp">（英語を勉強したい）← want の目的語</span></li>
  <li><span class="example">To play tennis is fun.</span> <span class="example-jp">（テニスをすることは楽しい）← 主語</span></li>
  <li><span class="example">My dream is to be a doctor.</span> <span class="example-jp">（私の夢は医者になることです）← 補語</span></li>
  <li><span class="example">I hope to see you again.</span> <span class="example-jp">（また会えることを望みます）</span></li>
</ul>
<div class="note"><strong>want to = 〜したい</strong> は中学英語で最も使う表現の一つ！</div>
"""),
        ("副詞的用法（〜するために）", """
<p>不定詞が動詞を修飾し「〜するために」という目的を表します。</p>
<ul>
  <li><span class="example">I went to Kyoto to see temples.</span> <span class="example-jp">（お寺を見るために京都に行きました）</span></li>
  <li><span class="example">She studied hard to pass the exam.</span> <span class="example-jp">（試験に合格するために一生懸命勉強した）</span></li>
  <li><span class="example">He came to meet me.</span> <span class="example-jp">（彼は私に会うために来ました）</span></li>
  <li><span class="example">I woke up early to catch the train.</span> <span class="example-jp">（電車に間に合うように早く起きました）</span></li>
</ul>
"""),
        ("形容詞的用法（〜するための）", """
<p>不定詞が名詞を修飾し「〜するための」「〜すべき」という意味を加えます。</p>
<ul>
  <li><span class="example">I have something to do.</span> <span class="example-jp">（やるべきことがあります）</span></li>
  <li><span class="example">I want something to drink.</span> <span class="example-jp">（何か飲むものが欲しい）</span></li>
  <li><span class="example">She has a lot of homework to do.</span> <span class="example-jp">（彼女にはやるべき宿題がたくさんある）</span></li>
  <li><span class="example">I need a pen to write with.</span> <span class="example-jp">（書くためのペンが必要です）</span></li>
</ul>
"""),
        ("動名詞との違い", """
<table>
<tr><th></th><th>不定詞（to do）</th><th>動名詞（doing）</th></tr>
<tr><td>意味</td><td>「〜すること」（未来志向）</td><td>「〜すること」（過去・習慣）</td></tr>
<tr><td>want + 〜</td><td>want to do ⭕</td><td>want doing ❌</td></tr>
<tr><td>enjoy + 〜</td><td>enjoy to do ❌</td><td>enjoy doing ⭕</td></tr>
<tr><td>like + 〜</td><td>like to do ⭕</td><td>like doing ⭕</td></tr>
</table>
<div class="tip-box"><h3>💡 覚え方のコツ</h3><p>「したい・したい」は不定詞（want to, hope to, wish to）<br>「楽しむ・終える」は動名詞（enjoy, finish, stop）</p></div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I want study.」</strong> → want のあとは to 不定詞。「I want to study.」が正解。</li>
  <li><strong>「I went to Kyoto for see temples.」</strong> → 目的を表すには for + 動名詞ではなく to 不定詞。</li>
  <li><strong>「I enjoy to play tennis.」</strong> → enjoy のあとは動名詞。「I enjoy playing tennis.」が正解。</li>
</ul></div>
"""),
    ]
},
"ippan.html": {
    "title": "一般動詞", "grade": "中学1年", "class": "g1",
    "sections": [
        ("一般動詞とは", """
<p>一般動詞は、be動詞（am, are, is）以外のすべての動詞のことです。「食べる」「走る」「勉強する」など、動作や行為を表します。</p>
<div class="highlight"><p><strong>be動詞</strong>：状態や存在を表す（am, are, is）<br><strong>一般動詞</strong>：動作や行為を表す（eat, run, study, play, read など）</p></div>
<table>
<tr><th>種類</th><th>例</th></tr>
<tr><td>日常動作</td><td>eat（食べる）, drink（飲む）, sleep（寝る）</td></tr>
<tr><td>勉強・仕事</td><td>study（勉強する）, read（読む）, write（書く）</td></tr>
<tr><td>趣味・スポーツ</td><td>play（遊ぶ）, run（走る）, swim（泳ぐ）</td></tr>
<tr><td>感覚</td><td>like（好き）, want（欲しい）, know（知っている）</td></tr>
</table>
"""),
        ("肯定文の作り方", """
<p>一般動詞の肯定文は「主語 + 動詞 + 〜」の順番です。</p>
<div class="highlight"><p>【公式】 主語 + 一般動詞 + 〜</p></div>
<ul>
  <li><span class="example">I eat breakfast every morning.</span> <span class="example-jp">（毎朝朝食を食べます）</span></li>
  <li><span class="example">She plays tennis on Sunday.</span> <span class="example-jp">（彼女は日曜日にテニスをします）</span></li>
  <li><span class="example">They study English at school.</span> <span class="example-jp">（彼らは学校で英語を勉強します）</span></li>
  <li><span class="example">We like Japanese food.</span> <span class="example-jp">（私たちは日本食が好きです）</span></li>
</ul>
<div class="note"><strong>注意！</strong> 主語が he, she, it（三人称単数）のときは動詞に s または es がつきます。</div>
"""),
        ("否定文の作り方", """
<p>一般動詞の否定文は <strong>do not (don't) / does not (doesn't)</strong> を使います。動詞は原形に戻します。</p>
<div class="highlight"><p>【公式】 主語 + <strong>don't / doesn't</strong> + 動詞の原形</p></div>
<ul>
  <li><span class="example">I don't like coffee.</span> <span class="example-jp">（コーヒーは好きではありません）</span></li>
  <li><span class="example">He doesn't play the piano.</span> <span class="example-jp">（彼はピアノを弾きません）</span></li>
  <li><span class="example">They don't eat meat.</span> <span class="example-jp">（彼らは肉を食べません）</span></li>
</ul>
<div class="tip-box"><h3>💡 覚え方のポイント</h3><p>否定文では does を使ったら動詞の s は取る！「He doesn't plays❌」→「He doesn't play⭕」</p></div>
"""),
        ("疑問文の作り方", """
<p>一般動詞の疑問文は <strong>Do / Does</strong> を文頭に置きます。動詞は原形に戻します。</p>
<div class="highlight"><p>【公式】 <strong>Do / Does + 主語</strong> + 動詞の原形？</p></div>
<ul>
  <li><span class="example">Do you like cats?</span> <span class="example-jp">（猫は好きですか？）</span></li>
  <li><span class="example">Does she speak English?</span> <span class="example-jp">（彼女は英語を話しますか？）</span></li>
</ul>
<p>答え方：Yes, I do. / No, I don't. / Yes, she does. / No, she doesn't.</p>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I not like coffee.」</strong> → 一般動詞の否定には do/does が必要。「I don't like coffee.」が正解。</li>
  <li><strong>「Does he plays?」</strong> → does を使ったら動詞は原形に戻す。「Does he play?」が正解。</li>
  <li><strong>「I am like coffee.」</strong> → be動詞と一般動詞を同時に使わない。</li>
</ul></div>
"""),
    ]
},
"be.html": {
    "title": "be動詞", "grade": "中学1年", "class": "g1",
    "sections": [
        ("be動詞とは", """
<p>be動詞は「〜です」「〜である」「〜にある/いる」という意味を表す動詞です。主語によって形が3つに変わります。</p>
<div class="highlight"><p>be動詞の3つの形：<br><strong>am</strong>（主語が I のとき）<br><strong>are</strong>（主語が you / 複数のとき）<br><strong>is</strong>（主語が he, she, it / 単数のとき）</p></div>
<table>
<tr><th>主語</th><th>be動詞</th><th>例</th></tr>
<tr><td>I</td><td>am</td><td>I am a student.</td></tr>
<tr><td>You</td><td>are</td><td>You are kind.</td></tr>
<tr><td>He / She / It</td><td>is</td><td>He is my friend.</td></tr>
<tr><td>We / They</td><td>are</td><td>We are happy.</td></tr>
</table>
"""),
        ("肯定文の作り方", """
<ul>
  <li><span class="example">I am 13 years old.</span> <span class="example-jp">（私は13歳です）</span></li>
  <li><span class="example">She is from Osaka.</span> <span class="example-jp">（彼女は大阪出身です）</span></li>
  <li><span class="example">We are in the classroom.</span> <span class="example-jp">（私たちは教室にいます）</span></li>
  <li><span class="example">It is sunny today.</span> <span class="example-jp">（今日は晴れです）</span></li>
  <li><span class="example">Are you hungry?</span> <span class="example-jp">（お腹すいてる？）</span></li>
</ul>
<div class="note"><strong>Check!</strong> be動詞は年齢・出身・位置・状態・天気など、とても多くの場面で使います。</div>
"""),
        ("否定文の作り方", """
<div class="highlight"><p>【公式】 主語 + be動詞 + <strong>not</strong> + 〜</p></div>
<ul>
  <li><span class="example">I am not a teacher.</span> <span class="example-jp">（私は教師ではありません）</span></li>
  <li><span class="example">She is not tired.</span> <span class="example-jp">（彼女は疲れていません）</span></li>
  <li><span class="example">They are not students.</span> <span class="example-jp">（彼らは学生ではありません）</span></li>
</ul>
"""),
        ("疑問文の作り方", """
<div class="highlight"><p>【公式】 <strong>Be動詞 + 主語</strong> + 〜？</p></div>
<ul>
  <li><span class="example">Are you a student?</span> <span class="example-jp">（あなたは学生ですか？）</span></li>
  <li><span class="example">Is he your brother?</span> <span class="example-jp">（彼はあなたの兄弟ですか？）</span></li>
  <li><span class="example">Are they from Japan?</span> <span class="example-jp">（彼らは日本出身ですか？）</span></li>
</ul>
<p>答え方：Yes, 主語 + be動詞. / No, 主語 + be動詞 + not.</p>
"""),
        ("短縮形（よく使う）", """
<table>
<tr><th>元の形</th><th>短縮形</th></tr>
<tr><td>I am</td><td>I'm</td></tr>
<tr><td>you are</td><td>you're</td></tr>
<tr><td>he is</td><td>he's</td></tr>
<tr><td>she is</td><td>she's</td></tr>
<tr><td>it is</td><td>it's</td></tr>
<tr><td>we are</td><td>we're</td></tr>
<tr><td>they are</td><td>they're</td></tr>
<tr><td>is not</td><td>isn't</td></tr>
<tr><td>are not</td><td>aren't</td></tr>
</table>
<div class="tip-box"><h3>💡 短縮形は会話で必須</h3><p>「I'm」「you're」「isn't」などの短縮形は、英会話やライティングで非常によく使います。</p></div>
"""),
        ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I are a student.」</strong> → I には必ず am を使います。</li>
  <li><strong>「You is kind.」</strong> → you には are を使います。</li>
  <li><strong>「He am my friend.」</strong> → He には is を使います。</li>
</ul></div>
"""),
    ]
},
"kako.html": {
    "title": "一般動詞の過去形", "grade": "中学1年", "class": "g1",
    "sections": [
        ("過去形とは", "<p>過去の出来事や状態を表すには、動詞を<strong>過去形</strong>にします。規則動詞（-edをつける）と不規則動詞（暗記必須）があります。</p>"),
        ("規則動詞（ed形）", """
<table>
<tr><th>ルール</th><th>例</th></tr>
<tr><td>ふつうは ed をつける</td><td>play → played, watch → watched</td></tr>
<tr><td>e で終わる → d だけ</td><td>like → liked, use → used</td></tr>
<tr><td>子音字+y → yをiに変えてed</td><td>study → studied, cry → cried</td></tr>
<tr><td>短母音+子音字 → 子音を重ねてed</td><td>stop → stopped</td></tr>
</table>
"""),
        ("不規則動詞（暗記必須）", """
<table>
<tr><th>原形</th><th>過去形</th><th>意味</th></tr>
<tr><td>go</td><td>went</td><td>行く</td></tr>
<tr><td>eat</td><td>ate</td><td>食べる</td></tr>
<tr><td>see</td><td>saw</td><td>見る</td></tr>
<tr><td>do</td><td>did</td><td>する</td></tr>
<tr><td>have</td><td>had</td><td>持っている</td></tr>
<tr><td>make</td><td>made</td><td>作る</td></tr>
<tr><td>buy</td><td>bought</td><td>買う</td></tr>
<tr><td>write</td><td>wrote</td><td>書く</td></tr>
<tr><td>read</td><td>read（発音が変わる）</td><td>読む</td></tr>
<tr><td>come</td><td>came</td><td>来る</td></tr>
</table>
"""),
        ("否定文・疑問文（did）", """
<p>過去形の否定文・疑問文は <strong>did / didn't</strong> を使います。動詞は<strong>原形に戻す</strong>！</p>
<ul>
  <li><span class="example">I didn't go to school yesterday.</span> <span class="example-jp">（昨日学校に行きませんでした）</span></li>
  <li><span class="example">Did you eat breakfast?</span> <span class="example-jp">（朝食を食べましたか？）</span></li>
  <li><span class="example">What did you do last night?</span> <span class="example-jp">（昨晩何をしましたか？）</span></li>
</ul>
<div class="note"><strong>超重要！</strong>did を使ったら動詞は原形！「I didn't went」は間違い。「I didn't go」が正解。</div>
"""),
    ]
},
}

if __name__ == "__main__":
    print("=== 全記事を拡充（厚い6記事はスキップ） ===")
    for fname, data in ALL_SECTIONS.items():
        if fname in THICK_ARTICLES:
            print(f"  SKIP {fname} (already thick)")
            continue
        write_full_article(fname, data["title"], data["grade"], data["class"], data["sections"])
    print("=== 完了 ===")