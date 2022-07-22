
import './App.css';
import Header from './Header.js';
import Home from './Home.js';
import Order from './Order.js';
import Footer from './Footer.js';

import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/order" element={<Order />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
