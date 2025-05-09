<script>
export let poll;
export let deletePoll;
import { scale } from 'svelte/transition';
import Button from "../shared/Button.svelte";
import { pollsStore } from "../store/Stores.svelte";

let isLoading = true;

setTimeout(() => {
	isLoading = false;
}, 1000);

$: totalVotes = poll.vote1 + poll.vote2;
$: percentA = Math.round(100 / totalVotes * poll.vote1) || 0;
$: percentB = Math.round(100 / totalVotes * poll.vote2) || 0;
$: isActive = Date.now() < new Date(poll.date).getTime();

const addVote = (choice) => {
	pollsStore.update(polls => {
		return polls.map(oldPoll => {
			if (oldPoll.id !== poll.id) {
				return oldPoll;
			}

			let copyPoll = { ...oldPoll };
			if (choice === 1) {
				copyPoll.vote1 += 1;
			} else {
				copyPoll.vote2 += 1;
			}
			return copyPoll;
		});
	});
}

</script>

    {#if poll && !isLoading}
        <div class="card mb-3 polls-container-box w-100">
            <div class="card-header polls gap-2">
                <div class="inner-poll-header">
                    <h4>{poll.question}</h4>
                    <span>Stemmer: {totalVotes}</span>
                </div>
                <Button on:click={() => deletePoll(poll)}>X</Button>
            </div>
            <div class="card-body">
                <div class="list-group gap-1">
                    <div class="pollbutton">
                        <button on:click={() => addVote(1)} disabled={!isActive}><strong>{poll.answer1}</strong></button>
                        <div class="pollbars">
                            <div class={poll.vote1 >= poll.vote2 ? 'win' : 'loss'} style="width: {percentA}%;" transition:scale={{duration: 300}}></div>
                        </div>
                        <div class="vote-score">{percentA}%</div>
                    </div>
                    <div class="pollbutton ">
                        <button on:click={() => addVote(2)} disabled={!isActive}><strong>{poll.answer2}</strong></button>
                        <div class="pollbars">
                            <div class={poll.vote2 >= poll.vote1 ? 'win' : 'loss'} style="width: {percentB}%;" transition:scale={{duration: 300}}></div>
                        </div>
                        <div class="vote-score">{percentB}%</div>
                    </div>
                </div>
            </div>
            <div>
                <p>{isActive ? `Avsluttes: ${new Date(poll.date).toLocaleString()}` : 'Avstemning er avsluttet'}</p>
            </div>
        </div>
    {:else}
        <div class="card mb-3 polls-container">
            <div class="d-flex justify-content-center align-items-center h-100">
                <div class="spinner-border text-success" role="status">
                    <span class="visually-hidden">Laster...</span>
                </div>
            </div>
        </div>
    {/if}


<style>
    .win {
        background-color: #45c496;
        border-left: 2px solid #45c496;
    }
    .loss {
        background-color: #d91b42;
        border-left: 2px solid #d91b42;
    }
    button:disabled {
        pointer-events: none;
    }

    .polls {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px;
    }

    .polls-container-box {
        min-width: 280px;
    }
    .pollbars {
        width: 100%;
        height: 28px;
        font-weight: bold;
    }
    .pollbars > div {
        height: 100%;
        border-radius: 5px;
        transition: width 0.3s ease;
    }
    .pollbutton {
        position: relative;
    }
    .vote-score {
        position: absolute;
        top: 0;
        right: 0;
        font-weight: bold;
        padding: 1px;
        width: 60px;
        text-align: center;
    }
    .pollbutton button {
        background: none;
        border: none;
        position: absolute;
        width: 100%;
        left: 0;
        height: 28px;
        transition: all 0.3s ease;
    }
    .pollbutton button:hover {
        cursor: pointer;
        box-shadow: 0 0 10px lightgray;
        border-radius: 5px;
    }
    .polls-container {
        height: 170px;
        min-width: 250px;
    }
    .inner-poll-header {
        display: flex;
        flex-direction: column;
        align-items: start;
    }
</style>