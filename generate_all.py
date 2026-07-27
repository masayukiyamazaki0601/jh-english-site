#!/usr/bin/env python3
"""中学英語サイト 全ページ一括ジェネレーター（完全版）"""
import os, json, re

BASE = os.path.dirname(os.path.abspath(__file__))

HEADER = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 中学英語学習サイト</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} | 中学英語学習サイト">
<meta property="og:description" content="{desc}">
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
</div>'''

FOOTER = '''<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a><a href="../grammar/genkan1.html">現在完了</a><a href="../grammar/kankeisi1.html">関係代名詞</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a><a href="../practice/futeisi.html">不定詞</a><a href="../practice/genkan.html">現在完了</a><a href="../practice/kankeisi.html">関係代名詞</a></div>
    <div><h3>確認テスト</h3><a href="../test/be_test.html">be動詞</a><a href="../test/futeisi_test.html">不定詞</a><a href="../test/genkan_test.html">現在完了</a><a href="../test/kankeisi_test.html">関係代名詞</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''

# === 文中リンク変換関数 ===
def render_text(text):
    """[link:key]テキスト[/link] をHTMLリンクに変換"""
    return re.sub(r'\[link:([a-zA-Z0-9_]+)\]([^[]+)\[/link\]', r'<a href="\1.html">\2</a>', text)

def render_content(blocks):
    html = ""
    for b in blocks:
        t = b[0]
        if t == "h2":
            html += f"<h2>{b[1]}</h2>\n"
        elif t == "h3":
            html += f"<h3>{b[1]}</h3>\n"
        elif t == "p":
            html += f"<p>{render_text(b[1])}</p>\n"
        elif t == "highlight":
            html += f'<div class="highlight"><p>{render_text(b[1])}</p></div>\n'
        elif t == "note":
            html += f'<div class="note"><strong>Check!</strong> {render_text(b[1])}</div>\n'
        elif t == "mistake":
            html += f'<div class="mistake"><strong>⚠️ よくある間違い</strong> {render_text(b[1])}</div>\n'
        elif t == "ul":
            html += "<ul>\n" + "".join(f"<li>{render_text(li)}</li>\n" for li in b[1]) + "</ul>\n"
        elif t == "ol":
            html += "<ol>\n" + "".join(f"<li>{render_text(li)}</li>\n" for li in b[1]) + "</ol>\n"
        elif t == "table":
            rows = b[1]
            html += "<table>\n"
            for i, row in enumerate(rows):
                tag = "th" if i == 0 else "td"
                html += "<tr>" + "".join(f"<{tag}>{render_text(c)}</{tag}>" for c in row) + "</tr>\n"
            html += "</table>\n"
    return html

# === 名前マップ ===
NAME_MAP = {
    "be":"be動詞","ippan":"一般動詞","gimonhitei":"疑問文・否定文","gimonsi":"疑問詞",
    "meirei":"命令文","santan":"三人称単数現在","shinko":"現在進行形","can":"can（助動詞）",
    "kako":"一般動詞の過去形","fukusu":"名詞の複数形","daimeisi":"代名詞",
    "bekako":"be動詞の過去形","kakosin":"過去進行形","mirai":"未来形",
    "doumei":"動名詞","futeisi1":"不定詞（基本）","jyodosi":"助動詞",
    "hikaku1":"比較","there":"there is 構文","setuzoku":"接続詞","ukemi":"受け身（受動態）",
    "genkan1":"現在完了（継続）","genkan2":"現在完了（経験）","genkan3":"現在完了（完了・結果）",
    "genkanSinkokei":"現在完了進行形","futeisi2":"不定詞（応用）","bunsi":"分詞",
    "kansetu":"間接疑問","kankeisi1":"関係代名詞","kateiho":"仮定法","genkeiFuteisi":"原形不定詞",
    "kansi":"冠詞（a, an, the）","zensi":"前置詞","suryo":"数量表現",
    "futeisi":"不定詞","genkan":"現在完了","hikaku":"比較","kankeisi":"関係代名詞",
}

# === 関連記事マッピング ===
RELATED_MAP = {
    "be": ["ippan", "gimonhitei", "shinko", "kansi"],
    "ippan": ["be", "santan", "gimonhitei", "kako"],
    "gimonhitei": ["be", "ippan", "santan", "gimonsi"],
    "gimonsi": ["gimonhitei", "kansetu"],
    "meirei": ["can", "jyodosi"],
    "santan": ["ippan", "gimonhitei", "kako"],
    "shinko": ["be", "kakosin", "genkanSinkokei"],
    "can": ["jyodosi", "meirei"],
    "kako": ["bekako", "kakosin", "genkan1"],
    "fukusu": ["daimeisi", "suryo"],
    "daimeisi": ["fukusu", "be"],
    "bekako": ["be", "kako", "kakosin"],
    "kakosin": ["shinko", "kako", "bekako"],
    "mirai": ["jyodosi", "futeisi1"],
    "doumei": ["futeisi1", "futeisi2", "shinko"],
    "futeisi1": ["futeisi2", "doumei", "genkeiFuteisi"],
    "jyodosi": ["can", "mirai", "genkeiFuteisi"],
    "hikaku1": ["futeisi1", "suryo"],
    "there": ["be", "fukusu", "zensi"],
    "setuzoku": ["futeisi1", "kankeisi1"],
    "ukemi": ["bunsi", "kako"],
    "genkan1": ["genkan2", "genkan3", "genkanSinkokei", "kako"],
    "genkan2": ["genkan1", "genkan3", "kako"],
    "genkan3": ["genkan1", "genkan2", "kako"],
    "genkanSinkokei": ["genkan1", "shinko"],
    "futeisi2": ["futeisi1", "genkeiFuteisi", "kansetu"],
    "bunsi": ["kankeisi1", "ukemi", "genkan1"],
    "kansetu": ["gimonsi", "kankeisi1", "futeisi2"],
    "kankeisi1": ["kansetu", "bunsi", "kateiho"],
    "kateiho": ["kankeisi1", "futeisi2", "jyodosi"],
    "genkeiFuteisi": ["futeisi1", "futeisi2", "jyodosi"],
    "kansi": ["be", "fukusu", "suryo", "daimeisi"],
    "zensi": ["there", "setuzoku", "genkan1"],
    "suryo": ["fukusu", "hikaku1", "kansi"],
}

def related_section(fname):
    related_ids = RELATED_MAP.get(fname, [])
    if not related_ids:
        return ""
    html = '\n<div class="related-articles">\n'
    html += '  <h2>📚 関連記事</h2>\n'
    html += '  <p>この単元と合わせて学ぼう</p>\n'
    html += '  <div class="related-grid">\n'
    for rid in related_ids:
        name = NAME_MAP.get(rid, rid)
        html += f'    <a href="{rid}.html" class="related-card">\n'
        html += f'      <span class="related-title">{name}</span>\n'
        html += f'      <span class="related-arrow">→</span>\n'
        html += f'    </a>\n'
    html += '  </div>\n</div>\n\n'
    return html

# === よくある間違いデータ ===
MISTAKE_MAP = {
    "be": [
        "「I am a student.」を「I are a student.」としない。I には必ず am。",
        "「He is not〜」を短縮せずに「He is not」でもOKだが、会話では「He isn't」が自然。",
        "「You are kind.」を「You is kind.」としない。you には are。",
    ],
    "ippan": [
        "三人称単数なのに動詞にsをつけ忘れる。「He play tennis.」は間違い→「He plays tennis.」",
        "否定文・疑問文で動詞にsをつけたままにする。「He doesn't plays.」は間違い→「He doesn't play.」",
        "be動詞と一般動詞を同じ文で両方使う「I am play tennis.」は間違い。",
    ],
    "gimonhitei": [
        "be動詞の疑問文なのに Do を使ってしまう「Do you are a student?」→「Are you a student?」",
        "一般動詞の疑問文なのに be動詞を文頭に置く「Are you like cats?」→「Do you like cats?」",
        "be動詞と一般動詞の区別がつかない。be動詞は am/are/is、それ以外は一般動詞。",
    ],
    "gimonsi": [
        "「Who is he?」への答えは「He is Taro.」が正しい。日本語の「誰」 = 「Who is」をセットで覚える。",
        "「How are you?」を理由を聞く質問だと思わない。これは「元気ですか？」の挨拶。",
    ],
    "meirei": [
        "命令文なのに主語をつけてしまう。「You sit down.」→「Sit down.」",
        "禁止文を「Not run.」としてしまう。正しくは「Don't run.」",
        "「Don't be late.」を「Don't late.」とbe動詞を省略しない。",
    ],
    "santan": [
        "「He go to school.」とsをつけ忘れる。「go→goes」に注意。",
        "「does」を使った疑問文で動詞にsをつけたまま「Does he plays?」→「Does he play?」",
    ],
    "shinko": [
        "「I am read a book.」とingをつけ忘れる。「I am reading a book.」が正しい。",
        "ing形のスペルミス（running を runing と書く、making を makeing と書く）。",
    ],
    "can": [
        "「He cans swim.」とcanにsをつけない。canは動詞の原形の前で形が変わらない。",
        "「I can to swim.」とtoをつけない。can + 動詞の原形（to不要）。",
    ],
    "kako": [
        "不規則動詞の過去形を暗記しないでedをつける「goed」「eated」は間違い。",
        "否定文で動詞を過去形のままにする「I didn't went.」→「I didn't go.」",
    ],
    "fukusu": [
        "「childs」ではなく「children」が正しい。不規則変化は暗記必須。",
        "「sheeps」としない。sheep は単複同形。",
    ],
    "daimeisi": [
        "「This is I pen.」と所有格を使わない。「This is my pen.」が正しい。",
        "主格と目的格を間違える。「Please help I.」→「Please help me.」",
    ],
    "bekako": [
        "「I were happy.」と主語とbe動詞を間違えない。I → was。",
    ],
    "kakosin": [
        "現在進行形と過去進行形を混同しない。現在は am/is/are、過去は was/were。",
    ],
    "mirai": [
        "「will」と「be going to」の違いがわからない。その場の決断はwill、前からの予定はbe going to。",
    ],
    "doumei": [
        "動名詞と現在進行形を混同しない。動名詞は名詞扱い、進行形は動詞扱い。",
    ],
    "futeisi1": [
        "「want + 動詞の原形」と「want + to + 動詞の原形」を混同しない。want のあとは必ず to不定詞。",
    ],
    "jyodosi": [
        "助動詞のあとは必ず動詞の原形。「must goes」→「must go」。",
    ],
    "hikaku1": [
        "比較級と最上級を混同しない。比較級は2つの比較（〜er）、最上級は3つ以上（the 〜est）。",
    ],
    "there": [
        "「There is」のあとに複数名詞を置かない。「There is many books.」→「There are many books.」",
    ],
    "setuzoku": [
        "「because」のあとに「So」を使わない。「Because〜, so〜」は重複表現。",
    ],
    "ukemi": [
        "受け身の過去分詞を原形のままにする。「is write」→「is written」。",
    ],
    "genkan1": [
        "「for」と「since」を混同しない。期間（5年間）は for、起点（2020年から）は since。",
    ],
    "genkan2": [
        "「have gone」と「have been」を混同しない。経験は have been、行ったきりは have gone。",
    ],
    "genkan3": [
        "「already」と「yet」の位置を間違えない。alreadyは動詞の前、yetは文末。",
    ],
    "genkanSinkokei": [
        "「have been + doing」の形を忘れない。doing が抜けて「have been study」にならないように。",
    ],
    "futeisi2": [
        "「It is 形容詞 for 人 to〜」のforを忘れない。「It is important to study」だけだと「誰が」が不明。",
    ],
    "bunsi": [
        "現在分詞と過去分詞の意味の違いを混同しない。doing = 能動（〜している）、done = 受動（〜された）。",
    ],
    "kansetu": [
        "間接疑問の語順を疑問文のままにしない。「Do you know where is he?」→「Do you know where he is?」",
    ],
    "kankeisi1": [
        "目的格の関係代名詞を省略できるのに省略しないという慎重すぎる間違いはOKだが、主格は省略できない。",
    ],
    "kateiho": [
        "仮定法で「If I was you」としない。仮定法では常に were を使う。「If I were you」が正しい。",
    ],
    "genkeiFuteisi": [
        "「make + 人 + to 動詞」とtoをつけてしまう。使役動詞のあとは動詞の原形（to不要）。",
    ],
    "kansi": [
        "「a university」を「an university」としない。母音の「音」で判断するので「a university」が正しい。",
        "「a hour」を「a hour」としない。「hour」はhが発音されないので「an hour」。音で判断！",
    ],
    "zensi": [
        "「at 7 o'clock」と「in the morning」の使い分けを間違えない。時刻はat、時間帯はin。",
        "「in Sunday」としない。曜日はon。「on Sunday」が正しい。",
    ],
    "suryo": [
        "「many time」としない。time（時間）は不可算名詞なので「much time」。",
        "「I don't have some money.」と肯定文と同じsomeを使わない。否定文・疑問文はany。",
    ],
}

