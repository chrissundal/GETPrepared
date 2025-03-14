import {NavLink} from "react-router-dom";

const Navbar = () => {
	return (
		<nav className="navbar">
			<h1>Mario blog</h1>
			<div className="links">
				<NavLink to="/" className={({ isActive }) => isActive ? 'active' : ''}>Home</NavLink>
				<NavLink to="/about" className={({ isActive }) => isActive ? 'active' : ''}>About Mario</NavLink>
				<NavLink to="/create" className={({ isActive }) => isActive ? 'active' : ''}>New blog</NavLink>
			</div>
		</nav>

	);
};

export default Navbar;