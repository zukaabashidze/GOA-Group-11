import './App.css';

export default function App() {
  const products = [
    { id: 1, name: 'Product 1', sales: 300 },
    { id: 2, name: 'Product 2', sales: 150 },
    { id: 3, name: 'Product 3', sales: 95 },
    { id: 4, name: 'Product 4', sales: 40 },
    { id: 5, name: 'Product 5', sales: 10 }
  ];

  const productList = () => {
    return (
      <div className="product-grid">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            {product.name}
          </div>
        ))}
      </div>
    );
  };

  console.log(productList());
}