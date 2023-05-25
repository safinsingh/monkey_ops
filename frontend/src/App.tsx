import { useEffect, useState } from "react";
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
			<div className="px-5 py-5">
				<h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl">
					Dashboard
				</h1>
				<table className="w-full text-sm text-left text-gray-500 border-light-500 rounded">
					<thead className="text-xs text-gray-700 uppercase bg-gray-50">
						<tr>
							<th scope="col" className="px-6 py-3">
								Container ID{" "}
							</th>
							<th scope="col" className="px-6 py-3">
								CPU%
							</th>
							<th scope="col" className="px-6 py-3">
								Memory
							</th>
						</tr>
					</thead>
					<tbody>
						{Object.entries(stats).map((stat) => (
							<tr className="bg-white border-b">
								<td className="px-6 py-4">{formatID(stat[0])}</td>
								<td className="px-6 py-4">{formatPercent(stat[1]["cpu_percentage"])}</td>
								<td className="px-6 py-4">{prettyBytes(stat[1]["mem_usage"])}</td>
							</tr>
						))}
					</tbody>
				</table>
			</div>
		</>
	);
}

export default App;
