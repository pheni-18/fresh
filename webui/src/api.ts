import axios from 'axios';
import { Todo, TodoForm } from 'models';

const client = axios.create({
  baseURL: 'http://localhost:1323',
  timeout: 3000,
  headers: {'Content-Type': 'application/json',}
});

export const apiFetchTodoList = async () => {
  return await client.get<Todo[]>('/todo');
};

export const apiCreateTodo = async (body: TodoForm) => {
  return await client.post<Todo>('/todo', body);
};

export const apiFetchTodo = async (id: number) => {
  return await client.get<Todo>(`/todo/${id}`);
};

export const apiUpdateTodo = async (id: number, body: TodoForm) => {
  return await client.patch<Todo>(`/todo/${id}`, body);
};

export const apiDeleteTodo = async (id: number) => {
  return await client.delete(`/todo/${id}`);
};
