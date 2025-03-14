import React from 'react';

const BlogList = ({blogs, title, deleteBlog, sendToDetails}) => {
	// const BlogList = (props) => {
	// const title = props.title;
	
	return (
		<div className="blog-list">
			<h2 className="Blog-title">{title}</h2>
			{blogs.map(blog => (
				<div className="blog-preview" key={blog.id} onClick={() => sendToDetails(blog)}>
					<h2>{blog.title}</h2>
					<p>Written by: {blog.author}</p>
					<button onClick={(e) => {
						e.stopPropagation();
						deleteBlog(blog.id)
					}}>delete</button>
				</div>
			))}
		</div>
	);
};

export default BlogList;
