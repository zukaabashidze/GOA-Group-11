import React from "react";

// 1. Rendering a List
const fruits = ["Apple", "Banana", "Cherry"];
const fruitList = fruits.map((fruit, index) => <li key={index}>{fruit}</li>);

// 2. Conditional Rendering
const isLoggedIn = true;

// 3. Dynamic Attributes
function ImageComponent() {
  const imageInfo = { src: "https://example.com/image.jpg", alt: "A beautiful scenery" };
  return <img src={imageInfo.src} alt={imageInfo.alt} />;
}

// 4. Inline Styles
const style = { backgroundColor: "blue", color: "white", padding: "10px" };

// 5. Rendering JSX from a Function
function GreetingMessage() {
  return <p>Hello, Alice!</p>;
}

// 6. Template Strings in JSX
const name = "John";
const age = 30;

// 7. Dynamic HTML Tag Rendering
const tagName = "h1";

// 8. Nested Map Rendering
const categories = [
  { name: "Fruit", items: ["Apple", "Banana", "Cherry"] },
  { name: "Vegetables", items: ["Carrot", "Broccoli", "Spinach"] }
];

// 9. Rendering a Table
const users = [
  { name: "zuka", age: 30 },
  { name: "jumberi", age: 25 },
  { name: "ivane ", age: 28 }
];

function App() {
  return (
    <div>
      {/* 2. Conditional Rendering */}
      {isLoggedIn ? <p>Welcome</p> : <p>Please log in</p>}
      
      {/* 1. Rendering a List */}
      <ul>{fruitList}</ul>

      {/* 3. Dynamic Attributes */}
      <ImageComponent />
      
      {/* 4. Inline Styles */}
      <div style={style}>This is a styled div</div>

      {/* 5. Rendering JSX from a Function */}
      <GreetingMessage />
      
      {/* 6. Template Strings in JSX */}
      <p>{`${name} is ${age} years old.`}</p>

      {/* 7. Dynamic HTML Tag Rendering */}
      {React.createElement(tagName, {}, "This is dynamic!")}
      
      {/* 8. Nested Map Rendering */}
      <div>
        {categories.map((category, index) => (
          <div key={index}>
            <h2>{category.name}</h2>
            <ul>
              {category.items.map((item, idx) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      {/* 9. Rendering a Table */}
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user, index) => (
            <tr key={index}>
              <td>{user.name}</td>
              <td>{user.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
