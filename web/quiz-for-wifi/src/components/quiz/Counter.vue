<template>
    <div class="counter">
        <h1>{{passCount}} / {{ totalCount }} </h1>
    </div>
</template>

<script>
    export default {
        name: 'Counter',
        props: {
            totalCount: Number,
            passCount: Number,
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
        }
    }
</style>
