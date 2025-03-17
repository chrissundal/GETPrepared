import React, {useState} from 'react';
import {useNavigate} from "react-router-dom";
import { v4 as uuidv4 } from 'uuid';
import postBlog from "./composables/postBlog";
import useFetch from "./composables/useFetch";

const Create = () => {
	const [title, setTitle] = useState("");
	const [body, setBody] = useState("");
	const [author, setAuthor] = useState("");
	const [isPending, setIsPending] = useState(false);
	const navigate = useNavigate();
	const [error, setError] = useState(null);
	const {data: players} = useFetch("http://localhost:8000/players")
	
	const newBlog = (e) => {
		e.preventDefault();
		let id = uuidv4();
		const createdBlog = { title, body, author, id, date: new Date()};
		let success = postBlog(createdBlog);
		if(success) {
			console.log("success adding")
			navigate("/");
			//navigate(-1) //back
			setIsPending(true)
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
				<label>Blog title: </label>
				<input type="text" onChange={(e) => setTitle(e.target.value)} required/>
				<label>Blog body: </label>
				<textarea onChange={(e) => setBody(e.target.value)} required></textarea>
				<select value={author} onChange={(e) => setAuthor(e.target.value)} required>
					<option value="" disabled>Select Author</option>
					{players && players.map(player => (
						<option key={player.id} value={player.name}>{player.name}</option>
					))}
				</select>
				{!isPending && <button type="submit">Post new blog</button>}
				{isPending && <button disabled>Adding blog...</button>}
				{error && <p>{error}</p>}
			</form>
		</div>
	);
};

export default Create;