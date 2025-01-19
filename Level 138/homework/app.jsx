import {useState} from 'react'
import './App.css'

export default function App(){
    const [count, setCount] = useState(0)
    return(
        <div>
            <h1>Counter: {count}</h1>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <button onClick={() => setCount(count - 1)}>Decrement</button>
        </div>
    )
}