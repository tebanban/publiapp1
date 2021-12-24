import React from "react";
import { Link } from "react-router-dom";
import logoNav from "../../img/logo-nav.png";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light mb-3">
			<Link to="/">
				<img className="navbar-brand px-3 mb-0 h1" src={logoNav} alt="Logo" />
			</Link>
			<div className="ml-auto">
				<Link to="/app">
					<button className="btn btn-primary mx-2">App</button>
				</Link>
				<Link to="/demo">
					<button className="btn btn-secondary mx-2">Demo</button>
				</Link>
			</div>
		</nav>
	);
};
