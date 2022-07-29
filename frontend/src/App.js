
import './App.css';
import Header from './common/Header.js';
import CatalogPage from './catalog/CatalogPage';
import OrderPage from './ordering/OrderPage.js';
import Footer from './common/Footer.js';

import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Header />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<CatalogPage />} />
          <Route path="/order" element={<OrderPage />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;
