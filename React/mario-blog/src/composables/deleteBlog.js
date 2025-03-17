// import axios from "axios";
//
// const deleteBlog = async (id) => {
// 	try {
// 		let response = await axios.delete(`http://localhost:8000/blogs/${String(id)}`)
// 		if(response.status === 200) {
// 			return true;
// 		}
// 	} catch (err) {
// 		console.log(err)
// 		return false;
// 	}
// }
// export default deleteBlog;
import axios from "axios";

const deleteBlog = (id) => {
	return axios.delete(`http://localhost:8000/blogs/${String(id)}`)
	.then(response => {
		if(response.status === 200) return true;})
	.catch(err => {
		console.log(err)
		return false;
	});
}
export default deleteBlog;