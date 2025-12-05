import React, { useState } from "react";
import TodoInput from "./TodoInput";
import TodoList from "./TodoList";

function App() {
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    setTodos([...todos, text]);
  };

  const deleteTodo = (index) => {
    setTodos(todos.filter((_, i) => i !== index));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Simple Todo App</h2>

      <TodoInput addTodo={addTodo} />

      <TodoList todos={todos} deleteTodo={deleteTodo} />
    </div>
  );
}

export default App;
