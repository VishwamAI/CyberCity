import React from 'react';
import { NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faTools, faComments } from '@fortawesome/free-solid-svg-icons';

const HomePage = () => {
  return (
    <div className="home-icons">
      <NavLink to="/" className="home-icon">
        <FontAwesomeIcon icon={faHome} />
        <span>Home</span>
      </NavLink>
      <NavLink to="/tools" className="home-icon">
        <FontAwesomeIcon icon={faTools} />
        <span>Tools</span>
      </NavLink>
      <NavLink to="/chat" className="home-icon">
        <FontAwesomeIcon icon={faComments} />
        <span>Chat</span>
      </NavLink>
      {/* Add additional icons as needed */}
    </div>
  );
};

export default HomePage;
