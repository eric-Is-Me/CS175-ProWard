import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import * as serviceWorker from './serviceWorker';
import firebase from 'firebase';

var config = {
  apiKey: "ask edward",
  authDomain: "proward-6b420.firebaseapp.com",
  databaseURL: "https://proward-6b420.firebaseio.com",
  projectId: "proward-6b420",
  storageBucket: "proward-6b420.appspot.com",
  messagingSenderId: "192314226070",
  appId: "1:192314226070:web:8226c57f3bfae7c62bd9b7",
  measurementId: "G-WVW284HWVL"
}
firebase.initializeApp(config);

ReactDOM.render((
    <BrowserRouter>
      <App />
    </BrowserRouter>
  ), document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
 
export default firebase