const App = () => {
    const [windowSize, setWindowSize] = React.useState({
      width: window.innerWidth,
      height: window.innerHeight,
    });
    const [bgColor, setBgColor] = React.useState('white');
    const [orientation, setOrientation] = React.useState(
      window.innerWidth > window.innerHeight ? 'ფანჯარა არის ჰორიზონტალური' : 'ფანჯარა არის ვერტიკალური'
    );

    React.useEffect(() => {
      const handleResize = () => {
        setWindowSize({
          width: window.innerWidth,
          height: window.innerHeight,
        });
        setOrientation(
          window.innerWidth > window.innerHeight ? 'ფანჯარა არის ჰორიზონტალური' : 'ფანჯარა არის ვერტიკალური'
        );
      };
  
      window.addEventListener('resize', handleResize);
      return () => {
        window.removeEventListener('resize', handleResize);
      };
    }, []);
  

    React.useEffect(() => {
      const timer = setInterval(() => {
        console.log('Loading...');
      }, 1000);
      return () => clearInterval(timer);
    }, []);
  
    const changeColor = () => {
      const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
      setBgColor(randomColor);
    };
  
    return (
      <div style={{ backgroundColor: bgColor, color: 'black', textAlign: 'center', height: '100vh' }}>
        <h1>React Tasks</h1>
  
        <div>
          <h2>Window Size</h2>
          <p>Width: {windowSize.width}px</p>
          <p>Height: {windowSize.height}px</p>
          <h3>{orientation}</h3>
        </div>
  
        <div>
          <button
            onClick={changeColor}
            style={{
              marginTop: '20px',
              padding: '10px 20px',
              fontSize: '16px',
              backgroundColor: 'black',
              color: 'white',
              border: 'none',
              cursor: 'pointer',
            }}
          >
            Change Background Color
          </button>
        </div>
      </div>
    );
  };
  
  ReactDOM.render(<App />, document.getElementById('root'));
  