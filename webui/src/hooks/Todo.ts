import React from 'react';
import { apiFetchTodoList, apiCreateTodo, apiFetchTodo, apiUpdateTodo, apiDeleteTodo } from 'api';
import { Todo, TodoForm } from 'models';

export const useTodo = () => {
  const [todoList, setTodoList] = React.useState([] as Todo[] | undefined);

  const getTodoList = async () => {
    try {
      const { data } = await apiFetchTodoList();
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  React.useEffect(() => {
    const results = getTodoList();
    results.then(todoList => {
      setTodoList(todoList);
    });
  }, []);

  const createTodo = async (todo: TodoForm) => {
    try {
      const { data } = await apiCreateTodo(todo);
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const getTodo = async (id: number) => {
    try {
      const { data } = await apiFetchTodo(id);
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const updateTodo = async (id: number, todo: TodoForm) => {
    try {
      const { data } = await apiUpdateTodo(id, todo);
      return data;
    } catch (e) {
      console.log(e);
    }
  };

  const deleteTodo = async (id: number) => {
    try {
      await apiDeleteTodo(id);
    } catch (e) {
      console.log(e);
    }
  };

  return {
    todoList
  };
};
