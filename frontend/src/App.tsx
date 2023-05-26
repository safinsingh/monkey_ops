import Nav from "./components/Nav";
import Dashboard from "./components/Dashboard";
import { BrowserRouter } from "react-router-dom";
import { Outlet } from "react-router-dom";

function App() {

	return (
		<>
			<Nav/>
<Outlet />
		</>
	);
}

export default App;
