import axios from "axios";
const postBlog = async (createdBlog) => {
	try {
		const response = await axios.post("http://localhost:8000/blogs", createdBlog)
		if(response.status === 201) {
			return true;
		}
	} catch (err) {
		console.log(err)
		return false;
	}
}
export default postBlog;