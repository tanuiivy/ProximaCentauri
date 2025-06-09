import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AuthForm from "./pages/AuthForm.jsx";
import Dashboard from './pages/Dashboard.jsx';
import Groups from './pages/Groups.jsx';
import Transaction from './pages/Transaction.jsx';
import Profile from './pages/Profile.jsx';
import NavBar from './components/NavBar.jsx';

function App() {
  const WithNav = ({Component}) => (
    <div className="dashboard">
      <NavBar />
      <main className="main-content">
        <Component />
      </main>
    </div>
  );
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AuthForm />} />
        <Route path="/dashboard" element={<WithNav Component={Dashboard} />} />
        <Route path="/groups" element={<WithNav Component={Groups} />} />
        <Route path="/transaction" element={<WithNav Component={Transaction} />} />
        <Route path="/profile" element={<WithNav Component={Profile} />} />
      </Routes>
    </Router>
  );
}

export default App;