# === 学習ロードマップ ===
ROADMAP_G1 = ["be", "ippan", "kansi", "suryo", "fukusu", "daimeisi", "gimonhitei", "gimonsi", "santan", "shinko", "can", "meirei", "kako"]
ROADMAP_G2 = ["bekako", "kakosin", "mirai", "jyodosi", "doumei", "futeisi1", "hikaku1", "zensi", "there", "setuzoku", "ukemi"]
ROADMAP_G3 = ["genkan1", "genkan2", "genkan3", "genkanSinkokei", "futeisi2", "bunsi", "genkeiFuteisi", "kansetu", "kankeisi1", "kateiho"]

ROADMAP_MAP = {"g1": ROADMAP_G1, "g2": ROADMAP_G2, "g3": ROADMAP_G3}

def roadmap_section(fname, gclass):
    roadmap = ROADMAP_MAP.get(gclass, [])
    try:
        idx = roadmap.index(fname)
    except ValueError:
        return ""
    prev_ = roadmap[idx - 1] if idx > 0 else None
    next_ = roadmap[idx + 1] if idx < len(roadmap) - 1 else None
    if not prev_ and not next_:
        return ""
    html = '\n<div class="roadmap-box">\n'
    html += '  <h2>🗺️ 学習の流れ</h2>\n'
    html += '  <div class="roadmap-links">\n'
    if prev_:
        pname = NAME_MAP.get(prev_, prev_)
        html += f'    <a href="{prev_}.html" class="roadmap-prev">← {pname}</a>\n'
    if next_:
        nname = NAME_MAP.get(next_, next_)
        html += f'    <a href="{next_}.html" class="roadmap-next">{nname} →</a>\n'
    html += '  </div>\n</div>\n\n'
    return html

# === 記事充実用追加コンテンツ ===
EXTRA_CONTENT = {
    "be": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["be動詞は am/are/is の3つ。主語によって形を選ぶ。","否定文は be動詞のうしろに not。疑問文は be動詞を文頭に。","短縮形（I'm, you're, isn'tなど）は日常会話で必須。","「〜です」「〜にいる」など日本語の「だ・である」に相当。"]),
        ("h2","📝 実践的な例文"),
        ("ul",["I am 13 years old.（私は13歳です）← 年齢は be動詞","She is from Osaka.（彼女は大阪出身です）← 出身も be動詞","We are in the classroom.（私たちは教室にいます）← 位置も be動詞","Are you hungry?（お腹すいてる？）← 状態も be動詞","It is sunny today.（今日は晴れです）← 天気も be動詞"]),
        ("p","be動詞は英語で最も使われる動詞。最初はたくさん例文を音読して、体で覚えよう！"),
    ],
    "ippan": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["一般動詞は動作や状態を表す（run, eat, play, studyなど）","be動詞と一般動詞の違いを理解することが最重要","否定文は don't/doesn't + 動詞の原形","疑問文は Do/Does + 主語 + 動詞の原形"]),
        ("h2","📝 実践的な例文"),
        ("ul",["I play soccer every Saturday.（毎週土曜日にサッカーをします）","She studies English every day.（彼女は毎日英語を勉強します）","They live in Tokyo.（彼らは東京に住んでいます）","We eat lunch at school.（学校で昼食を食べます）","My father works at a hospital.（父は病院で働いています）"]),
    ],
    "gimonhitei": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["be動詞の否定・疑問はbe動詞自身を使う（not / 文頭移動）","一般動詞の否定・疑問はdoを使う（don't/Do）","主語が3人称単数のときは does/doesn't を使う（動詞は原形）"]),
        ("h2","📝 be動詞 vs 一般動詞 比較表"),
        ("table",[["","be動詞","一般動詞"],["肯定文","She is kind.","She plays tennis."],["否定文","She is not kind.","She doesn't play tennis."],["疑問文","Is she kind?","Does she play tennis?"]]),
    ],
    "gimonsi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["疑問詞は文の先頭に置く","疑問詞のあとは疑問文の語順（be動詞/doを主語の前に）","howは「どのように」以外にも how many/much/old など多数の表現がある"]),
        ("h2","📝 実践的な会話例"),
        ("p","A: What is your name?<br>B: My name is Taro.<br><br>A: Where do you live?<br>B: I live in Kyoto.<br><br>A: Why are you studying English?<br>B: Because I want to travel abroad."),
    ],
    "meirei": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["命令文は動詞の原形で始める（主語不要）","禁止文は Don't + 動詞の原形","Let's + 動詞で「〜しましょう」（勧誘）","Please を付けると丁寧な依頼になる"]),
    ],
    "santan": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["主語が he/she/it のとき、動詞に s/es がつく","s,o,x,ch,sh で終わる動詞は es","子音+y で終わる動詞は y→ies","否定文・疑問文では does を使い、動詞は原形に戻す"]),
        ("h2","📝 よく使う三単現の動詞"),
        ("table",[["原形","三単現形","意味"],["go","goes","行く"],["do","does","する"],["have","has","持っている"],["study","studies","勉強する"],["watch","watches","見る"],["play","plays","遊ぶ/する"]]),
    ],
    "shinko": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["be動詞 + 動詞のing形で「今まさに〜している」","ing形のスペルルールを覚える（eをとる、子音を重ねる）","否定文・疑問文は be動詞と同じルール"]),
    ],
    "can": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["can + 動詞の原形（toは不要）","3単現でも can は形が変わらない","否定文は can't (cannot)、疑問文は Can を文頭に","「Can you〜?」は依頼・許可を求める丁寧な表現"]),
    ],
    "kako": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["規則動詞は語尾に ed をつける","不規則動詞は暗記必須（go→went, eat→ate, see→sawなど）","否定文・疑問文は did を使い、動詞は原形に戻す"]),
        ("h2","📝 暗記必須！不規則動詞20選"),
        ("table",[["原形","過去形","意味"],["go","went","行く"],["eat","ate","食べる"],["see","saw","見る"],["do","did","する"],["have","had","持っている"],["make","made","作る"],["take","took","取る"],["buy","bought","買う"],["get","got","得る"],["come","came","来る"]]),
    ],
    "fukusu": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["基本的に名詞に s をつける","s,o,x,ch,sh で終わる名詞は es","子音+y で終わる名詞は y→ies","不規則変化（child→children, man→menなど）は暗記"]),
    ],
    "daimeisi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["主格（I, he, she）は主語の位置","所有格（my, his, her）は名詞の前","目的格（me, him, her）は動詞・前置詞の後","所有代名詞（mine, his, hers）は「〜のもの」で単独使用"]),
    ],
    "bekako": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["be動詞の過去形は was（I/he/she/it）と were（you/we/they）","否定文は wasn't / weren't","疑問文は Was / Were を文頭に"]),
    ],
    "kakosin": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["was/were + 動詞のing形で「〜していた」","現在進行形の過去バージョン","よく使う時表現：at that time, when〜, at 5 o'clock yesterday"]),
    ],
    "mirai": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["will：その場で決めたこと・予測（助動詞）","be going to：前からの予定・確実な未来","否定文：will not (won't) / be not going to","疑問文：Will〜? / Are you going to〜?"]),
    ],
    "doumei": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["動名詞は「〜すること」（名詞扱い）","動詞のing形にする（規則は現在進行形と同じ）","不定詞と意味がほとんど同じ場合が多い（like, startなど）"]),
    ],
    "futeisi1": [
        ("h2","💡 3用法の見分け方"),
        ("p","名詞的用法：「〜すること」＝主語・目的語・補語の位置にある<br>副詞的用法：「〜するために」＝動詞を修飾（目的を表す）<br>形容詞的用法：「〜するための」＝名詞を修飾"),
        ("h2","📝 実践的な例文"),
        ("ul",["I want to be a doctor.（医者になりたい）← 名詞的用法","I went to the library to study.（勉強するために図書館に行った）← 副詞的用法","I need something to eat.（何か食べるものが必要）← 形容詞的用法"]),
    ],
    "jyodosi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["助動詞のあとは動詞の原形（必ず！）","must = have to（〜しなければならない）","may = 許可（〜してもよい）","should = アドバイス（〜すべきだ）"]),
    ],
    "hikaku1": [
        ("h2","💡 比較の3パターン"),
        ("table",[["用法","公式","例"],["比較級","〜er/more + than","taller than, more beautiful than"],["最上級","the + 〜est/most","the tallest, the most beautiful"],["原級比較","as + 原級 + as","as tall as, as big as"]]),
        ("h2","📝 不規則変化する形容詞"),
        ("table",[["原級","比較級","最上級"],["good/well","better","best"],["bad/badly","worse","worst"],["many/much","more","most"],["little","less","least"]]),
    ],
    "there": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["There is + 単数名詞 / There are + 複数名詞","否定文：There is not (isn't) / There are not (aren't)","疑問文：Is there〜? / Are there〜?"]),
    ],
    "setuzoku": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["接続詞は文と文をつなぐ言葉","and（追加）, but（対比）, because（理由）, when（時）, if（条件）が基本","because と so は一緒に使わない"]),
    ],
    "ukemi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["受け身 = be動詞 + 過去分詞","能動態の目的語が受け身の主語になる","動作主を示すときは by + 人","by 〜 は省略することも多い"]),
    ],
    "genkan1": [
        ("h2","💡 現在完了の3用法"),
        ("table",[["用法","意味","例文のキーワード"],["継続","ずっと〜している","for, since"],["経験","〜したことがある","ever, never, before"],["完了・結果","もう〜した/たった今〜した","already, just, yet"]]),
        ("h2","📝 for と since の違い"),
        ("p","for + 期間（for two years, for three hours）<br>since + 起点（since 2020, since last week）"),
    ],
    "genkan2": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["経験用法は「have/has + 過去分詞」","ever は疑問文「今までに〜？」","never は否定文「一度も〜ない」","been to 〜（行ったことがある）/ gone to 〜（行ってしまっている）の違いに注意"]),
    ],
    "genkan3": [
        ("h2","💡 already / just / yet の位置"),
        ("p","already：「もう〜した」（肯定文）→ have already + 過去分詞<br>just：「ちょうど〜した」（肯定文）→ have just + 過去分詞<br>yet：「もう〜？」（疑問文）/「まだ〜ない」（否定文）→ 文末"),
    ],
    "genkanSinkokei": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["have/has been + 動詞のing形","「ずっと〜し続けている」という継続の強調","for（期間）や since（起点）と一緒によく使う"]),
    ],
    "futeisi2": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["It is + 形容詞 + for + 人 + to〜：誰にとってどうかを明確に","疑問詞 + 不定詞（what to do, how to swim）は間接疑問の簡略版","ask/tell + 人 + to〜：依頼・指示の表現"]),
    ],
    "bunsi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["現在分詞（doing）：能動「〜している」","過去分詞（done）：受動「〜された」","後ろから名詞を修飾（後置修飾）","関係代名詞の代わりになる"]),
    ],
    "kansetu": [
        ("h2","💡 ポイントまとめ"),
        ("p","間接疑問の最大のルール：<br>❌ Do you know where is he?<br>✅ Do you know where he is?<br><br>疑問詞のあとは「主語 + 動詞」の順番になる！"),
    ],
    "kankeisi1": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["who = 人（主格）","which = 物（主格・目的格）","that = 人・物両方（主格・目的格）","主格の関係代名詞は省略できない","目的格の関係代名詞は省略できる"]),
    ],
    "kateiho": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["仮定法過去：「もし〜なら（実際は違う）」","If + 過去形, 主語 + would/could + 動詞の原形","be動詞は常に were（I でも were）","現実と違うことを仮定するときに使う"]),
    ],
    "genkeiFuteisi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["使役動詞（make, let, have）+ 人 + 動詞の原形","知覚動詞（see, hear, watch）+ 人 + 動詞の原形","to をつけない不定詞 = 原形不定詞"]),
    ],
    "kansi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["a/an：不特定のもの（初出）・1つの・種類全体","the：特定のもの（既出）・唯一無二・最上級","冠詞不要：固有名詞・食事・スポーツ・交通手段"]),
    ],
    "zensi": [
        ("h2","💡 ポイントまとめ"),
        ("ul",["場所：in（中）, on（上）, at（地点）, under（下）, near（近く）","時間：at（時刻）, in（月/年）, on（曜日）, for（期間）, since（起点）","方向：to（へ）, from（から）, for（目的・向かって）"]),
    ],
    "suryo": [
        ("h2","💡 可算名詞 vs 不可算名詞 一覧"),
        ("table",[["可算名詞（数えられる）","不可算名詞（数えられない）"],["book, cat, apple, student","water, music, information, money"],["chair, desk, pen, bottle","time, weather, homework, news"],["person, city, country, animal","advice, knowledge, luck, love"]]),
        ("h2","💡 ポイントまとめ"),
        ("ul",["many + 可算名詞 / much + 不可算名詞","some = 肯定文 / any = 疑問文・否定文","a few + 可算名詞 / a little + 不可算名詞","a lot of / lots of = 両方OK"]),
    ],
}

