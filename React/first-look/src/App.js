import Navbar from "./Navbar";
import Home from "./Home";
import {Route, Routes} from "react-router-dom";
import Create from "./Create";


function App() {
	
	return (
		<div className="App">
			<Navbar />
			<div className="content">
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/create" element={<Create />} />
			</Routes>
			</div>
		</div>
	);
}
// function App() {
// 	const title = "Welcome"
// 	const person = {name: "Chris", age: 37};
// 	const link = "http://www.google.com"
// 	return (
// 		<div className="App">
// 			<div className="content">
// 				<h1>{title}</h1>
// 				<p>{person.name} is {person.age} years old</p>
// 				<p>Array: {[1,2,3,4,5]}</p>
// 				<p>Random number: {Math.round(Math.random() * 10)}</p>
// 				<a href={link}>Google</a>
// 			</div>
// 		</div>
// 	);
// }
export default App;
