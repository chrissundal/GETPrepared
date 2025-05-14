<script>
	export let data;
	let guide = {};
    $: {
        if(data.guide) {
            guide = data.guide;
        }
    }
</script>

<div class="details">
    <h2>{guide.title}</h2>
    <p>{guide.body}</p>
</div>

<style>
    .details {
        text-align: center;
        display: block;
        margin: 20px auto;
    }
</style>

