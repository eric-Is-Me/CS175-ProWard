import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";

import Home from './pages/Home/Home.js'
import LogIn from './pages/LogIn/LogIn.js'
import Dashboard from './pages/Dashboard/Dashboard.js'

export default class Content extends Component {
    render() {
        return (
        <div>
            <Switch>
                <Route
                    exact
                    path="/"
                    component={Home}
                />
                <Route
                    exact
                    path="/Home"
                    component={Home}
                />

                <Route
                    exact
                    path="/Dashboard"
                    component={Dashboard}
                />
                <Route
                    exact
                    path="/LogIn"
                    component={LogIn}
                />
                {/* <Route component={errorPage} /> */}
            </Switch>
        </div>
        );
    }
}
