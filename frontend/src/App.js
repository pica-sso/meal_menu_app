import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './page/Home';
import CustomPage from './page/CustomPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/custum/url" element={<CustomPage />} />
      </Routes>
    </Router>
  );
}

export default App;
