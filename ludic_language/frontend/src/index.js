import React from 'react';
import {BrowserRouter as Router}  from "react-router-dom";
import ReactDOM from 'react-dom';
import './styles/index.css'
import App from './components/App';



ReactDOM.render(
    <React.StrictMode>
        <Router>
        <App />
        </Router>
    </React.StrictMode>,
    document.getElementById("root")
)