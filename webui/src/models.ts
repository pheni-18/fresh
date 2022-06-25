export interface Todo {
  ID: number;
  CreatedAt: Date;
  UpdatedAt: Date;
  DeletedAt: Date;
  title: string;
  description: string;
  done: number;
}

export interface TodoForm {
  title: string;
  description: string;
  done: number;
}
