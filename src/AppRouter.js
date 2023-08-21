import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App';
import SurveyComponent from './components/SurveyComponent';
import AnalyticsDashboard from './components/AnalyticsDashboard';

function AppRouter() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<App />} />
                <Route path="/survey" element={<SurveyComponent />} />
                <Route path="/analytics" element={<AnalyticsDashboard />} />
            </Routes>
        </Router>
    );
}

export default AppRouter;
