import React, {useState, useEffect, useContext } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import MicRecorder from 'mic-recorder-to-mp3';
import withRouter from './withRouter';
import '../styles/App.css';
import '../styles/RecorderMessage.css'
import axios from 'axios';
import Cookies from 'js-cookie';

const Mp3Recorder = new MicRecorder({ bitRate: 128 });


class RecorderMessage2 extends React.Component {
 
  constructor(props){
    super(props);
    this.state = {
      isRecording: false,
      blobURL: '',
      isBlocked: false,
    };
    this.resetPlayArea = this.resetPlayArea.bind(this);
  }

  resetPlayArea() {
    this.props.onGameOver(this.state.turns);

    this.setState({
      tiles: [],
      turns: 0,
      activeTile: null
    });
  }

  start = () => {
    console.log("start recorder")
    if (this.state.isBlocked) {
      console.log('Permission Denied');
    } else {
      Mp3Recorder
        .start()
        .then(() => {
          this.setState({ isRecording: true });
        }).catch((e) => console.error(e));
    }
  };

  stop = () => {
    Mp3Recorder
      .stop()
      .getMp3()
      .then(([buffer, blob]) => {
        const blobURL = URL.createObjectURL(blob)
        var wavfromblob = new File([blob], "incomingaudioclip.wav");
        console.log(wavfromblob)
        const blobmp3 = new Blob();
        this.setState({ blobURL, isRecording: false });
        this.sendAudioFile(wavfromblob);
      }).catch((e) => console.log(e));
  };

  sendAudioFile = (url) => {
    const data = new FormData();
    data.append("audio", url);
    data.append('exercise', this.props.params.id)
    
    console.log(data)
    return axios
      .post("http://127.0.0.1:8000/play_on/", data, {
        headers: {
          "content-Type": "multipart/form-data",
          'X-CSRFToken':Cookies.get('csrftoken'),
        },
      })
      .then((res) => {
        console.log(res);
        return res;
      })
  }

  componentDidMount() {
    navigator.mediaDevices.getUserMedia({ audio: true },
      () => {
        console.log('Permission Granted');
        this.setState({ isBlocked: false });
      },
      () => {
        console.log('Permission Denied');
        this.setState({ isBlocked: true })
      },
    );
  }

  
  render(){
    let cindex = 0
    return (
      <div className="RecorderMessage">
        <header className="recorder">
          <button  onClick={this.start} disabled={this.state.isRecording}className='btn_memory' >Record</button>
          <button  onClick={this.stop} disabled={!this.state.isRecording} className='btn_memory'>Stop</button>
          <audio className='audio_recorder' src={this.state.blobURL} controls="controls" />
        </header>
        
      </div>
    );
  }
}

export default withRouter(RecorderMessage2);
