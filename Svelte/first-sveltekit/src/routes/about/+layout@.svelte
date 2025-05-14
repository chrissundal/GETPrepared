<script>
	import '../../styles/global.css'
	import Title from "$lib/Title.svelte";
</script>

<header>
    <Title title="About us"/>
    <div class="links">
        <a href="/">Home</a>
        <a href="/guides">Guides</a>
    </div>
</header>

<main>
    <slot></slot>
</main>

<footer>
    <p>Chris 2025 &copy;</p>
</footer>
<style>
    header {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 20px;
    }
    main {
        max-width: 960px;
        margin: 20px auto;
    }
    footer {
        text-align: center;
    }
    .links {
        margin-left: auto;
    }
    a {
        margin-left: 10px;
    }
</style>