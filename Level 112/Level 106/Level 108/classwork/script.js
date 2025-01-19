const div = document.querySelector('div');
const promise = fetch('https://jsonplaceholder.typicode.com/todos');
function renderItems(items) {
    div.innerHTML = '';
    
    for(let item of items) {
        div.innerHTML += `
            <div>
                <p>userId:${item.userId}</p>
                <h2>${item.title}</h2>
                <p>Completed: ${item.completed}</p>
            </div> 
        `
    }
}