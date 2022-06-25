import axios from 'axios';
import { Article, ArticleForm } from 'models';

const client = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 3000,
  headers: {'Content-Type': 'application/json',}
});

const prefix = '/articles'

export const apiFetchArticleList = async () => {
  return await client.get<Article[]>(`${prefix}/`);
};

export const apiCreateArticle = async (body: ArticleForm) => {
  return await client.post<Article>(`${prefix}/`, body);
};

export const apiFetchArticle = async (id: number) => {
  return await client.get<Article>(`${prefix}/${id}`);
};

export const apiUpdateArticle = async (id: number, body: ArticleForm) => {
  return await client.patch<Article>(`${prefix}/${id}`, body);
};

export const apiDeleteArticle = async (id: number) => {
  return await client.delete(`${prefix}/${id}`);
};
