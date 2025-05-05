<script>
	import {createEventDispatcher, onMount} from 'svelte';
	import { v4 as uuidv4 } from 'uuid';
	let dispatch = createEventDispatcher();

	let firstNames = ['Jens','Bjarne','Marie','Lisa','Terje','Tore','Svein']
	let lastNames = ['Hagen','Jensen','Larsen','Hansen','Knutsen']

	let colors = ['svart','rød','grå','blå','turkis','brun','grønn']
	let colorDict = {
		svart: 'black',
		rød: 'red',
		grå: 'grey',
		blå: 'blue',
		turkis: 'aqua',
		brun: 'brown',
		grønn: 'green'
	}

	let firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
	let lastName = lastNames[Math.floor(Math.random() * lastNames.length)]
	$: fullName = `${firstName} ${lastName}`;
	// $: fullName = firstName + ' ' + lastName;
	//$: fullName = getFullName();
	// $: console.log(firstName) // når noe endrer firstName, vil denne logge ut det nye verdien av firstName
	$: {
		console.log(firstName)
		setPerson()
	}
	const setPerson = () => {
		const person = {
			id: uuidv4(),
			firstName,
			lastName
		}
		dispatch('addPerson', person)
    }
	onMount(() => {
		setPerson()
	})
	const getFullName = () => {
		firstName = firstNames[Math.floor(Math.random() * firstNames.length)]
		lastName = lastNames[Math.floor(Math.random() * lastNames.length)]
		return `${firstName} ${lastName}`;
	}
	const getRandomItem = () => {
		return colors[Math.floor(Math.random() * colors.length)];
	}
	const handleInput = (e) => {
		selectedColor = e.target.value;
	}
	let selectedColor = getRandomItem();
	const capitalize = (str) => {
		return str.charAt(0).toUpperCase() + str.slice(1);
	}
	const deleteColor = (color) => {
		colors = colors.filter(c => c !== color);
	}
	let num = 5;
</script>

<main>
    {#if num > 20}
        <h3>Større enn 20</h3>
    {:else if num > 5}
        <h3>Større enn 5</h3>
    {:else}
        <h3>Mindre enn 5</h3>
    {/if}

    <h1 style="color: {colorDict[selectedColor]}">Hello {fullName}!</h1>

    {#each colors as color, i}
        <div style="color: {colorDict[color]}">{i+1}. {capitalize(color)}</div>
        <!--		<button on:click={deleteColor(color)}>Slett farge</button>-->
        <button on:click={() => deleteColor(color)}>Slett farge</button>
    {:else}
        <p>Ingen tilgjengelige farger...</p>
    {/each}

    <p>Din favorittfarge er: <span style="color: {colorDict[selectedColor]}">{capitalize(selectedColor)}</span> </p>
    <button on:click={() => selectedColor = getRandomItem()}>Oppdater farge</button>
    <p>Skriv inn farge:</p>
    <!--	<input type="text" on:input={(e) => selectedColor = e.target.value}>-->
    <!--	<input type="text" on:input={handleInput}>-->
    <input type="text" bind:value={selectedColor}>
    <p>Navn:</p>
    <input type="text" bind:value={firstName}>
    <input type="text" bind:value={lastName}>
</main>

<style>
    button {
        border: none;
        background: white;
        padding: 7px;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 5px;
        box-shadow: 2px 2px 3px rgba(0,0,0,0.12);
        transition: all 0.4s;
    }
    button:hover {
        background: #bdbcbc;
        color: white;
    }
</style>