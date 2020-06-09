import React, { Component } from 'react';

import './App.css';

import Header from './components/Header';
import Content from './components/Content';
import firebase from 'firebase';


export default class App extends Component {

  constructor() {
    super();
    this.state = {
      speed: 11
    };
  }

  componentDidMount() { 
    const rootRef = firebase.database().ref();
    const speedRef = rootRef.child('speed');
    speedRef.on('value', snap => {
      this.setState = ({
        speed: snap.val()
      });
    });
  }

  render() {   
    return (
      <div className="App">
        <Header/>
        <h1>{this.state.speed}</h1>
        <br />
        <Content/>
     </div>
    );
  }
}
