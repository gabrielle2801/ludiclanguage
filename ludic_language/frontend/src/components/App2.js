import React from 'react';
import {BrowserRouter, Routes, Route, useParams} from 'react-router-dom';
import '../styles/App.css';
import RecorderMessage2 from "./RecorderMessage2"; 



class App2 extends React.Component {

  render() {
    return (
      <div>
      <Routes>
        <Route exact path="/play_on/:id"  element={<RecorderMessage2 />}/> 
      </Routes>
  </div>
    );
  }
}
export default App2