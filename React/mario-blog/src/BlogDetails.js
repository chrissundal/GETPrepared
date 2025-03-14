import React from 'react';
import {useLocation} from "react-router-dom";

const BlogDetails = () => {
	//const { id } = useParams();
	//const {data: blog, isPending} = useFetch("http://localhost:8000/blogs/" + id)
	const location = useLocation()
	const blog = location.state;
	const date = new Date(blog.date);
	return (
		<div>
			{/*{isPending && <p>Loading...</p>}*/}
			{!blog && <h1>Loading...</h1>}
			{blog && ( 
			<div className="blog-details">
				<h2>{blog.title}</h2>
				<div>{blog.body}</div><br/>
				<p className="author-tag">Written by: {blog.author}</p>
				<p className="date-tag">{date.toLocaleString()}</p>
			</div>
			)}
		</div>
	);
};

export default BlogDetails;
