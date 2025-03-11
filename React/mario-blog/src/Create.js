import React, {useState} from 'react';
import axios from "axios";
import {useNavigate} from "react-router-dom";
import { v4 as uuidv4 } from 'uuid';

const Create = () => {
	const [title, setTitle] = useState("");
	const [body, setBody] = useState("");
	const [author, setAuthor] = useState("");
	const navigate = useNavigate();

	const newBlog = (event) => {
		event.preventDefault();
		let id = uuidv4();
		const createdBlog = { title, body, author, id};
		axios.post("http://localhost:8000/blogs", createdBlog)
			.then(() => {
				navigate("/");
			})
			.catch((err) => {
				console.log("Error:", err);
			});
	};

	return (
		<div>
			<form className="create-blog" onSubmit={newBlog}>
				<input type="text" placeholder="Title" onChange={(e) => setTitle(e.target.value)} required/>
				<input type="text" placeholder="Body" onChange={(e) => setBody(e.target.value)} required/>
				<select value={author} onChange={(e) => setAuthor(e.target.value)} required>
					<option value="" disabled>Select Author</option>
					<option value="Mario">Mario</option>
					<option value="Luigi">Luigi</option>
					<option value="Yoshi">Yoshi</option>
					<option value="Peach">Peach</option>
				</select>
				<button type="submit">Post new blog</button>
			</form>
		</div>
	);
};

export default Create;