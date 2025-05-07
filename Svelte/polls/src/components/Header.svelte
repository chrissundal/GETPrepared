<script>
	import { push } from 'svelte-spa-router';
	import { link } from 'svelte-spa-router';
	import Links from "../shared/Links.svelte";
	import { activeItemStore } from "../store/Stores.svelte";

	let items = ['Polls','Legg til ny poll','Om oss']
    let activeItem = 'Polls';
	let isNavOpen = false;

	$: activeItem = $activeItemStore;

	const linkChange = (item) => {
		activeItemStore.set(item);

		if (item === 'Legg til ny poll') {
			push('/create')
		} else if (item === 'Om oss') {
			push('/about')
		} else {
			push('/');
		}

		isNavOpen = false;
	}
	const toggleMenu = () => {
		isNavOpen = !isNavOpen;
	}

</script>

<header>
    <div class="container">
        <div class="navbar">
            <div class="logo-container">
                <a href="/" use:link class="logo-box">
                    <span>Klikk & Krangle</span>
                </a>
            </div>

            <button class="hamburger d-md-none" on:click={toggleMenu} aria-label="Meny">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>

            <div class="nav-links d-none d-md-flex">
                <Links {activeItem} {items} onLinkChange={linkChange}/>
            </div>
        </div>

        {#if isNavOpen}
            <div class="mobile-menu d-md-none">
                <Links {activeItem} {items} onLinkChange={linkChange}/>
            </div>
        {/if}
    </div>
</header>

<style>
    header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        color: white;
        padding: 1rem 0;
        z-index: 1000;
        background: rgba(36, 36, 36, 0.87);
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .logo-box {
        text-decoration: none;
    }

    .logo-box span {
        font-size: clamp(1.4rem, 3vw, 3rem);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        cursor: pointer;
        color: white;
        font-family: Minnie;
        transition: all 0.4s;
    }

    .logo-box span:hover {
        transform: scale(1.01);
    }

    .nav-links {
        justify-content: center;
        width: 100%;
    }

    .hamburger {
        position: absolute;
        right: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        width: 30px;
        height: 21px;
        background: transparent;
        border: none;
        cursor: pointer;
        padding: 0;
        z-index: 10;
    }

    .hamburger-line {
        display: block;
        width: 100%;
        height: 3px;
        background-color: white;
        border-radius: 10px;
    }

    .mobile-menu {
        margin-top: 5px;
        padding: 5px;
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 5px;
    }

    @media (min-width: 768px) {
        .logo-container {
            width: auto;
            margin: 0 auto;
        }
    }
</style>


