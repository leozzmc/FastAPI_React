// import React, { useEffect, useState } from 'react'
import React from 'react'

let url = 'http://127.0.0.1:8000'
let val = {
  id: 0,
  scan_url: "www.ntust.edu.tw",
}


const Scan = ()=> {
    function postData(url, scan_url) {
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          //body: JSON.stringify(data),
          body: JSON.stringify(scan_url),
          redirect: 'follow',
      }

      fetch(`${url}/scanURL`, requestOptions)
          .then((response) => response.json())
          .then((result) => console.log(result))
          .catch((error) => console.log('error', error))
  }
    function getData(url, scan_url) {
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
          Scan
          <button onClick={postData(url, val)}>postData</button>
          <button onClick={getData(url, val)}>getData</button>
      </div>
    )
}

export default Scan;
