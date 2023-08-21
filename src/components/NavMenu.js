// import { Button } from '@mui/material';
import React from 'react';
import './NavMenu.css';
import { useNavigate } from 'react-router';
function NavMenu() {
  
  const navigate = useNavigate();
    const navigateToLogin = () => {
    navigate('/');
  };
    const navigateToAnalytics = () => {
    navigate('/analytics');
  };
    const navigateToSurvey = () => {
    navigate('/survey');
  };

  return (
    <div className = "navSection">
    <div className = "logoSection">
        <h2> Citizen . Council . Connect</h2>
    </div>
    <div className = "menuItemsBox">
      <a  href="#home" className = "menuItems" onClick={navigateToLogin}>
        Home
      </a>
      <a href="#dashboard" className = "menuItems" onClick={navigateToAnalytics}>
        AnalyticsDashboard
      </a>
      <a href="#survey" className = "menuItems" onClick={navigateToSurvey}>
        Survey
      </a>
    </div>
  </div>
  );
}

export default NavMenu;
