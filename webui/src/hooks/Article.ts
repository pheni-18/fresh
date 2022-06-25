import React from 'react';
import { apiFetchArticleList, apiCreateArticle, apiFetchArticle, apiUpdateArticle, apiDeleteArticle } from 'api';
import { Article, ArticleForm } from 'models';

export const useArticle = () => {
  const [articleList, setArticleList] = React.useState([] as Article[] | undefined);

  const getArticleList = async () => {
    try {
      const { data } = await apiFetchArticleList();
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  React.useEffect(() => {
    const results = getArticleList();
    results.then(articleList => {
      setArticleList(articleList);
    });
  }, []);

  const createArticle = async (article: ArticleForm) => {
    try {
      const { data } = await apiCreateArticle(article);
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const getArticle = async (id: number) => {
    try {
      const { data } = await apiFetchArticle(id);
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const updateArticle = async (id: number, article: ArticleForm) => {
    try {
      const { data } = await apiUpdateArticle(id, article);
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const deleteArticle = async (id: number) => {
    try {
      await apiDeleteArticle(id);
    } catch (e) {
      console.log(e);
    }
  };

  return {
    articleList,
    createArticle,
    getArticleList,
  };
};
