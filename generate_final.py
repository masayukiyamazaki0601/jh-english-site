#!/usr/bin/env python3
"""最終追加機能：リスニング・英作文・並べ替え・ダークモード・お問い合わせ・プライバシーポリシー"""
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
      <a href="../listening/index.html">リスニング</a>
      <a href="../test/index.html">確認テスト</a>
      <a href="../word/index.html">単語帳</a>
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
  <a href="../listening/index.html">リスニング練習</a>
  <a href="../test/index.html">確認テスト</a>
  <a href="../word/index.html">英単語帳</a>
  <a href="../verb/index.html">不規則動詞一覧</a>
  <a href="../exam/index.html">高校入試対策</a>
  <a href="../writing/index.html">英作文練習</a>
  <a href="../search.html">サイト内検索</a>
  <a href="../sitemap.html">サイトマップ</a>
</div>'''

FOOTER = '''<footer class="footer">
  <div class="footer-inner">
    <div><h3>📚 中学英語Lab</h3><p style="font-size:0.85rem;">中学生のための無料英語学習サイト。英文法・練習問題・確認テストで英語力を確実にアップ。</p></div>
    <div><h3>文法解説</h3><a href="../grammar/be.html">be動詞</a><a href="../grammar/futeisi1.html">不定詞</a><a href="../grammar/genkan1.html">現在完了</a><a href="../grammar/kankeisi1.html">関係代名詞</a></div>
    <div><h3>練習問題</h3><a href="../practice/be.html">be動詞</a><a href="../practice/futeisi.html">不定詞</a><a href="../practice/genkan.html">現在完了</a></div>
    <div><h3>確認テスト</h3><a href="../test/be_test.html">be動詞</a><a href="../test/futeisi_test.html">不定詞</a><a href="../test/genkan_test.html">現在完了</a></div>
    <div><h3>その他</h3><a href="../listening/index.html">リスニング</a><a href="../writing/index.html">英作文</a><a href="../word/index.html">単語帳</a><a href="../verb/index.html">不規則動詞</a><a href="../exam/index.html">入試対策</a><a href="../privacy.html">プライバシーポリシー</a><a href="../contact.html">お問い合わせ</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 中学英語Lab</div>
