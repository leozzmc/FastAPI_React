import React from 'react'

let url = 'http://127.0.0.1:8000'
let val = {
  id: 0,
  data: ['www.ntust.edu.tw', 'www.ntpu.edu.tw', 'www.ntu.edu.tw'],
}



const Scan = ()=> {
    function postData(url, data) {
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          //body: JSON.stringify(data),
          body: JSON.stringify(data),
          redirect: 'follow',
      }

      fetch(`${url}/scanURL`, requestOptions)
          .then((response) => response.json())
          .then((result) => console.log(result))
          .catch((error) => console.log('error', error))
  }
    function getData(url, data) {
        fetch(url, {
            method: 'GET',
            redirect: 'follow',
        })
            .then((response) =>  console.log(response))
            .then((result) => console.log(result))
            .catch((error) => console.log('error', error))
    }
    // useEffect(() => {}, [])
    return (
      <div>
          <h1>VirusTotal API Testing</h1>
          <button onClick={postData(url, val)}>postData</button>
          <button onClick={getData(url, val)}>getData</button>
      </div>
    )
}

export default Scan;
