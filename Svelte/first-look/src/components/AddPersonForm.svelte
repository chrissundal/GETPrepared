<script>
	export let toggleModal;
	import { selectedScamPayment } from "./Scams.svelte"

	let yearInput;
	let cvcInput;
	let scamPayment = selectedScamPayment();

	let user = {
		type: '',
		name: '',
		cardNumber: '',
		month: '',
		year: '',
		cvc: '',
        gender: [],
        occupation: '',
        payment: scamPayment
	}
	const handleInput = (event, maxLength, nextField) => {
		const input = event.target;
		if (input.value.length >= maxLength) {
			input.value = input.value.slice(0, maxLength);
			if (nextField) {
				nextField.focus();
			}
		}
	}
	const handleSubmit = () => {
		console.log(user);
		toggleModal()
	}
	const setPaymentMethod = (method) => {
		user.type = method;
	}

	// function setGender(gender) {
	// 	if (user.gender.includes(gender)) {
	// 		user.gender = user.gender.filter(g => g !== gender);
	// 	} else {
	// 		user.gender = [...user.gender, gender];
	// 	}
	// }
</script>

<main>
    <h3>{scamPayment}kr</h3>
    <form on:submit|preventDefault={handleSubmit}>
        <input type="text" placeholder="Navn" bind:value={user.name} required><br>
        <legend>Betalingsalternativer:</legend>
        <label>
            <input type="radio" name="payment" value="visa" on:change={() => setPaymentMethod('visa')}> Visa
        </label>
        <label>
            <input type="radio" name="payment" value="vipps" on:change={() => setPaymentMethod('vipps')}> Vipps
        </label>
        <label>
            <input type="radio" name="payment" value="klarna" on:change={() => setPaymentMethod('klarna')}> Klarna
        </label>
        <br>
        <label>Kjønn:</label>
<!--        <input type="checkbox" checked={user.gender.includes('male')} on:change={() => setGender('male')}> Mann-->
<!--        <input type="checkbox" checked={user.gender.includes('female')} on:change={() => setGender('female')}> Dame-->
<!--        <input type="checkbox" checked={user.gender.includes('none')} on:change={() => setGender('none')}> Vil ikke svare-->
        <input type="checkbox" bind:group={user.gender} value="male"> Mann
        <input type="checkbox" bind:group={user.gender} value="female"> Dame
        <input type="checkbox" bind:group={user.gender} value="none"> Ukjent
        <br>
        {#if user.type === 'visa'}
            <input type="text" placeholder="Kortnummer" bind:value={user.cardNumber} required>
            <div>
                <input type="number" min="1" max="12" placeholder="MM" bind:value={user.month} on:input={(e) => handleInput(e, 2, yearInput)} required>
                <input bind:this={yearInput} type="number" placeholder="YY" min="0" max="99" bind:value={user.year} on:input={(e) => handleInput(e, 2, cvcInput)} required>
                <input bind:this={cvcInput} type="number" placeholder="CVC" min="0" max="999" bind:value={user.cvc} on:input={(e) => handleInput(e, 3, null)} required>
            </div>
        {:else}
            <p>Ikke tilgjengelig</p>
        {/if}
        <label>Arbeidsstatus:</label>
        <select bind:value={user.occupation}>
            <option value="Arbeider">Arbeider</option>
            <option value="Leder">Leder</option>
            <option value="Direktør">Direktør</option>
            <option value="Student">Student</option>
            <option value="Arbeidsledig">Arbeidsledig</option>
        </select>
        <br>
        <button type="submit">Betal</button>
    </form>
</main>

<style>

</style>