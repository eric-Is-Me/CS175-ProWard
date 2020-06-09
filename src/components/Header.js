import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";

import GenMenuBar from './GenMenuBar'

export default class Header extends Component {
    render() {
        return (
        <div>
            <Switch>
                <Route
                    exact
                    path="/"
                    component={null}
                />
                 <Route component={GenMenuBar} />
            </Switch>
        </div>
        );
    }
}
