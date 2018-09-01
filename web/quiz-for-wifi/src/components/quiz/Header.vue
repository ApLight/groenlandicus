<template>
    <div class="header">
        <h1>{{ msg }}</h1>
    </div>
</template>

<script>
    export default {
        name: 'Header',
        props: {
            msg: String
        }
    }
</script>

<style scoped>
    h1{
        color: #ffffff;
    }
    @media screen and (max-width: 992px) {
        h1{
            font-size: 20px;
            margin-bottom: 0;
        }
    }
</style>
