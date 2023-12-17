// App.js

import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faTimes } from '@fortawesome/free-solid-svg-icons';
import Sidebar from './components/Sidebar';
import Home from './components/Home';
import CyberTools from './components/CyberTools';
import Training from './components/Training';
import Research from './components/Research';
import CyberFrauds from './components/CyberFrauds';
import EventsEntertainments from './components/EventsEntertainments';
import JobCalendars from './components/JobCalendars';
import Chat from './components/Chat';
import './App.css';

const App = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(prev => !prev); // Toggle based on previous state
  };

  const toggleTheme = () => {
    setIsDarkMode(prev => !prev); // Toggle based on previous state
  };

  return (
    <Router>
      <div className={`App ${isDarkMode ? 'dark-theme' : ''}`}>
        <button className={`hamburger ${sidebarOpen ? 'closed' : ''}`} onClick={toggleSidebar} aria-label="Menu">
          <FontAwesomeIcon icon={sidebarOpen ? faTimes : faBars} />
        </button>
        <Sidebar 
          isDarkMode={isDarkMode}
          toggleTheme={toggleTheme}
          sidebarOpen={sidebarOpen}
          setSidebarOpen={setSidebarOpen}
        />
        <main className={`main ${sidebarOpen ? '' : 'shifted'}`}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/cybertools" element={<CyberTools />} />
            <Route path="/training" element={<Training />} />
            <Route path="/research" element={<Research />} />
            <Route path="/cyberfrauds" element={<CyberFrauds />} />
            <Route path="/events-entertainments" element={<EventsEntertainments />} />
            <Route path="/job-calendars" element={<JobCalendars />} />
            <Route path="/chat" element={<Chat />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
