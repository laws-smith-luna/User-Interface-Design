import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

interface Todo {
  text: string;
  done: boolean;
}

@Component({
  selector: 'app-todo-list',
  imports: [FormsModule],
  templateUrl: './todo-list.html',
  styleUrl: './todo-list.css',
})
export class TodoList {
  todos: Todo[] = [];
  newTodo = '';

  addTodo() {
    if (this.newTodo.trim()) {
      this.todos.push({ text: this.newTodo.trim(), done: false });
      this.newTodo = '';
    }
  }

  toggleTodo(todo: Todo) {
    todo.done = !todo.done;
  }

  deleteTodo(index: number) {
    this.todos.splice(index, 1);
  }

  get remaining(): number {
    return this.todos.filter(t => !t.done).length;
  }
}
