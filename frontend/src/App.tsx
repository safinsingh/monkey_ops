import { useEffect, useState } from "react";
import "./App.css";
import { io } from "socket.io-client";
import prettyBytes from "pretty-bytes";

const formatID = (id: string) => {
	return id.slice(0, 8);
};

const formatPercent = (p: number) => {
	return (p * 100).toFixed(2) + "%";
};

function App() {
	const url = "http://localhost:8080";
	let sock;

	const [stats, setStats] = useState<{
		[id: string]: {
			cpu_percentage: number;
			mem_usage: number;
		};
	}>({});

	useEffect(() => {
		sock = io(url, { transports: ["websocket"] });

		sock.on("updateStats", (res) => {
			setStats(res.data);
		});
	});

	return (
		<>
			<table className="table-auto">
				<thead>
					<tr>
						<th>Container ID</th>
						<th>CPU%</th>
						<th>Memory</th>
					</tr>
				</thead>
				<tbody>
					{Object.entries(stats).map((stat) => (
						<tr>
							<td>{formatID(stat[0])}</td>
							<td>{formatPercent(stat[1]["cpu_percentage"])}</td>
							<td>{prettyBytes(stat[1]["mem_usage"])}</td>
						</tr>
					))}
				</tbody>
			</table>
		</>
	);
}

export default App;
