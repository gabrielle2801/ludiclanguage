import '../styles/MessageCard.css'
import React, { Component} from 'react';


export default function MessageCard({message, handleMessage,disabled }){
    const handleClick = ()=> {
        if (!disabled){
            handleMessage(message)
        }
        
    }
    return(
        <div className ="memory-card">
                <p className ="memory-win" 
                    onClick={handleClick}>{message.name}</p>
        </div>
    )
}