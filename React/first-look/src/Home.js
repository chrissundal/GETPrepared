const Home = () => {
	const handleClick = () => {
		console.log("clicked");
	}
	
	return (
		<div className="home">
			<h2>Test Home</h2>
			<button onClick={handleClick}>Klikk på meg</button>
		</div>
	);
};

export default Home;