</footer>
</body>
</html>'''

def gen_listening():
    """リスニング練習ページ - Web Speech API で読み上げ"""
    html = HEADER.format(title="リスニング練習", desc="中学英語のリスニング練習。英文を聞いて意味を理解しよう。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > リスニング練習</div>
<div class="page-header">
  <h1>🎧 リスニング練習</h1>
  <p>英文をクリックすると音声が流れます。スピード調整も可能。</p>
</div>
<div class="container">
  <div style="text-align:center;margin-bottom:20px;">
    <label style="font-weight:600;margin-right:8px;">スピード:</label>
    <select id="rateSelect" style="padding:8px 16px;border-radius:8px;border:2px solid var(--gray-200);font-size:1rem;">
      <option value="0.5">0.5倍</option>
      <option value="0.75">0.75倍</option>
      <option value="1" selected>等倍</option>
      <option value="1.25">1.25倍</option>
      <option value="1.5">1.5倍</option>
    </select>
  </div>
  <div id="listenApp">
    <div class="grammar-grid">
      <div class="grammar-card" v-for="(item, i) in items" :key="i" @click="speak(item.en)" style="cursor:pointer;">
        <h3>{{ item.en }}</h3>
        <p v-if="item.show" style="color:var(--primary);font-weight:600;">{{ item.ja }}</p>
        <p v-else style="color:var(--gray-400);">👆 クリックで発音 + タップで和訳表示</p>
        <p style="color:var(--gray-500);font-size:0.8rem;margin-top:4px;">{{ item.category }}</p>
      </div>
    </div>
  </div>
</div>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>'''
    html += FOOTER
    html += '''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const { createApp } = Vue;
createApp({
  data() {
    return {
      items: [
        {en:"Good morning.", ja:"おはようございます。",category:"挨拶"},
        {en:"How are you?", ja:"元気ですか？",category:"挨拶"},
        {en:"I am fine, thank you.", ja:"はい、元気です。ありがとう。",category:"挨拶"},
        {en:"What is your name?", ja:"あなたの名前は何ですか？",category:"質問"},
        {en:"My name is Taro.", ja:"私の名前は太郎です。",category:"質問"},
        {en:"Where are you from?", ja:"どこから来ましたか？",category:"質問"},
        {en:"I am from Japan.", ja:"日本から来ました。",category:"質問"},
        {en:"How old are you?", ja:"何歳ですか？",category:"質問"},
        {en:"I am 12 years old.", ja:"12歳です。",category:"質問"},
        {en:"What time is it?", ja:"今何時ですか？",category:"質問"},
        {en:"It is eight o'clock.", ja:"8時です。",category:"質問"},
        {en:"What day is it today?", ja:"今日は何曜日ですか？",category:"質問"},
        {en:"It is Monday.", ja:"月曜日です。",category:"曜日"},
        {en:"I like cats.", ja:"猫が好きです。",category:"好き嫌い"},
        {en:"Do you like music?", ja:"音楽は好きですか？",category:"好き嫌い"},
        {en:"Yes, I do.", ja:"はい、好きです。",category:"好き嫌い"},
        {en:"I can swim.", ja:"泳げます。",category:"能力"},
        {en:"Can you play the piano?", ja:"ピアノを弾けますか？",category:"能力"},
        {en:"I have a dog.", ja:"犬を飼っています。",category:"所有"},
        {en:"She is my friend.", ja:"彼女は私の友達です。",category:"紹介"},
        {en:"This is a pen.", ja:"これはペンです。",category:"もの"},
        {en:"There is a cat under the table.", ja:"テーブルの下に猫がいます。",category:"存在"},
        {en:"I go to school by bus.", ja:"バスで学校に行きます。",category:"日常"},
        {en:"I eat breakfast at seven.", ja:"7時に朝食を食べます。",category:"日常"},
        {en:"She reads books every day.", ja:"彼女は毎日本を読みます。",category:"日常"},
        {en:"He is taller than me.", ja:"彼は私より背が高いです。",category:"比較"},
        {en:"I want to be a doctor.", ja:"医者になりたいです。",category:"将来"},
        {en:"I have been to Kyoto.", ja:"京都に行ったことがあります。",category:"経験"},
        {en:"If it rains, I will stay home.", ja:"雨が降れば、家にいます。",category:"条件"},
        {en:"Thank you very much.", ja:"どうもありがとう。",category:"感謝"},
      ].map(item => ({...item, show: false}))
    };
  },
  methods: {
    speak(text) {
      const item = this.items.find(i => i.en === text);
      if (item) item.show = !item.show;
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      const rate = document.getElementById('rateSelect').value;
      utterance.rate = parseFloat(rate);
      speechSynthesis.cancel();
      speechSynthesis.speak(utterance);
    }
  }
}).mount('#listenApp');
</script>
</body>
</html>'''
    os.makedirs(os.path.join(BASE, "listening"), exist_ok=True)
    path = os.path.join(BASE, "listening", "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  listening/index.html")

