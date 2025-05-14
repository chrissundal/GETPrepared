<script>
    import {goto} from "$app/navigation";

</script>


<div class="about">
    <h2>About us</h2>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque dolorum quas nesciunt perspiciatis, dolore, maxime voluptate nobis consectetur, eum beatae nisi quam corporis repellendus officia. Aut ipsam enim asperiores, doloribus natus qui autem minima? Possimus dignissimos corrupti aspernatur totam excepturi ad deserunt debitis error eaque in incidunt ea, autem iure ab animi numquam illo, nam, laborum eligendi. Est eos quas ullam quam tenetur aliquam sint a qui earum incidunt? Est ab, esse architecto recusandae et officiis temporibus necessitatibus ipsum explicabo quas sapiente aut aliquid provident autem. Eaque maxime asperiores a eius iure mollitia sapiente in deleniti facere, incidunt sint fugit?</p>
    <button on:click={() => goto('/')}>Go Home</button>
</div>
<style>
    .about {
        text-align: center;
        display: block;
        margin: 20px auto;
    }
</style>