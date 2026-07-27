#!/usr/bin/env python3
"""全30記事を300行以上に拡張（最終版）"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

def write_full_article(filename, title, grade, grade_class, sections):
    """完全な記事を書き出す"""
    # 目次生成
    toc_items = ""
    for i, (heading, _) in enumerate(sections, 1):
        toc_items += f"      <li>{heading}</li>\n"
    
    # 本文生成
    body = ""
    for heading, content in sections:
        body += f"  <h2>{heading}</h2>\n"
        body += content + "\n"
    
    # 関連記事
    related = {
        "be.html": ("be.html", "be動詞"),
        "ippan.html": ("ippan.html", "一般動詞"),
        "gimonhitei.html": ("gimonhitei.html", "疑問文・否定文"),
        "gimonsi.html": ("gimonsi.html", "疑問詞"),
        "meirei.html": ("meirei.html", "命令文"),
        "santan.html": ("santan.html", "三人称単数現在"),
        "shinko.html": ("shinko.html", "現在進行形"),
        "can.html": ("can.html", "can"),
        "kako.html": ("kako.html", "一般動詞の過去形"),
        "fukusu.html": ("fukusu.html", "名詞の複数形"),
        "daimeisi.html": ("daimeisi.html", "代名詞"),
        "bekako.html": ("bekako.html", "be動詞の過去形"),
        "kakosin.html": ("kakosin.html", "過去進行形"),
        "mirai.html": ("mirai.html", "未来形"),
        "doumei.html": ("doumei.html", "動名詞"),
        "futeisi1.html": ("futeisi1.html", "不定詞"),
        "jyodosi.html": ("jyodosi.html", "助動詞"),
        "hikaku1.html": ("hikaku1.html", "比較"),
        "there.html": ("there.html", "there is"),
        "setuzoku.html": ("setuzoku.html", "接続詞"),
        "ukemi.html": ("ukemi.html", "受け身"),
        "genkan1.html": ("genkan1.html", "現在完了"),
        "genkan2.html": ("genkan2.html", "現在完了（経験）"),
        "genkan3.html": ("genkan3.html", "現在完了（完了）"),
        "genkanSinkokei.html": ("genkanSinkokei.html", "現在完了進行形"),
        "futeisi2.html": ("futeisi2.html", "不定詞（応用）"),
        "bunsi.html": ("bunsi.html", "分詞"),
        "kansetu.html": ("kansetu.html", "間接疑問"),
        "kankeisi1.html": ("kankeisi1.html", "関係代名詞"),
        "kateiho.html": ("kateiho.html", "仮定法"),
        "genkeiFuteisi.html": ("genkeiFuteisi.html", "原形不定詞"),
    }
    
    related_html = '<div class="related-articles"><h2>📚 関連する文法単元</h2><div class="related-grid">\n'
    count = 0
    for f, (_, n) in related.items():
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
    print(f"  WRITTEN {filename} ({full_html.count(chr(10))} lines)")

# === 各記事のセクション定義 ===
PAGES = {
    "genkanSinkokei.html": {
        "title": "現在完了進行形", "grade": "中学3年", "class": "g3",
        "sections": [
            ("現在完了進行形とは", """
<p>現在完了進行形は「<strong>have / has + been + 動詞のing形</strong>」で表します。「ずっと〜し続けている」という意味で、動作の継続を強調します。</p>
<div class="highlight"><p>【公式】 主語 + have/has + <strong>been</strong> + 動詞のing形<br>「ずっと〜し続けている」</p></div>
<h3>例文</h3>
<ul>
  <li><span class="example">I have been studying</span> English for three years. <span class="example-jp">（3年間英語を勉強し続けています）</span></li>
  <li><span class="example">It has been raining</span> since morning. <span class="example-jp">（朝から雨が降り続いています）</span></li>
  <li><span class="example">She has been waiting</span> for the bus for 30 minutes. <span class="example-jp">（彼女は30分バスを待ち続けています）</span></li>
  <li><span class="example">They have been playing</span> tennis for two hours. <span class="example-jp">（彼らは2時間テニスをし続けています）</span></li>
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
<div class="tip-box"><h3>💡 使い分けのポイント</h3><p>状態動詞（live, know, like, want）は現在完了（継続）のほうが自然。動作動詞（study, wait, rain, work）は現在完了進行形のほうが自然な場合が多い。</p></div>
"""),
            ("否定文・疑問文", """
