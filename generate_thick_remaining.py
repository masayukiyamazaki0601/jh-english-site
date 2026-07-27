#!/usr/bin/env python3
"""残り13ページを厚くする（第2弾）"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken_page(filename, extra_content):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    insert_pos = content.rfind("</article>")
    if insert_pos == -1:
        print(f"  SKIP {filename}")
        return
    line_count = content.count("\n")
    if line_count > 250:
        print(f"  SKIP {filename}: already thick ({line_count})")
        return
    new_content = content[:insert_pos] + extra_content + "\n" + content[insert_pos:]
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  THICKENED {filename} ({line_count} -> {new_content.count(chr(10))})")

def make_blocks(name, examples, tip, mistakes, next_links, practice):
    blocks = []
    if examples:
        ex = "<h2>📝 実践的な例文</h2>\n<ul>\n"
        for en, jp in examples:
            ex += f'  <li><span class="example">{en}</span> <span class="example-jp">（{jp}）</span></li>\n'
        ex += "</ul>\n"
        blocks.append(ex)
    if tip:
        blocks.append(f'<div class="tip-box"><h3>💡 {name}をマスターするコツ</h3><p>{tip}</p></div>\n')
    if mistakes:
        items = "".join(f"<li>{m}</li>\n" for m in mistakes)
        blocks.append(f'<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>\n{items}</ul></div>\n')
    if next_links:
        links = "".join(f'<a href="{u}" class="roadmap-next">{l} →</a>\n' for u, l in next_links)
        blocks.append(f'<div class="roadmap-box"><h2>🗺️ 学習の流れ</h2><p style="color:var(--gray-600);font-size:0.9rem;margin-bottom:12px;">{name}をマスターしたら、次の単元に進みましょう。</p><div class="roadmap-links">\n{links}</div></div>\n')
    if practice:
        blocks.append(f'<div class="practice-link-box"><p>✅ 理解を深めたら <a href="../practice/{practice}">練習問題を解く</a> か <a href="../test/{practice}_test.html">確認テストに挑戦</a> しよう。</p></div>\n')
    if next_links:
        related = ""
        for u, l in next_links[:6]:
            related += f'      <a href="{u}" class="related-card"><span class="related-title">{l}</span><span class="related-arrow">→</span></a>\n'
        blocks.append(f'<div class="related-articles"><h2>📚 関連する文法単元</h2><div class="related-grid">\n{related}</div></div>\n')
    return "\n".join(blocks)

pages = {
    "genkanSinkokei.html": {
        "name":"現在完了進行形","practice":"genkan",
        "examples":[("I have been studying for two hours.","2時間勉強し続けています"),("It has been raining since morning.","朝から雨が降り続いています"),("She has been waiting for 30 minutes.","彼女は30分待ち続けています")],
        "tip":"have/has + been + 動詞のing形。「ずっと〜し続けている」と強調したいときに使います。現在完了の継続用法の強調版です。",
        "mistakes":["<strong>beenを忘れる</strong> → have/has + been + doing。beenが必要です。","<strong>継続との違い</strong> → I have lived = 状態、I have been living = 動作を強調。"],
        "next":[("genkan1.html","現在完了"),("shinko.html","現在進行形")]
    },
    "genkan3.html": {
        "name":"現在完了（完了・結果）","practice":"genkan",
        "examples":[("I have just finished my homework.","ちょうど宿題を終えたところです"),("She has already eaten lunch.","彼女はもう昼食を食べました"),("Have you finished yet?","もう終わりましたか？"),("I haven't finished yet.","まだ終わっていません")],
        "tip":"just（ちょうど）、already（もう）、yet（もう？/まだ）がキーワード。alreadyは肯定文、yetは疑問文・否定文で使います。",
        "mistakes":["<strong>「I have just finished.」と「I just finished.」の違い</strong> → justは現在完了と一緒に使うのが正式、過去形でも通じるがテストでは現在完了が安全。","<strong>alreadyとyetの位置</strong> → alreadyはhaveのあと、yetは文末。"],
        "next":[("genkan1.html","現在完了"),("genkan2.html","現在完了（経験）")]
    },
    "kansetu.html": {
        "name":"間接疑問","practice":"kansetu",
        "examples":[("I know where he lives.","彼がどこに住んでいるか知っています"),("Do you know what this is?","これが何か知っていますか？"),("I don't know who she is.","彼女が誰かわかりません"),("Please tell me when the party starts.","パーティーがいつ始まるか教えてください")],
        "tip":"間接疑問の最大のポイントは「疑問文なのに語順が肯定文になる」こと。Do you know what <strong>this is</strong>?（what is this? ではない！）",
        "mistakes":["<strong>語順を疑問文のままにしてしまう</strong> → 「Do you know what is this?」は間違い。「Do you know what this is?」が正解。","<strong>関係代名詞と間接疑問の区別</strong> → 先行詞があれば関係代名詞、なければ間接疑問。"],
        "next":[("kankeisi1.html","関係代名詞"),("gimonsi.html","疑問詞")]
    },
    "kateiho.html": {
        "name":"仮定法","practice":"kateiho",
        "examples":[("If I were you, I would go there.","もし私があなたなら、そこに行くのに"),("If I had money, I would buy a car.","もしお金があれば、車を買うのに"),("If it were sunny, we could go out.","もし晴れていれば、外出できるのに")],
        "tip":"仮定法過去＝現実と違うことを仮定する。be動詞は主語がIでもwereを使う。would/could + 動詞の原形とセットで覚えましょう。",
        "mistakes":["<strong>「If I was you」</strong> → 仮定法では「If I <strong>were</strong> you」が正解。","<strong>wouldのあとにtoをつけてしまう</strong> → would + 動詞の原形。would to go は間違い。"],
        "next":[("futeisi1.html","不定詞"),("kankeisi1.html","関係代名詞")]
    },
    "genkeiFuteisi.html": {
        "name":"原形不定詞","practice":"genkei",
        "examples":[("He made me clean the room.","彼は私に部屋を掃除させた"),("I saw him cross the street.","彼が通りを渡るのを見た"),("She let me use her phone.","彼女は私に電話を使わせてくれた"),("I heard her sing in the room.","彼女が部屋で歌うのが聞こえた")],
        "tip":"使役動詞（make, let, have）や知覚動詞（see, hear, watch）のあとはtoをつけない不定詞＝原形不定詞を使います。",
        "mistakes":["<strong>「He made me to clean.」</strong> → makeのあとは原形不定詞（to不要）。","<strong>受身にするとtoが必要</strong> → I was made <strong>to</strong> clean the room."],
        "next":[("futeisi1.html","不定詞"),("futeisi2.html","不定詞（応用）")]
    },
    "genkan2.html": {
        "name":"現在完了（経験）","practice":"genkan",
        "examples":[("I have been to Kyoto twice.","京都に2回行ったことがあります"),("Have you ever seen a lion?","ライオンを見たことがありますか？"),("She has never eaten sushi.","彼女は寿司を食べたことがありません")],
        "tip":"経験用法 = 「〜したことがある」。ever（疑問文）、never（否定文）と一緒に使います。have been to（行ったことがある）とhave gone to（行ってしまった）の違いは超重要！",
        "mistakes":["<strong>「I have gone to Kyoto.」を「行ったことがある」の意味で使う</strong> → gone to = 行ってしまった（今いない）。been to = 行ったことがある。","<strong>neverの位置</strong> → have + never + 過去分詞。"],
        "next":[("genkan1.html","現在完了"),("genkan3.html","現在完了（完了）")]
    },
    "bunsi.html": {
        "name":"分詞","practice":"bunsi",
        "examples":[("The girl singing on stage is my sister.","ステージで歌っている女の子は私の妹です"),("The book written by him is interesting.","彼によって書かれた本は面白いです"),("I saw a broken window.","壊れた窓を見ました")],
        "tip":"現在分詞（doing）=「〜している」、過去分詞（done）=「〜された」。どちらも形容詞の役割をします。",
        "mistakes":["<strong>現在分詞と過去分詞の混同</strong> → 能動（〜している）なら現在分詞、受動（〜される）なら過去分詞。","<strong>分詞の位置</strong> → 1語なら名詞の前、2語以上なら名詞の後ろ。"],
        "next":[("kankeisi1.html","関係代名詞"),("futeisi1.html","不定詞")]
    },
    "daimeisi.html": {
        "name":"代名詞","practice":"daimeisi",
        "examples":[("This is my book. This book is mine.","これは私の本です。この本は私のものです"),("I like her. She is kind.","私は彼女が好きです。彼女は親切です"),("This is your pen. That one is yours.","これはあなたのペンです。あれはあなたのものです")],
        "tip":"代名詞の変化表（I/my/me/mine）は暗記必須！特に「所有格+名詞＝所有代名詞」の関係を理解しましょう。my book = mine。",
        "mistakes":["<strong>「This book is my.」</strong> → myのあとには名詞が必要。「This book is mine.」か「This is my book.」が正解。","<strong>主格と目的格の混同</strong> → 動詞の前は主格（I, he, she）、動詞/前置詞のあとは目的格（me, him, her）。"],
        "next":[("be.html","be動詞"),("fukusu.html","名詞の複数形")]
    },
    "fukusu.html": {
        "name":"名詞の複数形","practice":"fukusu",
        "examples":[("I have two cats.", "猫を2匹飼っています"),("There are many books on the desk.", "机の上にたくさんの本があります"),("The children are playing in the park.", "子供たちは公園で遊んでいます")],
        "tip":"複数形の基本ルール：普通はs、s/o/x/ch/shで終わる単語はes、子音字+yはyをiに変えてes。不規則変化（children, men, women）も覚えましょう。",
        "mistakes":["<strong>「childs」「mans」</strong> → children, men が正解。不規則変化は暗記。","<strong>数えられない名詞にsをつける</strong> → water, money, information には s をつけない。"],
        "next":[("daimeisi.html","代名詞"),("santan.html","三人称単数現在")]
    },
    "futeisi2.html": {
        "name":"不定詞（応用）","practice":"futeisi",
        "examples":[("It is important for you to study English.", "あなたが英語を勉強することは重要です"),("I don't know what to do.", "何をすればいいかわかりません"),("She told me to come here.", "彼女はここに来るように言いました")],
        "tip":"It is ... for 人 to〜 構文、疑問詞+不定詞（what to do, how to swim）、ask/tell 人 to〜 の3つが応用のポイント。",
        "mistakes":["<strong>「It is important for you study.」</strong> → for 人 + to + 動詞の原形。to を忘れずに。","<strong>「I don't know what do.」</strong> → 疑問詞+不定詞では to が必要。"],
        "next":[("futeisi1.html","不定詞"),("bunsi.html","分詞")]
    },
    "hikaku1.html": {
        "name":"比較","practice":"hikaku",
        "examples":[("Taro is taller than Jiro.", "太郎は次郎より背が高い"),("Mt. Fuji is the highest mountain in Japan.", "富士山は日本で一番高い山です"),("She is as tall as me.", "彼女は私と同じくらい背が高い")],
        "tip":"比較級（-er/more）+ than、最上級（the -est/the most）、原級（as + 原級 + as）。長い単語は more/most を使います。",
        "mistakes":["<strong>「more taller」</strong> → taller がすでに比較級。more は不要。「more beautiful」のように長い単語に使う。","<strong>最上級にtheをつけ忘れる</strong> → the tallest / the most beautiful が正解。"],
        "next":[("there.html","there is"),("setuzoku.html","接続詞")]
    },
    "ippan.html": {
        "name":"一般動詞","practice":"ippan",
        "examples":[("I play tennis every Sunday.", "毎週日曜日にテニスをします"),("She studies English every day.", "彼女は毎日英語を勉強します"),("Do you like cats?", "猫は好きですか？"),("I don't eat meat.", "肉を食べません")],
        "tip":"be動詞以外の動詞はすべて一般動詞。3人称単数現在のs、疑問文・否定文のdo/doesの使い分けがポイント。",
        "mistakes":["<strong>「He play soccer.」</strong> → 3人称単数にはsが必要。","<strong>一般動詞の疑問文に be動詞を使う</strong> → 「Are you like cats?」は間違い。「Do you like cats?」が正解。"],
        "next":[("gimonhitei.html","疑問文・否定文"),("santan.html","三人称単数現在")]
    },
    "shinko.html": {
        "name":"現在進行形","practice":"shinko",
        "examples":[("I am reading a book now.", "今本を読んでいます"),("She is watching TV.", "彼女はテレビを見ています"),("They are playing soccer.", "彼らはサッカーをしています"),("Are you studying now?", "今勉強していますか？")],
        "tip":"現在進行形 = be動詞 + 動詞のing形。今まさにしている動作を表します。状態動詞（know, like, want）は進行形にできないので注意。",
        "mistakes":["<strong>「I am know him.」</strong> → know は状態動詞なので進行形にできない。「I know him.」が正解。","<strong>ing形の作り方</strong> → make→makeingではなくmaking。run→runningのように子音を重ねるルールも。"],
        "next":[("kakosin.html","過去進行形"),("futeisi1.html","不定詞")]
    },
}

if __name__ == "__main__":
    print("=== 残りページを厚くします ===")
    for fname, data in pages.items():
        content = make_blocks(data["name"], data.get("examples",[]), data.get("tip",""), data.get("mistakes",[]), data.get("next",[]), data.get("practice",""))
        thicken_page(fname, content)
    print("=== 完了 ===")