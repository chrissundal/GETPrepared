<script>
	import RouteTransition from "./RouteTransition.svelte";
	import {pollsStore} from "../store/Stores.svelte";
	import Button from "../shared/Button.svelte";
	const deletePoll = (poll) => {
		pollsStore.update(polls => polls.filter(p => p.id !== poll.id))
    }

</script>

<RouteTransition>
    <div class="my-container">
        {#if $pollsStore.length === 0}
            <p>Ingen polls ennå...</p>
        {:else}
            {#each $pollsStore as poll, i}
                <div class="card mb-3">
                    <div class="card-header polls">
                        <h4>{poll.question}</h4>
                        <Button on:click={() => deletePoll(poll)}>X</Button>
                    </div>
                    <div class="card-body">
                        <div class="list-group gap-1">
                            {#if poll.vote1 <= 10 || poll.vote2 <= 10}
                            <div class="pollbutton">
                                <button on:click={() => poll.vote1++}>{poll.answer1}</button>
                                <div class="pollbars">
                                    <div style={`width: ${poll.vote1*10}%; background-color: ${poll.vote1 >= poll.vote2 ? '#45c496' : '#d91b42'};`}></div>
                                </div>
                            </div>
                            <div class="pollbutton">
                                <button on:click={() => poll.vote2++}>{poll.answer2}</button>
                                <div class="pollbars">
                                    <div style={`width: ${poll.vote2*10}%; background-color: ${poll.vote2 >= poll.vote1 ? '#45c496' : '#d91b42'};`}></div>
                                </div>
                            </div>
                            {:else}
                                <div class="pollbutton">
                                    <button on:click={() => poll.vote1++}>{poll.answer1}</button>
                                    <div class="pollbars">
                                        <div style={`width: ${poll.vote1}%; background-color: ${poll.vote1 >= poll.vote2 ? '#45c496' : '#d91b42'};`}></div>
                                    </div>
                                </div>
                                <div class="pollbutton">
                                    <button on:click={() => poll.vote2++}>{poll.answer2}</button>
                                    <div class="pollbars">
                                        <div style={`width: ${poll.vote2}%; background-color: ${poll.vote2 >= poll.vote1 ? '#45c496' : '#d91b42'};`}></div>
                                    </div>
                                </div>
                            {/if}
                        </div>
                    </div>
                </div>
            {/each}
        {/if}

    </div>
</RouteTransition>

<style>
    .polls {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .pollbars {
        width: 100%;
        height: 30px;
    }
    .pollbars > div {
        height: 100%;
        border-radius: 5px;
        transition: width 0.3s ease;
    }
    .pollbutton {
        position: relative;
    }
    .pollbutton button {
        background: none;
        border: none;
        position: absolute;
        width: 100%;
        left: 0;
    }
</style>