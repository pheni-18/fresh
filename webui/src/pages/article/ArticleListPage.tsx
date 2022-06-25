import React from 'react';
import { useArticle } from 'hooks/Article'
import { Button, Grid, Paper } from '@mui/material'
import { ArticleEditModal } from 'components/article/ArticleEditModal';
import { ArticleCard } from 'components/article/ArticleCard';

import { styled } from '@mui/system';

const StyledGridContainer = styled(Grid)({
  padding: 50,
});

export interface ArticleListPageProps {};

export const ArticleListPage: React.FC<ArticleListPageProps> = (props) => {
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);

  const { articleList } = useArticle();

  const handleClick = React.useCallback(() => {
    setIsModalOpen(true);
  }, []);

  const handleModalClose = React.useCallback(() => {
    setIsModalOpen(false);
  }, []);

  return (
      <React.Fragment>
        <StyledGridContainer container spacing={2}>
          <Grid item xs={12}>
            <h1>ArticleList</h1>
          </Grid>
          <Grid item xs={12}>
            <Button
              variant='outlined'
              onClick={handleClick}
            >Create</Button>
            <Grid item xs={12}>
              {
                articleList && articleList.map((article) => {
                  return (
                    <div key={article.id}>
                      <ArticleCard
                        title={article.title}
                        body={article.body}
                      />
                    </div>
                  );
                })
              }
            </Grid>
          </Grid>
        </StyledGridContainer>
        <ArticleEditModal
          open={isModalOpen}
          onClose={handleModalClose}
        />
			</React.Fragment>
  );
};