def mistake_section(fname):
    mistakes = MISTAKE_MAP.get(fname, [])
    if not mistakes:
        return ""
    html = '\n<div class="mistake-section">\n'
    html += '  <h2>⚠️ よくある間違い</h2>\n'
    html += '  <ul>\n'
    for m in mistakes:
        html += f'    <li>{render_text(m)}</li>\n'
    html += '  </ul>\n</div>\n\n'
    return html

# === 文法データ ===
GRAMMAR_DATA = [
    ("gimonhitei", "疑問文・否定文", "g1", [
        ("h2","be動詞の疑問文・否定文"),
        ("p","[link:be]be動詞[/link]の否定文は be動詞のうしろに not を置く。疑問文は be動詞を文頭に置く。"),
        ("highlight","否定文: 主語 + be動詞 + not 〜<br>疑問文: Be動詞 + 主語 + 〜？"),
        ("h2","一般動詞の疑問文・否定文"),
        ("p","[link:ippan]一般動詞[/link]の否定文は do not (don't) を使う。疑問文は Do を文頭に置く。"),
        ("highlight","否定文: 主語 + do not + 動詞の原形<br>疑問文: Do + 主語 + 動詞の原形？"),
        ("note","ちがいは？<br>be動詞は「be動詞自身」を使って否定・疑問を作る。<br>一般動詞は「do」を使って否定・疑問を作る。"),
    ]),
    ("gimonsi", "疑問詞", "g1", [
        ("h2","疑問詞とは？"),
        ("p","「何」「誰」「どこ」など、具体的な情報を尋ねるときに使う特別な疑問文。まずは[link:gimonhitei]疑問文・否定文[/link]をマスターしてから学ぼう。"),
        ("table",[["疑問詞","意味","例"],["what","何","What is this?"],["who","誰","Who is he?"],["where","どこ","Where are you?"],["when","いつ","When is your birthday?"],["why","なぜ","Why are you late?"],["how","どのように","How are you?"]]),
        ("p","疑問詞を使うときは、疑問詞を文の先頭に置き、そのあとに疑問文の語順が続く。深く学ぶなら[link:kansetu]間接疑問[/link]もチェック。"),
    ]),
    ("meirei", "命令文", "g1", [
        ("h2","命令文の作り方"),
        ("p","動詞の原形で文を始める。主語は必要ない。"),
        ("highlight","【公式】 動詞の原形 + 〜"),
        ("ul",["Sit down.（座りなさい）","Open your book.（本を開きなさい）","Stand up.（立ちなさい）"]),
        ("h2","禁止文（否定の命令）"),
        ("p","Don't を文頭に置く。一般動詞の否定と同じルール。関連：[link:gimonhitei]疑問文・否定文[/link]"),
        ("highlight","【公式】 Don't + 動詞の原形 + 〜"),
        ("ul",["Don't run.（走ってはいけません）","Don't be late.（遅れてはいけません）","Don't eat in class.（教室で食べてはいけません）"]),
        ("note", "[link:can]can[/link] や [link:jyodosi]助動詞[/link] と合わせて学ぶと理解が深まる。"),
    ]),
    ("santan", "三人称単数現在", "g1", [
        ("h2","三人称単数現在とは？"),
        ("p","主語が he, she, it（またはそれに相当する単数名詞）で、時制が現在のとき、動詞に s または es がつくルール。[link:ippan]一般動詞[/link]の応用。"),
        ("highlight","【公式】 主語(3人称単数) + 動詞 + s/es + 〜"),
        ("h2","s/esの付け方"),
        ("table",[["ルール","例"],["ふつうは s をつける","play → plays, eat → eats"],["s,o,x,ch,sh で終わる → es","go → goes, watch → watches"],["子音字+y で終わる → yをiに変えてes","study → studies"]]),
        ("h2","疑問文・否定文"),
        ("p","三人称単数現在の疑問文・否定文は does / doesn't を使う。動詞は原形に戻す。"),
        ("ul",["He plays tennis. → He doesn't play tennis.","She studies English. → Does she study English?"]),
    ]),
    ("shinko", "現在進行形", "g1", [
        ("h2","現在進行形とは"),
        ("p","「今まさに〜している」という動作の最中を表す。[link:be]be動詞[/link]と動詞のing形を組み合わせる。"),
        ("highlight","【公式】 主語 + be動詞 + 動詞のing形 + 〜"),
        ("ul",["I am reading a book.（本を読んでいます）","She is watching TV.（テレビを見ています）"]),
        ("h2","ing形の作り方"),
        ("table",[["ルール","例"],["ふつうは ing をつける","play → playing"],["e で終わる → e をとって ing","make → making"],["短母音+子音字 → 子音を重ねて ing","run → running, swim → swimming"]]),
        ("h2","否定文・疑問文"),
        ("p","be動詞の否定・疑問と同じルール。[link:gimonhitei]疑問文・否定文[/link]を復習しよう。"),
        ("ul",["He is not sleeping.（彼は寝ていません）","Are you studying?（勉強していますか？）"]),
        ("note", "過去の進行中は [link:kakosin]過去進行形[/link] を参照。"),
    ]),
    ("can", "can（助動詞）", "g1", [
        ("h2","canの意味"),
        ("p","「〜できる」という能力や可能性を表す助動詞。他の助動詞については[link:jyodosi]助動詞[/link]を参照。"),
        ("highlight","【公式】 主語 + can + 動詞の原形 + 〜"),
        ("ul",["I can swim.（泳げます）","She can speak English.（英語を話せます）"]),
        ("h2","否定文・疑問文"),
        ("p","否定は can not (can't)、疑問は Can を文頭に。"),
        ("ul",["I can't play the piano.（ピアノを弾けません）","Can you help me?（手伝ってくれますか？）","Yes, I can. / No, I can't."]),
        ("note", "[link:meirei]命令文[/link] と組み合わせて「Can you〜?」は丁寧な依頼表現としても使える。"),
    ]),
    ("kako", "一般動詞の過去形", "g1", [
        ("h2","過去形とは"),
        ("p","過去の出来事や状態を表す。動詞の形が変化する。[link:ippan]一般動詞[/link]の過去形バージョン。"),
        ("h2","規則動詞（ed形）"),
        ("table",[["ルール","例"],["ふつうは ed をつける","play → played"],["e で終わる → d だけ","like → liked"],["子音字+y → yをiに変えてed","study → studied"]]),
        ("h2","不規則動詞（暗記必須）"),
        ("p","不規則動詞は暗記するしかない。[link:genkan1]現在完了[/link]でも過去分詞が必要になるのでしっかり覚えよう。"),
        ("table",[["原形","過去形"],["go","went"],["eat","ate"],["see","saw"],["do","did"],["have","had"],["make","made"]]),
        ("h2","否定文・疑問文"),
        ("p","過去形の否定・疑問は did / didn't を使う。動詞は原形に戻す。[link:gimonhitei]疑問文・否定文[/link]の過去形版。"),
        ("ul",["I didn't go to school.（学校に行きませんでした）","Did you eat breakfast?（朝食を食べましたか？）"]),
    ]),
    ("fukusu", "名詞の複数形", "g1", [
        ("h2","複数形の作り方"),
        ("table",[["ルール","例"],["ふつうは s","cat → cats"],["s,o,x,ch,sh → es","box → boxes"],["子音+y → yをiに変えてes","baby → babies"],["f,fe → ves","knife → knives"]]),
        ("h2","不規則な複数形"),
        ("ul",["child → children","man → men","woman → women","foot → feet","tooth → teeth","sheep → sheep"]),
        ("p", "複数形と合わせて[link:suryo]数量表現[/link]（many/muchなど）も学ぶと実践的。"),
    ]),
    ("daimeisi", "代名詞", "g1", [
        ("h2","人称代名詞の変化表"),
        ("table",[["主格(〜は)","所有格(〜の)","目的格(〜を)","所有代名詞(〜のもの)"],["I","my","me","mine"],["you","your","you","yours"],["he","his","him","his"],["she","her","her","hers"],["it","its","it","its"],["we","our","us","ours"],["they","their","them","theirs"]]),
        ("note","「私の本」は my book。「私のもの」は mine。所有格+名詞 = 所有代名詞の関係を覚えよう。"),
        ("p", "代名詞は[link:be]be動詞[/link]や[link:ippan]一般動詞[/link]の例文でよく出てくる。合わせて復習しよう。"),
    ]),
    ("bekako", "be動詞の過去形", "g2", [
        ("h2","be動詞の過去形"),
        ("p","[link:be]be動詞[/link]の過去形は was / were。[link:kako]一般動詞の過去形[/link]と合わせて覚えよう。"),
        ("highlight","am, is → was<br>are → were"),
        ("table",[["主語","過去形"],["I","was"],["He, She, It","was"],["You, We, They","were"]]),
        ("h2","否定文・疑問文"),
        ("p","was not (wasn't) / were not (weren't) を使う。Was / Were を文頭に置く。"),
    ]),
    ("kakosin", "過去進行形", "g2", [
        ("h2","過去進行形とは"),
        ("p","「〜していた」過去のある時点で進行中の動作。[link:shinko]現在進行形[/link]の過去バージョン。"),
        ("highlight","【公式】 主語 + was/were + 動詞のing形 + 〜"),
        ("ul",["I was reading a book.（本を読んでいました）","They were playing soccer.（サッカーをしていました）"]),
    ]),
    ("mirai", "未来形", "g2", [
        ("h2","未来形の2つの表現"),
        ("p","英語の未来形には will と be going to の2つがある。[link:jyodosi]助動詞[/link]の一種。"),
        ("highlight","will: その場で決めたこと・予測<br>be going to: 予定・確実な未来"),
        ("ul",["I will help you.（手伝いますよ）← その場の意思","I am going to study tonight.（今夜勉強する予定）← 予定"]),
    ]),
    ("doumei", "動名詞", "g2", [
        ("h2","動名詞とは"),
        ("p","動詞のing形が名詞の役割をする。〜すること。[link:futeisi1]不定詞[/link]と似た意味になることが多い。"),
        ("highlight","【公式】 動詞の原形 + ing = 名詞"),
        ("ul",["I like swimming.（泳ぐことが好きです）","Playing tennis is fun.（テニスをすることは楽しいです）"]),
    ]),
    ("futeisi1", "不定詞（基本）", "g2", [
        ("h2","不定詞とは"),
        ("p","to + 動詞の原形 の形。3つの用法がある。[link:doumei]動名詞[/link]との違いも理解しよう。"),
        ("h2","名詞的用法"),
        ("p","「〜すること」 主語・目的語・補語になる。"),
        ("ul",["I want to go there.（そこに行きたい）","To study English is important.（英語を勉強することは大事だ）"]),
        ("h2","副詞的用法"),
        ("p","「〜するために」 目的を表す。"),
        ("ul",["I went to the library to study.（勉強するために図書館に行った）"]),
        ("h2","形容詞的用法"),
        ("p","「〜するための」 名詞を修飾。"),
        ("ul",["I have something to eat.（何か食べるものがある）"]),
        ("p", "応用編は[link:futeisi2]不定詞（応用）[/link]を、toなし不定詞は[link:genkeiFuteisi]原形不定詞[/link]を参照。"),
    ]),
    ("jyodosi", "助動詞", "g2", [
        ("h2","助動詞とは"),
        ("p","動詞の前に置いて、意味を付け加える言葉。[link:can]can[/link]も助動詞の一つ。"),
        ("table",[["助動詞","意味","例"],["must","〜しなければならない","You must study."],["have to","〜しなければならない","I have to go."],["may","〜してもよい","May I come in?"],["should","〜すべきだ","You should rest."]]),
        ("note","must と have to はほぼ同じ意味。must のほうがやや強い。"),
        ("p", "助動詞 + 動詞の原形 のルールは[link:genkeiFuteisi]原形不定詞[/link]の理解にもつながる。"),
    ]),
    ("hikaku1", "比較", "g2", [
        ("h2","比較級"),
        ("p","2つのものを比べて「より〜」と言いたいとき。"),
        ("highlight","【公式】 〜er / more + 〜 + than"),
        ("ul",["Taro is taller than Jiro.（太郎は次郎より背が高い）","She is more beautiful than me.（彼女は私より美しい）"]),
        ("h2","最上級"),
        ("p","3つ以上の中で「一番〜」と言いたいとき。"),
        ("highlight","【公式】 the + 〜est / the most + 〜"),
        ("ul",["Mt.Fuji is the highest mountain in Japan.（富士山は日本で一番高い山です）"]),
        ("h2","原級（as 〜 as）"),
        ("p","「〜と同じくらい」"),
        ("ul",["He is as tall as me.（彼は私と同じくらい背が高い）"]),
    ]),
    ("there", "there is 構文", "g2", [
        ("h2","there is / are の意味"),
        ("p","「〜がある・いる」という存在を表す。[link:be]be動詞[/link]の仲間。"),
        ("highlight","【公式】 There is + 単数名詞 + 場所<br>There are + 複数名詞 + 場所"),
        ("ul",["There is a cat under the table.（テーブルの下に猫がいます）","There are many books on the desk.（机の上にたくさんの本があります）"]),
    ]),
    ("setuzoku", "接続詞", "g2", [
        ("h2","接続詞とは"),
        ("p","文と文をつなぐ言葉。[link:kankeisi1]関係代名詞[/link]と似ているが、接続詞は文同士をつなぐだけ。"),
        ("table",[["接続詞","意味","例"],["and","〜と〜","I like cats and dogs."],["but","しかし","I like cats but I don't like dogs."],["because","なぜなら","I am happy because I got a present."],["when","〜するとき","Call me when you arrive."],["if","もし〜なら","If it rains, I will stay home."],["that","〜ということ","I think that he is kind."]]),
    ]),
    ("ukemi", "受け身（受動態）", "g2", [
        ("h2","受け身とは"),
        ("p","「〜される」という意味。動作を受ける側が主語になる。[link:kako]過去形[/link]や[link:bunsi]分詞[/link]の知識が必要。"),
        ("highlight","【公式】 主語 + be動詞 + 過去分詞 + by 〜"),
        ("ul",["English is spoken by many people.（英語は多くの人によって話されている）","This book was written by Soseki.（この本は漱石によって書かれた）"]),
    ]),
    ("genkan1", "現在完了（継続）", "g3", [
        ("h2","現在完了とは"),
        ("p","「過去のある時点から現在まで」を表す時制。3つの用法がある。まずは[link:kako]過去形[/link]との違いを理解しよう。"),
        ("highlight","【公式】 主語 + have/has + 過去分詞"),
        ("h2","継続用法"),
        ("p","「ずっと〜している」過去から現在まで続いている状態。"),
        ("ul",["I have lived in Tokyo for five years.（東京に5年間住んでいます）","She has been here since 2020.（彼女は2020年からここにいます）"]),
        ("p","[link:genkan2]経験用法[/link]・[link:genkan3]完了用法[/link]も合わせて学ぼう。"),
    ]),
    ("genkan2", "現在完了（経験）", "g3", [
        ("h2","経験用法"),
        ("p","「〜したことがある」今までの経験を表す。[link:genkan1]継続用法[/link]と形は同じだが意味が違う。"),
        ("ul",["I have been to Kyoto.（京都に行ったことがあります）","Have you ever seen a lion?（ライオンを見たことがありますか？）","She has never eaten sushi.（彼女は寿司を食べたことがありません）"]),
        ("note","ever（今までに）は疑問文、never（一度も〜ない）は否定文で使う。"),
    ]),
    ("genkan3", "現在完了（完了・結果）", "g3", [
        ("h2","完了・結果用法"),
        ("p","「ちょうど〜したところ」「もう〜した」動作の完了や結果を表す。"),
        ("ul",["I have just finished my homework.（ちょうど宿題を終えたところです）","She has already eaten lunch.（彼女はもう昼食を食べました）","Have you finished yet?（もう終わりましたか？）"]),
        ("note","already（もう）は肯定文、yet（もう〜？/まだ〜ない）は疑問文・否定文で使う。"),
    ]),
    ("genkanSinkokei", "現在完了進行形", "g3", [
        ("h2","現在完了進行形とは"),
        ("p","have/has been + doing 「ずっと〜し続けている」。 [link:genkan1]現在完了[/link]と[link:shinko]進行形[/link]の組み合わせ。"),
        ("highlight","【公式】 主語 + have/has + been + 動詞のing"),
        ("ul",["I have been studying for two hours.（2時間勉強し続けています）","It has been raining since morning.（朝から雨が降り続いています）"])]),
    ("futeisi2", "不定詞（応用）", "g3", [
        ("h2","It ... for ... to 構文"),
        ("p","「〜にとって…することは〜だ」。 [link:futeisi1]不定詞（基本）[/link]の応用。"),
        ("highlight","It is + 形容詞 + for + 人 + to + 動詞の原形"),
        ("ul",["It is important for you to study English.（あなたが英語を勉強することは重要です）"]),
        ("h2","疑問詞 + 不定詞"),
        ("ul",["I don't know what to do.（何をすればいいかわかりません）","He taught me how to swim.（彼は泳ぎ方を教えてくれました）"]),
        ("h2","ask/tell + 人 + to"),
        ("ul",["She told me to come here.（彼女はここに来るように言いました）","He asked me to help him.（彼は私に助けるように頼みました）"])]),
    ("bunsi", "分詞", "g3", [
        ("h2","分詞とは"),
        ("p","動詞のing形（現在分詞）と過去分詞が形容詞の役割をする。[link:kankeisi1]関係代名詞[/link]の代わりにもなる。"),
        ("h2","現在分詞（〜している）"),
        ("ul",["The girl singing on stage is my sister.（ステージで歌っている女の子は私の妹です）"]),
        ("h2","過去分詞（〜された・〜されたもの）"),
        ("ul",["The book written by him is interesting.（彼によって書かれた本は面白いです）"])]),
    ("kansetu", "間接疑問", "g3", [
        ("h2","間接疑問とは"),
        ("p","疑問文が文中に埋め込まれる形。語順に注意。[link:gimonsi]疑問詞[/link]の知識が必要。"),
        ("highlight","【公式】 主語 + 動詞 + 疑問詞 + 主語 + 動詞"),
        ("ul",["I know where he lives.（彼がどこに住んでいるか知っています）","Do you know what this is?（これが何か知っていますか？"]),
        ("note","間接疑問のあとは疑問文の語順ではなく、肯定文の語順（主語+動詞）になる！")]),
    ("kankeisi1", "関係代名詞", "g3", [
        ("h2","関係代名詞とは"),
        ("p","名詞を後ろから説明する。who（人）, which（物）, that（人・物両方）。[link:bunsi]分詞[/link]でも似た表現ができる。"),
        ("highlight","【公式】 名詞 + who/which/that + 動詞 + 〜"),
        ("ul",["The boy who is running is Taro.（走っている男の子は太郎です）","The book which I bought is interesting.（私が買った本は面白いです）"]),
        ("note","目的格の関係代名詞は省略できることがある。")]),
    ("kateiho", "仮定法", "g3", [
        ("h2","仮定法過去"),
        ("p","「もし〜なら（実際は違うけど）」現実と違うことを仮定する。[link:kankeisi1]関係代名詞[/link]などの文法をマスターしてから挑戦しよう。"),
        ("highlight","【公式】 If + 主語 + 過去形 + 〜, 主語 + would/could + 動詞の原形"),
        ("ul",["If I were you, I would go there.（もし私があなたなら、そこに行くのに） ← 実際はあなたではない"]),
        ("note","仮定法では be動詞は常に were を使う（主語が I でも were）。")]),
    ("genkeiFuteisi", "原形不定詞", "g3", [
        ("h2","原形不定詞とは"),
        ("p","to をつけない不定詞。知覚動詞や使役動詞のあとに使う。[link:futeisi1]不定詞[/link]と[link:jyodosi]助動詞[/link]の知識が前提。"),
        ("highlight","【公式】 使役動詞 + 人 + 動詞の原形"),
        ("ul",["He made me clean the room.（彼は私に部屋を掃除させた）","I saw him cross the street.（彼が通りを渡るのを見た）"]),
        ("note","let, make, have（使役）, see, hear, watch（知覚）のあとは動詞の原形。")]),
    ("kansi", "冠詞（a, an, the）", "g1", [
        ("h2","冠詞とは"),
        ("p","冠詞（かんし）は名詞の前に置く言葉。英語には a / an（不定冠詞）と the（定冠詞）の2種類がある。[link:fukusu]複数形[/link]と合わせて覚えると効果的。"),
        ("h2","a と an の使い分け"),
        ("p","a は子音の音で始まる名詞の前に、an は母音の音（a,i,u,e,o）で始まる名詞の前につける。"),
        ("highlight","a: a book, a cat, a university（子音の音）<br>an: an apple, an hour, an umbrella（母音の音）"),
        ("h2","a / an（不定冠詞）の使い方"),
        ("ul",["初めて話題に出るときに使う「I saw a cat.（猫を見た）」","「1つの」という意味「I need a pen.（ペンが1本必要）」","種類全体を表す「A cat is an animal.（猫は動物です）」"]),
        ("h2","the（定冠詞）の使い方"),
        ("ul",["すでに話題に出たもの「I saw a cat. The cat was black.」","文脈から明らかなもの「Please open the window.（その窓を開けて）」","唯一無二のもの「the sun, the moon, the earth」","最上級の前「the tallest boy」"]),
        ("h2","冠詞をつけない場合（無冠詞）"),
        ("ul",["固有名詞（Tokyo, Japan, Taro）","  meals（breakfast, lunch, dinner）","スポーツ・科目（play tennis, study English）","交通手段（by bus, by train）"]),
        ("note","冠詞は日本語にない概念なので難しい。最初は a = 1つの、the = その、とざっくり覚えよう！"),
    ]),
    ("zensi", "前置詞", "g2", [
        ("h2","前置詞とは"),
        ("p","前置詞（ぜんちし）は名詞の前に置いて、位置・方向・時間などの関係を表す言葉。[link:there]there is 構文[/link]と組み合わせてよく使う。"),
        ("h2","場所・位置の前置詞"),
        ("table",[["前置詞","意味","例"],["in","〜の中に","in the box"],["on","〜の上に","on the desk"],["at","〜で（地点）","at the station"],["under","〜の下に","under the bed"],["near","〜の近くに","near the park"],["between","〜の間に","between A and B"],["in front of","〜の前に","in front of the school"],["behind","〜の後ろに","behind the door"]]),
        ("h2","時間の前置詞"),
        ("table",[["前置詞","意味","例"],["at","〜に（時点）","at 7 o'clock, at night"],["in","〜に（月・年・季節）","in May, in 2024, in summer"],["on","〜に（曜日・日付）","on Sunday, on May 5th"],["for","〜の間（期間）","for two hours"],["since","〜から（起点）","since 2020"]]),
        ("h2","方向・その他の前置詞"),
        ("ul",["to（〜へ）: go to school","from（〜から）: come from Japan","with（〜と一緒に）: play with friends","for（〜のために）: study for the exam","by（〜によって）: by bus, by Soseki"]),
        ("note","前置詞は1つの言葉に複数の意味があるので、例文ごと覚えるのが効果的！"),
    ]),
    ("suryo", "数量表現", "g1", [
        ("h2","数量表現とは"),
        ("p","「たくさん」「いくつか」「少し」など、ものの数量を表す表現。可算名詞（数えられる）と不可算名詞（数えられない）で使い分ける。[link:fukusu]複数形[/link]と合わせて覚えよう。"),
        ("h2","可算名詞と不可算名詞"),
        ("p","可算名詞: 数えられる名詞（cat, book, apple）<br>不可算名詞: 数えられない名詞（water, music, information, money）"),
        ("h2","many / much"),
        ("p","manyは可算名詞、muchは不可算名詞に使う。「たくさん〜」"),
        ("highlight","many + 可算名詞: many books, many students<br>much + 不可算名詞: much water, much time"),
        ("h2","some / any"),
        ("p","someは肯定文、anyは否定文・疑問文で使う。「いくつかの〜」「いくらかの〜」"),
        ("highlight","some: I have some friends.（肯定文）<br>any: Do you have any questions?（疑問文）<br>any: I don't have any money.（否定文）"),
        ("h2","a few / a little"),
        ("p","a fewは可算名詞、a littleは不可算名詞。「少し〜」"),
        ("highlight","a few + 可算名詞: a few books（数冊の本）<br>a little + 不可算名詞: a little water（少しの水）"),
        ("h2","a lot of / lots of"),
        ("p","可算・不可算どちらにも使える「たくさんの〜」。"),
        ("highlight","a lot of friends / a lot of money<br>lots of people / lots of time"),
        ("note","可算名詞か不可算名詞かで使える表現が変わる。名詞の種類を意識しよう！"),
    ]),
]

