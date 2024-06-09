import React, { useState, useEffect } from 'react';
import TodoList from './components/TodoList';
import TodoForm from './components/TodoForm';

function App() {
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        fetch('/api/todos')
            .then(response => response.json())
            .then(data => setTodos(data));
    }, []);

    const addTodo = (todo) => {
        fetch('/api/todos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(todo),
        })
            .then(response => response.json())
            .then(newTodo => setTodos([...todos, newTodo]));
    };

    const updateTodo = (id, updatedTodo) => {
        fetch(`/api/todos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedTodo),
        })
            .then(response => response.json())
            .then(updated => {
                const updatedTodos = todos.map(todo => todo.id === id ? updated : todo);
                setTodos(updatedTodos);
            });
    };

    const deleteTodo = (id) => {
        fetch(`/api/todos/${id}`, {
            method: 'DELETE',
        })
            .then(() => {
                const remainingTodos = todos.filter(todo => todo.id !== id);
                setTodos(remainingTodos);
            });
    };

    return (
        <div className="App">
            <TodoForm addTodo={addTodo} />
            <TodoList todos={todos} updateTodo={updateTodo} deleteTodo={deleteTodo} />
        </div>
    );
}

export default App;
