<script>
	export let activeItem;
	export let items;
	export let onLinkChange;
</script>

<main>
    <div class="links">
        {#each items as item}
            <button class:active={item === activeItem} disabled={item === activeItem} on:click={() => onLinkChange(item)}>{item}</button>
        {/each}
    </div>
</main>

<style>
    .links {
        list-style: none;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        margin-right: 5px;
    }

    .active {
        font-weight: bold;
        color: #bdbcbc;
        border: 1px solid #bdbcbc;
        border-radius: 8px;
        padding: 0.2em 0.6em;
        cursor: default;
    }
    button {
        cursor: pointer;
        border: none;
        background: none;
        padding: 0;
        font: inherit;
        color: inherit;
    }
</style>