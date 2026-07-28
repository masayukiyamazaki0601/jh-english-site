#!/usr/bin/env python3
"""残り記事を220-250行からさらに拡充"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def thicken(filename, extra):
    path = os.path.join(BASE, "grammar", filename)
    with open(path, "r") as f:
        content = f.read()
    lines = content.count("\n")
    if lines >= 800:
        print(f"  SKIP {filename} ({lines} lines)")
        return
    pos = content.rfind("</article>")
    if pos == -1:
        return
    after = content[pos:]
    new = content[:pos] + extra + "\n" + after
    with open(path, "w") as f:
        f.write(new)
    print(f"  OK {filename} ({lines} -> {new.count(chr(10))} lines)")

thicken("genkan1.html", """
<h2>現在完了（継続） 穴埋め問題（全20問）</h2>
<ol>
<li>I have lived here ( ) five years. → for</li>
<li>She has studied English ( ) 2020. → since</li>
<li>They have known each other ( ) childhood. → since</li>
<li>He has been sick ( ) Monday. → since</li>
<li>We have been friends ( ) ten years. → for</li>
<li>I have ( ) seen him since last week. → not</li>
<li>She has ( ) a teacher since 2019. → been</li>
<li>How long have you ( ) in Tokyo? → lived</li>
<li>( ) she been a teacher for 10 years? → Has</li>
<li>They have lived here ( ) 2015. → since</li>
<li>I have known him ( ) we were kids. → since</li>
<li>She has worked here ( ) three months. → for</li>
<li>We have ( ) to each other for years. → talked</li>
<li>He has had that car ( ) 2020. → since</li>
<li>I have been busy ( ) this morning. → since</li>
<li>They have ( ) married for 20 years. → been</li>
<li>She has studied French ( ) two years. → for</li>
<li>I have ( ) this book for a week. → had</li>
<li>We have lived in this town ( ) 2010. → since</li>
<li>How long has it been raining? —It has been raining ( ) 3 hours. → for</li>
</ol>
<h2>現在完了（継続） 最終チェックリスト</h2>
<ul>
<li>✅ for + 数字（期間の長さ）</li>
<li>✅ since + 時点（開始点）</li>
<li>✅ How long = 期間を尋ねる</li>
<li>✅ 過去形との区別（今も続いているか）</li>
<li>✅ 状態動詞（live, know, have, be）との相性</li>
</ul>
""")

thicken("genkan2.html", """
<h2>現在完了（経験） 穴埋め問題（全20問）</h2>
<ol>
<li>Have you ( ) been to Kyoto? → ever</li>
<li>I have ( ) eaten sushi. → never</li>
<li>She has been to the US ( ). → twice</li>
<li>I have seen this movie ( ). → before</li>
<li>He has ( ) been abroad. → never</li>
<li>( ) you ever eaten Italian food? → Have</li>
<li>I have ( ) to Kyoto twice. → been</li>
<li>She has ( ) to Kyoto. → gone</li>
<li>How many times have you ( ) to the US? → been</li>
<li>I have never ( ) to Hokkaido. → been</li>
<li>Have you ever ( ) natto? → eaten</li>
<li>She has never ( ) a snake. → seen</li>
<li>I have been to the US three ( ). → times</li>
<li>He has ( ) tried sushi. → never</li>
<li>Have you ever ( ) to a concert? → been</li>
<li>I have ( ) seen such a beautiful sunset. → never</li>
<li>She has been to that restaurant ( ). → before</li>
<li>Have you ( ) ridden a horse? → ever</li>
<li>I have never ( ) a kite. → flown</li>
<li>He has ( ) climbed Mt. Fuji. → never / already</li>
</ol>
<h2>現在完了（経験） 最終チェックリスト</h2>
<ul>
<li>✅ Have you ever + 過去分詞？「今までに〜したことがある？」</li>
<li>✅ I have never + 過去分詞「一度も〜したことがない」</li>
<li>✅ been to「行ったことがある」vs gone to「行ってしまった」</li>
<li>✅ 回数表現（once, twice, three times, many times）</li>
<li>✅ before「以前に」の位置は文末</li>
</ul>
""")

print("=== 最終拡充完了 ===")