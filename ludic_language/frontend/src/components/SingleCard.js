import '../styles/SingleCard.css';
import React, { Component} from 'react';
import cover from "../assets/img/cover.png";

export default function SingleCard({card, handleChoice, flipped, disabled }){
    const handleClick = ()=> {
        if (!disabled){
            handleChoice(card)
        }
        
    }
    return(
        <div className ="memory-card">
            <div className={flipped ? "flipped": ""}>
                <img className ="front" src={card.src} alt="card front" />
                <img 
                    className ="back" 
                    src={cover} 
                    onClick={handleClick}
                    alt="card back" />
            </div>
        </div>
    )
}