import React, { Component } from 'react';
import Slider from "react-slick";

let url = 'http://127.0.0.1:8000'






    
    // return (
    //   <div>
    //       <h1>Meme Catcher</h1>
    //       <button onClick={getData(url)}>getData</button>
    //   </div>
    // )


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
  
  class SimpleSlider extends Component {
  render() {
    const settings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1
    };
    return (
      <div>
        <h1>Meme Catcher</h1>
        <h2> Single Item</h2>
        <Slider {...settings}>
          <div>
            <h3>1</h3>
            <button onClick={getData(url)}>getData</button>
          </div>
          <div>
            <h3>2</h3>
            <button onClick={getData(url)}>getData</button>
          </div>
          <div>
            <h3>3</h3>
            <button onClick={getData(url)}>getData</button>
          </div>
          <div>
            <h3>4</h3>
            <button onClick={getData(url)}>getData</button>
          </div>
          <div>
            <h3>5</h3>
            <button onClick={getData(url)}>getData</button>
          </div>
          <div>
            <h3>6</h3>
            <button onClick={getData(url)}>getData</button>
          </div>
        </Slider>
      </div>
    );
  }
}
}
export default Scan;
