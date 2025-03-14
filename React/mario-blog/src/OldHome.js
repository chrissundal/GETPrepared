import {useEffect, useState} from "react";
import BlogList from "./BlogList";
import fetchUsers from "./composables/fetchUsers";
import fetchBlogs from "./composables/fetchBlogs";
import deleteBlog from "./composables/deleteBlog";

const Home = () => {
	const [players, setPlayers] = useState([])
	const [blogs, setBlogs] = useState(null);
	const [name, setName] = useState(null);
	const [isPending, setIsPending] = useState(true);
	const [num, setNum] = useState(1);
	const getDeleteBlog = async (id) => {
		// const newBlogs = blogs.filter(blog => blog.id !== id)
		// setBlogs(newBlogs)
		//setBlogs(oldBlogs => oldBlogs.filter(blog => blog.id !== id))
		const success = await deleteBlog(id);
		if(success) {
			asyncFetch();
			console.log("success deleting")
		}
	}
	
	const asyncFetch = async () => {
		const fetchedPlayers = await fetchUsers();
		const fetchedBlogs = await fetchBlogs();
		if (fetchedBlogs && fetchedBlogs.length > 0) {
			setIsPending(false)
			setBlogs(fetchedBlogs)
		}
		if(fetchedPlayers && fetchedPlayers.length > 0) {
			setPlayers(fetchedPlayers)
			setName(fetchedPlayers[0].name)
		}
	}
	
	useEffect(() => {
		asyncFetch()
	}, []);
	
	const filteredList = blogs && name ? blogs.filter(blog => blog.author === name) : [];
	
	const setNextName = (() => {
		if (players.length > 0) {
			setName(players[num].name);
			setNum((prevNum) => (prevNum + 1) % players.length);
		}
	});

	return (
		<div className="home">
			{isPending && <h1>Loading...</h1>}
			{players && blogs && <BlogList blogs={blogs} title="Blogs" deleteBlog={getDeleteBlog}/>}
			{players && blogs && name && filteredList.length > 0 ? (
				<BlogList blogs={filteredList} title={name + "'s Blogs"} />
			) : (
				 <div className="no-results-container">
					<h2>{name + "'s Blogs"}</h2>
					<p>No blogs found for {name}</p>
				</div>
			)}
			
			<div className={"cycle-container"}>
				<button onClick={setNextName}>
					Cycle selected blogs
				</button>
			</div>
		</div>

	);
};

export default Home;