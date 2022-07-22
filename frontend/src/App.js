
import './App.css';
import Header from './common/Header.js';
import Catalog from './catalog/Catalog';
import OrderPage from './ordering/OrderPage.js';
import Footer from './common/Footer.js';

import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Catalog />} />
          <Route path="/order" element={<OrderPage />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
