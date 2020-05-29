import React, { Component } from 'react';
import { Menu } from 'semantic-ui-react';
import { Link, withRouter } from 'react-router-dom';

const links = [
    { name: 'Home',         link: '/' },
    { name: 'LogIn',        link: '/LogIn' },
    { name: 'Dashboard',    link: '/Dashboard' },
];

class Header extends Component{

    handleItemClick = (e, { name }) => this.setState({ activeItem: name })

    getActiveItem = () => {
        for ( var i in links){
            if (this.props.location.pathname === links[i].link){
                return links[i].name;
            } 
        }
        return 'Map';
    }

    state = { activeItem: this.getActiveItem() };

    render() {
        const { activeItem } = this.state
        return (
            <div>
                <Menu pointing secondary >
                {
                    links.map( (i, idx) => {
                        return (
                            <Menu.Item
                                name = {i.name}
                                active = {activeItem === i.name}
                                onClick = {this.handleItemClick}
                                as = {Link} 
                                to = {i.link}
                            />
                        );
                    })
                }
                </Menu>
            </div>
        );
    }
}

export default withRouter(Header);