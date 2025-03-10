import {Link} from "react-router-dom";

const Navbar = () => {
	return (
		<nav className="navbar">
			<h1>Test navbar</h1>
			<div className="links">
				{/*<a href="/">Home</a>*/}
				{/*<a href="/create">New</a>*/}
				<Link to={"/"}>Home</Link>
				<Link to={"/create"}>New</Link>
			</div>
		</nav>
	);
};

export default Navbar;