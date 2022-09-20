import React from 'react'

let url = 'http://127.0.0.1:8000'



const Scan = ()=> {
    function getData(url) {
        fetch(url, {
            method: 'GET',
            redirect: 'follow',
        })
            .then((response) =>  console.log(response))
            .then((result) => console.log(result))
            .catch((error) => console.log('error', error))
    }
    return (
      <div>
          <h1>Meme Catcher</h1>
          <button onClick={getData(url)}>getData</button>
      </div>
    )
}

export default Scan;
