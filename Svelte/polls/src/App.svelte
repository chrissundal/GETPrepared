<script>
	import Header from "./components/Header.svelte";
	import Footer from "./components/Footer.svelte";
	import CreateNewPoll from "./components/CreateNewPoll.svelte";
	import Router from 'svelte-spa-router';
	import About from "./components/About.svelte";
	import Home from "./components/Home.svelte";

	const routes = {
		'/': Home,
		'/about': About,
        '/create': CreateNewPoll,
	};

</script>

<main>
    <Header />
        <Router {routes} />
    <Footer />
</main>

<style>


</style>
