import React, { useEffect, useState } from 'react';
import { useParams } from "react-router-dom";
import Cookies from 'js-cookie';
import axios from "axios";

// Get ID from URL
const ExerciseDetail = ()=> {
    const data = new FormData
    const {id} = useParams();
    //console.log({id})
    //const value = parseInt(id);
    //console.log('test    ', value)
    //data.append('exercise', value)

    useEffect(()=> {
        axios
        .get("http://127.0.0.1:8000/play_on/"+id,{
        headers: {
          "content-Type": "multipart/form-data",
          'X-CSRFToken':Cookies.get('csrftoken'),
        },
      })
            
    });
    return (
        <div>{id}</div>
    )
    
}

export default ExerciseDetail;