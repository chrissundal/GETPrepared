<script>
	import Intro from "./components/Intro.svelte";
	import Modal from "./components/Modal.svelte";
	import { fade, fly, blur, slide } from "svelte/transition";
	let visible = true;
	let showModal = false;
	const toggleModal = () => {
		showModal = !showModal
    }
</script>
<main>
    <button on:click={() => visible = !visible}>Test fade</button>
    {#if visible}
        <div transition:blur>
            <Intro />
        </div>
    {/if}
    <button class="offer" on:click={toggleModal}>Once in a lifetime mulighet</button>
    {#if showModal}
        <div transition:fade>
            <Modal closeModal={toggleModal}/>
        </div>
    {/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
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
    .offer {
        animation: colorPulse 0.5s infinite alternate;
        color: white;
    }

    @keyframes colorPulse {
        0% {
            background: red;
            color: white;
        }
        100% {
            background: yellow;
            color: red;
        }
    }

    .offer:hover {
        animation: none;
        background: yellow;
        color: red;
    }

</style>