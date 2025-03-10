const Navbar = () => {
	const design = {
	color: "white",
	backgroundColor: "#f1356d",
	borderRadius: "8px",}
	return (
		<nav className="navbar">
			<h1>Mario blog</h1>
			<div className="links">
				<a href="/">Home</a>
				<a href="/create" style={design}>New blog</a>
				{/*<a href="/create" style={{*/}
				{/*	color: "white",*/}
				{/*	backgroundColor: "#f1356d",*/}
				{/*	borderRadius: "8px",*/}
				{/*}}>New blog</a>*/}
			</div>
		</nav>
	);
};

export default Navbar;