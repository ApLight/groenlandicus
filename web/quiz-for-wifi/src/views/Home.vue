<template>
    <div class="home">
        <img class="icon-wifi" src="../assets/icon-wifi.png">
        <HelloWorld msg="OO카페의 WiFi에 접속하려면"/>
        <HelloWorld msg="둘 중 하나를 선택해주세요"/>


        <div class="btn-box">
            <router-link class="btn-default btn-pass" to="/camera">
                <p class="link-icon">☕️</p>
                <p class="text">머그잔 인증샷!</p>
            </router-link>
            <router-link class="btn-default btn-quiz" to="/quiz">
                <p class="link-icon">⭕ ❌️</p>
                <p class="text">환경 퀴즈 풀기</p>
            </router-link>
        </div>

    </div>
</template>

<script>
    // @ is an alias to /src
    import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'home',
        components: {
            HelloWorld,
        }
    }
</script>
<style>
    body {
        background-color: #2ee5a3;
    }
</style>
<style scoped>
    .home{
        padding: 50px 0;
    }
    .icon-wifi {
        width: 75px;
    }

    .btn-box {
        width: 1000px;
        margin: 15px auto;
        display: flex;
        flex-direction: row;
    }

    .btn-default {
        font-size: 1em;
        width: 100%;
        padding: 45px 15px;
        text-decoration: none;
        display: block;

        border-radius: 7.7px;
        background-color: #ffffff;
        box-shadow: 0 6px 21px 2px rgba(157, 157, 157, 0.5);
    }

    .btn-pass{
        margin-right: 10px;
    }

    .btn-quiz{
        margin-left: 10px;
    }

    .btn-default p{
        margin: 0;
    }

    .link-icon{
        font-size: 5em;
        padding: 25px 0;
    }
    .btn-default .text{
        font-size: 2.5em;
    }

    @media screen and (max-width: 992px) {
        .home{
            padding: 20px;
        }
        .btn-box {
            width: 100%;
            flex-direction: column;
        }
        .btn-default{
            padding: 30px 10px;
            width: auto;
            margin-bottom: 20px;
        }
        .btn-pass{
            margin-right: 0px;
        }

        .btn-quiz{
            margin-left: 0px;
        }
        .link-icon{
            font-size: 4em;
        }
        .btn-default .text{
            font-size: 1.5em;
        }
    }
</style>