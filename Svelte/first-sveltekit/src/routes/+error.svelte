<script>
	import { page } from '$app/state';
    let status = page.status;
	let message = page.error.message;
</script>

<div class="error-container">
    <h1>{status}:</h1>
    <p>{message}</p>
    <a href="/">Gå tilbake til forsiden</a>
</div>

<style>
    .error-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        text-align: center;
        padding: 2rem;
    }

    h1 {
        color: #e74c3c;
    }
</style>


