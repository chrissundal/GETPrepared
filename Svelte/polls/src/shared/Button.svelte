<script>
    export let type = 'primary';
	export let flat = false;
	export let inverse = false;
</script>

<button class={type} class:flat={flat} class:inverse={inverse} on:click>
    <slot></slot>
</button>

<style>
    button {
        padding: 8px 12px;
        border-radius: 6px;
        border: none;
        cursor: pointer;
        font-weight: bold;
        box-shadow: 1px 2px 3px rgba(0,0,0,0.2);
    }
    .primary {
        background-color: #d91b42;
        color: white;
    }
    .secondary {
        background-color: #45c496;
        color: white;
    }
    .flat {
        box-shadow: none;
    }
    .primary.inverse {
        background-color: white;
        color: #d91b42;
    }
    .secondary.inverse {
        background-color: white;
        color: #45c496;
    }
</style>