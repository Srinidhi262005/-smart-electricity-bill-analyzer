import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE || '';

export const predictBill = (units, userId = 1) =>
  axios.post(`${API_BASE}/api/predict`, { units, user_id: userId });

export const analyzeUsage = (history) =>
  axios.post(`${API_BASE}/api/usage/analyze`, { history });

export const uploadOCR = (file) => {
  const data = new FormData();
  data.append('file', file);
  return axios.post(`${API_BASE}/api/ocr`, data, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const getSuggestions = (units, history = []) => {
  return axios.get(`${API_BASE}/api/suggestions`, {
    params: { units, history: history.join(',') },
  });
};

export const sendChat = (message, lang) =>
  axios.post(`${API_BASE}/api/chat`, { message, lang });
