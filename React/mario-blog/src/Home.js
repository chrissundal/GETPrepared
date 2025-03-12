import {useEffect, useState} from "react";
import BlogList from "./BlogList";
import axios from "axios";

const Home = () => {
	const [players, setPlayers] = useState([
		{name: "Mario", id: 1},
		{name: "Luigi", id: 2},
		{name: "Yoshi", id: 3},
		{name: "Peach", id: 4},
	])
	const randomName = () => {
		const randomIndex = Math.floor(Math.random() * players.length);
		return players[randomIndex].name;
	}
	const [blogs, setBlogs] = useState(null);
	const [name, setName] = useState(randomName);
	const [isPending, setIsPending] = useState(true);
	const deleteBlog = async (id) => {
		// const newBlogs = blogs.filter(blog => blog.id !== id)
		// setBlogs(newBlogs)
		//setBlogs(oldBlogs => oldBlogs.filter(blog => blog.id !== id))
		await axios.delete(`http://localhost:8000/blogs/${String(id)}`)
		fetchBlogs();
	}
	
	const fetchBlogs = () => {
		axios.get("http://localhost:8000/blogs")
			.then(response => {
				setBlogs(response.data)
				setIsPending(false)
			})
			.catch(err => {
				console.log(err)
			})
	}
	
	useEffect(() => {
		console.log("Home rendered");
		fetchBlogs();
	}, []);
	
	return (
		<div className="home">
			{isPending && <h1>Loading...</h1>}
			{blogs && <BlogList blogs={blogs} title="Blogs" deleteBlog={deleteBlog}/>}
			{blogs && blogs.filter(blog => blog.author === name).length > 0 ? (
				<BlogList blogs={blogs.filter(blog => blog.author === name)} title={name + "'s Blogs"} />
			) : (
				<div className="no-results-container">
					<h2>{name + "'s Blogs"}</h2>
					<p>No blogs found for {name}</p>
				</div>
			)}
			{/*<BlogList blogs={blogs.filter(blog => blog.author === name)} title={name + "'s Blogs"}/>*/}
			<div className={"cycle-container"}>
				<button  onClick={() => setName(oldName => {
					let newName;
					do {
						newName = randomName();
					} while (newName === oldName) return newName;
				})}>
					Cycle selected blogs
				</button>
			</div>
		</div>
	);
};

export default Home;