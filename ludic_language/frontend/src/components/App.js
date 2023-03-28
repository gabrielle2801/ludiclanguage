import React, { useEffect, useState } from "react";
import {BrowserRouter, Routes, Route, useParams} from 'react-router-dom';
import Alert from 'react-bootstrap/Alert';
import '../styles/App.css';
import loup from "../assets/img/Loup.png";
import renard from "../assets/img/Renard.png";
import SingleCard from "./SingleCard";
import RecorderMessage from "./RecorderMessage";
import ExerciseDetail from './ExerciseParams';







const cardImages = [
    { "src": loup, matched: false},
    { "src": renard, matched: false},
]

const cardMessages = [
    {"name":"La vie est belle"},
    {"name":"la cigale et la fourmi"} ,
    {"name":"Ton thé t’a-t-il ôté ta toux ?"} ,
    {"name":"Tata, ta tarte tatin tenta Tonton ; Tonton tâta ta tarte tatin, Tata."} ,
    {"name":"Trois tortues trottaient sur un trottoir très étroit."} ,
]
function App() {
    const [cards, setCards] = useState([])
    const [turns, setTurns] = useState(0)
    const [choiceOne, setChoiceOne] = useState(null)
    const [choiceTwo, setChoiceTwo] = useState(null)
    const [disabled, setDisabled] = useState(false)
    const[messages, setMessages]=useState("")
    const [showMessage, setShowMessage] = useState(false)



    // shuffle cards
    const shuffleCards = () => {
        const shuffleCards = [...cardImages, ...cardImages]
            .sort(() => Math.random() - 0.5)
            .map((card) => ({ ...card, id: Math.random()}))

        setChoiceOne(null)
        setChoiceTwo(null)
        setCards(shuffleCards)
        setTurns(0)
        setMessages("")
        setShowMessage(false)

    }
     // shuffle messages
     const shuffleMessages = () => {
        const index = Math.floor(Math.random()*cardMessages.length)
        const mess=cardMessages[index]
        setMessages(mess.name)
        
    }

// handle a choice
const handleChoice =(card) => {
    choiceOne ? setChoiceTwo(card) : setChoiceOne(card)
}

// compare 2 selected cards
useEffect (() => {
    if (choiceOne && choiceTwo) {
        setDisabled(true)
        if (choiceOne.src === choiceTwo.src) {
            setCards(prevCards => {
                return prevCards.map(card => {
                    if (card.src === choiceOne.src){
                        shuffleMessages()
                        setShowMessage(true)
                        return {...card, matched: true}
                    } else {
                        return card
                    }
                })
            })
            resetTurn()
        } else {
            setTimeout(() => resetTurn(), 1000)
        }
    }
}, [choiceOne, choiceTwo])

console.log(cards)
console.log(messages)
// reset choices @ increase turn 
const resetTurn = () => {
    setChoiceOne(null)
    setChoiceTwo(null)
    setTurns(prevTurns => prevTurns + 1)
    setDisabled(false)
    setMessages("")
    setShowMessage(false)
}
useEffect(()=> {
    shuffleCards()
}, [])


    return (
        <div className='App'>
           
            <button onClick={shuffleCards}>New Game</button>
            
            <div className= "memory-game">
                {cards.map(card => (
                    <SingleCard 
                    key={card.id} 
                    card={card}
                    handleChoice={handleChoice}
                    flipped = {card === choiceOne || card === choiceTwo || card.matched}
                    disabled={disabled}
                    />
                ))}
            </div>
            <p>Turns: {turns}</p>
         
            <Alert 
                show={showMessage}
                variant="success">
                <p>{messages}</p>
            </Alert>
            <div>
            <Routes>
                <Route path="/play_on/:id" element={<RecorderMessage />} /> 
            </Routes>
                
            </div>            
        </div>
    )
}

export default App