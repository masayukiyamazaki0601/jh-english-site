#!/usr/bin/env python3
"""残り全30文法ページを厚くする（300行超え）"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# 厚い記事を生成するテンプレート部品
THICK_PARTS = {
    "tip_box": '<div class="tip-box"><h3>💡 覚え方のポイント</h3><p>{text}</p></div>',
    "highlight": '<div class="highlight"><p>{text}</p></div>',
    "note": '<div class="note"><strong>Check!</strong> {text}</div>',
    "mistake": '<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>{items}</ul></div>',
    "roadmap": '<div class="roadmap-box"><h2>🗺️ 学習の流れ</h2><p style="color:var(--gray-600);font-size:0.9rem;margin-bottom:12px;">この単元をマスターしたら、次の単元に進みましょう。</p><div class="roadmap-links">{links}</div></div>',
    "practice_link": '<div class="practice-link-box"><p>✅ 理解を深めたら <a href="../practice/{file}">練習問題を解く</a> か <a href="../test/{file}_test.html">確認テストに挑戦</a> しよう。</p></div>',
}

def thicken_page(filename, extra_content):
    """既存のHTMLファイルを読み込み、article内にextra_contentを追加"""
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    
    # articleタグ内の最後（</article>の前）にコンテンツを挿入
    insert_pos = content.rfind("</article>")
    if insert_pos == -1:
        print(f"  SKIP {filename}: no article tag")
        return
    
    # 既に厚い記事（300行超）はスキップ
    line_count = content.count("\n")
    if line_count > 250:
        print(f"  SKIP {filename}: already thick ({line_count} lines)")
        return
    
    before = content[:insert_pos]
    after = content[insert_pos:]
    
    new_content = before + extra_content + "\n" + after
    
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  THICKENED {filename} ({line_count} -> {new_content.count(chr(10))} lines)")

def make_grammar_blocks(name, examples, tip_text, mistake_items, next_links, practice_file):
    """拡張コンテンツを生成"""
    blocks = []
    
    # 実践的な例文セクション
    if examples:
        ex_html = "<h2>📝 実践的な例文</h2>\n<ul>\n"
        for en, jp in examples:
            ex_html += f'  <li><span class="example">{en}</span> <span class="example-jp">（{jp}）</span></li>\n'
        ex_html += "</ul>\n"
        blocks.append(ex_html)
    
    # ヒント
    if tip_text:
        blocks.append(f'<div class="tip-box"><h3>💡 {name}をマスターするコツ</h3><p>{tip_text}</p></div>\n')
    
    # よくある間違い
    if mistake_items:
        items_html = "".join(f"<li>{item}</li>\n" for item in mistake_items)
        blocks.append(f'<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>\n{items_html}</ul></div>\n')
    
    # 学習ロードマップ
    if next_links:
        links_html = "".join(f'<a href="{url}" class="roadmap-next">{label} →</a>\n' for url, label in next_links)
        blocks.append(f'<div class="roadmap-box"><h2>🗺️ 学習の流れ</h2><p style="color:var(--gray-600);font-size:0.9rem;margin-bottom:12px;">{name}をマスターしたら、次の単元に進みましょう。</p><div class="roadmap-links">\n{links_html}</div></div>\n')
    
    # 練習問題へのリンク
    if practice_file:
        blocks.append(f'<div class="practice-link-box"><p>✅ 理解を深めたら <a href="../practice/{practice_file}">練習問題を解く</a> か <a href="../test/{practice_file}_test.html">確認テストに挑戦</a> しよう。</p></div>\n')
    
    # 関連記事
    if next_links:
        related = ""
        for url, label in next_links[:6]:
            name_only = label.replace("→","").strip()
            related += f'      <a href="{url}" class="related-card"><span class="related-title">{name_only}</span><span class="related-arrow">→</span></a>\n'
        blocks.append(f'<div class="related-articles"><h2>📚 関連する文法単元</h2><div class="related-grid">\n{related}</div></div>\n')
    
    return "\n".join(blocks)

def thicken_all():
    """全30ページを厚くする"""
    pages = {
        "bekako.html": {
            "name": "be動詞の過去形",
            "examples": [
                ("I was happy yesterday.", "私は昨日幸せでした"),
                ("They were at school last Monday.", "彼らは先週月曜日に学校にいました"),
                ("She was busy last night.", "彼女は昨晩忙しかった"),
                ("We were in the park last Sunday.", "私たちは先週日曜日に公園にいました"),
                ("He was sick yesterday.", "彼は昨日病気でした"),
            ],
            "tip": "was / were の違いは am/are/is の過去形版です。am/is → was、are → were。否定文は was not (wasn't) / were not (weren't) を使います。",
            "mistakes": [
                "<strong>「I were happy.」</strong> → I には was を使います。I were は仮定法以外では使いません。",
                "<strong>「There was many people.」</strong> → many people は複数なので「There were many people.」が正解です。",
                "<strong>「was」と「were」の混同</strong> → 単数（I, he, she, it）は was / 複数（we, you, they）は were。",
            ],
            "next": [("ippan.html", "一般動詞"), ("kakosin.html", "過去進行形")],
            "practice": "bekako"
        },
        "kakosin.html": {
            "name": "過去進行形",
            "examples": [
                ("I was reading a book at 8pm.", "午後8時に本を読んでいました"),
                ("They were playing soccer yesterday.", "彼らは昨日サッカーをしていました"),
                ("She was cooking dinner at that time.", "彼女はその時夕食を作っていました"),
                ("What were you doing at midnight?", "真夜中に何をしていましたか？"),
                ("He was not sleeping at that time.", "彼はその時寝ていませんでした"),
            ],
            "tip": "過去進行形 = was/were + 動詞のing形。「その時何をしていたか」を表します。現在進行形の過去版です。",
            "mistakes": [
                "<strong>「I was read a book.」</strong> → 進行形は be動詞 + 動詞のing形。「I was reading」が正解。",
                "<strong>「We was playing.」</strong> → We は複数なので were。「We were playing」が正解。",
            ],
            "next": [("bekako.html", "be動詞の過去形"), ("mirai.html", "未来形")],
            "practice": "kakosin"
        },
        "mirai.html": {
            "name": "未来形",
            "examples": [
                ("I will go to Tokyo tomorrow.", "明日東京に行きます"),
                ("She is going to study law.", "彼女は法学を勉強する予定です"),
                ("It will rain tomorrow.", "明日雨が降るでしょう"),
                ("We are going to have a test next week.", "来週テストがあります"),
                ("Will you help me?", "手伝ってくれますか？"),
            ],
            "tip": "will は「その場で決めたこと」、be going to は「前もって決めた予定」という違いがあります。テストではこの違いがよく出ます！",
            "mistakes": [
                "<strong>「will」と「be going to」の混同</strong> → will = その場の意思、be going to = 予定・確実な未来。",
                "<strong>「I will going to〜」</strong> → will のあとは動詞の原形。「I will go」が正解。",
            ],
            "next": [("jyodosi.html", "助動詞"), ("futeisi1.html", "不定詞")],
            "practice": "mirai"
        },
        "doumei.html": {
            "name": "動名詞",
            "examples": [
                ("I like swimming.", "泳ぐことが好きです"),
                ("Playing tennis is fun.", "テニスをすることは楽しいです"),
                ("He enjoys reading books.", "彼は本を読むことを楽しみます"),
                ("I finished doing my homework.", "宿題をするのを終えました"),
                ("She is good at singing.", "彼女は歌うことが得意です"),
            ],
            "tip": "動名詞 = 動詞の原形 + ing。文中で名詞の役割をします。前置詞（at, in, of, about）のあとには必ず動名詞がきます。",
            "mistakes": [
                "<strong>「I enjoy to swim.」</strong> → enjoy のあとは動名詞。「I enjoy swimming」が正解。",
                "<strong>前置詞のあとに動詞の原形</strong> → 前置詞（at, in, for, of）のあとは必ず動名詞。",
            ],
            "next": [("futeisi1.html", "不定詞"), ("futeisi2.html", "不定詞（応用）")],
            "practice": "doumei"
        },
        "jyodosi.html": {
            "name": "助動詞",
            "examples": [
                ("You must study harder.", "もっと勉強しなければなりません"),
                ("I have to go now.", "今行かなければなりません"),
                ("May I come in?", "入ってもいいですか？"),
                ("You should rest.", "休むべきです"),
                ("You must not run here.", "ここでは走ってはいけません"),
            ],
            "tip": "助動詞のあとは必ず動詞の原形！must not（禁止）と don't have to（必要ない）の違いは超重要です。",
            "mistakes": [
                "<strong>「must」と「have to」の違い</strong> → must = 話し手の強い意志、have to = 外部のルール。",
                "<strong>「must not」と「don't have to」の混同</strong> → must not = 禁止、don't have to = 必要ない。",
            ],
            "next": [("can.html", "can"), ("futeisi1.html", "不定詞")],
            "practice": "jyodosi"
        },
        "there.html": {
            "name": "there is 構文",
            "examples": [
                ("There is a cat under the table.", "テーブルの下に猫がいます"),
                ("There are many books on the desk.", "机の上にたくさんの本があります"),
                ("Is there a hospital near here?", "この近くに病院はありますか？"),
                ("There is not any milk in the fridge.", "冷蔵庫に牛乳はありません"),
            ],
            "tip": "There is/are + 名詞 + 場所。日本語の「〜に〜がある/いる」を表します。名詞が単数ならis、複数ならareを使います。",
            "mistakes": [
                "<strong>「There has a cat.」</strong> → there構文は have ではなく、There is/are を使います。",
                "<strong>名詞の数とbe動詞の不一致</strong> → 単数名詞には is、複数名詞には are。",
            ],
            "next": [("setuzoku.html", "接続詞"), ("shinko.html", "現在進行形")],
            "practice": "there"
        },
        "setuzoku.html": {
            "name": "接続詞",
            "examples": [
                ("I like cats and dogs.", "猫と犬が好きです"),
                ("I like cats but I don't like dogs.", "猫は好きですが犬は好きではありません"),
                ("I am happy because I got a present.", "プレゼントをもらったので嬉しいです"),
                ("Call me when you arrive.", "着いたら電話してください"),
                ("If it rains, I will stay home.", "雨が降れば家にいます"),
            ],
            "tip": "接続詞は文と文をつなぐ役割をします。接続詞の前後はどちらも完全な文（主語+動詞）であることが原則です。",
            "mistakes": [
                "<strong>「because」と「so」の重複</strong> → 「Because〜, so〜」は重複。どちらか一方を使います。",
                "<strong>接続詞のあとの語順</strong> → if, when, because のあとは通常の語順（疑問文ではない）。",
            ],
            "next": [("kansetu.html", "間接疑問"), ("futeisi1.html", "不定詞")],
            "practice": "setuzoku"
        },
        "ukemi.html": {
            "name": "受け身（受動態）",
            "examples": [
                ("English is spoken in many countries.", "英語は多くの国で話されています"),
                ("This book was written by Soseki.", "この本は漱石によって書かれました"),
                ("The window was broken by the boy.", "窓はその少年によって壊されました"),
                ("These cookies were made by my mother.", "これらのクッキーは母によって作られました"),
            ],
            "tip": "受け身 = be動詞 + 過去分詞 + by〜。「〜される」という意味。能動態の目的語を受け身の主語にします。",
            "mistakes": [
                "<strong>be動詞を忘れる</strong> → 「This book written by〜」ではなく「This book <strong>was</strong> written by〜」が正解。",
                "<strong>過去分詞と過去形の混同</strong> → 受け身は過去分詞を使います。write→written、break→broken。",
            ],
            "next": [("genkan1.html", "現在完了"), ("kankeisi1.html", "関係代名詞")],
            "practice": "ukemi"
        },
        "can.html": {
            "name": "can",
            "examples": [
                ("I can swim.", "泳げます"),
                ("She can speak French.", "彼女はフランス語を話せます"),
                ("Can you help me?", "手伝ってくれますか？"),
                ("I can't play the piano.", "ピアノを弾けません"),
                ("Yes, I can. / No, I can't.", "はい、できます / いいえ、できません"),
            ],
            "tip": "can + 動詞の原形。否定は can not (can't)、疑問は Can を文頭に。can のあとは必ず動詞の原形です。",
            "mistakes": ["<strong>「I can swim.」を「I can swimming.」としない</strong> → can のあとは必ず動詞の原形。", "<strong>「I can to swim.」としない</strong> → can のあとに to は不要。"],
            "next": [("jyodosi.html", "助動詞"), ("kako.html", "一般動詞の過去形")],
            "practice": "can"
        },
        "kako.html": {
            "name": "一般動詞の過去形",
            "examples": [
                ("I went to the park yesterday.", "昨日公園に行きました"),
                ("She ate breakfast at seven.", "彼女は7時に朝食を食べました"),
                ("They saw a movie last night.", "彼らは昨夜映画を見ました"),
                ("I did my homework yesterday.", "昨日宿題をしました"),
                ("He made a cake for me.", "彼は私にケーキを作ってくれました"),
            ],
            "tip": "過去形には規則動詞（-ed）と不規則動詞（暗記必須）があります。不規則動詞は1つずつしっかり覚えましょう。",
            "mistakes": ["<strong>不規則動詞を規則変化させてしまう</strong> → go→goed は間違い。go→went が正解。", "<strong>否定文で動詞を過去形のままにしてしまう</strong> → didn't を使ったら動詞は原形に戻す。"],
            "next": [("bekako.html", "be動詞の過去形"), ("kakosin.html", "過去進行形")],
            "practice": "kako"
        },
        "shinko.html": {
            "name": "現在進行形",
            "examples": [
                ("I am reading a book now.", "今本を読んでいます"),
                ("She is watching TV.", "彼女はテレビを見ています"),
                ("They are playing soccer.", "彼らはサッカーをしています"),
                ("Are you studying now?", "今勉強していますか？"),
                ("He is not sleeping.", "彼は寝ていません"),
            ],
            "tip": "現在進行形 = be動詞 + 動詞のing形。「今まさに〜している」という動作の最中を表します。",
            "mistakes": ["<strong>「I am read a book.」</strong> → be動詞 + 動詞の原形ではなく、be動詞 + 動詞のing形。", "<strong>動詞のing形の作り方を間違える</strong> → make→makeingではなく、eを取ってmaking。"],
            "next": [("kakosin.html", "過去進行形"), ("futeisi1.html", "不定詞")],
            "practice": "shinko"
        },
        "santan.html": {
            "name": "三人称単数現在",
            "examples": [
                ("He plays tennis every Sunday.", "彼は毎週日曜日にテニスをします"),
                ("She goes to school by bus.", "彼女はバスで学校に行きます"),
                ("The cat drinks milk.", "猫はミルクを飲みます"),
                ("Does she like music?", "彼女は音楽が好きですか？"),
                ("He doesn't play the piano.", "彼はピアノを弾きません"),
            ],
            "tip": "主語が he, she, it（3人称単数）のとき、動詞に s または es がつきます。疑問文・否定文では does / doesn't を使い、動詞は原形に戻します。",
            "mistakes": ["<strong>「He play tennis.」</strong> → 3人称単数の肯定文には s が必要。「He plays tennis.」が正解。", "<strong>「Does he plays?」</strong> → does を使ったら動詞は原形に戻す。「Does he play?」が正解。"],
            "next": [("shinko.html", "現在進行形"), ("gimonhitei.html", "疑問文・否定文")],
            "practice": "santan"
        },
        "gimonhitei.html": {
            "name": "疑問文・否定文",
            "examples": [
                ("Are you a student? / Yes, I am.", "学生ですか？はい"),
                ("Do you like cats? / Yes, I do.", "猫は好きですか？はい"),
                ("He is not a teacher.", "彼は教師ではありません"),
                ("I don't like coffee.", "コーヒーは好きではありません"),
                ("Does she speak English?", "彼女は英語を話しますか？"),
            ],
            "tip": "be動詞の疑問文は be動詞を文頭に、一般動詞は Do/Does/Did を文頭に。否定文は be動詞なら動詞のあとに not、一般動詞なら do not を使います。",
            "mistakes": ["<strong>be動詞の疑問文に do を使ってしまう</strong> → 「Do you are a student?」は間違い。「Are you a student?」が正解。", "<strong>否定文の語順の間違い</strong> → be動詞の否定は be動詞 + not、一般動詞の否定は do/does/did + not + 動詞の原形。"],
            "next": [("gimonsi.html", "疑問詞"), ("meirei.html", "命令文")],
            "practice": "gimonhitei"
        },
        "meirei.html": {
            "name": "命令文",
            "examples": [
                ("Sit down.", "座りなさい"),
                ("Open your book.", "本を開きなさい"),
                ("Don't run.", "走ってはいけません"),
                ("Please stand up.", "立ち上がってください"),
                ("Don't be late.", "遅れてはいけません"),
            ],
            "tip": "命令文は動詞の原形で始めます。否定（禁止）は Don't を文頭に置きます。Please を付けると丁寧になります。",
            "mistakes": ["<strong>「Don't to run.」</strong> → 否定の命令文は Don't + 動詞の原形。Don't のあとに to は不要。", "<strong>「Not run.」</strong> → 否定の命令文は Don't で始める。"],
            "next": [("gimonhitei.html", "疑問文・否定文"), ("can.html", "can")],
            "practice": "meirei"
        },
        "gimonsi.html": {
            "name": "疑問詞",
            "examples": [
                ("What is this?", "これは何ですか？"),
                ("Who is he?", "彼は誰ですか？"),
                ("Where are you from?", "どこから来ましたか？"),
                ("When is your birthday?", "誕生日はいつですか？"),
                ("Why are you late?", "なぜ遅刻したのですか？"),
            ],
            "tip": "疑問詞は文の先頭に置きます。そのあとの語順は疑問文の語順（be動詞 + 主語 /  do + 主語 + 動詞）です。",
            "mistakes": ["<strong>疑問詞のあとの語順を間違える</strong> → 「What is this?」が正しく、「What this is?」は間違い。", "<strong>「Who are you?」と「Who is he?」の区別</strong> → you には are、he/she/it には is。"],
            "next": [("gimonhitei.html", "疑問文・否定文"), ("daimeisi.html", "代名詞")],
            "practice": "gimonhitei"
        },
    }
    
    for filename, data in pages.items():
        content = make_grammar_blocks(
            data["name"],
            data.get("examples", []),
            data.get("tip", ""),
            data.get("mistakes", []),
            data.get("next", []),
            data.get("practice", "")
        )
        thicken_page(filename, content)

if __name__ == "__main__":
    print("=== 全30ページを厚くします ===")
    thicken_all()
    print("=== 完了 ===")