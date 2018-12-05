export default {
  state: {
    chapters: [],
  },
  mutations: {
    setChapters(state, chapters) {
      state.chapters = chapters;
    },
  },
  actions: {
    fetchChapters()
  },
};
