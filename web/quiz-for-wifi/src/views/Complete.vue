<template>
    <div class="complete">
        <div class="toast">
            <img class="icon-100" src="../assets/JGT.png" alt="">
            <div class="text">
                <h1>설기를 키워 보아요.</h1>
                <h3>머그잔 이용시, 포인트 획득!</h3>
            </div>
            <a href="#" class="btn-shortcut">앱 바로가기</a>
        </div>
        <div class="body-box">
            <p class="icon-body">🎉 </p>
            <h1>축하합니다!</h1>
            <h2>퀴즈 3개를 모두 맞추셨습니다.</h2>
            <h2>WiFi에 연결되었어요</h2>
        </div>
        <div class="btn-box">
            <button @click="moveToHome()">확인</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'complete',
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
        padding: 120px 0 50px 0;
        margin: auto;
    }

    .toast {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 90px;
        background-color: rgba(255, 255, 255, .8);
        z-index: 10000;
        padding: 15px 7.5px;
    }

    .toast .text{
        display: inline-block;
        vertical-align: middle;
    }

    .toast .text h1,
    .toast .text h3{
        margin: 0 50px 0 0;
        text-align: left;
    }

    .icon-100 {
        width: 90px;
        vertical-align: middle;
        margin-right: 10px;
    }

    .btn-shortcut {
        background-color: #3592ff;
        border-radius: 4.8px;
        border: none;
        padding: 15px 40px;
        color: #ffffff;
        text-decoration: none;
    }

    .icon-body {
        font-size: 3em;
    }

    .btn-box {
        margin: 15px auto;
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
            padding-left: 20px;
            padding-right: 20px;
            width: auto;
        }

        .btn-box {
            width: 100%;
            flex-direction: column;
        }

        .body-box h1 {
            font-size: 20px;
        }

        .toast {
            height: 70px;
            padding: 15px 7.5px;
        }

        .toast .text h1{
            font-size: 1.1em;
            margin: 0 10px 0 0;
        }

        .toast .text h3{
            margin: 0 10px 0 0;
            font-size: 0.9em;
        }

        .icon-100 {
            width: 70px;
            margin-right: 10px;
        }

        .btn-shortcut {
            padding: 15px 7.5px;
            font-size: 16px;
        }
    }
</style>