import { Component } from '@angular/core';
import { TodoList } from './todo-list/todo-list';

@Component({
  selector: 'app-root',
  imports: [TodoList],
  template: '<app-todo-list />',
  styleUrl: './app.css'
})
export class App {}
