import React from 'react';
import { NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { 
  faHome, 
  faTools, 
  faChalkboardTeacher, 
  faSearch, 
  faUserSecret, 
  faCalendarAlt, 
  faCommentDots, 
  faSun, 
  faMoon 
} from '@fortawesome/free-solid-svg-icons';
import { faCog, faQuestionCircle } from '@fortawesome/free-solid-svg-icons'; // Import additional icons

const Sidebar = ({ isDarkMode, toggleTheme, sidebarOpen }) => {
  return (
      <div className={`sidebar ${!sidebarOpen ? 'closed' : ''}`}>

      <NavLink to="/" className="sidebar-item">
        <FontAwesomeIcon icon={faHome} /><span>Home</span>

      </NavLink>
      <NavLink to="/cybertools" className="sidebar-item">
        <FontAwesomeIcon icon={faTools} /><span>Cyber Tools</span>
      </NavLink>
      <NavLink to="/training" className="sidebar-item">
        <FontAwesomeIcon icon={faChalkboardTeacher} /><span>Training</span>
      </NavLink>
      <NavLink to="/research" className="sidebar-item">
        <FontAwesomeIcon icon={faSearch} /><span>Research</span>
      </NavLink>
      <NavLink to="/cyberfrauds" className="sidebar-item">
        <FontAwesomeIcon icon={faUserSecret} /><span>Cyber Frauds</span>
      </NavLink>
      <NavLink to="/events-entertainments" className="sidebar-item">
        <FontAwesomeIcon icon={faCalendarAlt} /><span>Events & Entertainment</span>
      </NavLink>
      <NavLink to="/job-calendars" className="sidebar-item">
        <FontAwesomeIcon icon={faCalendarAlt} /><span>Job Calendars</span>
      </NavLink>
      <NavLink to="/chat" className="sidebar-item">
        <FontAwesomeIcon icon={faCommentDots} /><span>Chat</span>
      </NavLink>

      {/* Theme toggle at the bottom */}
      <div className="sidebar-item theme-toggle" onClick={toggleTheme}>
        <FontAwesomeIcon icon={isDarkMode ? faSun : faMoon} /><span>Toggle Theme</span>
        <div className="bottom-nav">
        
      
      </div>
    </div>
    </div>
    
  );
};

export default Sidebar;
