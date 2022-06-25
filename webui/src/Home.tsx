import React from 'react';
import { useTodo } from 'hooks/Todo'

const Home: React.FC = () => {
  const { todoList } = useTodo();

  return (
      <React.Fragment>
        <h1>Home!</h1>
        {
          todoList && todoList.map((todo) => {
            return (
              <p>{todo.title}</p>
            );
          })
        }
			</React.Fragment>
  );
};

export default Home;
