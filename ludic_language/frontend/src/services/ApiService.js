import axios from 'axios';

export function getmessage() {
    return axios.get('http://127.0.0.1:8000/play_on/')
    .then(res => {
        return res.data
    })
}

export function addmessage(messages) {
    return axios.post('http://127.0.0.1:8000/play_on/',
    {
        sentence : messages.setMessages
    })
    .then (res => {
        console.log('response', res)
        return res.data
    })
}