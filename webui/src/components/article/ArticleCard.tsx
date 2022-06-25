import React from 'react';
import { Card, CardContent, Typography, CardActions, Button } from '@mui/material';
import { styled } from '@mui/system';

const StyledCard = styled(Card)({
  margin: 20,
  padding: 10,
});

export interface ArticleCardProps {
  title: string;
  body: string;
}

export const ArticleCard: React.FC<ArticleCardProps> = (props) => {
  const { title, body } = props;

  return (
    <StyledCard sx={{ minWidth: 275 }}>
      <CardContent>
        {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          Word of the Day
        </Typography> */}
        <Typography variant="h5" component="div">
          {title}
        </Typography>
        {/* <Typography sx={{ mb: 1.5 }} color="text.secondary">
          adjective
        </Typography> */}
        <Typography variant="body2">
          {body}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </StyledCard>
  );
};
