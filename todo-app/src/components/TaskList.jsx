import React from 'react';

const TaskList = ({ tasks, completeTask, removeTask }) => {
  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id} style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
          {task.title}
          <button onClick={() => completeTask(task.id)}>Complete</button>
          <button onClick={() => removeTask(task.id)}>Remove</button>
        </li>
      ))}
    </ul>
  );
};

export default TaskList;
