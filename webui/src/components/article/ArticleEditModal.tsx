import React from 'react';
import { Modal, Box, Button, Typography, TextField, Stack } from '@mui/material';
import { ArticleForm } from 'models';
import { useArticle } from 'hooks/Article'
import { useForm, SubmitHandler } from "react-hook-form";

export interface ArticleEditModalProps {
  open: boolean;
  onClose: () => void;
}

export const ArticleEditModal: React.FC<ArticleEditModalProps> = (props) => {
  const { open, onClose } = props;

  const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

  const { register, handleSubmit, watch, formState: { errors } } = useForm<ArticleForm>();

  const { createArticle, getArticleList } = useArticle();

  const onSubmit: SubmitHandler<ArticleForm> = React.useCallback(async (data) => {
    await createArticle(data);
    await getArticleList();
    onClose();
  }, [createArticle, onClose])

  return (
    <Modal
      open={open}
      onClose={onClose}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <Box sx={style}>
        <Typography id="modal-modal-title" variant="h6" component="h2">
          Article
        </Typography>
        <form>
          <Stack spacing={3}>
            <TextField required label="Title" {...register('title')} />
            <TextField required label="Body" {...register('body')} />
            <Button
              variant='outlined'
              onClick={handleSubmit(onSubmit)}
            >
              Submit
            </Button>
          </Stack>
        </form>
      </Box>
    </Modal>
  );
};
