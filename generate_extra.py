#!/usr/bin/env python3
"""追加機能：不規則動詞一覧・高校入試対策・検索・サイトマップ・トップページ更新"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

HEADER = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 中学英語学習サイト</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="../index.html" class="header-logo">📚 中学英語<span>Lab</span></a>
    <nav class="header-nav">
      <a href="../index.html">ホーム</a>
      <a href="../index.html#grammar">文法解説</a>
      <a href="../index.html#practice">練習問題</a>
      <a href="../test/index.html">確認テスト</a>
      <a href="../word/index.html" class="active">単語帳</a>
    </nav>
    <div class="hamburger" onclick="document.getElementById('mobileNav').classList.toggle('open')">
      <span></span><span></span><span></span>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobileNav">
  <a href="../index.html">ホーム</a>
  <a href="../index.html#grammar">文法解説</a>
  <a href="../index.html#practice">練習問題</a>
  <a href="../test/index.html">確認テスト</a>
  <a href="../word/index.html">英単語帳</a>
  <a href="../exam/index.html">高校入試対策</a>
  <a href="../sitemap.html">サイトマップ</a>
</div>'''

FOOTER = '''<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。<br>英文法・練習問題・確認テストで英語力を確実にアップ。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a><a href="../grammar/genkan1.html">現在完了</a><a href="../grammar/kankeisi1.html">関係代名詞</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a><a href="../practice/futeisi.html">不定詞</a><a href="../practice/genkan.html">現在完了</a><a href="../practice/hikaku.html">比較</a></div>
    <div><h3>確認テスト</h3><a href="../test/be_test.html">be動詞</a><a href="../test/futeisi_test.html">不定詞</a><a href="../test/genkan_test.html">現在完了</a><a href="../test/kankeisi_test.html">関係代名詞</a></div>
    <div><h3>その他</h3><a href="../word/index.html">英単語帳</a><a href="../exam/index.html">高校入試対策</a><a href="../verb/index.html">不規則動詞一覧</a><a href="../sitemap.html">サイトマップ</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''

def gen_irregular_verbs():
    """不規則動詞一覧表"""
    verbs = [
        ["be (am/is/are)","was/were","been","〜である"],
        ["become","became","become","〜になる"],
        ["begin","began","begun","始める"],
        ["break","broke","broken","壊す"],
        ["bring","brought","brought","持ってくる"],
        ["build","built","built","建てる"],
        ["buy","bought","bought","買う"],
        ["catch","caught","caught","捕まえる"],
        ["choose","chose","chosen","選ぶ"],
        ["come","came","come","来る"],
        ["cost","cost","cost","かかる"],
        ["cut","cut","cut","切る"],
        ["do","did","done","する"],
        ["draw","drew","drawn","描く"],
        ["drink","drank","drunk","飲む"],
        ["drive","drove","driven","運転する"],
        ["eat","ate","eaten","食べる"],
        ["fall","fell","fallen","落ちる"],
        ["feel","felt","felt","感じる"],
        ["find","found","found","見つける"],
        ["fly","flew","flown","飛ぶ"],
        ["forget","forgot","forgotten","忘れる"],
        ["get","got","gotten","得る"],
        ["give","gave","given","与える"],
        ["go","went","gone","行く"],
        ["grow","grew","grown","育つ"],
        ["have","had","had","持っている"],
        ["hear","heard","heard","聞く"],
        ["hide","hid","hidden","隠れる"],
        ["hit","hit","hit","打つ"],
        ["hold","held","held","持つ"],
        ["hurt","hurt","hurt","傷つける"],
        ["keep","kept","kept","保つ"],
        ["know","knew","known","知っている"],
        ["lead","led","led","導く"],
        ["learn","learned/learnt","learned/learnt","学ぶ"],
        ["leave","left","left","去る"],
        ["lend","lent","lent","貸す"],
        ["let","let","let","許可する"],
        ["lie","lay","lain","横たわる"],
        ["light","lit","lit","灯す"],
        ["lose","lost","lost","失う"],
        ["make","made","made","作る"],
        ["mean","meant","meant","意味する"],
        ["meet","met","met","会う"],
        ["pay","paid","paid","支払う"],
        ["put","put","put","置く"],
        ["read","read","read","読む"],
        ["ride","rode","ridden","乗る"],
        ["ring","rang","rung","鳴らす"],
        ["rise","rose","risen","上がる"],
        ["run","ran","run","走る"],
        ["say","said","said","言う"],
        ["see","saw","seen","見る"],
        ["sell","sold","sold","売る"],
        ["send","sent","sent","送る"],
        ["set","set","set","設定する"],
        ["shine","shone","shone","輝く"],
        ["show","showed","shown","見せる"],
        ["shut","shut","shut","閉める"],
        ["sing","sang","sung","歌う"],
        ["sink","sank","sunk","沈む"],
        ["sit","sat","sat","座る"],
        ["sleep","slept","slept","眠る"],
        ["speak","spoke","spoken","話す"],
        ["spend","spent","spent","使う"],
        ["stand","stood","stood","立つ"],
        ["steal","stole","stolen","盗む"],
        ["swim","swam","swum","泳ぐ"],
        ["take","took","taken","取る"],
        ["teach","taught","taught","教える"],
        ["tell","told","told","伝える"],
        ["think","thought","thought","考える"],
        ["throw","threw","thrown","投げる"],
        ["understand","understood","understood","理解する"],
        ["wake","woke","woken","目覚める"],
        ["wear","wore","worn","着る"],
        ["win","won","won","勝つ"],
        ["write","wrote","written","書く"],
    ]
    rows = ""
    for v in verbs:
        rows += f"<tr><td>{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td><td>{v[3]}</td></tr>\n"
    
    html = HEADER.format(title="不規則動詞一覧表", desc="中学英語の不規則動詞一覧。原形・過去形・過去分詞形・意味をまとめました。")
    html += f'''<div class="breadcrumb"><a href="../index.html">ホーム</a> > 不規則動詞一覧</div>
<article class="grammar-detail">
  <h1>📋 不規則動詞一覧表</h1>
  <p style="color:var(--gray-500);margin-bottom:24px;">中学英語で必須の不規則動詞をまとめました。原形・過去形・過去分詞形の3つセットで覚えましょう。</p>
  <div class="highlight"><p><strong>覚え方のコツ</strong><br>
  ① 3つとも同じ形：cut-cut-cut, put-put-put<br>
  ② 過去形と過去分詞が同じ：buy-bought-bought, catch-caught-caught<br>
  ③ 3つとも違う形：swim-swam-swum, write-wrote-written</p></div>
  <table>
    <tr><th>原形</th><th>過去形</th><th>過去分詞</th><th>意味</th></tr>
    {rows}
  </table>
</article>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>'''
    html += FOOTER
    os.makedirs(os.path.join(BASE, "verb"), exist_ok=True)
    path = os.path.join(BASE, "verb", "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  verb/index.html")

def gen_exam_page():
    """高校入試対策ページ"""
    html = HEADER.format(title="高校入試対策", desc="中学英語の高校入試対策。頻出文法・問題形式別の学習法まとめ。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > 高校入試対策</div>
<article class="grammar-detail">
  <h1>🎯 高校入試対策</h1>
  <p style="color:var(--gray-500);margin-bottom:24px;">高校入試の英語で高得点を取るための対策をまとめました。</p>
  
  <h2>出題傾向と対策</h2>
  <table>
    <tr><th>大問</th><th>出題内容</th><th>対策</th></tr>
    <tr><td>リスニング</td><td>対話・英文の聞き取り</td><td>教科書の音声を毎日聞く。シャドーイングが効果的。</td></tr>
    <tr><td>発音・アクセント</td><td>単語の発音・強勢</td><td>英単語を覚えるときに発音記号も確認する。</td></tr>
    <tr><td>語順並べ替え</td><td>与えられた語を並べ替えて英文完成</td><td>文法の語順ルールを完璧に。5文型を理解する。</td></tr>
    <tr><td>文法選択</td><td>空欄補充（4択）</td><td>各単元の練習問題を反復。間違えた問題を記録。</td></tr>
    <tr><td>長文読解</td><td>400〜800語の英文読解</td><td>毎日1題は長文を読む。知らない単語は文脈で推測。</td></tr>
    <tr><td>英作文</td><td>テーマに沿った英文作成</td><td>基本文型を暗記。自分の意見を持ち、表現できるように。</td></tr>
  </table>

  <h2>重要文法チェックリスト</h2>
  <ul>
    <li>✅ be動詞（am/are/is）の使い分け</li>
    <li>✅ 一般動詞の疑問文・否定文（do/does/did）</li>
    <li>✅ 三人称単数現在のs/es</li>
    <li>✅ 現在進行形・過去進行形</li>
    <li>✅ 未来形（will / be going to）</li>
    <li>✅ 不定詞（3用法）</li>
    <li>✅ 動名詞</li>
    <li>✅ 比較級・最上級</li>
    <li>✅ 受け身（受動態）</li>
    <li>✅ 現在完了（3用法）</li>
    <li>✅ 関係代名詞（who/which/that）</li>
    <li>✅ 間接疑問</li>
    <li>✅ 仮定法</li>
  </ul>

  <h2>よく出る不規則動詞（厳選20）</h2>
  <table>
    <tr><th>原形</th><th>過去形</th><th>意味</th></tr>
    <tr><td>be</td><td>was/were</td><td>〜である</td></tr>
    <tr><td>become</td><td>became</td><td>〜になる</td></tr>
    <tr><td>begin</td><td>began</td><td>始める</td></tr>
    <tr><td>break</td><td>broke</td><td>壊す</td></tr>
    <tr><td>come</td><td>came</td><td>来る</td></tr>
    <tr><td>do</td><td>did</td><td>する</td></tr>
    <tr><td>eat</td><td>ate</td><td>食べる</td></tr>
    <tr><td>get</td><td>got</td><td>得る</td></tr>
    <tr><td>go</td><td>went</td><td>行く</td></tr>
    <tr><td>have</td><td>had</td><td>持つ</td></tr>
    <tr><td>know</td><td>knew</td><td>知っている</td></tr>
    <tr><td>make</td><td>made</td><td>作る</td></tr>
    <tr><td>read</td><td>read</td><td>読む</td></tr>
    <tr><td>see</td><td>saw</td><td>見る</td></tr>
    <tr><td>speak</td><td>spoke</td><td>話す</td></tr>
    <tr><td>take</td><td>took</td><td>取る</td></tr>
    <tr><td>teach</td><td>taught</td><td>教える</td></tr>
    <tr><td>tell</td><td>told</td><td>伝える</td></tr>
    <tr><td>think</td><td>thought</td><td>考える</td></tr>
    <tr><td>write</td><td>wrote</td><td>書く</td></tr>
  </table>

  <div class="note"><strong>入試までのスケジュール例</strong><br>
  3ヶ月前：全単元の文法を復習（このサイトで！）<br>
  2ヶ月前：過去問を解き始める（週1回）<br>
  1ヶ月前：苦手単元を集中的に対策<br>
  2週間前：時間を計って過去問演習<br>
  1週間前：間違えた問題の最終確認</div>

  <h2>おすすめ学習の流れ</h2>
  <ol>
    <li><a href="../index.html#grammar">文法解説</a>で単元を理解する</li>
    <li><a href="../index.html#practice">練習問題</a>で基本を固める</li>
    <li><a href="../test/index.html">確認テスト</a>で実力をチェック</li>
    <li><a href="../word/index.html">英単語帳</a>で語彙力アップ</li>
    <li>間違えた問題は<strong>必ず</strong>復習する</li>
  </ol>
</article>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>'''
    html += FOOTER
    os.makedirs(os.path.join(BASE, "exam"), exist_ok=True)
    path = os.path.join(BASE, "exam", "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  exam/index.html")

def gen_sitemap():
    """サイトマップ"""
    sections = {
        "ホーム": [("index.html", "トップページ")],
        "文法解説": [],
        "練習問題": [],
        "確認テスト": [],
        "その他": []
    }
    grammar_pages = [
        ("be.html","be動詞"),("ippan.html","一般動詞"),("gimonhitei.html","疑問文・否定文"),
        ("gimonsi.html","疑問詞"),("meirei.html","命令文"),("santan.html","三人称単数現在"),
        ("shinko.html","現在進行形"),("can.html","can"),("kako.html","一般動詞の過去形"),
        ("fukusu.html","名詞の複数形"),("daimeisi.html","代名詞"),("bekako.html","be動詞の過去形"),
        ("kakosin.html","過去進行形"),("mirai.html","未来形"),("doumei.html","動名詞"),
        ("futeisi1.html","不定詞（基本）"),("jyodosi.html","助動詞"),("hikaku1.html","比較"),
        ("there.html","there is"),("setuzoku.html","接続詞"),("ukemi.html","受け身"),
        ("genkan1.html","現在完了（継続）"),("genkan2.html","現在完了（経験）"),("genkan3.html","現在完了（完了）"),
        ("genkanSinkokei.html","現在完了進行形"),("futeisi2.html","不定詞（応用）"),
        ("bunsi.html","分詞"),("kansetu.html","間接疑問"),("kankeisi1.html","関係代名詞"),
        ("kateiho.html","仮定法"),("genkeiFuteisi.html","原形不定詞")
    ]
    practice_pages = [
        ("be.html","be動詞"),("ippan.html","一般動詞"),("santan.html","三人称単数現在"),
        ("gimonhitei.html","疑問文・否定文"),("meirei.html","命令文"),("can.html","can"),
        ("kako.html","一般動詞の過去形"),("shinko.html","現在進行形"),("bekako.html","be動詞の過去形"),
        ("kakosin.html","過去進行形"),("mirai.html","未来形"),("doumei.html","動名詞"),
        ("futeisi.html","不定詞"),("jyodosi.html","助動詞"),("hikaku.html","比較"),
        ("there.html","there is"),("setuzoku.html","接続詞"),("ukemi.html","受け身"),
        ("genkan.html","現在完了"),("kankeisi.html","関係代名詞")
    ]
    test_pages = [
        ("be_test.html","be動詞"),("ippan_test.html","一般動詞"),("santan_test.html","三人称単数現在"),
        ("gimonhitei_test.html","疑問文・否定文"),("meirei_test.html","命令文"),("can_test.html","can"),
        ("kako_test.html","一般動詞の過去形"),("shinko_test.html","現在進行形"),("bekako_test.html","be動詞の過去形"),
        ("kakosin_test.html","過去進行形"),("mirai_test.html","未来形"),("doumei_test.html","動名詞"),
        ("futeisi_test.html","不定詞"),("jyodosi_test.html","助動詞"),("hikaku_test.html","比較"),
        ("there_test.html","there is"),("setuzoku_test.html","接続詞"),("ukemi_test.html","受け身"),
        ("genkan_test.html","現在完了"),("kankeisi_test.html","関係代名詞")
    ]
    
    html = HEADER.format(title="サイトマップ", desc="中学英語学習サイトのサイトマップ。全ページの一覧。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > サイトマップ</div>
<article class="grammar-detail">
  <h1>📂 サイトマップ</h1>
  <p style="color:var(--gray-500);margin-bottom:24px;">全ページの一覧です。</p>
  
  <h2>🏠 ホーム</h2>
  <ul><li><a href="../index.html">トップページ</a></li></ul>
  
  <h2>📖 文法解説（34単元）</h2>
  <ul>'''
    for fname, name in grammar_pages:
        html += f'<li><a href="../grammar/{fname}">{name}</a></li>\n'
    html += '''</ul>
  
  <h2>✏️ 練習問題（20単元）</h2>
  <ul>'''
    for fname, name in practice_pages:
        html += f'<li><a href="../practice/{fname}">{name}</a></li>\n'
    html += '''</ul>
  
  <h2>📝 確認テスト（20単元）</h2>
  <ul>'''
    for fname, name in test_pages:
        html += f'<li><a href="../test/{fname}">{name}</a></li>\n'
    html += '''</ul>
  
  <h2>📚 その他</h2>
  <ul>
    <li><a href="../word/index.html">英単語帳</a></li>
    <li><a href="../verb/index.html">不規則動詞一覧</a></li>
    <li><a href="../exam/index.html">高校入試対策</a></li>
  </ul>
</article>'''
    html += FOOTER
    path = os.path.join(BASE, "sitemap.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  sitemap.html")

def update_index():
    """トップページを更新（英単語帳・不規則動詞・入試対策へのリンク追加）"""
    path = os.path.join(BASE, "index.html")
    with open(path, "r") as f:
        content = f.read()
    
    # 特徴部分の後にリンクセクションを追加
    insert_point = '<!-- Features -->'
    extra_content = '''
<!-- Extra Links -->
<section class="container">
  <h2 class="section-title">📚 学習ツール</h2>
  <p class="section-subtitle">英語学習をもっと便利に。</p>
  <div class="stats-grid">
    <a href="word/index.html" class="stat-card" style="text-decoration:none;color:inherit;cursor:pointer;">
      <div class="num" style="font-size:2rem;">📖</div>
      <h3 style="margin:8px 0;font-size:1rem;">英単語帳</h3>
      <div class="label">中学1年〜3年の英単語をチェック</div>
    </a>
    <a href="verb/index.html" class="stat-card" style="text-decoration:none;color:inherit;cursor:pointer;">
      <div class="num" style="font-size:2rem;">📋</div>
      <h3 style="margin:8px 0;font-size:1rem;">不規則動詞一覧</h3>
      <div class="label">原形・過去形・過去分詞を一覧で</div>
    </a>
    <a href="exam/index.html" class="stat-card" style="text-decoration:none;color:inherit;cursor:pointer;">
      <div class="num" style="font-size:2rem;">🎯</div>
      <h3 style="margin:8px 0;font-size:1rem;">高校入試対策</h3>
      <div class="label">出題傾向・チェックリスト・学習計画</div>
    </a>
    <a href="sitemap.html" class="stat-card" style="text-decoration:none;color:inherit;cursor:pointer;">
      <div class="num" style="font-size:2rem;">📂</div>
      <h3 style="margin:8px 0;font-size:1rem;">サイトマップ</h3>
      <div class="label">全ページ一覧</div>
    </a>
  </div>
</section>

'''
    content = content.replace(insert_point, extra_content + insert_point)
    
    # フッターを更新
    new_footer = '''<footer class="footer">
  <div class="footer-inner">
    <div>
      <h3>📚 中学英語Lab</h3>
      <p style="font-size:0.85rem;line-height:1.6;">中学生のための無料英語学習サイト。<br>英文法・練習問題・確認テストで<br>英語力を確実にアップ。</p>
    </div>
    <div>
      <h3>文法解説</h3>
      <a href="grammar/be.html">be動詞</a>
      <a href="grammar/futeisi1.html">不定詞</a>
      <a href="grammar/genkan1.html">現在完了</a>
      <a href="grammar/kankeisi1.html">関係代名詞</a>
    </div>
    <div>
      <h3>練習問題</h3>
      <a href="practice/be.html">be動詞 問題</a>
      <a href="practice/futeisi.html">不定詞 問題</a>
      <a href="practice/genkan.html">現在完了 問題</a>
      <a href="practice/hikaku.html">比較 問題</a>
    </div>
    <div>
      <h3>確認テスト</h3>
      <a href="test/be_test.html">be動詞 テスト</a>
      <a href="test/futeisi_test.html">不定詞 テスト</a>
      <a href="test/genkan_test.html">現在完了 テスト</a>
      <a href="test/kankeisi_test.html">関係代名詞 テスト</a>
    </div>
    <div>
      <h3>その他</h3>
      <a href="word/index.html">英単語帳</a>
      <a href="verb/index.html">不規則動詞一覧</a>
      <a href="exam/index.html">高校入試対策</a>
      <a href="sitemap.html">サイトマップ</a>
    </div>
  </div>
  <div class="footer-bottom">
    &copy; 2026 中学英語Lab. Created with AI.
  </div>
</footer>'''
    old_footer = '''<footer class="footer">
  <div class="footer-inner">
    <div>
      <h3>📚 中学英語Lab</h3>
      <p style="font-size:0.85rem;line-height:1.6;">中学生のための無料英語学習サイト。<br>英文法・練習問題・確認テストで<br>英語力を確実にアップ。</p>
    </div>
    <div>
      <h3>文法解説</h3>
      <a href="grammar/be.html">be動詞</a>
      <a href="grammar/futeisi1.html">不定詞</a>
      <a href="grammar/genkan1.html">現在完了</a>
      <a href="grammar/kankeisi1.html">関係代名詞</a>
    </div>
    <div>
      <h3>練習問題</h3>
      <a href="practice/be.html">be動詞 問題</a>
      <a href="practice/futeisi.html">不定詞 問題</a>
      <a href="practice/genkan.html">現在完了 問題</a>
      <a href="practice/hikaku.html">比較 問題</a>
    </div>
    <div>
      <h3>確認テスト</h3>
      <a href="test/be_test.html">be動詞 テスト</a>
      <a href="test/futeisi_test.html">不定詞 テスト</a>
      <a href="test/genkan_test.html">現在完了 テスト</a>
      <a href="test/kankeisi_test.html">関係代名詞 テスト</a>
    </div>
  </div>
  <div class="footer-bottom">
    &copy; 2026 中学英語Lab. Created with AI.
  </div>
</footer>'''
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
    
    with open(path, "w") as f:
        f.write(content)
    print(f"  index.html updated")

def update_test_index():
    """テスト一覧ページを更新（全テスト追加）"""
    path = os.path.join(BASE, "test", "index.html")
    with open(path, "r") as f:
        content = f.read()
    
    all_tests = [
        ("be_test.html", "✅", "be動詞 テスト", "am, are, is の使い分け", "g1"),
        ("ippan_test.html", "🏃", "一般動詞 テスト", "一般動詞の肯定・否定・疑問文", "g1"),
        ("santan_test.html", "👤", "三人称単数現在 テスト", "三単現のs", "g1"),
        ("can_test.html", "💪", "can テスト", "〜できる", "g1"),
        ("kako_test.html", "⏪", "過去形 テスト", "一般動詞の過去形", "g1"),
        ("shinko_test.html", "🔄", "現在進行形 テスト", "be+ing", "g1"),
        ("gimonhitei_test.html", "❓", "疑問文・否定文 テスト", "be動詞と一般動詞の違い", "g1"),
        ("meirei_test.html", "❗", "命令文 テスト", "命令文・禁止文", "g1"),
        ("bekako_test.html", "✅⏪", "be動詞過去 テスト", "was/were", "g2"),
        ("kakosin_test.html", "🔄⏪", "過去進行形 テスト", "was/were+ing", "g2"),
        ("mirai_test.html", "🔮", "未来形 テスト", "will/be going to", "g2"),
        ("doumei_test.html", "🏊", "動名詞 テスト", "〜すること", "g2"),
        ("futeisi_test.html", "🎯", "不定詞 テスト", "3用法", "g2"),
        ("jyodosi_test.html", "⚡", "助動詞 テスト", "must/have to/may/should", "g2"),
        ("hikaku_test.html", "📊", "比較 テスト", "比較級・最上級", "g2"),
        ("there_test.html", "📍", "there is テスト", "〜がある・いる", "g2"),
        ("setuzoku_test.html", "🔗", "接続詞 テスト", "and/but/because/when/if", "g2"),
        ("ukemi_test.html", "🔄", "受け身 テスト", "受動態", "g2"),
        ("genkan_test.html", "📌", "現在完了 テスト", "継続・経験・完了", "g3"),
        ("kankeisi_test.html", "🔗👤", "関係代名詞 テスト", "who/which/that", "g3"),
    ]
    
    cards = ""
    for href, icon, name, desc, badge in all_tests:
        cards += f'''    <a href="{href}" class="grammar-card">
      <span class="icon">{icon}</span>
      <h3>{name}</h3>
      <p>{desc}</p>
      <span class="badge {badge}">{badge.replace("g1","中学1年").replace("g2","中学2年").replace("g3","中学3年")}</span>
    </a>
'''
    
    old_section = '<div class="grammar-grid">'
    new_section = f'<div class="grammar-grid">\n{cards}'
    content = content.replace(old_section, new_section)
    
    # フッター更新
    new_footer = '''<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a></div>
    <div><h3>確認テスト</h3><a href="be_test.html">be動詞</a><a href="futeisi_test.html">不定詞</a><a href="genkan_test.html">現在完了</a></div>
    <div><h3>その他</h3><a href="../word/index.html">英単語帳</a><a href="../verb/index.html">不規則動詞</a><a href="../exam/index.html">入試対策</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>'''
    old_footer = '''<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a></div>
    <div><h3>確認テスト</h3><a href="be_test.html">be動詞</a><a href="futeisi_test.html">不定詞</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>'''
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
    
    with open(path, "w") as f:
        f.write(content)
    print(f"  test/index.html updated")

if __name__ == "__main__":
    print("=== 不規則動詞一覧 ===")
    gen_irregular_verbs()
    print("=== 高校入試対策 ===")
    gen_exam_page()
    print("=== サイトマップ ===")
    gen_sitemap()
    print("=== トップページ更新 ===")
    update_index()
    print("=== テスト一覧更新 ===")
    update_test_index()
    print("=== 完了 ===")