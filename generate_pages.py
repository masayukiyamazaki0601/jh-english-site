#!/usr/bin/env python3
"""中学英語サイトの全ページを一括生成するスクリプト"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

GRAMMAR_TEMPLATE = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 中学英語学習サイト</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="../index.html" class="header-logo">📚 中学英語<span>Lab</span></a>
    <nav class="header-nav">
      <a href="../index.html">ホーム</a>
      <a href="../index.html#grammar" class="active">文法解説</a>
      <a href="../index.html#practice">練習問題</a>
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
  <a href="../index.html#practice">練習問題</a>
  <a href="../test/index.html">確認テスト</a>
</div>
<div class="breadcrumb">
  <a href="../index.html">ホーム</a> > <a href="../index.html#grammar">文法解説</a> > {name}
</div>
<article class="grammar-detail">
  <span class="grade-badge badge {grade_class}">{grade}</span>
  <h1>{name}</h1>
  <p style="color: var(--gray-500); margin-bottom: 24px;">{subtitle}</p>
  {content}
</article>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>
<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>文法解説</h3><a href="be.html">be動詞</a><a href="ippan.html">一般動詞</a><a href="futeisi1.html">不定詞</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a></div>
    <div><h3>確認テスト</h3><a href="../test/be_test.html">be動詞 テスト</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''

PRACTICE_TEMPLATE = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} 練習問題 | 中学英語学習サイト</title>
<meta name="description" content="{name}の練習問題。{q_count}問の選択問題で実力をチェック。">
<link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="../index.html" class="header-logo">📚 中学英語<span>Lab</span></a>
    <nav class="header-nav">
      <a href="../index.html">ホーム</a>
      <a href="../index.html#grammar">文法解説</a>
      <a href="../index.html#practice" class="active">練習問題</a>
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
  <a href="../index.html#practice">練習問題</a>
  <a href="../test/index.html">確認テスト</a>
</div>
<div class="breadcrumb">
  <a href="../index.html">ホーム</a> > <a href="../index.html#practice">練習問題</a> > {name}
</div>
<div class="page-header">
  <h1>{name} 練習問題</h1>
  <p>全{q_count}問。選択肢から正しいものを選んでください。</p>
</div>
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
        <template v-else-if="answered[i]">❌ 不正解。正解は「{{{{ q.answer }}}}」です。 {{{{ q.explanation }}}}</template>
      </div>
    </div>
    <div style="text-align:center;margin:24px 0;">
      <button class="hero-btn primary" @click="resetAll" style="border:none;cursor:pointer;">🔄 やり直す</button>
    </div>
    <div class="test-result" v-if="allAnswered">
      <div class="score">{{{{ score }}}} / {q_count}</div>
      <div class="label">正答率</div>
      <div class="rank">{{{{ score === questions.length ? '🎉 満点！' : score >= 7 ? '👍 よくできました！' : '💪 もう一度！' }}}}</div>
    </div>
  </div>
</div>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>
<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/ippan.html">一般動詞</a></div>
    <div><h3>練習問題</h3><a href="be.html">be動詞</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const {{ createApp }} = Vue;
createApp({{
  data() {{
    return {{
      selected: {{}},
      answered: {{}},
      questions: {questions_js}
    }};
  }},
  computed: {{
    allAnswered() {{ return this.questions.every((_, i) => this.answered[i]); }},
    score() {{ return this.questions.filter((q, i) => this.selected[i] === q.answer).length; }}
  }},
  methods: {{
    selectAnswer(i, opt) {{ if (this.answered[i]) return; this.selected[i] = opt; this.answered[i] = true; }},
    resetAll() {{ this.selected = {{}}; this.answered = {{}}; }}
  }}
}}).mount('#practiceApp');
</script>
</body>
</html>'''

TEST_TEMPLATE = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} 確認テスト | 中学英語学習サイト</title>
<meta name="description" content="{name}の確認テスト。制限時間付きで実力をチェック。">
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
      <a href="index.html" class="active">確認テスト</a>
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
  <a href="index.html">確認テスト</a>
</div>
<div class="breadcrumb">
  <a href="../index.html">ホーム</a> > <a href="index.html">確認テスト</a> > {name}
</div>
<div class="page-header">
  <h1>{name} 確認テスト</h1>
  <p>制限時間5分。全{q_count}問。</p>
</div>
<div class="container">
  <div class="test-header">
    <div class="timer" id="timerDisplay">05:00</div>
    <div class="progress" id="progressDisplay">0 / {q_count} 問解答</div>
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
      <div class="score">{{{{ score }}}} / {q_count}</div>
      <div class="label">正答率 {{{{ Math.round(score / questions.length * 100) }}}}%</div>
      <div class="rank">{{{{ score === questions.length ? '🎉 満点！' : score >= 7 ? '👍 よくできました！' : '💪 もう一度！' }}}}</div>
      <div style="margin-top:16px;">
        <button class="hero-btn secondary" @click="retry" style="border:none;cursor:pointer;background:var(--gray-600);color:#fff;">🔄 もう一度</button>
      </div>
    </div>
  </div>
</div>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>
<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。</p></div>
    <div><h3>確認テスト</h3><a href="be_test.html">be動詞</a><a href="ippan_test.html">一般動詞</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const {{ createApp }} = Vue;
createApp({{
  data() {{
    return {{
      selected: {{}},
      finished: false,
      timerMinutes: 5, timerSeconds: 0, timerInterval: null, timeUp: false,
      questions: {questions_js}
    }};
  }},
  computed: {{
    allAnswered() {{ return this.questions.every((_, i) => this.selected[i]); }},
    score() {{ return this.questions.filter((q, i) => this.selected[i] === q.answer).length; }}
  }},
  methods: {{
    selectAnswer(i, opt) {{ if (this.finished || this.timeUp) return; this.selected[i] = opt; document.getElementById('progressDisplay').textContent = `${{{{Object.keys(this.selected).length}}}} / ${{{{this.questions.length}}}} 問解答`; }},
    submitTest() {{ if (!this.allAnswered) return; this.finished = true; if (this.timerInterval) clearInterval(this.timerInterval); }},
    retry() {{ this.selected = {{}}; this.finished = false; this.timeUp = false; this.timerMinutes = 5; this.timerSeconds = 0; document.getElementById('timerDisplay').textContent = '05:00'; document.getElementById('progressDisplay').textContent = '0 / {q_count} 問解答'; this.startTimer(); }},
    startTimer() {{ this.timerInterval = setInterval(() => {{ if (this.timerSeconds === 0) {{ if (this.timerMinutes === 0) {{ clearInterval(this.timerInterval); this.timeUp = true; this.finished = true; return; }} this.timerMinutes--; this.timerSeconds = 59; }} else {{ this.timerSeconds--; }} document.getElementById('timerDisplay').textContent = `${{{{String(this.timerMinutes).padStart(2, '0')}}}}:${{{{String(this.timerSeconds).padStart(2, '0')}}}}`; }}, 1000); }}
  }},
  mounted() {{ this.startTimer(); }}
}}).mount('#testApp');
</script>
</body>
</html>'''

def generate_grammar_pages():
    pages = [
        ("gimonhitei", "疑問文・否定文", "中学1年", "g1", "be動詞と一般動詞、それぞれの疑問文と否定文の作り方を比較学習。", """
