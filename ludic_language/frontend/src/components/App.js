import React, { useEffect, useState,useReducer, useContext } from "react";
import {BrowserRouter, Routes, Route, useParams} from 'react-router-dom';
import '../styles/App.css';
import RecorderMessage from "./RecorderMessage"; 



class App extends React.Component {
  constructor() {
    super();

    this.state = {
      score: 0,
      gameOver: true
      
    };

    this.initCards = this.initCards.bind(this);
    this.restartGame = this.restartGame.bind(this);
  }

  initCards() {
    this.setState({
      score: 0,
      gameOver: false
    });
  }

  restartGame(turns) {
    const score = Math.round(120 / turns * 100);

    this.setState({
      score: score,
      gameOver: true
    });
  }

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