<script>
	import RouteTransition from "./RouteTransition.svelte";
	import { pollsStore, activeItemStore } from "../store/Stores.svelte";
	import { push } from 'svelte-spa-router';
	import Button from "../shared/Button.svelte";
	import { v4 as uuidv4 } from 'uuid';

	let newPoll = {
		id: uuidv4(),
		question: "",
		answer1: "",
        answer2: "",
		vote1: 0,
		vote2: 0,
    };
	let error = {
		question: "",
		answer1: "",
		answer2: ""
	};
	let valid = false;

	const handleSubmit = () => {
		valid = true;
		validation('question');
		validation('answer1');
		validation('answer2');

		if (valid) {
		    pollsStore.update(polls => [...polls, newPoll]);
		    activeItemStore.set("Polls");
		    push('/');
        }
	}
	const validation = (input) => {
		let dict = {
			question: 'Spørsmål',
			answer1: 'Alternativ 1',
			answer2: 'Alternativ 2',
		}

		if (input === 'question') {
			if (newPoll[input].trim().length < 5) {
				valid = false;
				error[input] = `${dict[input]} må være minst 5 tegn`;
			} else {
				error[input] = '';
			}
		} else {
			if (newPoll[input].trim().length < 2) {
				valid = false;
				error[input] = `${dict[input]} må være minst 2 tegn`;
			} else {
				error[input] = '';
			}
		}
		if(newPoll.answer1.toLowerCase() === newPoll.answer2.toLowerCase() && newPoll.answer1.trim().length > 0) {
			valid = false
            error.answer2 = "Alternativ 1 kan ikke være likt alternativ 2"
        }
	}


</script>

<RouteTransition>
    <form on:submit|preventDefault={handleSubmit} class="my-container">
        <div class="form-floating mb-3">
            <input type="text" class="form-control" name="floatingInput" placeholder="" bind:value={newPoll.question}>
            <label for="floatingInput">Nytt spørsmål</label>
            <div class="text-danger">{error.question}</div>
        </div>
        <div class="form-floating mb-3">
            <input type="text" class="form-control" name="floatingInput" placeholder="" bind:value={newPoll.answer1}>
            <label for="floatingInput">Alternativ 1</label>
            <div class="text-danger">{error.answer1}</div>
        </div>
        <div class="form-floating mb-3">
            <input type="text" class="form-control" name="floatingInput" placeholder="" bind:value={newPoll.answer2}>
            <label for="floatingInput">Alternativ 2</label>
            <div class="text-danger">{error.answer2}</div>
        </div>
<!--        <div class="container">-->
<!--            <p class="text-bg-danger">{error.question || error.answer1 || error.answer2}</p>-->
<!--        </div>-->
        <div class="container">
            <Button type="secondary" inverse={true} flat={false}>Legg til</Button>
        </div>
    </form>
</RouteTransition>

<style>


</style>