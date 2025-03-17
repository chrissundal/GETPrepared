// import axios from "axios";
// const postBlog = async (createdBlog) => {
// 	try {
// 		const response = await axios.post("http://localhost:8000/blogs", createdBlog)
// 		if(response.status === 201) {
// 			return true;
// 		}
// 	} catch (err) {
// 		console.log(err)
// 		return false;
// 	}
// }
// export default postBlog;
import axios from "axios";
const postBlog = (createdBlog) => {
		return axios.post("http://localhost:8000/blogs", createdBlog)
			.then(response => {
				return response.status === 201;
			})
		.catch(err => {
				console.log(err)
				return false;
			});
	} 
export default postBlog;