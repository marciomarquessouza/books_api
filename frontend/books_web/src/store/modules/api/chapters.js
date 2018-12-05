import axios from 'axios';

const errors = [];
const url = 'http://127.0.0.1:8000';

export default {
  list: () => {
    axios.get(`${url}/chapter/`)
      .then(response => (response.data))
      .catch(e => (errors.push(e)));
  },
  get: (id) => {
    axios.get(`${url}/chapter/${id}`)
      .then(response => (response.data))
      .catch(e => (errors.push(e)));
  },
  listByBookId: (bookId) => {
    axios.get(`${url}/book/${bookId}/chapter/`)
      .then(response => (response.data))
      .catch(e => (errors.push(e)));
  },
  getByBookId: (bookId, chapterId) => {
    axios.get(`${url}/book/${bookId}/chapter/${chapterId}`)
      .then(response => (response.data))
      .catch(e => (errors.push(e)));
  },
};
