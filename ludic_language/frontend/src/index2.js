import React from 'react';
import {BrowserRouter as Router}  from "react-router-dom";
import ReactDOM from 'react-dom';
import App2 from './components/App2';



ReactDOM.render(
    <React.StrictMode>
        <Router>
        <App2 />
        </Router>
    </React.StrictMode>,
    document.getElementById("root2"))