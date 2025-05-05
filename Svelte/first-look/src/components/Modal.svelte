<script>
    import { selectedScam } from "./Scams.svelte";

	export let isPromo = false;
	export let togglePromo;
</script>

<main>
<!--    on:click sender ett emit, self er event modifier -->
    <div class="backdrop" class:promo={isPromo} on:click|self>
        <div class="modal">
            <slot name="title"></slot>
            <p>{selectedScam()}</p>
            <slot></slot>
            <button on:click={togglePromo}>Bytt klasse</button>
        </div>
    </div>
</main>

<style>
.backdrop {
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    background-color: rgba(0,0,0,0.8);
}
.modal {
    padding: 10px;
    border-radius: 10px;
    max-width: 400px;
    margin: 10% auto;
    text-align: center;
    background-color: white;
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
.promo .modal{
    background: crimson;
    color: white;
}
</style>