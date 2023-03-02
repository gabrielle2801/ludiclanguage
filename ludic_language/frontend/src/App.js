import React, { useState } from "react";
import './App.css';
import loup from "../assets/img/Loup.jpg";
import renard from "../assets/img/Renard.jpg";


const cardImages = [
    { "src": loup },
    { "src": renard },
]

function App() {
    const [cards, setCards] = useState([])
    const [turns, setTurns] = useState(0)

    // shuffle cards
    const shuffleCards = () => {
        const shuffleCards = [...cardImages, ...cardImages]
            .sort(() => Math.random() - 0.5)
            .map((card) => ({ ...card, id: Math.random()}))

        setCards(shuffleCards)
        setTurns(0)
    }
console.log(cards, turns)
    return (
        <div className='App'>
            <button onClick={shuffleCards}>New Game</button>
            <div className= "card-grid">
                {cards.map(card => (
                    <div className ="card" key={card.id}>
                        <div>
                            <h1>Test</h1>
                            <img className ="front" src={card.src} alt="card front" />
                        </div>
                    </div>
                    ))}

            </div>

            
        </div>
    )
}

export default App