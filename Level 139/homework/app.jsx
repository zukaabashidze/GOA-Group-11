import './App.css';
import React, { useState } from 'react';

export default function App() {
  const StudentList = () => {
    const [students, setStudents] = useState([
      { id: 1, name: 'ზუკა', grade: 999},
      { id: 2, name: 'babo', grade: 89 },
      { id: 3, name: 'ჯემალი', grade: 99 },
    ]);

    return (
      <ul>
        {students.map((student) => (
          <li key={student.id}>
            {student.name}: {student.grade}
          </li>
        ))}
      </ul>
    );
  };

  return (
    <div>
      <h1>Student List</h1>
      <StudentList />
    </div>
  );
}
