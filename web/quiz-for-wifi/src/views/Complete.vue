<template>
    <div class="complete">

        <div class="body-box">
            <p class="icon-body">🎉 </p>
            <h1>축하합니다!</h1>
            <h2>퀴즈 3개를 모두 맞추셨습니다.</h2>
            <h2>WiFi에 연결되었어요</h2>
        </div>
        <div class="btn-box">
            <router-link to="#" @click="">확인</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'complete',
    }
</script>
<style scoped>
    .complete {
        padding: 50px 0;
    }

    .icon-body {
        font-size: 3em;
    }

    .btn-box {
        width: 1000px;
        margin: 15px auto;
    }

    .body-box {

        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 5px 16px 1px rgba(157, 157, 157, 0.5);
        padding: 45px;
        margin-bottom: 25px;
    }

    @media screen and (max-width: 992px) {
        .complete {
            padding: 20px;
        }

        .btn-box {
            width: 100%;
            flex-direction: column;
        }

        .body-box h1 {
            font-size: 20px;
        }
    }
</style>