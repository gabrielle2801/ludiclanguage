import React, {useState, useEffect, useContext } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import MicRecorder from 'mic-recorder-to-mp3';
import Alert from 'react-bootstrap/Alert';
import withRouter from './withRouter';
import loup from "../assets/img/Loup.png";
import renard from "../assets/img/Renard.png";
import apple from "../assets/img/apple.png"
import bird from "../assets/img/bird.png"
import bird2 from "../assets/img/bird2.png"
import flower from "../assets/img/flower.png"
import flower2 from "../assets/img/flower2.png"
import flower3 from "../assets/img/flower3.png"
import fox from "../assets/img/fox.png"
import wolf from "../assets/img/wolf.png"
import Tile from "./SingleCard";
import '../styles/App.css';
import '../styles/RecorderMessage.css'
import axios from 'axios';
import Cookies from 'js-cookie';

const Mp3Recorder = new MicRecorder({ bitRate: 128 });


class RecorderMessage extends React.Component {
  tiles = [
    {
      name: "Loup",
      accent: "#ffcc33",
      src: loup,
    },
    {
      name: "Renard",
      accent: "rgb(171, 153, 142)",
      src: renard,
    }, 
    {
      name: "apple",
      accent: "rgb(171, 153, 142)",
      src: apple,
    }, 
    {
      name: "bird",
      accent: "rgb(171, 153, 142)",
      src: bird,
    }, 
    {
      name: "bird2",
      accent: "rgb(171, 153, 142)",
      src: bird2,
    }, 
    {
      name: "flower",
      accent: "rgb(171, 153, 142)",
      src: flower,
    }, 
    {
      name: "flower2",
      accent: "rgb(171, 153, 142)",
      src: flower2,
    }, 
    {
      name: "flower3",
      accent: "rgb(171, 153, 142)",
      src: flower3,
    }, 
    {
      name: "fox",
      accent: "rgb(171, 153, 142)",
      src: fox,
    }, 
    {
      name: "wolf",
      accent: "rgb(171, 153, 142)",
      src: wolf,
    }, 
  ];
  messages = [
    "La vie est belle",
    "la cigale et la fourmi" ,
    "Ton thé t’a-t-il ôté ta toux ?",
    "Tata, ta tarte tatin tenta Tonton ; Tonton tâta ta tarte tatin, Tata." ,
    "Trois tortues trottaient sur un trottoir très étroit." ,
  ]
  constructor(props){
    super(props);
    this.state = {
      tiles: [],
      messages: "",
      turns: 0,
      activeTile: null,
      isRecording: false,
      blobURL: '',
      isBlocked: false,
      showMessage:false,
      

    };
    this.handleClick = this.handleClick.bind(this);
    this.resetPlayArea = this.resetPlayArea.bind(this);
  }
  shuffleTiles(tiles) {
    let j, x, i;
    console.log("shuffletiles")

    for (i = tiles.length - 1; i > 0; i--) {
      j = Math.floor(Math.random() * (i + 1));
      x = tiles[i];
      tiles[i] = tiles[j];
      tiles[j] = x;
    }

    return tiles;
  }
  multiplyTiles(tiles) {
    return tiles
      .map(item => {
        // Use Object.assign to create a new object rather than passing the same reference twice
        return [item, Object.assign({}, item)];
      })
      .reduce((a, b) => {
        return a.concat(b);
      });
  }
  shuffleCards = () =>  {
    const newTiles = this.tiles.map(e => {
      e.status = "unselected";

      return e;
    });

    this.setState({
      tiles: this.shuffleTiles(this.multiplyTiles(newTiles)),
      turns:0
    });
    
  }
  shuffleMessages () {
    const index = Math.floor(Math.random()*this.messages.length)
    const mess=this.messages[index]
    console.log(mess)
    this.setState({messages:mess})
    this.setState({showMessage:true})
    
}
  handleClick(index) {
    // Update turns on every click
    console.log("click")
    this.setState({ turns: this.state.turns + 1 });

    const selectedTile = this.state.tiles[index];
    const updatedTiles = this.state.tiles.slice();

    selectedTile.status = "selected";
    updatedTiles[index] = selectedTile;

    this.setState({
      tiles: updatedTiles
    });

    if (this.state.activeTile === null) {
      this.setState({
        activeTile: selectedTile
      });
    } else if (selectedTile.name === this.state.activeTile.name) {
      let matched = 0;

      const updatedTiles = this.state.tiles.map(e => {
        if (e.name === selectedTile.name) e.status = "matched";
        if (e.status === "matched") matched++;

        return e;
      });

      this.setState({
        tiles: updatedTiles,
        activeTile: null
      });

      if (matched === 20) this.shuffleMessages();
      
      console.log(this.props.match.params.id)
      
    } else {
      const _this = this;

      setTimeout(function() {
        const updatedTiles = _this.state.tiles.map(e => {
          if (
            e.name === _this.state.activeTile.name ||
            e.name === selectedTile.name
          ) {
            e.status = "unselected";
          }

          return e;
        });

        _this.setState({
          activeTile: null,
          tiles: updatedTiles
        });
      }, 700);
    }
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
    data.append('sentence', this.state.messages)
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
  componentDidMount(){
    this.shuffleCards()
  }
  
  
  render(){
    let cindex = 0
    return (
      <div className="RecorderMessage">
        <button onClick={this.shuffleCards}>New Game</button>
        <p>Turns: {this.state.turns}</p>
        <div className="area">
          {this.state.tiles.map(e => (
            <Tile
              index={cindex++}
              status={e.status}
              name={e.name}
              src={e.src}
              accent={e.accent}
              onClickListener={this.handleClick}
            />
          ))}
        </div>
        <Alert 
            show={this.state.showMessage}
            variant="success">
            <p>{this.state.messages}</p>
          </Alert>
        <header className="recorder">
          <button onClick={this.start} disabled={this.state.isRecording}>Record</button>
          <button onClick={this.stop} disabled={!this.state.isRecording}>Stop</button>
          <audio className='recorder' src={this.state.blobURL} controls="controls" />
        </header>
        
      </div>
    );
  }
}

export default withRouter(RecorderMessage);
