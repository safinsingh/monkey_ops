<script lang="ts">
	import '../app.css';
	import { io } from 'socket.io-client';

	const url = 'http://localhost:8080';
	const sock = io(url, { transports: ['websocket'] });

	let stats = {} as {
		[id: string]: {
			cpu_percentage: number;
			mem_usage: number;
		};
	};

	sock.on('updateStats', (data) => {
		stats = data;
	});
</script>

<table class="table-auto">
	<thead>
		<tr>
			<th>Container ID</th>
			<th>CPU%</th>
			<th>Memory</th>
		</tr>
	</thead>
	<tbody>
		{#each Object.entries(stats) as stat}
			<tr>
				<td>{stat[0]}</td>
				<td>{stat[1]['cpu_percentage']}</td>
				<td>{stat[1]['mem_usage']}</td>
			</tr>
		{/each}
	</tbody>
</table>

<slot />
