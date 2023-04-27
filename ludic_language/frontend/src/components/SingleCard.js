import '../styles/SingleCard.css';
import React, { Component} from 'react';
import cover from "../assets/img/cover.png";

class Tile extends React.Component {
    constructor(props) {
      super(props);
  
      this.handleClick = this.handleClick.bind(this);
    }
  
    handleClick() {
      console.log("click singlecard")
      if (this.props.status === "unselected") {
        this.props.onClickListener(this.props.index);
      } else {
        console.warn("The tile has already been " + this.props.status);
      }
    }
  
    render() {
      return (

          <div
            onClick={this.handleClick}
            className={
              "tile " +
              (this.props.status === "selected"
                ? "tile--selected"
                : this.props.status === "matched"
                  ? "tile--selected tile--matched"
                  : "")
            }
          >
            <img className="tile--front" src={cover}/>
            <img className="tile--back" src={this.props.src}
              style={{ backgroundColor: this.props.accent }}/>
          </div>

      );
    }
  }
  export default Tile
  