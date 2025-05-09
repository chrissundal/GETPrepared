<script>
	import RouteTransition from "./RouteTransition.svelte";
	import { pollsStore } from "../store/Stores.svelte";
	import { flip } from 'svelte/animate'
	import PollDetails from "./PollDetails.svelte";

	const deletePoll = (poll) => {
		pollsStore.update(polls => polls.filter(p => p.id !== poll.id))
    }
	$: sortedPolls = [...$pollsStore].sort((a, b) => (b.vote1 + b.vote2) - (a.vote1 + a.vote2));

</script>

<RouteTransition>
    <div class="my-container">
        {#if sortedPolls.length === 0}
            <p>Ingen polls ennå...</p>
        {:else}
            <div class="row">
                {#each sortedPolls as poll(poll.id)}
                    <div class="col-12 col-md-{$pollsStore.length === 1 ? '12' : '6'} col-lg-{$pollsStore.length === 1 ? '12' : '4'} mb-3 mx-auto" animate:flip={{duration: 500}}>
                        <PollDetails {poll} {deletePoll}/>
                    </div>
                {/each}
            </div>
        {/if}

    </div>
</RouteTransition>

<style>

</style>