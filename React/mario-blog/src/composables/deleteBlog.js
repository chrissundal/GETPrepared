import axios from "axios";

const deleteBlog = async (id) => {
	try {
		let response = await axios.delete(`http://localhost:8000/blogs/${String(id)}`)
		if(response.status === 200) {
			return true;
		}
	} catch (err) {
		console.log(err)
		return false;
	}
}
export default deleteBlog;