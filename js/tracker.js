// 学習進捗トラッカー - localStorage で学習記録を管理
const StudyTracker = {
  STORAGE_KEY: 'jh-english-progress',
  
  init() {
    if (!localStorage.getItem(this.STORAGE_KEY)) {
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify({
        completedLessons: [],
        quizScores: {},
        lastStudyDate: null,
        streak: 0
      }));
    }
  },
  
  getData() {
    return JSON.parse(localStorage.getItem(this.STORAGE_KEY));
  },
  
  saveData(data) {
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
  },
  
  markLessonComplete(lessonId, lessonName) {
    const data = this.getData();
    if (!data.completedLessons.find(l => l.id === lessonId)) {
      data.completedLessons.push({ id: lessonId, name: lessonName, date: new Date().toISOString() });
    }
    this.updateStreak(data);
    this.saveData(data);
  },
  
  saveQuizScore(topic, score, total) {
    const data = this.getData();
    if (!data.quizScores[topic] || data.quizScores[topic].score < score) {
      data.quizScores[topic] = { score, total, date: new Date().toISOString() };
    }
    this.updateStreak(data);
    this.saveData(data);
  },
  
  updateStreak(data) {
    const today = new Date().toDateString();
    if (data.lastStudyDate !== today) {
      const yesterday = new Date(Date.now() - 86400000).toDateString();
      if (data.lastStudyDate === yesterday) {
        data.streak = (data.streak || 0) + 1;
      } else {
        data.streak = 1;
      }
      data.lastStudyDate = today;
    }
  },
  
  getProgress() {
    const data = this.getData();
    const totalLessons = 34;
    const completed = data.completedLessons.length;
    return {
      completedLessons: completed,
      totalLessons: totalLessons,
      percentage: Math.round(completed / totalLessons * 100),
      streak: data.streak || 0,
      quizScores: data.quizScores,
      lastStudyDate: data.lastStudyDate
    };
  },
  
  resetProgress() {
    if (confirm('学習記録をすべてリセットしますか？')) {
      localStorage.removeItem(this.STORAGE_KEY);
      this.init();
      return true;
    }
    return false;
  }
};

// 自動初期化
StudyTracker.init();