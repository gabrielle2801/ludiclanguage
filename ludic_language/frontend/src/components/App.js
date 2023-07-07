import React, { useEffect, useState,useReducer, useContext } from "react";
import {BrowserRouter, Routes, Route, useParams} from 'react-router-dom';
import '../styles/App.css';
import RecorderMessage from "./RecorderMessage"; 



class App extends React.Component {

  render() {
    return (
      <div>
      <Routes>
        <Route exact path="/play_on/:id"  element={<RecorderMessage />}/> 
      </Routes>
  </div>
    );
  }
}
export default App