<h2>be動詞の疑問文・否定文</h2>
<p>be動詞の否定文は be動詞のうしろに not を置く。疑問文は be動詞を文頭に置く。</p>
<div class="highlight"><p>否定文: 主語 + be動詞 + not + 〜<br>疑問文: Be動詞 + 主語 + 〜？</p></div>
<h2>一般動詞の疑問文・否定文</h2>
<p>一般動詞の否定文は do not (don't) を使う。疑問文は Do を文頭に置く。</p>
<div class="highlight"><p>否定文: 主語 + do not + 動詞の原形<br>疑問文: Do + 主語 + 動詞の原形？</p></div>
<div class="note"><strong>ちがいは？</strong><br>be動詞は「be動詞自身」を使って否定・疑問を作る。<br>一般動詞は「do」を使って否定・疑問を作る。これが最大の違い！</div>
"""),
        ("gimonsi", "疑問詞", "中学1年", "g1", "what, who, where, when, why, how を使った疑問文。", """
<h2>疑問詞とは？</h2>
<p>「何」「誰」「どこ」など、具体的な情報を尋ねるときに使う特別な疑問文。</p>
<table><tr><th>疑問詞</th><th>意味</th><th>例</th></tr>
<tr><td>what</td><td>何</td><td>What is this?</td></tr>
<tr><td>who</td><td>誰</td><td>Who is he?</td></tr>
<tr><td>where</td><td>どこ</td><td>Where are you?</td></tr>
<tr><td>when</td><td>いつ</td><td>When is your birthday?</td></tr>
<tr><td>why</td><td>なぜ</td><td>Why are you late?</td></tr>
<tr><td>how</td><td>どのように</td><td>How are you?</td></tr>
</table>
"""),
        ("meirei", "命令文", "中学1年", "g1", "「〜しなさい」「〜してはいけません」命令文・禁止文。", """
<h2>命令文の作り方</h2>
<p>動詞の原形で文を始める。主語は必要ない。</p>
<div class="highlight"><p>【公式】 動詞の原形 + 〜</p></div>
<ul><li>Sit down.（座りなさい）</li><li>Open your book.（本を開きなさい）</li></ul>
<h2>禁止文（否定の命令）</h2>
<p>Don't を文頭に置く。</p>
<div class="highlight"><p>【公式】 Don't + 動詞の原形 + 〜</p></div>
<ul><li>Don't run.（走ってはいけません）</li><li>Don't be late.（遅れてはいけません）</li></ul>
"""),
        ("santan", "三人称単数現在", "中学1年", "g1", "三単現のsの付け方・発音。疑問文・否定文ではdoesを使用。", """
<h2>三人称単数現在とは？</h2>
<p>主語が he, she, it（またはそれに相当する単数名詞）で、時制が現在のとき、動詞に s または es がつくルール。</p>
<div class="highlight"><p>【公式】 主語(3人称単数) + 動詞 + s/es + 〜</p></div>
<h2>s/esの付け方</h2>
<table><tr><th>ルール</th><th>例</th></tr>
<tr><td>ふつうは s をつける</td><td>play → plays, eat → eats</td></tr>
<tr><td>s,o,x,ch,sh で終わる → es</td><td>go → goes, watch → watches</td></tr>
<tr><td>子音字+y で終わる → yをiに変えてes</td><td>study → studies</td></tr>
</table>
<h2>疑問文・否定文</h2>
<p>三人称単数現在の疑問文・否定文は does / doesn't を使う。動詞は原形に戻す。</p>
<ul><li>He plays tennis. → He doesn't play tennis.</li><li>She studies English. → Does she study English?</li></ul>
"""),
        ("shinko", "現在進行形", "中学1年", "g1", "「〜している」be動詞 + 動詞のing形。", """
<h2>現在進行形とは</h2>
<p>「今まさに〜している」という動作の最中を表す。</p>
<div class="highlight"><p>【公式】 主語 + be動詞 + 動詞のing形 + 〜</p></div>
<ul><li>I am reading a book.（本を読んでいます）</li><li>She is watching TV.（テレビを見ています）</li></ul>
<h2>ing形の作り方</h2>
<table><tr><th>ルール</th><th>例</th></tr>
<tr><td>ふつうは ing をつける</td><td>play → playing</td></tr>
<tr><td>e で終わる → e をとって ing</td><td>make → making</td></tr>
<tr><td>短母音+子音字 → 子音を重ねて ing</td><td>run → running, swim → swimming</td></tr>
</table>
<h2>否定文・疑問文</h2>
<p>be動詞の否定・疑問と同じルール。</p>
<ul><li>He is not sleeping.（彼は寝ていません）</li><li>Are you studying?（勉強していますか？）</li></ul>
"""),
        ("can", "can（助動詞）", "中学1年", "g1", "「〜できる」の表現。canの使い方。", """
<h2>canの意味</h2>
<p>「〜できる」という能力や可能性を表す助動詞。</p>
<div class="highlight"><p>【公式】 主語 + can + 動詞の原形 + 〜</p></div>
<ul><li>I can swim.（泳げます）</li><li>She can speak English.（英語を話せます）</li></ul>
<h2>否定文・疑問文</h2>
<p>否定は can not (can't)、疑問は Can を文頭に。</p>
<ul><li>I can't play the piano.（ピアノを弾けません）</li><li>Can you help me?（手伝ってくれますか？）</li></ul>
"""),
        ("kako", "一般動詞の過去形", "中学1年", "g1", "動詞の過去形（ed形・不規則変化）。", """
<h2>過去形とは</h2>
<p>過去の出来事や状態を表す。動詞の形が変化する。</p>
<h2>規則動詞（ed形）</h2>
<table><tr><th>ルール</th><th>例</th></tr>
<tr><td>ふつうは ed をつける</td><td>play → played</td></tr>
<tr><td>e で終わる → d だけ</td><td>like → liked</td></tr>
<tr><td>子音字+y → yをiに変えてed</td><td>study → studied</td></tr>
</table>
<h2>不規則動詞（暗記必須）</h2>
<table><tr><th>原形</th><th>過去形</th></tr>
<tr><td>go</td><td>went</td></tr>
<tr><td>eat</td><td>ate</td></tr>
<tr><td>see</td><td>saw</td></tr>
<tr><td>do</td><td>did</td></tr>
<tr><td>have</td><td>had</td></tr>
<tr><td>make</td><td>made</td></tr>
</table>
<h2>否定文・疑問文</h2>
<p>過去形の否定・疑問は did / didn't を使う。動詞は原形に戻す。</p>
<ul><li>I didn't go to school.（学校に行きませんでした）</li><li>Did you eat breakfast?（朝食を食べましたか？）</li></ul>
"""),
        ("fukusu", "名詞の複数形", "中学1年", "g1", "複数形のルール。a/anの使い分け。", """
<h2>複数形の作り方</h2>
<table><tr><th>ルール</th><th>例</th></tr>
<tr><td>ふつうは s</td><td>cat → cats</td></tr>
<tr><td>s,o,x,ch,sh → es</td><td>box → boxes</td></tr>
<tr><td>子音+y → yをiに変えてes</td><td>baby → babies</td></tr>
<tr><td>f,fe → ves</td><td>knife → knives</td></tr>
</table>
<h2>不規則な複数形</h2>
<ul><li>child → children</li><li>man → men</li><li>woman → women</li><li>foot → feet</li><li>tooth → teeth</li><li>sheep → sheep</li></ul>
"""),
        ("daimeisi", "代名詞", "中学1年", "g1", "I, my, me, mine 人称代名詞の変化。", """
<h2>人称代名詞の変化表</h2>
<table><tr><th>主格(〜は)</th><th>所有格(〜の)</th><th>目的格(〜を)</th><th>所有代名詞(〜のもの)</th></tr>
<tr><td>I</td><td>my</td><td>me</td><td>mine</td></tr>
<tr><td>you</td><td>your</td><td>you</td><td>yours</td></tr>
<tr><td>he</td><td>his</td><td>him</td><td>his</td></tr>
<tr><td>she</td><td>her</td><td>her</td><td>hers</td></tr>
<tr><td>it</td><td>its</td><td>it</td><td>its</td></tr>
<tr><td>we</td><td>our</td><td>us</td><td>ours</td></tr>
<tr><td>they</td><td>their</td><td>them</td><td>theirs</td></tr>
</table>
<div class="note">「私の本」は my book。「私のもの」は mine。所有格+名詞 = 所有代名詞の関係を覚えよう。</div>
"""),
    ]
    
    for fname, name, grade, gclass, desc, content in pages:
        path = os.path.join(BASE, "grammar", f"{fname}.html")
        html = GRAMMAR_TEMPLATE.format(title=f"{name}の解説", description=desc, name=name, grade=grade, grade_class=gclass, subtitle=desc, content=content)
        with open(path, "w") as f:
            f.write(html)
        print(f"  grammar/{fname}.html")

generate_grammar_pages()
print("文法ページ生成完了")