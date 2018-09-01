<template>
    <div class="complete">
        <p class="icon-body">👍</p>
        <h1>머그잔 인증완료!</h1>
        <h2>머그잔을 이용한 당신은</h2>
        <h2>환경 히어로</h2>
        <h2>이제 WiFi를 마음껏 즐기세요~</h2>
        <div class="btn-box">
            <button @click="moveToHome()">확인</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'cameraResult',
        methods:{
            moveToHome(){
                this.$router.push('/')
            }
        }
    }
</script>
<style scoped>
    .complete {
        width: 1000px;
        padding: 50px 0;
        margin: auto;
    }

    .complete h1,
    .complete h2{
        color: #ffffff;
    }

    .icon-body {
        font-size: 4em;
        margin-bottom: 0;
    }

    .btn-box {
        margin: 110px auto 15px auto;
    }

    .body-box {

        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 5px 16px 1px rgba(157, 157, 157, 0.5);
        padding: 45px;
        margin-bottom: 25px;
    }

    .btn-box button {
        width: 100%;
        padding: 20px;
        font-size: 1.5em;
        border-radius: 8px;
        background-color: #00a878;
        border: none;
        color: #ffffff;
        font-weight: bold;
    }

    @media screen and (max-width: 992px) {
        .complete {
            width: auto;
            padding: 20px;
        }

        .btn-box {
            width: 100%;
            flex-direction: column;
        }

        .body-box h1 {
            font-size: 1.5em;
        }
    }
</style>