GRAMMAR_DATA = [
    ("be", "be動詞", "g1", [
        ("h2","be動詞とは？"),
        ("p","be動詞は「〜です」「〜である」「〜にある/いる」という意味を表す動詞です。主語によって形が3つに変わります。[link:ippan]一般動詞[/link]と並んで英語の超基礎。"),
        ("highlight","be動詞の3つの形：<br>am（主語が I のとき）<br>are（主語が you / 複数のとき）<br>is（主語が he, she, it / 単数のとき）"),
        ("h2","肯定文の作り方"),
        ("table",[["主語","be動詞","例"],["I","am","I am a student."],["You","are","You are kind."],["He / She / It","is","He is my friend."],["We / They","are","We are happy."]]),
        ("h2","否定文の作り方"),
        ("p","be動詞のうしろに not を置くだけ。[link:gimonhitei]疑問文・否定文[/link]でさらに詳しく学べる。"),
        ("highlight","主語 + be動詞 + not + 〜<br>例: I am not a teacher. / She is not tired."),
        ("h2","疑問文の作り方"),
        ("p","be動詞を文頭に持ってくる。"),
        ("highlight","Be動詞 + 主語 + 〜？<br>例: Are you a student? / Is he your brother?"),
        ("h2","短縮形（よく使う）"),
        ("table",[["元の形","短縮形"],["I am","I'm"],["you are","you're"],["he is","he's"],["she is","she's"],["it is","it's"],["we are","we're"],["they are","they're"],["is not","isn't"],["are not","aren't"]]),
        ("note","短縮形は会話やライティングで非常によく使うので、必ず覚えよう！"),
        ("p", "be動詞の過去形は[link:bekako]be動詞の過去形[/link]を参照。現在進行形にも使うので[link:shinko]現在進行形[/link]もチェック。"),
    ]),
    ("ippan", "一般動詞", "g1", [
        ("h2","一般動詞とは？"),
        ("p","be動詞以外の動詞を「一般動詞」と呼ぶ。run（走る）, eat（食べる）, play（遊ぶ）, study（勉強する）など、動作や状態を表す。[link:be]be動詞[/link]との違いをしっかり理解しよう。"),
        ("h2","肯定文の作り方"),
        ("p","主語 + 動詞 + 〜 の順番。主語が3人称単数のときは動詞に s または es がつく（[link:santan]三単現[/link]）。"),
        ("highlight","【公式】 主語 + 動詞 + 〜<br>I play tennis.（私はテニスをします）<br>He plays tennis.（彼はテニスをします）"),
        ("h2","否定文の作り方"),
        ("p","do not (don't) / does not (doesn't) を使う。動詞は原形に戻す。[link:gimonhitei]疑問文・否定文[/link]でさらに詳しく。"),
        ("highlight","【公式】 主語 + do/does + not + 動詞の原形<br>I don't like coffee.（コーヒーが好きではありません）<br>She doesn't play soccer.（彼女はサッカーをしません）"),
        ("h2","疑問文の作り方"),
        ("p","Do / Does を文頭に置く。動詞は原形に戻す。"),
        ("highlight","【公式】 Do/Does + 主語 + 動詞の原形 + 〜？<br>Do you like cats?（猫が好きですか？）<br>Does he study English?（彼は英語を勉強しますか？）"),
        ("note","be動詞と違って、一般動詞は「do」を使って否定文・疑問文を作る。このちがいは超重要！"),
        ("p", "一般動詞の過去形は[link:kako]一般動詞の過去形[/link]を参照。三人称単数のsは[link:santan]三単現[/link]で詳しく解説。"),
    ]),
] + GRAMMAR_DATA

