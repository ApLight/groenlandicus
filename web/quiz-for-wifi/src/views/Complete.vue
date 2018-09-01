<template>
    <div class="complete">
        <div class="body-box">
            <p class="icon-body">🎉 </p>
            <h1>축하합니다!</h1>
            <h2>퀴즈 3개를 모두 맞추셨습니다.</h2>
            <h2>WiFi에 연결되었어요</h2>
        </div>
        <div class="btn-box">
            <button @click="">확인</button>
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
        width: 1000px;
        padding: 50px 0;
        margin: auto;
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

    .btn-box button{
        width: 100%;
        padding: 20px ;
        font-size: 1.5em;
        border-radius: 8px;
        background-color: #00a878;
        border: none;
        color: #ffffff;
        font-weight: bold;
    }

    @media screen and (max-width: 992px) {
        .complete {
            padding: 20px;
            width: auto;
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