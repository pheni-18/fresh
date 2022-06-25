import React from 'react';
import { useArticle } from 'hooks/Article'

const Home: React.FC = () => {
  const { articleList } = useArticle();

  return (
      <React.Fragment>
        <h1>Home!</h1>
        {
          articleList && articleList.map((article) => {
            return (
              <p key={article.id}>{article.title}</p>
            );
          })
        }
			</React.Fragment>
  );
};

export default Home;