def gen_writing():
    """英作文練習ページ"""
    topics = [
        {"ja":"あなたの趣味について教えてください", "hint":"I like ~ / My hobby is ~", "keywords":"like, enjoy, play, read"},
        {"ja":"あなたの学校について説明してください", "hint":"My school is ~ / There are ~", "keywords":"school, teacher, student, building"},
        {"ja":"あなたの家族を紹介してください", "hint":"I have ~ / My father is ~", "keywords":"father, mother, brother, sister"},
        {"ja":"昨日したことについて書いてください", "hint":"I went to ~ / I ate ~ / I played ~", "keywords":"yesterday, went, ate, played, watched"},
        {"ja":"あなたの町の好きなところ", "hint":"There is/are ~ / I like ~ because", "keywords":"park, shop, station, river, mountain"},
        {"ja":"将来の夢について教えてください", "hint":"I want to be ~ / I want to ~", "keywords":"doctor, teacher, singer, pilot"},
        {"ja":"環境のためにできること", "hint":"We should ~ / It is important to ~", "keywords":"recycle, save, energy, water"},
        {"ja":"好きな季節とその理由", "hint":"I like ~ because ~", "keywords":"spring, summer, autumn, winter, weather"},
        {"ja":"休みの日にしたいこと", "hint":"I want to ~ / I am going to ~", "keywords":"visit, play, go, see, eat"},
        {"ja":"大切にしているもの", "hint":"My ~ is important because ~", "keywords":"gift, book, photo, friend, family"},
    ]
    
    html = HEADER.format(title="英作文練習", desc="中学英語の英作文練習。テーマに沿って英文を作成しよう。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > 英作文練習</div>
<div class="page-header">
  <h1>✍️ 英作文練習</h1>
  <p>テーマに沿って英文を作成しましょう。ヒントとキーワードを参考に。</p>
</div>
<div class="container">
  <div id="writingApp">
    <div class="question-card" v-for="(topic, i) in topics" :key="i">
      <div class="q-number">{{ i + 1 }}</div>
      <div class="q-text" style="font-size:1.1rem;font-weight:700;">{{ topic.ja }}</div>
      <div class="note" style="margin:12px 0;">
        <strong>💡 ヒント: </strong>{{ topic.hint }}<br>
        <strong>🔑 キーワード: </strong>{{ topic.keywords }}
      </div>
      <textarea class="q-input" rows="4" v-model="topic.answer" placeholder="ここに英文を書いてみよう..." style="resize:vertical;"></textarea>
      <div style="margin-top:8px;text-align:right;color:var(--gray-500);font-size:0.85rem;">
        文字数: {{ topic.answer.length }}
      </div>
    </div>
    <div style="text-align:center;margin:24px 0;">
      <button class="hero-btn primary" @click="clearAll" style="border:none;cursor:pointer;">🔄 すべてクリア</button>
    </div>
  </div>
</div>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>'''
    html += FOOTER
    html += '''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const { createApp } = Vue;
createApp({
  data() {
    return {
      topics: ''' + json.dumps([{**t, "answer":""} for t in topics], ensure_ascii=False) + '''
    };
  },
  methods: {
    clearAll() {
      this.topics.forEach(t => t.answer = "");
    }
  }
}).mount('#writingApp');
</script>
</body>
</html>'''
    os.makedirs(os.path.join(BASE, "writing"), exist_ok=True)
    path = os.path.join(BASE, "writing", "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  writing/index.html")

def gen_darkmode_css():
    """ダークモードCSSを追記"""
    css_path = os.path.join(BASE, "css", "style.css")
    dark_css = '''
/* ===== Dark Mode ===== */
@media (prefers-color-scheme: dark) {
  :root {
    --gray-50: #0f172a;
    --gray-100: #1e293b;
    --gray-200: #334155;
    --gray-300: #475569;
    --gray-400: #94a3b8;
    --gray-500: #cbd5e1;
    --gray-600: #e2e8f0;
    --gray-700: #f1f5f9;
    --gray-800: #f8fafc;
    --gray-900: #ffffff;
    --primary-light: #1e3a5f;
    --shadow: 0 1px 3px rgba(0,0,0,0.3);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.3);
  }
  .header { background: #1e293b; }
  .grammar-detail, .question-card, .test-header, .test-result, .stat-card { background: #1e293b; }
  .grammar-card { background: #1e293b; }
  .hero { background: linear-gradient(135deg, #1e40af 0%, #5b21b6 100%); }
  .grade-tab { background: #334155; border-color: #475569; color: var(--gray-300); }
  .grade-tab.active { background: var(--primary); border-color: var(--primary); color: #fff; }
  .q-option { border-color: #475569; }
  .q-option:hover { border-color: var(--primary); }
  .highlight { background: #1e3a5f; }
  .note { background: #3d2e0a; }
  .page-header { background: #1e293b; border-color: #334155; }
  .ad-placeholder { background: #1e293b; border-color: #334155; color: #64748b; }
  .breadcrumb { color: #94a3b8; }
  .footer { background: #020617; }
}
/* Dark mode toggle */
.dark-toggle {
  display: flex; align-items: center; gap: 8px;
  cursor: pointer; padding: 4px 12px;
  border-radius: 999px; border: 2px solid var(--gray-200);
  background: var(--gray-100); font-size: 0.85rem;
  transition: all 0.3s;
}
.dark-toggle:hover { border-color: var(--primary); }
'''
    with open(css_path, "a") as f:
        f.write(dark_css)
    print(f"  css/style.css updated (dark mode)")

def gen_search():
    """サイト内検索ページ"""
    # 全ページのタイトルを収集
    pages = [
        ("index.html", "ホーム - 中学英語Lab"),
        ("grammar/be.html", "be動詞の解説"),
        ("grammar/ippan.html", "一般動詞の解説"),
        ("grammar/gimonhitei.html", "疑問文・否定文の解説"),
        ("grammar/gimonsi.html", "疑問詞の解説"),
        ("grammar/meirei.html", "命令文の解説"),
        ("grammar/santan.html", "三人称単数現在の解説"),
        ("grammar/shinko.html", "現在進行形の解説"),
        ("grammar/can.html", "canの解説"),
        ("grammar/kako.html", "一般動詞の過去形の解説"),
        ("grammar/fukusu.html", "名詞の複数形の解説"),
        ("grammar/daimeisi.html", "代名詞の解説"),
        ("grammar/bekako.html", "be動詞の過去形の解説"),
        ("grammar/kakosin.html", "過去進行形の解説"),
        ("grammar/mirai.html", "未来形の解説"),
        ("grammar/doumei.html", "動名詞の解説"),
        ("grammar/futeisi1.html", "不定詞（基本）の解説"),
        ("grammar/jyodosi.html", "助動詞の解説"),
        ("grammar/hikaku1.html", "比較の解説"),
        ("grammar/there.html", "there is構文の解説"),
        ("grammar/setuzoku.html", "接続詞の解説"),
        ("grammar/ukemi.html", "受け身の解説"),
        ("grammar/genkan1.html", "現在完了（継続）の解説"),
        ("grammar/genkan2.html", "現在完了（経験）の解説"),
        ("grammar/genkan3.html", "現在完了（完了）の解説"),
        ("grammar/genkanSinkokei.html", "現在完了進行形の解説"),
        ("grammar/futeisi2.html", "不定詞（応用）の解説"),
        ("grammar/bunsi.html", "分詞の解説"),
        ("grammar/kansetu.html", "間接疑問の解説"),
        ("grammar/kankeisi1.html", "関係代名詞の解説"),
        ("grammar/kateiho.html", "仮定法の解説"),
        ("grammar/genkeiFuteisi.html", "原形不定詞の解説"),
        ("word/index.html", "英単語帳"),
        ("verb/index.html", "不規則動詞一覧"),
        ("exam/index.html", "高校入試対策"),
        ("test/index.html", "確認テスト一覧"),
        ("listening/index.html", "リスニング練習"),
        ("writing/index.html", "英作文練習"),
        ("sitemap.html", "サイトマップ"),
        ("privacy.html", "プライバシーポリシー"),
        ("contact.html", "お問い合わせ"),
    ]
    pages_json = json.dumps(pages, ensure_ascii=False)
    
    html = HEADER.format(title="サイト内検索", desc="中学英語学習サイトのサイト内検索。")
    html += f'''<div class="breadcrumb"><a href="../index.html">ホーム</a> > サイト内検索</div>
<div class="page-header">
  <h1>🔍 サイト内検索</h1>
  <p>キーワードを入力してページを検索できます。</p>
</div>
<div class="container">
  <div id="searchApp">
    <div style="max-width:600px;margin:0 auto 32px;">
      <input type="text" v-model="query" @input="search" placeholder="検索キーワードを入力（例: be動詞、不定詞、現在完了）"
        style="width:100%;padding:16px 20px;border:2px solid var(--gray-200);border-radius:12px;font-size:1.1rem;outline:none;transition:0.2s;font-family:var(--font);"
        :style="dynamicStyle">
      <p style="text-align:center;color:var(--gray-500);margin-top:8px;font-size:0.9rem;">{{ resultCount }} 件見つかりました</p>
    </div>
    <div class="grammar-grid">
      <a v-for="page in filteredPages" :key="page[0]" :href="page[0]" class="grammar-card">
        <h3>{{{{ page[1] }}}}</h3>
      </a>
    </div>
    <p v-if="query && filteredPages.length === 0" style="text-align:center;color:var(--gray-400);padding:40px;">
      該当するページが見つかりませんでした。別のキーワードで試してください。
    </p>
  </div>
</div>
<div class="ad-placeholder">広告スペース（AdSense設置予定）</div>'''
    html += FOOTER
    html += f'''
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
const pages = {pages_json};
const {{ createApp }} = Vue;
createApp({{
  data() {{
    return {{ query: '', filtered: [] }};
  }},
  computed: {{
    filteredPages() {{
      if (!this.query) return [];
      const q = this.query.toLowerCase();
      return pages.filter(p => p[1].toLowerCase().includes(q) || p[0].toLowerCase().includes(q));
    }},
    resultCount() {{
      return this.query ? this.filteredPages.length : 0;
    }}
  }},
  methods: {{
    search() {{ /* reactive */ }}
  }}
}}).mount('#searchApp');
</script>
</body>
</html>'''
    path = os.path.join(BASE, "search.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  search.html")

def gen_privacy():
    """プライバシーポリシー"""
    html = HEADER.format(title="プライバシーポリシー", desc="中学英語学習サイトのプライバシーポリシー。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > プライバシーポリシー</div>
<article class="grammar-detail">
  <h1>🔒 プライバシーポリシー</h1>
  <p style="color:var(--gray-500);margin-bottom:24px;">当サイトのプライバシーポリシーについて説明します。</p>
  <h2>個人情報の収集について</h2>
  <p>当サイトでは、お問い合わせフォームを通じてお名前とメールアドレスを収集することがあります。これらの情報はお問い合わせへの返信のみに使用し、第三者に提供することはありません。</p>
  <h2>アクセス解析ツールについて</h2>
  <p>当サイトでは、Googleによるアクセス解析ツール「Googleアナリティクス」を使用しています。Googleアナリティクスはデータの収集のためにCookieを使用します。このデータは匿名で収集されており、個人を特定するものではありません。</p>
  <h2>広告について</h2>
  <p>当サイトでは、Googleアドセンスなどの広告サービスを利用する予定です。広告配信事業者は、ユーザーの興味に応じた広告を表示するためにCookieを使用することがあります。</p>
  <h2>免責事項</h2>
  <p>当サイトのコンテンツ・情報について、可能な限り正確な情報を提供するよう努めていますが、正確性や安全性を保証するものではありません。当サイトの情報を用いて行う一切の行為について、責任を負いかねますのでご了承ください。</p>
  <h2>お問い合わせ</h2>
  <p>プライバシーポリシーに関するお問い合わせは、<a href="../contact.html">お問い合わせフォーム</a>からお願いいたします。</p>
  <p style="color:var(--gray-500);margin-top:32px;">制定日: 2026年7月27日</p>
</article>'''
    html += FOOTER
    path = os.path.join(BASE, "privacy.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  privacy.html")

def gen_contact():
    """お問い合わせページ（メールリンク）"""
    html = HEADER.format(title="お問い合わせ", desc="中学英語学習サイトのお問い合わせページ。")
    html += '''<div class="breadcrumb"><a href="../index.html">ホーム</a> > お問い合わせ</div>
<article class="grammar-detail">
  <h1>📧 お問い合わせ</h1>
  <p style="color:var(--gray-500);margin-bottom:24px;">ご質問・ご要望は以下のメールアドレスまでお気軽にご連絡ください。</p>
  <div class="highlight" style="text-align:center;padding:40px;">
    <p style="font-size:1.3rem;font-weight:700;color:var(--primary);">contact@jh-english-lab.example.com</p>
    <p style="color:var(--gray-500);margin-top:12px;">お問い合わせ内容を明記の上、上記アドレスまでメールをお送りください。<br>返信までに数日かかる場合がございます。</p>
  </div>
  <h2>よくある質問（FAQ）</h2>
  <h3>Q: このサイトは本当に無料ですか？</h3>
  <p>A: はい、完全無料です。登録も不要です。</p>
  <h3>Q: 商用利用は可能ですか？</h3>
  <p>A: 現在は個人学習目的でのご利用をお願いしております。商用利用をご希望の場合は別途ご連絡ください。</p>
  <h3>Q: 間違いを発見しました</h3>
  <p>A: お手数ですが、お問い合わせフォームよりご連絡いただけると幸いです。迅速に修正いたします。</p>
</article>'''
    html += FOOTER
    path = os.path.join(BASE, "contact.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  contact.html")

def update_top_header():
    """トップページのヘッダーにダークモードボタンとリスニング・検索リンク追加"""
    path = os.path.join(BASE, "index.html")
    with open(path, "r") as f:
        content = f.read()
    
    # ヘッダーナビ更新
    new_nav = '''      <a href="index.html" class="active">ホーム</a>
      <a href="#grammar">文法解説</a>
      <a href="#practice">練習問題</a>
      <a href="listening/index.html">リスニング</a>
      <a href="test/index.html">確認テスト</a>
      <a href="search.html">検索</a>'''
    old_nav = '''      <a href="index.html" class="active">ホーム</a>
      <a href="#grammar">文法解説</a>
      <a href="#practice">練習問題</a>
      <a href="test/index.html">確認テスト</a>'''
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
    
    # モバイルナビ更新
    old_mobile = '''  <a href="index.html">ホーム</a>
  <a href="#grammar">文法解説</a>
  <a href="#practice">練習問題</a>
  <a href="test/index.html">確認テスト</a>'''
    new_mobile = '''  <a href="index.html">ホーム</a>
  <a href="#grammar">文法解説</a>
  <a href="#practice">練習問題</a>
  <a href="listening/index.html">リスニング練習</a>
  <a href="test/index.html">確認テスト</a>
  <a href="word/index.html">英単語帳</a>
  <a href="writing/index.html">英作文練習</a>
  <a href="exam/index.html">高校入試対策</a>
  <a href="search.html">サイト内検索</a>
  <a href="sitemap.html">サイトマップ</a>'''
    if old_mobile in content:
        content = content.replace(old_mobile, new_mobile)
    
    # フッター更新
    old_footer = '''  <a href="word/index.html">英単語帳</a>
      <a href="verb/index.html">不規則動詞一覧</a>
      <a href="exam/index.html">高校入試対策</a>
      <a href="sitemap.html">サイトマップ</a>'''
    new_footer = '''  <a href="word/index.html">英単語帳</a>
      <a href="verb/index.html">不規則動詞一覧</a>
      <a href="listening/index.html">リスニング</a>
      <a href="writing/index.html">英作文練習</a>
      <a href="exam/index.html">高校入試対策</a>
      <a href="search.html">検索</a>
      <a href="sitemap.html">サイトマップ</a>
      <a href="privacy.html">プライバシーポリシー</a>
      <a href="contact.html">お問い合わせ</a>'''
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
    
    with open(path, "w") as f:
        f.write(content)
    print(f"  index.html updated (nav + footer)")

if __name__ == "__main__":
    print("=== リスニング練習 ===")
    gen_listening()
    print("=== 英作文練習 ===")
    gen_writing()
    print("=== ダークモードCSS ===")
    gen_darkmode_css()
    print("=== サイト内検索 ===")
    gen_search()
    print("=== プライバシーポリシー ===")
    gen_privacy()
    print("=== お問い合わせ ===")
    gen_contact()
    print("=== トップページ更新 ===")
    update_top_header()
    print("=== 完了 ===")