import React, {useEffect, useState} from 'react';
import {useNavigate} from "react-router-dom";
import { v4 as uuidv4 } from 'uuid';
import postBlog from "./composables/postBlog";
import useFetch from "./composables/useFetch";

const Create = () => {
	const [title, setTitle] = useState("");
	const [body, setBody] = useState("");
	const [author, setAuthor] = useState("");
	const navigate = useNavigate();
	const [error, setError] = useState(null);
	const {data: players} = useFetch("http://localhost:8000/players")
	
	useEffect(() => {
		
	}, []);
	const newBlog = (event) => {
		event.preventDefault();
		let id = uuidv4();
		const createdBlog = { title, body, author, id, date: new Date()};
		let success = postBlog(createdBlog);
		if(success) {
			console.log("success adding")
			navigate("/");
		} else {
			setError("Error posting blog");
			setTimeout(() => {
				setError(null);
			}, 3000
			)
		}
	};

	return (
		<div>
			<form className="create-blog" onSubmit={newBlog}>
				<input type="text" placeholder="Title" onChange={(e) => setTitle(e.target.value)} required/>
				<input type="text" placeholder="Body" onChange={(e) => setBody(e.target.value)} required/>
				<select value={author} onChange={(e) => setAuthor(e.target.value)} required>
					<option value="" disabled>Select Author</option>
					{players && players.map(player => (
						<option key={player.id} value={player.name}>
							{player.name}
						</option>
					))}
				</select>
				<button type="submit">Post new blog</button>
				{error && <p>{error}</p>}
			</form>
		</div>
	);
};

export default Create;