<script>
	import {goto} from "$app/navigation";
	export let data;
	let guides = [];

	if(data) {
        guides = data.guides;
	}


</script>
<div class="guides">
    {#if guides.length > 0}
        <ul>
            {#each guides as guide (guide.id)}
                <li>
                    <a data-sveltekit-prefetch href="/guides/{guide.id}">{guide.title}</a>
                </li>
            {/each}
        </ul>
    {:else}
        <p>Loading...</p>
    {/if}
    <button on:click={() => goto('/')}>Go Home</button>
</div>


<style>
    .guides {
        margin-top: 20px;
    }
    ul {
        list-style: none;
        padding: 0;
        margin-left: 20px;
    }
    a {
        display: inline-block;
        text-decoration: none;
        margin-top: 10px;
        padding: 10px;
        border: 1px dotted rgba(255, 255, 255, 0.2);
    }
</style>