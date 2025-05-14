import {error} from "@sveltejs/kit";

export const load = async ({ fetch }) => {
	try {
		const response = await fetch('https://jsonplaceholder.typicode.com/posts');

		if (!response.ok) {
			error(response.status, `Feil ved henting av data: ${response.statusText}`);
		}

		return { guides: await response.json() };

	} catch (err) {
		if (err.status || err.location) {
			throw err;
		}
		console.error('Uventet feil ved lasting av data:', err);
		throw error(500, 'En uventet feil oppstod ved henting av guidene');
	}
}
