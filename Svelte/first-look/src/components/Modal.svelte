<script>
    export let closeModal;
</script>

<main>
    <div class="backdrop">
        <div class="modal">
            <p>Din grand-tante fra sveits har dessverre gått bort, men gode nyheter. Du har arvet en masse penger! Eneste som trengs er at du betaler inn noe kroner i frakt! </p>
            <button on:click={closeModal}>Lukk</button>
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
</style>