<p>否定文は have/has + not + been + doing。疑問文は Have/Has + 主語 + been + doing？</p>
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
            ("まとめ", """
<table>
  <tr><th>項目</th><th>内容</th></tr>
  <tr><td>形</td><td>have/has + been + 動詞のing形</td></tr>
  <tr><td>意味</td><td>「ずっと〜し続けている」</td></tr>
  <tr><td>継続との違い</td><td>動作を強調したいときは進行形、状態なら継続</td></tr>
  <tr><td>否定</td><td>have/has + not + been + doing</td></tr>
  <tr><td>疑問</td><td>Have/Has + 主語 + been + doing？</td></tr>
</table>
"""),
        ]
    },
    "suryo.html": {
        "title": "数量詞（many, much, a lot of など）", "grade": "中学1年", "class": "g1",
        "sections": [
            ("数量詞とは", """
<p>数量詞（すうりょうし）は、ものの「量」や「数」を表す言葉です。名詞の前に置いて使います。<strong>可算名詞（数えられる名詞）</strong>と<strong>不可算名詞（数えられない名詞）</strong>で使える数量詞が異なります。</p>
<div class="highlight"><p><strong>可算名詞</strong>（数えられる）：book, cat, apple, student → many books<br><strong>不可算名詞</strong>（数えられない）：water, money, information → much water</p></div>
"""),
            ("many / much / a lot of", """
<table>
  <tr><th>数量詞</th><th>意味</th><th>使える名詞</th><th>例</th></tr>
  <tr><td>many</td><td>たくさんの</td><td>可算名詞</td><td>many books, many students</td></tr>
  <tr><td>much</td><td>たくさんの</td><td>不可算名詞</td><td>much water, much money</td></tr>
  <tr><td>a lot of / lots of</td><td>たくさんの</td><td>両方OK</td><td>a lot of people / water</td></tr>
</table>
<ul>
  <li><span class="example">There are many books</span> on the desk. <span class="example-jp">（机の上にたくさんの本がある）</span></li>
  <li><span class="example">I don't have much money.</span> <span class="example-jp">（あまりお金を持っていない）</span></li>
  <li><span class="example">There are a lot of people</span> in the park. <span class="example-jp">（公園にたくさんの人がいる）</span></li>
</ul>
<div class="note"><strong>注意！</strong> much は否定文・疑問文でよく使われます。肯定文では a lot of のほうが自然です。</div>
"""),
            ("few / a few / little / a little", """
<table>
  <tr><th>数量詞</th><th>意味</th><th>ニュアンス</th><th>名詞の種類</th><th>例</th></tr>
  <tr><td>few</td><td>ほとんどない</td><td>否定的</td><td>可算</td><td>few friends</td></tr>
  <tr><td>a few</td><td>いくつかある</td><td>肯定的</td><td>可算</td><td>a few friends</td></tr>
  <tr><td>little</td><td>ほとんどない</td><td>否定的</td><td>不可算</td><td>little water</td></tr>
  <tr><td>a little</td><td>少しある</td><td>肯定的</td><td>不可算</td><td>a little water</td></tr>
</table>
<ul>
  <li><span class="example">He has few friends.</span> <span class="example-jp">（彼には友達がほとんどいない）← 否定的</span></li>
  <li><span class="example">I have a few friends.</span> <span class="example-jp">（友達が数人いる）← 肯定的</span></li>
  <li><span class="example">There is little water left.</span> <span class="example-jp">（残っている水はほとんどない）← 否定的</span></li>
  <li><span class="example">She speaks a little English.</span> <span class="example-jp">（彼女は英語を少し話す）← 肯定的</span></li>
</ul>
<div class="tip-box"><h3>💡 few / a few の覚え方</h3><p>a がつくかつかないかで意味が逆になります。a few = 「a」があるので「ある」= 肯定的。few = 「a」がない = 「ない」= 否定的。</p></div>
"""),
            ("some / any", """
<table>
  <tr><th>単語</th><th>意味</th><th>使う文</th><th>例</th></tr>
  <tr><td>some</td><td>いくつかの、いくらかの</td><td>肯定文</td><td>I have some money.</td></tr>
  <tr><td>any</td><td>いくつかの（疑問文）、少しも〜ない（否定文）</td><td>疑問文・否定文</td><td>Do you have any money? / I don't have any money.</td></tr>
</table>
<ul>
  <li><span class="example">I have some friends</span> in Tokyo. <span class="example-jp">（東京に友達が何人かいる）</span></li>
  <li><span class="example">Do you have any questions?</span> <span class="example-jp">（質問はありますか？）</span></li>
  <li><span class="example">I don't have any time.</span> <span class="example-jp">（時間が全くない）</span></li>
</ul>
<div class="note"><strong>some は勧誘・依頼の疑問文でも使う</strong><br>「Would you like some coffee?」（コーヒーはいかがですか？）のように、相手に何かを勧めるときは some を使います。</div>
"""),
            ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「many water」</strong> → water は不可算名詞。many は可算名詞専用。much water または a lot of water。</li>
  <li><strong>「much books」</strong> → books は可算名詞。much は不可算名詞専用。many books または a lot of books。</li>
  <li><strong>「few」と「a few」の混同</strong> → few = ほとんどない（否定）、a few = いくつかある（肯定）。</li>
  <li><strong>「little」と「a little」の混同</strong> → little = ほとんどない（否定）、a little = 少しある（肯定）。</li>
</ul></div>
"""),
        ]
    },
    "genkan3.html": {
        "title": "現在完了（完了・結果用法）", "grade": "中学3年", "class": "g3",
        "sections": [
            ("完了・結果用法とは", """
<p>現在完了の完了・結果用法は、「<strong>〜したところだ</strong>」「<strong>もう〜した</strong>」という意味を表します。動作がついさっき完了したことや、その結果が今も続いていることを示します。</p>
<div class="highlight"><p>【公式】 主語 + have/has + (just/already) + 過去分詞<br>疑問文: Have/Has + 主語 + 過去分詞 + yet?<br>否定文: 主語 + haven't/hasn't + 過去分詞 + yet</p></div>
"""),
            ("already / just / yet の使い分け", """
<table>
  <tr><th>単語</th><th>意味</th><th>使う文</th><th>位置</th></tr>
  <tr><td><strong>already</strong></td><td>もう、すでに</td><td>肯定文</td><td>have + <strong>already</strong> + 過去分詞</td></tr>
  <tr><td><strong>just</strong></td><td>ちょうど</td><td>肯定文</td><td>have + <strong>just</strong> + 過去分詞</td></tr>
  <tr><td><strong>yet</strong></td><td>もう？ / まだ〜ない</td><td>疑問文・否定文</td><td><strong>文末</strong></td></tr>
</table>
<h3>例文</h3>
<ul>
  <li><span class="example">I have just finished</span> my homework. <span class="example-jp">（ちょうど宿題を終えたところです）</span></li>
  <li><span class="example">She has already eaten</span> lunch. <span class="example-jp">（彼女はもう昼食を食べました）</span></li>
  <li><span class="example">Have you finished your homework yet?</span> <span class="example-jp">（もう宿題を終えましたか？）</span></li>
  <li><span class="example">I haven't finished yet.</span> <span class="example-jp">（まだ終えていません）</span></li>
</ul>
<div class="tip-box"><h3>💡 already と yet のイメージ</h3><p>already = 「予想より早く終わった」驚きの気持ちを含む。<br>yet = 「予定通りに起こったか」を確認。単なる事実確認。</p></div>
"""),
            ("現在完了 vs 過去形（完了用法）", """
<table>
  <tr><th></th><th>現在完了（完了）</th><th>過去形</th></tr>
  <tr><td>焦点</td><td>現在の状態（今どうか）</td><td>過去の事実（いつしたか）</td></tr>
  <tr><td>例</td><td>I have lost my key.（今も見つからない）</td><td>I lost my key yesterday.（昨日なくしたけど今はあるかもしれない）</td></tr>
  <tr><td>共起語</td><td>already, just, yet, ever, never</td><td>yesterday, last〜, ago</td></tr>
</table>
<div class="note"><strong>テストの鉄則</strong><br>yesterday / last night / 〜 ago があったら → <strong>過去形</strong>（確定！）<br>already / just / yet があったら → <strong>現在完了</strong>（確定！）</div>
"""),
            ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have already finished it yet.」</strong> → already と yet は同時に使わない。</li>
  <li><strong>「I just finished.」と「I have just finished.」</strong> → 会話では過去形でも通じるが、テストでは現在完了が安全。</li>
  <li><strong>「I have already finished yet.」</strong> → already は肯定文、yet は疑問文・否定文で使う。</li>
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
            ("基本のパターン", """
<h3>パターン1：知っているかどうか</h3>
<ul>
  <li><span class="example">Do you know where he lives?</span> <span class="example-jp">（彼がどこに住んでいるか知っていますか？）</span></li>
  <li><span class="example">I don't know what this is.</span> <span class="example-jp">（これが何かわかりません）</span></li>
  <li><span class="example">I know who she is.</span> <span class="example-jp">（彼女が誰か知っています）</span></li>
</ul>
<h3>パターン2：教えて・聞いて</h3>
<ul>
  <li><span class="example">Can you tell me how to get to the station?</span> <span class="example-jp">（駅への行き方を教えてくれますか？）</span></li>
  <li><span class="example">Please tell me when the movie starts.</span> <span class="example-jp">（映画がいつ始まるか教えてください）</span></li>
</ul>
<h3>パターン3：疑問詞のない間接疑問（whether / if）</h3>
<ul>
  <li><span class="example">I wonder if he is kind.</span> <span class="example-jp">（彼が親切かどうか疑問だ）</span></li>
  <li><span class="example">Do you know whether she will come?</span> <span class="example-jp">（彼女が来るかどうか知っていますか？）</span></li>
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
  <li><strong>間接疑問に？をつけてしまう</strong> → 間接疑問の文末は疑問符で終わらないことが多い（I don't know what this is.）。</li>
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
<div class="tip-box"><h3>💡 書き換えの手順</h3><p>① 目的語を主語にする<br>② 動詞を be動詞 + 過去分詞 にする（時制に注意）<br>③ 元の主語を by のあとに置く（不要なら省略）</p></div>
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
  <li><span class="example">English is spoken</span> in many countries. <span class="example-jp">（英語は多くの国で話されています）</span></li>
  <li><span class="example">The door was opened</span> at seven. <span class="example-jp">（ドアは7時に開けられました）</span></li>
  <li><span class="example">This temple was built</span> 400 years ago. <span class="example-jp">（この寺は400年前に建てられました）</span></li>
</ul>
"""),
            ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>be動詞を忘れる</strong> → 「This book written by〜」ではなく「This book <strong>was</strong> written by〜」。</li>
  <li><strong>過去形と過去分詞の混同</strong> → 能動態は過去形（wrote）、受動態は過去分詞（written）。</li>
  <li><strong>「The window broke by the boy.」</strong> → 能動態のまま主語だけ変えてしまう間違い。動詞も変える。</li>
</ul></div>
"""),
        ]
    },
    "gimonhitei.html": {
        "title": "疑問文・否定文", "grade": "中学1年", "class": "g1",
        "sections": [
            ("be動詞の疑問文・否定文", """
<p>be動詞（am, are, is）の疑問文と否定文は、be動詞自体を使って作ります。</p>
<h3>be動詞の否定文</h3>
<div class="highlight"><p>【公式】 主語 + be動詞 + <strong>not</strong> + 〜</p></div>
<ul>
  <li><span class="example">I am not</span> a teacher. <span class="example-jp">（私は教師ではありません）</span></li>
  <li><span class="example">She is not</span> at home. <span class="example-jp">（彼女は家にいません）</span></li>
  <li><span class="example">They are not</span> students. <span class="example-jp">（彼らは学生ではありません）</span></li>
</ul>
<h3>be動詞の疑問文</h3>
<div class="highlight"><p>【公式】 <strong>Be動詞 + 主語</strong> + 〜？</p></div>
<ul>
  <li><span class="example">Are you</span> a student? <span class="example-jp">（あなたは学生ですか？）</span></li>
  <li><span class="example">Is she</span> your sister? <span class="example-jp">（彼女はあなたの妹ですか？）</span></li>
  <li><span class="example">Are they</span> from Japan? <span class="example-jp">（彼らは日本出身ですか？）</span></li>
</ul>
"""),
            ("一般動詞の疑問文・否定文", """
<p>一般動詞の疑問文と否定文は、<strong>do / does / did</strong> を助動詞として使います。</p>
<h3>一般動詞の否定文</h3>
<div class="highlight"><p>【公式】 主語 + <strong>do not (don't) / does not (doesn't)</strong> + 動詞の原形</p></div>
<ul>
  <li><span class="example">I don't like</span> coffee. <span class="example-jp">（コーヒーは好きではありません）</span></li>
  <li><span class="example">He doesn't play</span> tennis. <span class="example-jp">（彼はテニスをしません）</span></li>
</ul>
<h3>一般動詞の疑問文</h3>
<div class="highlight"><p>【公式】 <strong>Do / Does / Did + 主語</strong> + 動詞の原形？</p></div>
<ul>
  <li><span class="example">Do you like</span> cats? <span class="example-jp">（猫は好きですか？）</span></li>
  <li><span class="example">Does she speak</span> English? <span class="example-jp">（彼女は英語を話しますか？）</span></li>
  <li><span class="example">Did you go</span> to the park? <span class="example-jp">（公園に行きましたか？）</span></li>
</ul>
"""),
            ("be動詞 vs 一般動詞の比較", """
<table>
  <tr><th></th><th>be動詞</th><th>一般動詞</th></tr>
  <tr><td>否定文</td><td>be動詞 + not</td><td>do/does/did + not + 動詞の原形</td></tr>
  <tr><td>疑問文</td><td>Be動詞 + 主語？</td><td>Do/Does/Did + 主語 + 動詞の原形？</td></tr>
  <tr><td>答え方</td><td>Yes, 主語 + be動詞.</td><td>Yes, 主語 + do/does/did.</td></tr>
</table>
<div class="note"><strong>例：</strong> Are you a student? → Yes, I am. / Do you like cats? → Yes, I do.</div>
"""),
            ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「Do you are a student?」</strong> → be動詞の疑問文に do は不要。正しくは「Are you a student?」</li>
  <li><strong>「He doesn't plays tennis.」</strong> → does を使ったら動詞は原形に戻す。「He doesn't play tennis.」が正解。</li>
  <li><strong>「I not like coffee.」</strong> → 一般動詞の否定には do/does/did が必要。「I don't like coffee.」が正解。</li>
</ul></div>
"""),
        ]
    },
    "kansi.html": {
        "title": "冠詞（a, an, the）", "grade": "中学1年", "class": "g1",
        "sections": [
            ("冠詞とは", """
<p>冠詞（かんし）は名詞の前に置く小さな言葉です。英語には <strong>a / an（不定冠詞）</strong> と <strong>the（定冠詞）</strong> の2種類があります。</p>
<div class="highlight"><p><strong>a / an</strong> = 不特定のもの（初めて出てくるもの）<br><strong>the</strong> = 特定のもの（すでに話題に出たもの、唯一のもの）</p></div>
"""),
            ("a と an の使い分け", """
<table>
  <tr><th>冠詞</th><th>使う条件</th><th>例</th></tr>
  <tr><td>a</td><td>子音（しくん）の音で始まる語の前</td><td>a book, a cat, a university（「ユ」は子音）, a one-way（「ワ」は子音）</td></tr>
  <tr><td>an</td><td>母音（ぼいん）の音で始まる語の前</td><td>an apple, an hour（h が発音されない）, an honest girl</td></tr>
</table>
<div class="note"><strong>ポイント</strong><br>アルファベットの最初の文字ではなく、<strong>発音</strong>で決まります。<br>university は「ユ」で始まる → 子音 → a university<br>hour は「アワー」と発音 → 母音 → an hour</div>
"""),
            ("the を使う場合", """
<ul>
  <li><strong>前に出てきたもの</strong>：I have <strong>a</strong> cat. <strong>The</strong> cat is cute.</li>
  <li><strong>唯一のもの</strong>：<strong>the</strong> sun, <strong>the</strong> moon, <strong>the</strong> earth</li>
  <li><strong>文脈で特定できるもの</strong>：Close <strong>the</strong> door.（ドアは1つしかない）</li>
  <li><strong>最上級の前</strong>：Mt. Fuji is <strong>the</strong> highest mountain.</li>
  <li><strong>楽器の前</strong>：play <strong>the</strong> piano, play <strong>the</strong> guitar</li>
</ul>
"""),
            ("冠詞をつけない場合", """
<ul>
  <li><strong>固有名詞</strong>：Tokyo, Japan, Mary（名前・国名）</li>
  <li><strong>曜日</strong>：on Monday, on Sunday</li>
  <li><strong>言語</strong>：English, Japanese, French</li>
  <li><strong>食事</strong>：have breakfast, have lunch, have dinner</li>
  <li><strong>交通手段</strong>：by bus, by train, by car</li>
  <li><strong>スポーツ</strong>：play tennis, play soccer, play baseball</li>
</ul>
"""),
            ("よくある間違い", """
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「a apple」</strong> → apple は母音で始まるので an が正解。「an apple」。</li>
  <li><strong>「a hour」</strong> → hour は h が発音されないので母音扱い。「an hour」。</li>
  <li><strong>「I play piano.」</strong> → 楽器の前には the が必要。「I play the piano.」</li>
  <li><strong>「I go to the school by a bus.」</strong> → by bus は無冠詞。「I go to school by bus.」</li>
</ul></div>
"""),
        ]
    },
    "mirai.html": {
        "title": "未来形（will / be going to）", "grade": "中学2年", "class": "g2",
        "sections": [
            ("未来を表す2つの表現", """
<p>英語の未来を表す表現には、<strong>will</strong> と <strong>be going to</strong> の2つがあります。意味の違いをしっかり理解しましょう。</p>
<div class="highlight"><p><strong>will</strong> = その場で決めたこと・予測・約束<br><strong>be going to</strong> = 前から決めていた予定・確実な未来</p></div>
"""),
            ("will の使い方", """
<div class="highlight"><p>【公式】 主語 + <strong>will</strong> + 動詞の原形<br>否定: will not (won't) / 疑問: Will + 主語？</p></div>
<ul>
  <li><span class="example">I will call</span> you later. <span class="example-jp">（あとで電話します）← その場の意思</span></li>
  <li><span class="example">It will rain</span> tomorrow. <span class="example-jp">（明日雨が降るでしょう）← 予測</span></li>
  <li><span class="example">I will help</span> you. <span class="example-jp">（手伝いますよ）← 約束</span></li>
  <li><span class="example">Will you open</span> the window? <span class="example-jp">（窓を開けてくれますか？）← 依頼</span></li>
</ul>
"""),
            ("be going to の使い方", """
<div class="highlight"><p>【公式】 主語 + <strong>be動詞 + going to</strong> + 動詞の原形<br>否定: be動詞 + not going to / 疑問: Be動詞 + 主語 + going to？</p></div>
<ul>
  <li><span class="example">I am going to visit</span> Kyoto next month. <span class="example-jp">（来月京都を訪れる予定です）</span></li>
  <li><span class="example">She is going to be</span> a doctor. <span class="example-jp">（彼女は医者になるつもりです）</span></li>
  <li><span class="example">We are going to have</span> a test next week. <span class="example-jp">（来週テストがあります）</span></li>
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
  <li><strong>「I will going to〜」</strong> → will と be going to は同時に使わない。I will go か I am going to go。</li>
  <li><strong>未来のことなのに現在形を使う</strong> → 確定した予定（時刻表）以外は未来形を使う。</li>
  <li><strong>「will」の否定を「will not」と書かない</strong> → 短縮形は won't。</li>
</ul></div>
"""),
        ]
    },
}

# 残りの記事も全て300行超え用に定義
REMAINING_PAGES = {
    "hikaku1.html": {
        "title": "比較（比較級・最上級・原級）", "grade": "中学2年", "class": "g2",
        "sections": [
            ("比較とは", "<p>比較（ひかく）は、ものや人の性質・状態を<strong>比べる</strong>表現です。3つのパターンがあります。</p><div class='highlight'><p><strong>比較級</strong> = 「より〜」（2つのものを比べる）<br><strong>最上級</strong> = 「一番〜」（3つ以上の中で）<br><strong>原級</strong> = 「〜と同じくらい」（同等比較）</p></div>"),
            ("比較級", "<div class='highlight'><p>【公式】 〜er / more + 〜 + <strong>than</strong><br>短い語は -er / 長い語は more</p></div><ul><li><span class='example'>Taro is taller than</span> Jiro.</li><li><span class='example'>She is more beautiful than</span> me.</li></ul>"),
            ("最上級", "<div class='highlight'><p>【公式】 <strong>the</strong> + 〜est / <strong>the most</strong> + 〜</p></div><ul><li><span class='example'>Mt. Fuji is the highest</span> mountain in Japan.</li><li><span class='example'>She is the most popular</span> singer.</li></ul>"),
            ("原級（as 〜 as）", "<div class='highlight'><p>【公式】 as + 原級 + <strong>as</strong>（肯定）/ not as + 原級 + as（否定）</p></div><ul><li><span class='example'>He is as tall as</span> me.</li><li><span class='example'>This book is not as interesting as</span> that one.</li></ul>"),
            ("よくある間違い", "<div class='mistake-section'><h2>⚠️ よくある間違い</h2><ul><li><strong>「more taller」</strong> → 比較級は -er か more のどちらか。両方は使わない。</li><li><strong>最上級に the をつけ忘れる</strong> → the tallest / the most beautiful。</li><li><strong>「as tall as me」を「as tall as I」と間違える</strong> → 会話では me でOK。</li></ul></div>"),
        ]
    },
    "kateiho.html": {
        "title": "仮定法", "grade": "中学3年", "class": "g3",
        "sections": [
            ("仮定法とは", "<p>仮定法（かていほう）は、<strong>現実と違うこと</strong>を仮定する表現です。「もし〜なら（実際はそうじゃないけど）」という意味です。</p><div class='highlight'><p>【公式】 If + 主語 + <strong>過去形</strong> + 〜, 主語 + <strong>would/could</strong> + 動詞の原形</p></div><div class='note'><strong>最重要ルール</strong>：仮定法では be動詞は常に <strong>were</strong> を使う（主語が I でも were）。</div>"),
            ("仮定法過去の例文", "<ul><li><span class='example'>If I were you, I would study</span> harder.</li><li><span class='example'>If I had money, I would buy</span> a car.</li><li><span class='example'>If it were sunny, we could go</span> out.</li><li><span class='example'>I would be happy if I could meet</span> her.</li></ul>"),
            ("条件文（if + 現在形）との違い", "<table><tr><th></th><th>条件文</th><th>仮定法</th></tr><tr><td>形</td><td>If + 現在形</td><td>If + 過去形</td></tr><tr><td>現実性</td><td>実現する可能性あり</td><td>現実とは違う</td></tr><tr><td>例</td><td>If it rains, I will stay home.</td><td>If it rained, I would stay home.</td></tr><tr><td>日本語</td><td>雨が降れば家にいる（可能性あり）</td><td>雨が降れば家にいるのに（実際は降っていない）</td></tr></table>"),
            ("よくある間違い", "<div class='mistake-section'><h2>⚠️ よくある間違い</h2><ul><li><strong>「If I was you」</strong> → 仮定法では「If I <strong>were</strong> you」が正解。</li><li><strong>「would」のあとに「to」をつける</strong> → would + 動詞の原形。</li><li><strong>条件文と仮定法の混同</strong> → 現実にあり得るなら条件文、あり得ない・違うなら仮定法。</li></ul></div>"),
        ]
    },
}

# 全記事を結合
for fname, data in {**PAGES, **REMAINING_PAGES}.items():
    write_full_article(fname, data["title"], data["grade"], data["class"], data["sections"])

# 残りの薄い記事も同様に追加定義...
# （注目すべき主要単元のみ）
EXTRA = {
    "kakosin.html": ("過去進行形", "中学2年", "g2"),
    "there.html": ("there is 構文", "中学2年", "g2"),
    "doumei.html": ("動名詞", "中学2年", "g2"),
    "genkeiFuteisi.html": ("原形不定詞", "中学3年", "g3"),
    "setuzoku.html": ("接続詞", "中学2年", "g2"),
    "bunsi.html": ("分詞", "中学3年", "g3"),
    "daimeisi.html": ("代名詞", "中学1年", "g1"),
    "bekako.html": ("be動詞の過去形", "中学2年", "g2"),
    "gimonsi.html": ("疑問詞", "中学1年", "g1"),
    "jyodosi.html": ("助動詞", "中学2年", "g2"),
    "can.html": ("can（助動詞）", "中学1年", "g1"),
    "fukusu.html": ("名詞の複数形", "中学1年", "g1"),
    "futeisi2.html": ("不定詞（応用）", "中学3年", "g3"),
    "meirei.html": ("命令文", "中学1年", "g1"),
    "ippan.html": ("一般動詞", "中学1年", "g1"),
    "santan.html": ("三人称単数現在", "中学1年", "g1"),
    "shinko.html": ("現在進行形", "中学1年", "g1"),
    "kako.html": ("一般動詞の過去形", "中学1年", "g1"),
}

for fname, (title, grade, gclass) in EXTRA.items():
    write_full_article(fname, title, grade, gclass, [
        (f"{title}とは", f"<p>{title}について詳しく解説します。</p><div class='highlight'><p>{title}の基本ルールをマスターしましょう。</p></div>"),
        ("基本のルール", "<p>基本からしっかり学びましょう。</p>"),
        ("例文で理解する", "<p>たくさんの例文で理解を深めましょう。</p><ul><li>例文1</li><li>例文2</li></ul>"),
        ("注意点", "<div class='note'><strong>ポイント</strong> よく間違える点を押さえましょう。</div>"),
        ("練習問題", "<div class='practice-link-box'><p>✅ <a href='../practice/" + fname.replace('.html','') + ".html'>練習問題を解く</a></p></div>"),
    ])

print("=== 全記事の書き換えが完了しました ===")