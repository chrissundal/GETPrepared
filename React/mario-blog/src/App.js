import Navbar from "./Navbar";
import Home from "./Home";
import About from "./About";
import {Route, Routes} from "react-router-dom";
import Create from "./Create";
import BlogDetails from "./BlogDetails";

function App() {
	return (
		<div className="App">
			<Navbar />
			<div className="content">
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/about" element={<About />} />
					<Route path="/create" element={<Create />} />
					<Route path="/blog/:id" element={<BlogDetails />} />
					<Route path="*" element={<h2>404 This page does not exist</h2>} />
				</Routes>
			</div>
		</div>
	);
}


export default App;
