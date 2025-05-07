<script context="module">
	import { writable } from 'svelte/store';

	export const pollsStore = writable([]);
	export const activeItemStore = writable('Polls');


</script>