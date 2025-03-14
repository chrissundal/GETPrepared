import {useEffect, useState} from "react";
import BlogList from "./BlogList";
import deleteBlog from "./composables/deleteBlog";
import useFetch from "./composables/useFetch";
import {useNavigate} from "react-router-dom";

const Home = () => {
	const {data: players} = useFetch("http://localhost:8000/players")
	const {data: blogs, error: isPending} = useFetch("http://localhost:8000/blogs");
	const [name, setName] = useState(null);
	const [num, setNum] = useState(1);
	const [localBlogs, setLocalBlogs] = useState([]);
	const navigate = useNavigate();
	const getDeleteBlog = async (id) => {
		const success = await deleteBlog(id);
		if(success) {
			console.log("success deleting")
			setLocalBlogs(localBlogs.filter((blog) => blog.id !== id).sort((a,b) => new Date(b.date) - new Date(a.date)));
		}
	}
	const sendToDetails = (blog) => {
		navigate(`/blog/${blog.id}`, {state: blog})
	}
	
	useEffect(() => {
		if (blogs) {
			setLocalBlogs(blogs.sort((a,b) => new Date(b.date) - new Date(a.date)));
		}
		if(players) {
			setName(players[0].name)
		}
	}, [players,blogs]);
	
	const filteredList = localBlogs && name ? localBlogs.filter(blog => blog.author === name).sort((a,b) => new Date(b.date) - new Date(a.date)) : [];
	
	const setNextName = (() => {
		if (players) {
			setName(players[num].name);
			setNum((prevNum) => (prevNum + 1) % players.length);
		}
	});
	const isLoaded = players && blogs && localBlogs;
	
	return (
		<div className="home">
			{isPending && <h1>Loading...</h1>}
			{!isPending && blogs?.length === 0 && <h2>No blogs available</h2>}
			{isLoaded && <BlogList blogs={localBlogs} title="Blogs" deleteBlog={getDeleteBlog} sendToDetails={sendToDetails}/>}
			{isLoaded && filteredList.length > 0 ? (
				<BlogList blogs={filteredList} title={`${name}'s Blogs`} deleteBlog={getDeleteBlog} sendToDetails={sendToDetails}/>
			) : (
				 <div className="no-results-container">
					<h2>{`${name}'s Blogs`}</h2>
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