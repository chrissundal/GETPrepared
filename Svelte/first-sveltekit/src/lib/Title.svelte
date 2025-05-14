<script>
    let title = 'Home';
    export { title };
</script>
    <div class="title">
        <img src="/controller.svg" alt="site logo">
        <a href="/">
            <h1>{title}</h1>
        </a>
    </div>

<style>
    .title {
        display: flex;
        align-items: center;
    }
    .title img {
        display: inline-block;
        filter: invert(88%) sepia(18%) saturate(886%) hue-rotate(199deg) brightness(100%) contrast(90%);
    }
    .title h1 {
        margin-left: 10px;
    }
    a {
        text-decoration: none;
    }
</style>