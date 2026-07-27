#!/usr/bin/env python3
"""30ページを全て200行超えに拡張（第3弾：徹底厚書）"""
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
    if lc >= 230:
        print(f"  SKIP {filename}: already {lc}")
        return
    new = content[:pos] + extra + "\n" + content[pos:]
    with open(path, "w") as f:
        f.write(new)
    print(f"  {filename}: {lc} -> {new.count(chr(10))} (+{new.count(chr(10))-lc})")

def mk_quiz(qs):
    html = '<h2>🎯 理解度チェック</h2>\n<p>以下の問題に答えてみましょう。</p>\n'
    for i, (q, opts, ans_text) in enumerate(qs):
        html += f'<div class="quiz-embed"><p style="font-weight:700;font-size:1.05rem;">Q{i+1}. {q}</p><div class="mini-options">\n'
        for opt in opts:
            c = 'selected-correct' if opt == ans_text else 'selected-wrong'
            fb_text = '✅ 正解！' if opt == ans_text else '❌ 不正解。'
            html += f'  <span class="mini-opt" style="pointer-events:none;" onclick="this.classList.add(\'{c}\')">{opt}</span>\n'
        html += '</div></div>\n'
    return html

pages = {
    "genkanSinkokei.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I have been studying English for three years.</span> <span class="example-jp">（3年間英語を勉強し続けています）</span></li>
  <li><span class="example">She has been waiting for the bus since 8am.</span> <span class="example-jp">（彼女は午前8時からバスを待ち続けています）</span></li>
  <li><span class="example">They have been playing tennis since morning.</span> <span class="example-jp">（彼らは朝からテニスをし続けています）</span></li>
</ul>
<div class="tip-box"><h3>💡 現在完了進行形と現在完了（継続）の違い</h3><p>現在完了進行形 = have/has + been + doing。動作そのものを強調します。現在完了（継続）は状態を表す動詞（live, know, have）とよく使われます。動作動詞（study, wait, rain）には現在完了進行形が自然です。</p></div>
<div class="note"><strong>よく使う表現</strong><br>for + 期間 / since + 時点 + been + doing の形を覚えましょう。I have been studying for 2 hours. / It has been raining since yesterday.</div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have been study.」</strong> → have + been + doing。「studying」が必要。</li>
  <li><strong>「I am studying for 2 hours.」</strong> → 現在進行形は「今している」だけ。継続には現在完了進行形を使う。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/genkan.html">現在完了の練習問題を解く</a> か <a href="../test/genkan_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "ukemi.html": {
        "extra": """
<h2>📝 さらに詳しく</h2>
<p>受け身は「〜される」という意味。目的語を主語にして、動詞を「be + 過去分詞」に変えます。by 〜で行為者を表します。</p>
<div class="highlight"><p>能動態: The boy <strong>broke</strong> the window.<br>受動態: The window <strong>was broken</strong> by the boy.</p></div>
<h3>時制ごとの受け身</h3>
<table><tr><th>時制</th><th>能動態</th><th>受動態</th></tr>
<tr><td>現在</td><td>He cleans the room.</td><td>The room is cleaned（by him）.</td></tr>
<tr><td>過去</td><td>He cleaned the room.</td><td>The room was cleaned（by him）.</td></tr>
<tr><td>未来</td><td>He will clean the room.</td><td>The room will be cleaned（by him）.</td></tr>
<tr><td>現在完了</td><td>He has cleaned the room.</td><td>The room has been cleaned（by him）.</td></tr></table>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>be動詞を忘れる</strong> → 「The window broken.」ではなく「The window <strong>was</strong> broken.」が正解。</li>
  <li><strong>能動態のまま目的語だけ移動</strong> → 「The window broke by the boy.」は間違い。動詞も変える。</li>
  <li><strong>by + 行為者を書き忘れる</strong> → 必要なときは by 〜を忘れずに。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/ukemi.html">受け身の練習問題を解く</a> か <a href="../test/ukemi_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "genkan3.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I have already seen this movie.</span> <span class="example-jp">（この映画はもう見ました）</span></li>
  <li><span class="example">She has just left the office.</span> <span class="example-jp">（彼女はちょうど事務所を出ました）</span></li>
  <li><span class="example">Have you finished your homework yet?</span> <span class="example-jp">（もう宿題を終えましたか？）</span></li>
  <li><span class="example">I haven't decided yet.</span> <span class="example-jp">（まだ決めていません）</span></li>
</ul>
<div class="tip-box"><h3>💡 already / yet / just のイメージ</h3><p><strong>already</strong> = 予想より早く「もう」。驚きの気持ちを含む。<br><strong>yet</strong> = 予定通りに起こったかどうかの確認。「もう？/まだ」<br><strong>just</strong> = 「ついさっき」。ごく最近の完了。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have already finished it yet.」</strong> → already と yet は同時に使わない。</li>
  <li><strong>「I just finished.」と「I have just finished.」</strong> → 会話では過去形も使われるが、テストでは現在完了が安全。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/genkan.html">現在完了の練習問題を解く</a> か <a href="../test/genkan_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "kansetu.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I don't know where she lives.</span> <span class="example-jp">（彼女がどこに住んでいるか知らない）</span></li>
  <li><span class="example">Can you tell me how to get to the station?</span> <span class="example-jp">（駅への行き方を教えてくれますか？）</span></li>
  <li><span class="example">I wonder why he is late.</span> <span class="example-jp">（なぜ彼が遅れているのか不思議だ）</span></li>
  <li><span class="example">Please tell me what time it is.</span> <span class="example-jp">（今何時か教えてください）</span></li>
</ul>
<div class="highlight"><p>【最重要ルール】間接疑問のあとは <strong>肯定文の語順</strong>（主語 + 動詞）になる！</p></div>
<div class="tip-box"><h3>💡 関係代名詞との違い</h3><p>関係代名詞：先行詞（名詞）がある。The boy <strong>who</strong> is running ...<br>間接疑問：先行詞がない。I know <strong>who</strong> he is.<br>疑問詞のあとに「主語+動詞」が続けば間接疑問、「動詞」が続けば関係代名詞。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「Do you know what is this?」</strong> → 「Do you know what this is?」が正解。語順に注意。</li>
  <li><strong>「Tell me where is the station.」</strong> → 「Tell me where the station is.」が正解。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/kansetu.html">間接疑問の練習問題を解く</a> か <a href="../test/kansetu_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "mirai.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I will call you later.</span> <span class="example-jp">（あとで電話します）← その場の意思</span></li>
  <li><span class="example">We are going to visit Kyoto next month.</span> <span class="example-jp">（来月京都を訪れる予定です）← 計画</span></li>
  <li><span class="example">It will be rainy tomorrow.</span> <span class="example-jp">（明日は雨でしょう）← 予測</span></li>
  <li><span class="example">I am going to be a doctor.</span> <span class="example-jp">（医者になるつもりです）← 将来の夢</span></li>
</ul>
<div class="highlight"><p><strong>will</strong> = その場で決めたこと・予測・約束<br><strong>be going to</strong> = 前から決めていた予定・確実な未来</p></div>
<div class="tip-box"><h3>💡 未来を表すその他の表現</h3><p><strong>be about to</strong> = 「まさに〜しようとしている」（間近の未来）<br><strong>be doing</strong> = 現在進行形で近い未来の予定（I am meeting him tomorrow.）<br><strong>be to + 動詞</strong> = 「〜することになっている」（公式の予定）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I will going to〜」</strong> → will のあとは動詞の原形。be going to とは一緒に使わない。</li>
  <li><strong>未来のことなのに現在形を使う</strong> → 確定した予定（時刻表など）以外は未来形を使う。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/mirai.html">未来形の練習問題を解く</a> か <a href="../test/mirai_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "kateiho.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">If I were a bird, I could fly to you.</span> <span class="example-jp">（もし鳥なら、あなたのところに飛んでいけるのに）</span></li>
  <li><span class="example">If she had more time, she would learn piano.</span> <span class="example-jp">（もっと時間があれば、ピアノを学ぶのに）</span></li>
  <li><span class="example">If it were not rainy, we could go hiking.</span> <span class="example-jp">（雨でなければ、ハイキングに行けるのに）</span></li>
  <li><span class="example">I would be happy if I could meet her.</span> <span class="example-jp">（彼女に会えるなら幸せなのに）</span></li>
</ul>
<div class="tip-box"><h3>💡 仮定法の基本形</h3><p>If + 主語 + 過去形（were）〜, 主語 + would/could + 動詞の原形<br>例）If I were you, I would study harder.</p></div>
<div class="tip-box"><h3>💡 仮定法と条件文（if + 現在形）の違い</h3><p>条件文（if + 現在形）：現実に起こりうる条件。If it rains, I will stay home.（雨が降れば家にいる）<br>仮定法（if + 過去形）：現実と違う仮定。If it rained, I would stay home.（もし雨が降れば家にいるのに ← 実際は降っていない）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>条件文と仮定法の混同</strong> → 現実にあり得るなら条件文、あり得ない・違うなら仮定法。</li>
  <li><strong>wouldのあとにtoをつける</strong> → would + 動詞の原形。would to go は間違い。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/kateiho.html">仮定法の練習問題を解く</a> か <a href="../test/kateiho_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "there.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">There is a park near my house.</span> <span class="example-jp">（私の家の近くに公園があります）</span></li>
  <li><span class="example">There are many stars in the sky.</span> <span class="example-jp">（空にたくさんの星があります）</span></li>
  <li><span class="example">Is there a convenience store around here?</span> <span class="example-jp">（この辺りにコンビニはありますか？）</span></li>
  <li><span class="example">There was a big earthquake last year.</span> <span class="example-jp">（去年大きな地震がありました）</span></li>
</ul>
<div class="tip-box"><h3>💡 there is/are の時制変化</h3><p>現在：There is/are / 過去：There was/were / 未来：There will be / 現在完了：There have/has been<br>There <strong>will be</strong> a concert next week.（来週コンサートがあります）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「There has a book.」</strong> → there + have は間違い。There is/are が正解。</li>
  <li><strong>複数なのに is を使ってしまう</strong> → 「There is many people.」は間違い。「There are many people.」が正解。</li>
  <li><strong>There is と It is の混同</strong> → 「〜がある」は There is / 「それは〜だ」は It is。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/there.html">there is の練習問題を解く</a> か <a href="../test/there_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "doumei.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I finished reading the book.</span> <span class="example-jp">（その本を読み終えました）</span></li>
  <li><span class="example">She enjoys listening to music.</span> <span class="example-jp">（彼女は音楽を聴くのを楽しみます）</span></li>
  <li><span class="example">He gave up smoking.</span> <span class="example-jp">（彼はタバコをやめました）</span></li>
  <li><span class="example">I am interested in learning Japanese.</span> <span class="example-jp">（日本語を学ぶことに興味があります）</span></li>
</ul>
<div class="tip-box"><h3>💡 動名詞が主語になる場合</h3><p>動名詞は文の主語になることができます。<br><strong>Playing</strong> tennis is fun.（テニスをすることは楽しいです）<br>この場合、動名詞は3人称単数扱いなので、動詞には三単現のsがつきます。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I enjoy to swim.」</strong> → enjoy のあとは動名詞。enjoy + doing。</li>
  <li><strong>「I look forward to hear from you.」</strong> → look forward to の to は前置詞。あとは動名詞。「I look forward to <strong>hearing</strong> from you.」</li>
  <li><strong>動名詞と現在分詞の混同</strong> → 動名詞は名詞の役割（主語・目的語）、現在分詞は形容詞の役割。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/doumei.html">動名詞の練習問題を解く</a> か <a href="../test/doumei_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "genkan2.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I have never seen such a beautiful sunset.</span> <span class="example-jp">（こんなに美しい夕日を見たことがない）</span></li>
  <li><span class="example">Have you ever been abroad?</span> <span class="example-jp">（外国に行ったことがありますか？）</span></li>
  <li><span class="example">She has never driven a car.</span> <span class="example-jp">（彼女は車を運転したことがありません）</span></li>
  <li><span class="example">I have eaten Japanese food many times.</span> <span class="example-jp">（日本食を何度も食べたことがあります）</span></li>
</ul>
<div class="highlight"><p><strong>have been to</strong> vs <strong>have gone to</strong> vs <strong>have been in</strong><br>
✅ have been to = 行ったことがある（行って帰ってきた）<br>
✅ have gone to = 行ってしまった（今ここにいない）<br>
✅ have been in = 〜に住んでいる（継続）</p></div>
<div class="tip-box"><h3>💡 ever と never の覚え方</h3><p>「Have you ever 〜？」= 「〜したことある？」（疑問文）<br>「I have never 〜」= 「一度も〜ない」（否定文）<br>ever は疑問文だけ、never は否定文だけ。このルールを覚えましょう。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I have ever been to Kyoto.」</strong> → ever は疑問文で使う。肯定文では使わない。</li>
  <li><strong>「She has gone to Kyoto.」を行ったことがあるの意味で使う</strong> → gone to は「行ってしまった」。「行ったことがある」は been to。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/genkan.html">現在完了の練習問題を解く</a> か <a href="../test/genkan_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "genkeiFuteisi.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">He made me wait for an hour.</span> <span class="example-jp">（彼は私を1時間待たせた）</span></li>
  <li><span class="example">I saw her cross the street.</span> <span class="example-jp">（彼女が通りを渡るのを見た）</span></li>
  <li><span class="example">She let me borrow her car.</span> <span class="example-jp">（彼女は私に車を借りさせてくれた）</span></li>
  <li><span class="example">I heard him play the guitar.</span> <span class="example-jp">（彼がギターを弾くのを聞いた）</span></li>
</ul>
<div class="highlight"><p>【使役動詞】make + 人 + 動詞の原形 = 人に〜させる<br>【知覚動詞】see/hear/watch + 人 + 動詞の原形 = 人が〜するのを見る/聞く</p></div>
<div class="tip-box"><h3>💡 受身にすると to が必要</h3><p>能動態：He made me <strong>clean</strong> the room.<br>受動態：I was made <strong>to clean</strong> the room.<br>受身になると to 不定詞に変わります。この違いはテスト頻出です。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I saw her to cross the street.」</strong> → 知覚動詞のあとは原形不定詞（to不要）。</li>
  <li><strong>「He made me to wait.」</strong> → make のあとも原形不定詞（to不要）。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/genkei.html">原形不定詞の練習問題を解く</a> か <a href="../test/genkei_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "kakosin.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I was taking a shower at 7am.</span> <span class="example-jp">（午前7時にシャワーを浴びていました）</span></li>
  <li><span class="example">They were having dinner when I called.</span> <span class="example-jp">（私が電話したとき、彼らは夕食を食べていました）</span></li>
  <li><span class="example">She was studying all night.</span> <span class="example-jp">（彼女は一晩中勉強していました）</span></li>
  <li><span class="example">We were not watching TV at that time.</span> <span class="example-jp">（その時テレビを見ていませんでした）</span></li>
</ul>
<div class="tip-box"><h3>💡 過去進行形と過去形の違い</h3><p>過去進行形：ある時点で「進行中」だった動作。<br>過去形：「完了した」動作。<br>I was reading a book when she came.（彼女が来たとき、本を読んでいた）= 読んでいる途中に来た<br>I read a book last night.（昨夜本を読んだ）= 読み終わった</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「When I was young, I was playing soccer.」</strong> → 習慣や状態は過去形。When I was young, I played soccer. が自然。</li>
  <li><strong>was/were の使い分け</strong> → I/he/she/it → was / you/we/they → were。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/kakosin.html">過去進行形の練習問題を解く</a> か <a href="../test/kakosin_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "setuzoku.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I studied hard, so I passed the exam.</span> <span class="example-jp">（一生懸命勉強したので、試験に合格しました）</span></li>
  <li><span class="example">She was tired, but she continued working.</span> <span class="example-jp">（彼女は疲れていたが、仕事を続けた）</span></li>
  <li><span class="example">Call me when you get home.</span> <span class="example-jp">（家に着いたら電話してください）</span></li>
  <li><span class="example">I think that she is right.</span> <span class="example-jp">（彼女が正しいと思います）</span></li>
</ul>
<div class="tip-box"><h3>💡 接続詞の種類</h3><p>等位接続詞：and / but / or / so（同じレベルの文をつなぐ）<br>従位接続詞：because / when / if / that / while / after / before（主節と従属節をつなぐ）</p></div>
<div class="tip-box"><h3>💡 従位接続詞の語順に注意</h3><p>When + 文 , 文 / 文 + when + 文。カンマの有無は決まりはないが、従位接続詞で始まるときはカンマを使うことが多い。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「Because〜, so〜」の重複</strong> → 「Because it rained, so I stayed home.」は重複。どちらか一方だけ。</li>
  <li><strong>「I think」のあとに不要な that がない</strong> → that は省略可能。I think (that) he is kind.</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/setuzoku.html">接続詞の練習問題を解く</a> か <a href="../test/setuzoku_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "bunsi.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">The woman sitting next to me is my aunt.</span> <span class="example-jp">（私の隣に座っている女性は私の叔母です）</span></li>
  <li><span class="example">The car made in Japan is popular.</span> <span class="example-jp">（日本で作られた車は人気があります）</span></li>
  <li><span class="example">I saw a running dog in the park.</span> <span class="example-jp">（公園で走っている犬を見ました）</span></li>
</ul>
<div class="tip-box"><h3>💡 分詞の位置のルール</h3><p>1語の分詞 → 名詞の前に置く（a <strong>broken</strong> window, a <strong>running</strong> dog）<br>2語以上の分詞句 → 名詞の後ろに置く（The window <strong>broken by the boy</strong> ...）</p></div>
<div class="tip-box"><h3>💡 関係代名詞からの書き換え</h3><p>分詞は関係代名詞の文を短くしたもの。<br>The boy <strong>who is running</strong> → The boy <strong>running</strong><br>能動態（doing）でも受動態（done）でも使える。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>現在分詞と過去分詞の意味の混同</strong> → a surprising result（驚かせる結果）= 能動 / a surprised boy（驚かされた少年）= 受動</li>
  <li><strong>分詞の位置を間違える</strong> → 「a sleeping cat」が正しく「a cat sleeping」も可だが、意味が変わる場合がある。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/bunsi.html">分詞の練習問題を解く</a> か <a href="../test/bunsi_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "daimeisi.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">This is my bag. That is yours.</span> <span class="example-jp">（これは私のカバンです。あれはあなたのです）</span></li>
  <li><span class="example">I gave her a present. She liked it.</span> <span class="example-jp">（彼女にプレゼントをあげました。彼女はそれを気に入りました）</span></li>
  <li><span class="example">Our school is bigger than theirs.</span> <span class="example-jp">（私たちの学校は彼らのより大きい）</span></li>
</ul>
<div class="highlight"><p><strong>人称代名詞の変化表（暗記必須）</strong><br>
I - my - me - mine / you - your - you - yours / he - his - him - his<br>
she - her - her - hers / it - its - it - its / we - our - us - ours / they - their - them - theirs</p></div>
<div class="tip-box"><h3>💡 所有格 + 名詞 = 所有代名詞の関係</h3><p>my book = mine / your pen = yours / his car = his / her bag = hers / our house = ours / their school = theirs<br>「私のもの」= mine。「私の」= my + 名詞。この違いをしっかり覚えましょう。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「This is mine book.」</strong> → mine は所有代名詞で単独で使う。my book か mine のどちらか。</li>
  <li><strong>「This book is my.」</strong> → my のあとには名詞が必要。This book is mine. が正解。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/daimeisi.html">代名詞の練習問題を解く</a> か <a href="../test/daimeisi_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "bekako.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">I was at home yesterday.</span> <span class="example-jp">（昨日家にいました）</span></li>
  <li><span class="example">They were very busy last week.</span> <span class="example-jp">（彼らは先週とても忙しかった）</span></li>
  <li><span class="example">She was not at school yesterday.</span> <span class="example-jp">（彼女は昨日学校にいませんでした）</span></li>
  <li><span class="example">Were you tired after the game?</span> <span class="example-jp">（試合の後疲れていましたか？）</span></li>
</ul>
<div class="tip-box"><h3>💡 was/were の使い分け表</h3><p>I → was / You → were / He/She/It → was / We → were / They → were<br>否定：was not (wasn't) / were not (weren't)<br>疑問：Was I〜? / Were you〜? / Was he/she/it〜? / Were we/they〜?</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「There was many people.」</strong> → many people は複数なので「There were many people.」。要注意。</li>
  <li><strong>疑問文への答え方</strong> → 「Were you〜?」に「Yes, you were.」と答えない。「Yes, I was.」</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/bekako.html">be動詞過去形の練習問題を解く</a> か <a href="../test/bekako_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "gimonsi.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">What do you want for dinner?</span> <span class="example-jp">（夕食に何が欲しいですか？）</span></li>
  <li><span class="example">Who is that girl over there?</span> <span class="example-jp">（あそこにいる女の子は誰ですか？）</span></li>
  <li><span class="example">Where did you go yesterday?</span> <span class="example-jp">（昨日どこに行きましたか？）</span></li>
  <li><span class="example">When does the movie start?</span> <span class="example-jp">（映画はいつ始まりますか？）</span></li>
  <li><span class="example">How many books do you have?</span> <span class="example-jp">（何冊本を持っていますか？）</span></li>
</ul>
<div class="tip-box"><h3>💡 疑問詞のあとの語順ルール</h3><p>疑問詞 + <strong>be動詞 + 主語</strong>（What is this? / Where are you?）<br>疑問詞 + <strong>do/does/did + 主語 + 動詞</strong>（What do you like? / Where did you go?）<br>疑問詞が主語のときは語順が変わらない（Who <strong>is</strong> that? / What <strong>happened</strong>?）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「What you like?」</strong> → do が必要。「What do you like?」が正解。</li>
  <li><strong>「Who is he?」と「Who is he?」の区別</strong> → be動詞の疑問文では主語と動詞が倒置。Who is he? が正しく、Who he is? は間違い。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/gimonhitei.html">疑問詞の練習問題を解く</a> か <a href="../test/gimonhitei_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "jyodosi.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">You must wear a seatbelt.</span> <span class="example-jp">（シートベルトを着用しなければならない）</span></li>
  <li><span class="example">We have to clean the classroom.</span> <span class="example-jp">（教室を掃除しなければならない）</span></li>
  <li><span class="example">May I use your phone?</span> <span class="example-jp">（電話を使ってもいいですか？）</span></li>
  <li><span class="example">You should see a doctor.</span> <span class="example-jp">（医者に診てもらうべきです）</span></li>
  <li><span class="example">You must not smoke here.</span> <span class="example-jp">（ここでタバコを吸ってはいけません）</span></li>
</ul>
<div class="highlight"><p><strong>助動詞の重要ポイント</strong><br>
✅ 助動詞のあとは必ず <strong>動詞の原形</strong><br>
✅ 否定文は <strong>助動詞 + not</strong><br>
✅ 疑問文は <strong>助動詞を文頭に</strong></p></div>
<div class="tip-box"><h3>💡 must not と don't have to の違い</h3><p><strong>must not</strong> = 禁止（してはいけない）<br><strong>don't have to</strong> = 必要ない（しなくてもよい）<br>You must not go.（行ってはいけない）← 禁止<br>You don't have to go.（行く必要はない）← 選択の自由</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I must to go.」</strong> → must のあとは動詞の原形。to は不要。</li>
  <li><strong>「must not」と「don't have to」の意味を逆に覚える</strong> → must not = 禁止、don't have to = 必要ない。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/jyodosi.html">助動詞の練習問題を解く</a> か <a href="../test/jyodosi_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "can.html": {
        "extra": """
<h2>📝 さらに詳しく</h2>
<div class="tip-box"><h3>💡 can の4つの意味</h3><p>①能力：I can swim.（泳げる）<br>②許可：Can I use your pen?（使ってもいい？）<br>③可能性：It can be true.（あり得る）<br>④依頼：Can you help me?（手伝ってくれる？）</p></div>
<div class="tip-box"><h3>💡 can の過去形 could</h3><p>can の過去形は could。<br>肯定：I could swim when I was five.（5歳のとき泳げた）<br>否定：I could not (couldn't) swim.（泳げなかった）<br>疑問：Could you swim?（泳げましたか？）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I can to swim.」</strong> → can のあとは動詞の原形。to は不要。</li>
  <li><strong>「I can swimming.」</strong> → can のあとは動詞の原形。ing はつけない。</li>
  <li><strong>「I can swim.」の否定を「I don't can swim.」としない</strong> → can の否定は can not (can't)。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/can.html">canの練習問題を解く</a> か <a href="../test/can_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "fukusu.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">There are five apples on the table.</span> <span class="example-jp">（テーブルの上に5つのりんごがある）</span></li>
  <li><span class="example">I have two brothers and one sister.</span> <span class="example-jp">（兄弟が2人と姉妹が1人います）</span></li>
  <li><span class="example">The children are playing in the park.</span> <span class="example-jp">（子供たちは公園で遊んでいます）</span></li>
  <li><span class="example">There are many sheep in the field.</span> <span class="example-jp">（畑にたくさんの羊がいます）</span></li>
</ul>
<div class="tip-box"><h3>💡 不規則な複数形の覚え方</h3><p>man → men（男性） / woman → women（女性） / child → children（子供）<br>foot → feet（足） / tooth → teeth（歯） / mouse → mice（ネズミ）<br>fish → fish（魚） / deer → deer（鹿） / sheep → sheep（羊）→ 変化しないグループ</p></div>
<div class="tip-box"><h3>💡 数えられる名詞と数えられない名詞</h3><p>可算名詞（数えられる）：book, cat, apple, student → 複数形あり<br>不可算名詞（数えられない）：water, money, information, news → 複数形なし。a piece of 〜 で数える。</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「childs」</strong> → children が正解。child → children の不規則変化。</li>
  <li><strong>「informations」</strong> → information は不可算名詞。複数形はない。</li>
  <li><strong>「two fish」と「two fishes」</strong> → 同じ種類なら fish、異なる種類なら fishes。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/fukusu.html">複数形の練習問題を解く</a> か <a href="../test/fukusu_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "futeisi2.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">It is difficult for me to solve this problem.</span> <span class="example-jp">（私にとってこの問題を解くことは難しい）</span></li>
  <li><span class="example">I don't know what to say.</span> <span class="example-jp">（何と言えばいいかわからない）</span></li>
  <li><span class="example">She asked me to help her.</span> <span class="example-jp">（彼女は私に助けるように頼んだ）</span></li>
  <li><span class="example">He was too tired to walk.</span> <span class="example-jp">（彼は疲れすぎて歩けなかった）</span></li>
</ul>
<div class="highlight"><p><strong>応用パターン集</strong><br>
It is ... for 人 to〜 = 人にとって〜することは...だ<br>
疑問詞 + to + 動詞の原形 = 〜すべきか（what to do, how to go）<br>
ask/tell 人 to〜 = 人に〜するように頼む/言う<br>
too ... to〜 = 〜すぎて...できない / ... enough to〜 = 〜するのに十分...だ</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「I don't know what do.」</strong> → 疑問詞+不定詞では to が必要。what to do が正解。</li>
  <li><strong>too...to 構文を否定文と混同</strong> → too tired to walk = 疲れすぎて歩けない（否定の意味があるが形は肯定）。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/futeisi.html">不定詞の練習問題を解く</a> か <a href="../test/futeisi_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
    "meirei.html": {
        "extra": """
<h2>📝 実践的な例文</h2>
<ul>
  <li><span class="example">Be quiet in the library.</span> <span class="example-jp">（図書館では静かにしなさい）</span></li>
  <li><span class="example">Don't forget your homework.</span> <span class="example-jp">（宿題を忘れてはいけません）</span></li>
  <li><span class="example">Please turn off the lights.</span> <span class="example-jp">（電気を消してください）</span></li>
  <li><span class="example">Let's play together.</span> <span class="example-jp">（一緒に遊びましょう）</span></li>
</ul>
<div class="tip-box"><h3>💡 丁寧な命令文の作り方</h3><p><strong>Please</strong> を文頭または文末に置く → Please sit down. / Sit down, please.<br><strong>Let's + 動詞の原形</strong> = 「〜しましょう」（勧誘）<br><strong>Why don't we〜?</strong> = 「〜しませんか？」（より丁寧な勧誘）</p></div>
<div class="mistake-section"><h2>⚠️ よくある間違い</h2><ul>
  <li><strong>「Don't to run.」</strong> → 否定命令文は Don't + 動詞の原形。Don't のあとに to は不要。</li>
  <li><strong>「No smoking.」と「Don't smoke.」の違い</strong> → No + 動名詞 = 掲示用（標識）。Don't + 動詞の原形 = 口頭での命令。</li>
</ul></div>
<div class="practice-link-box"><p>✅ <a href="../practice/meirei.html">命令文の練習問題を解く</a> か <a href="../test/meirei_test.html">確認テストに挑戦</a> しよう。</p></div>
"""
    },
}

if __name__ == "__main__":
    print("=== 最終徹底厚書 ===")
    for fname, data in pages.items():
        thicken(fname, data["extra"])
    print("=== 完了 ===")