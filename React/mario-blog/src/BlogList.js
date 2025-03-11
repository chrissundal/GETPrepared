import React from 'react';

const BlogList = ({blogs, title, deleteBlog}) => {
	// const BlogList = (props) => {
	// const title = props.title;
	
	return (
		<div className="blog-list">
			<h2 className="Blog-title">{title}</h2>
			{blogs.map(blog => (
				<div className="blog-preview" key={blog.id}>
					<h2>{blog.title}</h2>
					<p>Written by: {blog.author}</p>
					<button onClick={() => deleteBlog(blog.id)}>delete</button>
				</div>
			))}
		</div>
	);
};

export default BlogList;