# === 練習問題 ===
PRACTICE_QUESTIONS = {
    "gimonhitei": [
        {"text":"___ you a student?", "options":["Am","Are","Is"], "answer":"Are","explanation":"you の疑問文は Are you"},
        {"text":"She ___ not my sister.", "options":["am","are","is"], "answer":"is","explanation":"be動詞の否定文：She is not"},
        {"text":"I ___ like coffee.", "options":["don't","doesn't","am not"], "answer":"don't","explanation":"一般動詞の否定は don't"},
        {"text":"___ you like sushi?", "options":["Do","Does","Are"], "answer":"Do","explanation":"you の疑問文は Do you"},
        {"text":"___ he play tennis?", "options":["Do","Does","Is"], "answer":"Does","explanation":"3単現の疑問文は Does he"},
        {"text":"He ___ like fish.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"3単現の否定文は doesn't"},
        {"text":"___ they your friends?", "options":["Am","Are","Is"], "answer":"Are","explanation":"they の疑問文は Are they"},
        {"text":"This ___ my book.", "options":["am not","are not","is not"], "answer":"is not","explanation":"This には is not"},
        {"text":"We ___ play soccer on Sunday.", "options":["don't","doesn't","aren't"], "answer":"don't","explanation":"We には don't"},
        {"text":"___ you from Japan?", "options":["Do","Are","Is"], "answer":"Are","explanation":"出身を尋ねるbe動詞の疑問文は Are you from"}
    ],
    "gimonsi": [
        {"text":"___ is this? It's a pen.", "options":["What","Who","Where"], "answer":"What","explanation":"ものを尋ねる疑問詞は What"},
        {"text":"___ is he? He's Taro.", "options":["What","Who","Where"], "answer":"Who","explanation":"人を尋ねる疑問詞は Who"},
        {"text":"___ are you going? To the library.", "options":["What","Who","Where"], "answer":"Where","explanation":"場所を尋ねる疑問詞は Where"},
        {"text":"___ do you get up? At seven.", "options":["What","When","Why"], "answer":"When","explanation":"時を尋ねる疑問詞は When"},
        {"text":"___ are you late? Because I missed the bus.", "options":["What","When","Why"], "answer":"Why","explanation":"理由を尋ねる疑問詞は Why"},
        {"text":"___ old are you? I'm 12.", "options":["What","How","Who"], "answer":"How","explanation":"How old で年齢を尋ねる"},
        {"text":"___ is your birthday? It's May 5th.", "options":["What","When","Where"], "answer":"When","explanation":"時を尋ねる疑問詞は When"},
        {"text":"___ do you go to school? By bus.", "options":["What","How","When"], "answer":"How","explanation":"方法を尋ねる疑問詞は How"},
        {"text":"___ is your favorite subject? English.", "options":["Who","What","Where"], "answer":"What","explanation":"好きな教科は What"},
        {"text":"___ are you from? I'm from Japan.", "options":["What","Where","Who"], "answer":"Where","explanation":"出身地を尋ねる疑問詞は Where"}
    ],
    "meirei": [
        {"text":"___ down.", "options":["Sit","Sitting","Sits"], "answer":"Sit","explanation":"命令文は動詞の原形で始める"},
        {"text":"___ your book.", "options":["Open","Opening","Opens"], "answer":"Open","explanation":"命令文は動詞の原形"},
        {"text":"___ in class.", "options":["Don't eat","Doesn't eat","Not eat"], "answer":"Don't eat","explanation":"禁止文は Don't + 動詞の原形"},
        {"text":"___ up.", "options":["Stand","Standing","Stands"], "answer":"Stand","explanation":"命令文は動詞の原形"},
        {"text":"___ run in the hallway.", "options":["Don't","Doesn't","Not"], "answer":"Don't","explanation":"禁止文は Don't + 動詞の原形"},
        {"text":"___ your name here.", "options":["Write","Writes","Writing"], "answer":"Write","explanation":"命令文は動詞の原形"},
        {"text":"___ the window.", "options":["Open","Opening","Opens"], "answer":"Open","explanation":"命令文は動詞の原形"},
        {"text":"___ be late.", "options":["Don't","Doesn't","Not"], "answer":"Don't","explanation":"be動詞の禁止文も Don't"},
        {"text":"___ my hand.", "options":["Hold","Holding","Holds"], "answer":"Hold","explanation":"命令文は動詞の原形"},
        {"text":"___ quiet.", "options":["Be","Being","Is"], "answer":"Be","explanation":"命令文 Be + 形容詞"}
    ],
    "kako": [
        {"text":"I ___ tennis yesterday.", "options":["play","played","playing"], "answer":"played","explanation":"play → played（規則動詞ed形）"},
        {"text":"She ___ to the park last Sunday.", "options":["go","went","goes"], "answer":"went","explanation":"go → went（不規則変化）"},
        {"text":"We ___ a movie last night.", "options":["see","saw","seeing"], "answer":"saw","explanation":"see → saw（不規則変化）"},
        {"text":"He ___ breakfast at seven.", "options":["eat","ate","eats"], "answer":"ate","explanation":"eat → ate（不規則変化）"},
        {"text":"They ___ their homework yesterday.", "options":["do","did","does"], "answer":"did","explanation":"do → did（不規則変化）"},
        {"text":"I ___ TV last night.", "options":["didn't watch","didn't watched","don't watch"], "answer":"didn't watch","explanation":"否定文は didn't + 動詞の原形"},
        {"text":"___ you go to school yesterday?", "options":["Do","Did","Does"], "answer":"Did","explanation":"過去の疑問文は Did + 主語 + 動詞の原形"},
        {"text":"She ___ a good time at the party.", "options":["have","had","has"], "answer":"had","explanation":"have → had（不規則変化）"},
        {"text":"He ___ his room yesterday.", "options":["clean","cleaned","cleans"], "answer":"cleaned","explanation":"clean → cleaned（規則動詞ed形）"},
        {"text":"Where ___ you go yesterday?", "options":["do","did","are"], "answer":"did","explanation":"過去の疑問詞疑問文は did + 主語 + 動詞の原形"}
    ],
    "fukusu": [
        {"text":"I have two ___.", "options":["cat","cats","caties"], "answer":"cats","explanation":"複数形はふつう s"},
        {"text":"There are three ___.", "options":["box","boxes","boxs"], "answer":"boxes","explanation":"xで終わる → es"},
        {"text":"I have two ___.", "options":["baby","babies","babys"], "answer":"babies","explanation":"子音+y → yをiに変えてes"},
        {"text":"I saw two ___.", "options":["knife","knifes","knives"], "answer":"knives","explanation":"f/fe → ves"},
        {"text":"There are many ___.", "options":["child","childs","children"], "answer":"children","explanation":"child の複数形は children（不規則）"},
        {"text":"Two ___ are playing.", "options":["woman","womans","women"], "answer":"women","explanation":"woman の複数形は women（不規則）"},
        {"text":"I have ten ___.", "options":["tooth","tooths","teeth"], "answer":"teeth","explanation":"tooth の複数形は teeth（不規則）"},
        {"text":"There are five ___.", "options":["sheep","sheeps","sheepes"], "answer":"sheep","explanation":"sheep は単複同形"},
        {"text":"I have three ___.", "options":["pen","pens","penns"], "answer":"pens","explanation":"ふつうは s をつける"},
        {"text":"We have two ___.", "options":["foot","foots","feet"], "answer":"feet","explanation":"foot の複数形は feet（不規則）"}
    ],
    "daimeisi": [
        {"text":"___ am a student.", "options":["I","My","Me"], "answer":"I","explanation":"主語の位置は主格 I"},
        {"text":"This is ___ book.", "options":["I","my","me"], "answer":"my","explanation":"「私の」所有格は my"},
        {"text":"Please help ___.", "options":["I","my","me"], "answer":"me","explanation":"目的語の位置は目的格 me"},
        {"text":"This pen is ___.", "options":["I","my","mine"], "answer":"mine","explanation":"「私のもの」所有代名詞は mine"},
        {"text":"___ is a teacher.", "options":["She","Her","Hers"], "answer":"She","explanation":"主語の位置は主格 She"},
        {"text":"I like ___ dog.", "options":["she","her","hers"], "answer":"her","explanation":"「彼女の」所有格は her"},
        {"text":"I gave it to ___.", "options":["he","his","him"], "answer":"him","explanation":"目的語の位置は目的格 him"},
        {"text":"That bike is ___.", "options":["he","his","him"], "answer":"his","explanation":"所有代名詞 his"},
        {"text":"___ are my friends.", "options":["They","Their","Them"], "answer":"They","explanation":"主語の位置は主格 They"},
        {"text":"This is ___ house.", "options":["they","their","theirs"], "answer":"their","explanation":"「彼らの」所有格は their"}
    ],
    "shinko": [
        {"text":"I ___ a book now.", "options":["read","am reading","reading"], "answer":"am reading","explanation":"be動詞（am）+ reading"},
        {"text":"She ___ TV right now.", "options":["is watching","watching","watches"], "answer":"is watching","explanation":"She + is + watching"},
        {"text":"They ___ soccer at the park.", "options":["are playing","playing","play"], "answer":"are playing","explanation":"They + are + playing"},
        {"text":"We ___ dinner now.", "options":["eat","are eating","eating"], "answer":"are eating","explanation":"We + are + eating"},
        {"text":"He is ___ a letter.", "options":["write","writes","writing"], "answer":"writing","explanation":"write → writing（eをとってing）"},
        {"text":"I'm ___ a bath now.", "options":["take","takes","taking"], "answer":"taking","explanation":"take → taking（eをとってing）"},
        {"text":"The baby ___ now.", "options":["is sleep","is sleeping","sleeping"], "answer":"is sleeping","explanation":"is + sleeping"},
        {"text":"He ___ cooking now.", "options":["isn't","don't","not"], "answer":"isn't","explanation":"否定文は is not (isn't)"},
        {"text":"___ you studying now?", "options":["Do","Are","Is"], "answer":"Are","explanation":"you の疑問文は Are you + doing"},
        {"text":"Look! The cat ___ a tree.", "options":["is climbing","climbs","climbing"], "answer":"is climbing","explanation":"The cat + is + climbing"}
    ],
    "can": [
        {"text":"I ___ swim.", "options":["can","can to","am can"], "answer":"can","explanation":"can + 動詞の原形"},
        {"text":"She ___ play the piano.", "options":["can","cans","can to"], "answer":"can","explanation":"3単現でも can の形は変わらない"},
        {"text":"He ___ speak Japanese.", "options":["can't","don't can","isn't can"], "answer":"can't","explanation":"否定文は can + not（can't）"},
        {"text":"___ you help me?", "options":["Do","Can","Are"], "answer":"Can","explanation":"疑問文は Can を文頭に置く"},
        {"text":"Yes, I ___.", "options":["am","do","can"], "answer":"can","explanation":"Can you? → Yes, I can."},
        {"text":"No, I ___.", "options":["can't","don't","am not"], "answer":"can't","explanation":"否定の答えは No, I can't."},
        {"text":"We ___ run fast.", "options":["can","cans","can to"], "answer":"can","explanation":"We + can + run（原形）"},
        {"text":"My sister ___ cook well.", "options":["can","cans","is can"], "answer":"can","explanation":"3単数でも can は不変"},
        {"text":"I ___ play the guitar.", "options":["not can","don't can","can't"], "answer":"can't","explanation":"否定文は can't"},
        {"text":"___ your father drive a car?", "options":["Do","Is","Can"], "answer":"Can","explanation":"疑問文は Can + 主語 + 動詞の原形"}
    ],
    "be": [
        {"text":"I ___ a student.", "options":["am","are","is"], "answer":"am","explanation":"I には am"},
        {"text":"She ___ my friend.", "options":["am","are","is"], "answer":"is","explanation":"She には is"},
        {"text":"We ___ in the classroom.", "options":["am","are","is"], "answer":"are","explanation":"We には are"},
        {"text":"___ you a teacher?", "options":["Am","Are","Is"], "answer":"Are","explanation":"you の疑問文は Are"},
        {"text":"He ___ not tall.", "options":["am","are","is"], "answer":"is","explanation":"He には is"},
        {"text":"They ___ happy.", "options":["am","are","is"], "answer":"are","explanation":"They には are"},
        {"text":"___ it a pen?", "options":["Am","Are","Is"], "answer":"Is","explanation":"it の疑問文は Is"},
        {"text":"I ___ not a doctor.", "options":["am","are","is"], "answer":"am","explanation":"I の否定文は am not"},
        {"text":"My parents ___ at home.", "options":["am","are","is"], "answer":"are","explanation":"parents は複数なので are"},
        {"text":"The cat ___ under the table.", "options":["am","are","is"], "answer":"is","explanation":"The cat は単数なので is"}
    ],
    "ippan": [
        {"text":"I ___ tennis.", "options":["play","plays","playing"], "answer":"play","explanation":"I には原形 play"},
        {"text":"She ___ English.", "options":["study","studies","studying"], "answer":"studies","explanation":"She (3人称単数) なので studies"},
        {"text":"___ you like cats?", "options":["Do","Does","Are"], "answer":"Do","explanation":"you の疑問文は Do"},
        {"text":"He ___ play soccer.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"He の否定文は doesn't"},
        {"text":"They ___ lunch at school.", "options":["eat","eats","eating"], "answer":"eat","explanation":"They には原形 eat"},
        {"text":"___ he study math?", "options":["Do","Does","Is"], "answer":"Does","explanation":"he の疑問文は Does"},
        {"text":"I ___ get up at six.", "options":["don't","doesn't","isn't"], "answer":"don't","explanation":"I の否定文は don't"},
        {"text":"We ___ to school by bus.", "options":["go","goes","going"], "answer":"go","explanation":"We には原形 go"},
        {"text":"My mother ___ dinner.", "options":["make","makes","making"], "answer":"makes","explanation":"My mother (3人称単数) なので makes"},
        {"text":"___ they live in Tokyo?", "options":["Do","Does","Are"], "answer":"Do","explanation":"they の疑問文は Do"}
    ],
    "santan": [
        {"text":"He ___ tennis every Sunday.", "options":["play","plays","playing"], "answer":"plays","explanation":"He (3人称単数) なので plays"},
        {"text":"She ___ to school by bus.", "options":["go","goes","going"], "answer":"goes","explanation":"She (3人称単数) + goes"},
        {"text":"The cat ___ milk.", "options":["drink","drinks","drinking"], "answer":"drinks","explanation":"The cat (3人称単数) なので drinks"},
        {"text":"___ she like music?", "options":["Do","Does","Is"], "answer":"Does","explanation":"she の疑問文は Does"},
        {"text":"He ___ play the piano.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"He の否定文は doesn't"},
        {"text":"My father ___ newspapers every morning.", "options":["read","reads","reading"], "answer":"reads","explanation":"My father (3人称単数) なので reads"},
        {"text":"___ he get up early?", "options":["Do","Does","Is"], "answer":"Does","explanation":"he の疑問文は Does"},
        {"text":"She ___ watch TV.", "options":["don't","doesn't","isn't"], "answer":"doesn't","explanation":"She の否定文は doesn't"},
        {"text":"It ___ a lot in June.", "options":["rain","rains","raining"], "answer":"rains","explanation":"It (3人称単数) なので rains"},
        {"text":"He ___ his homework every day.", "options":["do","does","doing"], "answer":"does","explanation":"He (3人称単数) なので does"}
    ],
    "futeisi": [
        {"text":"I want ___ to the park.", "options":["go","to go","going"], "answer":"to go","explanation":"want + to + 動詞の原形"},
        {"text":"___ English is fun.", "options":["Study","To study","Studies"], "answer":"To study","explanation":"主語になる不定詞（名詞的用法）"},
        {"text":"I went to the library ___ books.", "options":["read","to read","reading"], "answer":"to read","explanation":"目的を表す不定詞（副詞的用法）"},
        {"text":"I have something ___ today.", "options":["eat","to eat","eating"], "answer":"to eat","explanation":"名詞を修飾（形容詞的用法）"},
        {"text":"She wants ___ a doctor.", "options":["be","to be","being"], "answer":"to be","explanation":"want + to + 動詞の原形"},
        {"text":"It's important ___ early.", "options":["sleep","to sleep","sleeping"], "answer":"to sleep","explanation":"It is + 形容詞 + to + 動詞の原形"},
        {"text":"I went to Kyoto ___ my grandparents.", "options":["visit","to visit","visiting"], "answer":"to visit","explanation":"目的を表す 不定詞"},
        {"text":"He wants ___ a singer.", "options":["become","to become","becoming"], "answer":"to become","explanation":"want + to + 動詞の原形"},
        {"text":"I need ___ water.", "options":["buy","to buy","buying"], "answer":"to buy","explanation":"need + to + 動詞の原形"},
        {"text":"The best way ___ English is to practice.", "options":["learn","to learn","learning"], "answer":"to learn","explanation":"名詞を修飾する不定詞"}
    ],
    "genkan": [
        {"text":"I ___ to Kyoto.", "options":["have been","have gone","went"], "answer":"have been","explanation":"経験「行ったことがある」は have been"},
        {"text":"She ___ in Tokyo for five years.", "options":["live","lives","has lived"], "answer":"has lived","explanation":"継続「ずっと住んでいる」は has lived"},
        {"text":"I have ___ finished my homework.", "options":["just","ever","never"], "answer":"just","explanation":"完了「ちょうど終えた」は just"},
        {"text":"Have you ___ seen a lion?", "options":["just","ever","already"], "answer":"ever","explanation":"経験の疑問文は ever"},
        {"text":"He has ___ been to America.", "options":["ever","never","just"], "answer":"never","explanation":"否定の経験「一度もない」は never"},
        {"text":"I have ___ finished.", "options":["already","ever","never"], "answer":"already","explanation":"完了「もう終わった」は already"},
        {"text":"Have you finished ___?", "options":["just","already","yet"], "answer":"yet","explanation":"疑問文の「もう」は yet"},
        {"text":"She has lived here ___ 2020.", "options":["for","since","from"], "answer":"since","explanation":"起点には since"},
        {"text":"He has studied English ___ two hours.", "options":["for","since","from"], "answer":"for","explanation":"期間には for"},
        {"text":"I have ___ seen such a beautiful view.", "options":["ever","never","already"], "answer":"never","explanation":"「一度も見たことがない」は never"}
    ],
    "hikaku": [
        {"text":"Taro is ___ than Jiro.", "options":["tall","taller","tallest"], "answer":"taller","explanation":"比較級は -er"},
        {"text":"Mt.Fuji is ___ mountain in Japan.", "options":["high","higher","the highest"], "answer":"the highest","explanation":"最上級は the + -est"},
        {"text":"She is as ___ as me.", "options":["tall","taller","tallest"], "answer":"tall","explanation":"原級 as + 原級 + as"},
        {"text":"This book is ___ than that one.", "options":["interesting","more interesting","most interesting"], "answer":"more interesting","explanation":"長い語の比較級は more"},
        {"text":"He is ___ student in the class.", "options":["smart","smarter","the smartest"], "answer":"the smartest","explanation":"最上級は the + -est"},
        {"text":"This problem is ___ difficult than that.", "options":["more","most","as"], "answer":"more","explanation":"比較級 + than"},
        {"text":"She runs ___ in her school.", "options":["fast","faster","the fastest"], "answer":"the fastest","explanation":"最上級"},
        {"text":"My bag is ___ than yours.", "options":["heavy","heavier","heaviest"], "answer":"heavier","explanation":"子音+y の比較級は y→i で -er"},
        {"text":"This is ___ movie I've ever seen.", "options":["good","better","the best"], "answer":"the best","explanation":"good の最上級は best"},
        {"text":"He is not as ___ as his brother.", "options":["tall","taller","tallest"], "answer":"tall","explanation":"否定の原級 as + 原級 + as"}
    ],
    "kankeisi": [
        {"text":"The boy ___ is running is Taro.", "options":["who","which","whose"], "answer":"who","explanation":"人の主格は who"},
        {"text":"The book ___ I bought is interesting.", "options":["who","which","whose"], "answer":"which","explanation":"物の目的格は which"},
        {"text":"The girl ___ hair is long is Mary.", "options":["who","which","whose"], "answer":"whose","explanation":"「〜の」所有は whose"},
        {"text":"I know a man ___ can speak five languages.", "options":["who","which","whose"], "answer":"who","explanation":"人の主格は who"},
        {"text":"This is the house ___ my grandfather built.", "options":["who","which","whose"], "answer":"which","explanation":"物の目的格は which"},
        {"text":"The woman ___ lives next door is a teacher.", "options":["who","which","whose"], "answer":"who","explanation":"人の主格は who"},
        {"text":"I have a friend ___ father is a doctor.", "options":["who","which","whose"], "answer":"whose","explanation":"所有は whose"},
        {"text":"This is the car ___ I want to buy.", "options":["who","which","whose"], "answer":"which","explanation":"物の目的格は which"},
        {"text":"The students ___ study hard will pass.", "options":["who","which","whose"], "answer":"who","explanation":"人の主格は who"},
        {"text":"I like music ___ makes me happy.", "options":["who","which","whose"], "answer":"which","explanation":"物の主格は which"}
    ],
    "kansi": [
        {"text":"I saw ___ cat.", "options":["a","an","the"], "answer":"a","explanation":"初めて話題に出すものには a"},
        {"text":"She is ___ teacher.", "options":["a","an","the"], "answer":"a","explanation":"職業の前には a"},
        {"text":"He ate ___ apple.", "options":["a","an","the"], "answer":"an","explanation":"apple は母音で始まるので an"},
        {"text":"Please open ___ window.", "options":["a","an","the"], "answer":"the","explanation":"目の前のものには the"},
        {"text":"I saw a bird. ___ bird was singing.", "options":["A","An","The"], "answer":"The","explanation":"2回目以降は the"},
        {"text":"___ sun rises in the east.", "options":["A","An","The"], "answer":"The","explanation":"唯一無二のものは the"},
        {"text":"I have ___ umbrella.", "options":["a","an","the"], "answer":"an","explanation":"umbrella は母音で始まるので an"},
        {"text":"She is ___ best student.", "options":["a","an","the"], "answer":"the","explanation":"最上級の前は the"},
        {"text":"I go to school by ___ bus.", "options":["a","an","(不要)"], "answer":"(不要)","explanation":"交通手段には冠詞不要"},
        {"text":"He plays ___ piano well.", "options":["a","an","the"], "answer":"the","explanation":"楽器の前には the"},
    ],
    "zensi": [
        {"text":"The cat is ___ the box.", "options":["in","on","at"], "answer":"in","explanation":"「中に」は in"},
        {"text":"The book is ___ the desk.", "options":["in","on","at"], "answer":"on","explanation":"「上に」は on"},
        {"text":"I get up ___ 7 o'clock.", "options":["in","on","at"], "answer":"at","explanation":"時刻の前は at"},
        {"text":"My birthday is ___ May 5th.", "options":["in","on","at"], "answer":"on","explanation":"日付の前は on"},
        {"text":"I was born ___ 2010.", "options":["in","on","at"], "answer":"in","explanation":"年の前は in"},
        {"text":"I go ___ school every day.", "options":["to","for","at"], "answer":"to","explanation":"「〜へ」方向は to"},
        {"text":"She came ___ Japan.", "options":["to","from","at"], "answer":"from","explanation":"「〜から」は from"},
        {"text":"I studied ___ two hours.", "options":["for","since","in"], "answer":"for","explanation":"期間は for"},
        {"text":"I have lived here ___ 2020.", "options":["for","since","in"], "answer":"since","explanation":"起点は since"},
        {"text":"The cat is ___ the table.", "options":["under","on","in"], "answer":"under","explanation":"「下に」は under"},
    ],
    "suryo": [
        {"text":"I have ___ books.", "options":["many","much","a little"], "answer":"many","explanation":"可算名詞には many"},
        {"text":"I don't have ___ time.", "options":["many","much","a few"], "answer":"much","explanation":"不可算名詞の否定文は much"},
        {"text":"There are ___ apples.", "options":["some","any","much"], "answer":"some","explanation":"肯定文では some"},
        {"text":"Do you have ___ questions?", "options":["some","any","much"], "answer":"any","explanation":"疑問文では any"},
        {"text":"I have ___ money.", "options":["a few","a little","many"], "answer":"a little","explanation":"不可算名詞には a little"},
        {"text":"She has ___ friends.", "options":["a few","a little","much"], "answer":"a few","explanation":"可算名詞には a few"},
        {"text":"I need ___ water.", "options":["some","any","many"], "answer":"some","explanation":"肯定文では some"},
        {"text":"There isn't ___ milk.", "options":["some","any","a few"], "answer":"any","explanation":"否定文では any"},
        {"text":"He has ___ money.", "options":["a lot of","many","a few"], "answer":"a lot of","explanation":"a lot of は可算・不可算どちらでもOK"},
        {"text":"How ___ apples do you want?", "options":["many","much","a lot of"], "answer":"many","explanation":"可算名詞の疑問文は how many"},
    ],
}

DESC_MAP = {
    "be": "中学英語のbe動詞（am, are, is）をわかりやすく解説。肯定文・否定文・疑問文の作り方、短縮形、主語による使い分けをマスター。練習問題と確認テストで完全理解。",
    "ippan": "中学英語の一般動詞（run, eat, playなど）の使い方を解説。肯定文・否定文・疑問文の作り方、do/doesの使い分けを基礎から徹底学習。",
    "gimonhitei": "中学英語の疑問文・否定文をbe動詞と一般動詞に分けて比較解説。do/doesとbe動詞の違いを理解して確実に使い分けられるように。",
    "gimonsi": "中学英語の疑問詞（what, who, where, when, why, how）を完全解説。各疑問詞の意味・使い方・例文を一覧で学べる。",
    "meirei": "中学英語の命令文・禁止文をマスター。動詞の原形で始める命令文、Don'tを使った禁止文の作り方を例文付きで解説。",
    "santan": "中学英語の三人称単数現在（三単現のs）を完全解説。s/esの付け方、doesを使った否定文・疑問文まで網羅。",
    "shinko": "中学英語の現在進行形をわかりやすく解説。be動詞+動詞のing形の作り方、否定文・疑問文、ing形のスペルルールまで。",
    "can": "中学英語の助動詞canを完全解説。「〜できる」の肯定文・否定文・疑問文の作り方。3単現でも形が変わらないルール。",
    "kako": "中学英語の一般動詞の過去形を解説。規則動詞のed形の付け方、不規則動詞の一覧、didを使った否定文・疑問文まで。",
    "fukusu": "中学英語の名詞の複数形を完全解説。s/esの付け方、子音+y→ies、f/fe→ves、不規則変化まで網羅。",
    "daimeisi": "中学英語の人称代名詞の変化表を一覧で解説。主格・所有格・目的格・所有代名詞の使い分けを表で覚えよう。",
    "bekako": "中学英語のbe動詞の過去形（was/were）を解説。肯定文・否定文・疑問文の作り方、主語による使い分け。",
    "kakosin": "中学英語の過去進行形（was/were + doing）をわかりやすく解説。「〜していた」過去の進行中の動作をマスター。",
    "mirai": "中学英語の未来形（will / be going to）の違いを解説。その場の意思と予定の使い分け、否定文・疑問文まで。",
    "doumei": "中学英語の動名詞（動詞のing形が名詞の役割）を解説。不定詞との意味の違い、ing形の作り方。",
    "futeisi1": "中学英語の不定詞（to + 動詞の原形）の3つの用法を解説。名詞的用法・副詞的用法・形容詞的用法を例文付きで。",
    "jyodosi": "中学英語の助動詞（must, have to, may, should, can）をまとめて解説。各助動詞の意味・使い方・例文一覧。",
    "hikaku1": "中学英語の比較表現（比較級・最上級・原級）をわかりやすく解説。er/estの付け方、more/mostの使い分け。",
    "there": "中学英語のthere is/are構文を解説。「〜がある・いる」の肯定文・否定文・疑問文。単数と複数の使い分け。",
    "setuzoku": "中学英語の接続詞（and, but, because, when, if, that）を一覧で解説。文と文をつなぐ基本ルール。",
    "ukemi": "中学英語の受け身（受動態）をわかりやすく解説。be動詞+過去分詞の形、能動態からの書き換えルール。",
    "genkan1": "中学英語の現在完了（継続用法）を解説。have/has+過去分詞「ずっと〜している」の表現。for/sinceの使い分け。",
    "genkan2": "中学英語の現在完了（経験用法）を解説。「〜したことがある」の表現。ever/neverの使い方。",
    "genkan3": "中学英語の現在完了（完了・結果用法）を解説。「ちょうど〜した」「もう〜した」の表現。already, just, yetの使い分け。",
    "genkanSinkokei": "中学英語の現在完了進行形を解説。have/has been + doing「ずっと〜し続けている」の強調表現。",
    "futeisi2": "中学英語の不定詞（応用）を解説。It ... for ... to構文、疑問詞+不定詞、ask/tell+人+toの表現。",
    "bunsi": "中学英語の分詞（現在分詞・過去分詞）の形容詞的用法を解説。後置修飾のルールと例文。",
    "kansetu": "中学英語の間接疑問をわかりやすく解説。Do you know where he lives?の語順のルールに注意。",
    "kankeisi1": "中学英語の関係代名詞（who, which, that）を解説。主格・目的格の使い分け、先行詞との関係。",
    "kateiho": "中学英語の仮定法過去を解説。「もし〜なら（実際は違う）」の表現。If + 過去形, would/couldの使い方。",
    "genkeiFuteisi": "中学英語の原形不定詞（toなし不定詞）を解説。使役動詞（make, let, have）と知覚動詞（see, hear）の後ろの動詞の原形。",
    "kansi": "中学英語の冠詞（a, an, the）をわかりやすく解説。不定冠詞と定冠詞の使い分け、冠詞をつけない場合のルールまで完全網羅。",
    "zensi": "中学英語の前置詞（in, on, at, for, since, to, fromなど）を一覧で解説。位置・時間・方向の前置詞を例文付きでマスター。",
    "suryo": "中学英語の数量表現（many, much, some, any, a few, a little, a lot of）を解説。可算名詞・不可算名詞の区別も学べる。",
}

def gen_grammar():
    for fname, name, gclass, blocks in GRAMMAR_DATA:
        grade_map = {"g1":"中学1年","g2":"中学2年","g3":"中学3年"}
        grade = grade_map[gclass]
        desc = DESC_MAP.get(fname, f"中学英語 {name} をわかりやすく解説")
        content = render_content(blocks)
        html = HEADER.format(title=f"{name}の解説", desc=desc)
        html += f'<div class="breadcrumb"><a href="../index.html">ホーム</a> > <a href="../index.html#grammar">文法解説</a> > {name}</div>\n'
        html += f'<article class="grammar-detail">\n'
        html += f'  <span class="grade-badge badge {gclass}">{grade}</span>\n'
        html += f'  <h1>{name}</h1>\n'
        html += f'  {content}\n'
        # 追加コンテンツ（ポイントまとめ・実践例文など）
        extra = EXTRA_CONTENT.get(fname, [])
        if extra:
            for block in extra:
                t = block[0]
                if t == "h2":
                    html += f"<h2>{block[1]}</h2>\n"
                elif t == "h3":
                    html += f"<h3>{block[1]}</h3>\n"
                elif t == "p":
                    html += f"<p>{render_text(block[1])}</p>\n"
                elif t == "ul":
                    html += "<ul>\n" + "".join(f"<li>{render_text(li)}</li>\n" for li in block[1]) + "</ul>\n"
                elif t == "table":
                    rows = block[1]
                    html += "<table>\n"
                    for i, row in enumerate(rows):
                        tag = "th" if i == 0 else "td"
                        html += "<tr>" + "".join(f"<{tag}>{render_text(c)}</{tag}>" for c in row) + "</tr>\n"
                    html += "</table>\n"
        html += roadmap_section(fname, gclass)
        html += mistake_section(fname)
        html += related_section(fname)
        html += '  <div class="practice-link-box">\n'
        html += f'    <p>理解を深めたら <a href="../practice/{fname}.html">練習問題を解く</a> か <a href="../test/{fname}_test.html">確認テストに挑戦</a> しよう。</p>\n'
        html += '  </div>\n'
        html += '</article>\n'
        html += '<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>\n'
        html += FOOTER
        path = os.path.join(BASE, "grammar", f"{fname}.html")
        with open(path, "w") as f:
            f.write(html)
        print(f"  grammar/{fname}.html")

def gen_practice():
    for key, questions in PRACTICE_QUESTIONS.items():
        name = NAME_MAP[key]
        q_json = json.dumps(questions, ensure_ascii=False)
        desc = f"中学英語 {name} の練習問題。全{len(questions)}問の選択式問題で理解度をチェック。解答・解説付き。"
        html = HEADER.format(title=f"{name} 練習問題", desc=desc)
        html += f'<div class="breadcrumb"><a href="../index.html">ホーム</a> > <a href="../practice/index.html">練習問題</a> > {name}</div>\n'
        html += f'<div class="page-header"><h1>{name} 練習問題</h1><p>全{len(questions)}問。選択肢から正しいものを選んでください。</p></div>\n'
        html += f'''
<div class="container">
  <div class="practice-box" id="practiceApp">
    <div class="question-card" v-for="(q, i) in questions" :key="i">
      <div class="q-number">{{{{ i + 1 }}}}</div>
      <div class="q-text">{{{{ q.text }}}}</div>
      <div class="q-options">
        <div v-for="opt in q.options" :key="opt"
          class="q-option"
          :class="{{ '{' }} correct: answered[i] && opt === q.answer, wrong: answered[i] && selected[i] === opt && opt !== q.answer {{ '}' }}"
          @click="selectAnswer(i, opt)">
          {{{{ opt }}}}
        </div>
      </div>
      <div class="feedback" :class="{{ '{' }} show: answered[i], correct: answered[i] && selected[i] === q.answer, wrong: answered[i] && selected[i] !== q.answer {{ '}' }}">
        <template v-if="answered[i] && selected[i] === q.answer">✅ 正解！ {{{{ q.explanation }}}}</template>
        <template v-else-if="answered[i]">❌ 正解は「{{{{ q.answer }}}}」 {{{{ q.explanation }}}}</template>
      </div>
    </div>
    <div style="text-align:center;margin:24px 0;">
      <button class="hero-btn primary" @click="resetAll" style="border:none;cursor:pointer;">🔄 やり直す</button>
    </div>
    <div class="test-result" v-if="allAnswered">
      <div class="score">{{{{ score }}}} / {len(questions)}</div>
      <div class="label">正答率</div>
      <div class="rank">{{{{ score === questions.length ? '🎉 満点！' : score >= 7 ? '👍 よくできました！' : '💪 もう一度！' }}}}</div>
    </div>
  </div>
</div>
'''
        html += FOOTER
        html += '''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const { createApp } = Vue;
createApp({
  data() {
    return {
      selected: {},
      answered: {},
      questions: ''' + q_json + '''
    };
  },
  computed: {
    allAnswered() { return this.questions.every((_, i) => this.answered[i]); },
    score() { return this.questions.filter((q, i) => this.selected[i] === q.answer).length; }
  },
  methods: {
    selectAnswer(i, opt) { if (this.answered[i]) return; this.selected[i] = opt; this.answered[i] = true; },
    resetAll() { this.selected = {}; this.answered = {}; }
  }
}).mount('#practiceApp');
</script>
</body>
</html>'''
        path = os.path.join(BASE, "practice", f"{key}.html")
        with open(path, "w") as f:
            f.write(html)
        print(f"  practice/{key}.html")

def gen_tests():
    for key, questions in PRACTICE_QUESTIONS.items():
        name = NAME_MAP[key]
        q_json = json.dumps(questions, ensure_ascii=False)
        desc = f"中学英語 {name} の確認テスト。制限時間5分、全{len(questions)}問。時間内に全問解答して実力をチェック。"
        html = HEADER.format(title=f"{name} 確認テスト", desc=desc)
        html += f'<div class="breadcrumb"><a href="../index.html">ホーム</a> > <a href="index.html">確認テスト</a> > {name}</div>\n'
        html += f'<div class="page-header"><h1>{name} 確認テスト</h1><p>制限時間5分。全{len(questions)}問。</p></div>\n'
        html += f'''
<div class="container">
  <div class="test-header">
    <div class="timer" id="timerDisplay">05:00</div>
    <div class="progress" id="progressDisplay">0 / {len(questions)} 問解答</div>
  </div>
  <div class="practice-box" id="testApp">
    <div class="question-card" v-for="(q, i) in questions" :key="i">
      <div class="q-number">{{{{ i + 1 }}}}</div>
      <div class="q-text">{{{{ q.text }}}}</div>
      <div class="q-options">
        <div v-for="opt in q.options" :key="opt"
          class="q-option"
          :class="{{ '{' }} correct: finished && opt === q.answer, wrong: finished && selected[i] === opt && opt !== q.answer {{ '}' }}"
          @click="selectAnswer(i, opt)">
          {{{{ opt }}}}
        </div>
      </div>
    </div>
    <div style="text-align:center;margin:24px 0;">
      <button class="hero-btn primary" @click="submitTest" :disabled="!allAnswered" style="border:none;cursor:pointer;">📊 採点する</button>
    </div>
    <div class="test-result" v-if="finished">
      <div class="score">{{{{ score }}}} / {len(questions)}</div>
      <div class="label">正答率 {{{{ Math.round(score / questions.length * 100) }}}}%</div>
      <div class="rank">{{{{ score === questions.length ? '🎉 満点！' : score >= 7 ? '👍 よくできました！' : '💪 もう一度！' }}}}</div>
      <div style="margin-top:16px;">
        <button class="hero-btn secondary" @click="retry" style="border:none;cursor:pointer;background:var(--gray-600);color:#fff;">🔄 もう一度</button>
      </div>
    </div>
  </div>
</div>
'''
        html += FOOTER
        html += '''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const { createApp } = Vue;
createApp({
  data() {
    return {
      selected: {},
      finished: false,
      timerMinutes: 5, timerSeconds: 0, timerInterval: null, timeUp: false,
      questions: ''' + q_json + '''
    };
  },
  computed: {
    allAnswered() { return this.questions.every((_, i) => this.selected[i]); },
    score() { return this.questions.filter((q, i) => this.selected[i] === q.answer).length; }
  },
  methods: {
    selectAnswer(i, opt) { if (this.finished || this.timeUp) return; this.selected[i] = opt; document.getElementById('progressDisplay').textContent = `${{Object.keys(this.selected).length}} / ${{this.questions.length}} 問解答`; },
    submitTest() { if (!this.allAnswered) return; this.finished = true; if (this.timerInterval) clearInterval(this.timerInterval); },
    retry() { this.selected = {}; this.finished = false; this.timeUp = false; this.timerMinutes = 5; this.timerSeconds = 0; document.getElementById('timerDisplay').textContent = '05:00'; document.getElementById('progressDisplay').textContent = '0 / ''' + str(len(questions)) + ''' 問解答'; this.startTimer(); },
    startTimer() { this.timerInterval = setInterval(() => { if (this.timerSeconds === 0) { if (this.timerMinutes === 0) { clearInterval(this.timerInterval); this.timeUp = true; this.finished = true; return; } this.timerMinutes--; this.timerSeconds = 59; } else { this.timerSeconds--; } document.getElementById('timerDisplay').textContent = `${{String(this.timerMinutes).padStart(2, '0')}}:${{String(this.timerSeconds).padStart(2, '0')}}`; }, 1000); }
  },
  mounted() { this.startTimer(); }
}).mount('#testApp');
</script>
</body>
</html>'''
        path = os.path.join(BASE, "test", f"{key}_test.html")
        with open(path, "w") as f:
            f.write(html)
        print(f"  test/{key}_test.html")

if __name__ == "__main__":
    print("=== 文法ページ生成 ===")
    gen_grammar()
    print("=== 練習問題ページ生成 ===")
    gen_practice()
    print("=== 確認テストページ生成 ===")
    gen_tests()
    print("=== 全ページ生成完了 ===")