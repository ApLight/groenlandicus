<template>
    <div v-if="userAnswer === null" class="quiz">
        <div class="header-box">
            <img v-if="this.currentIndex === 1" class="icon-wifi" src="../assets/icon-wifi.png">
            <Header :msg="changeHeaderText"></Header>
            <Counter :totalCount="totalCount" :passCount="passCount"></Counter>
        </div>
        <div class="body-box">
            <div class="icon-quiz">Quiz</div>
            <!--TODO: GET DATA - 문제 가져오기-->
            <h1>{{quiz[quizIndex].problem}}</h1>
            <img class="body-img" src="../assets/img-wind.png" alt="">
        </div>
        <div class="answer-container">
            <div class="btn-answer btn-yes" @click="isCorrectAnswer(true)">
                <img src="../assets/icon-yes.png" alt="">
            </div>
            <div class="btn-answer btn-no" @click="isCorrectAnswer(false)">
                <img src="../assets/icon-no.png" alt="">
            </div>
        </div>
    </div>
    <div v-else-if="userAnswer === true" class="complete">
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
    <div v-else-if="userAnswer === false" class="complete">
        <div class="body-box">
            <p class="icon-body">🎉 </p>
            <h1>틀렷!</h1>
            <h2>퀴즈 3개를 모두 맞추셨습니다.</h2>
            <h2>WiFi에 연결되었어요</h2>
        </div>
        <div class="btn-box">
            <router-link to="#">확인</router-link>
        </div>
    </div>
</template>


<script>
    // @ is an alias to /src
    import Header from '@/components/quiz/Header.vue'
    import Counter from '@/components/quiz/Counter.vue'

    export default {
        name: 'home',
        components: {
            Header,
            Counter
        },
        data: function () {
            return {
                passCount: 0,
                totalCount: 3,
                currentIndex: 1,
                userAnswer: null,
                quiz: undefined,
                quizIndex: 0,
            }
        },
        methods: {
            isCorrectAnswer(answer) {

                //TODO: 답확인
                if (answer === this.quiz[this.quizIndex].answer) {
                    console.log("정답!")
                    this.quizIndex++;
                    this.userAnswer = true;
                    // if(this.quizIndex > 2){
                    //     새요청 => 데이터 받아오기
                    // }
                } else {
                    this.userAnswer = false;
                }
                // this.passCount++;
                //
                // if(this.passCount === 3){
                //     this.$router.push('complete')
                // }
            }
        }
        ,
        computed: {
            changeHeaderText() {
                if (this.userAnswer === null) {
                    switch (this.passCount) {
                        case 0:
                            return "퀴즈 3개를 맞추면 WiFi에 연결할 수 있어요!";
                        case 1:
                            return "정답을 맞췄어요 ^_^";
                        case 2:
                            return "하나만 더 맞추면 돼요!"
                    }
                } else if(this.userAnswer === false){
                    return "틀렸어요 ㅠㅠ";
                } else{
                    return ""
                }

            }
        },
        created: function () {
            // const baseURI = 'http://35.226.157.77';
            //
            // let config = {
            //     headers: {
            //         // 'Content-type': 'application/json',
            //         'Access-Control-Allow-Origin': '*',
            //     }
            // };
            //
            // this.$http.get(`${baseURI}/quizzes/`, config)
            //     .then((result) => {
            //         console.log(result)
            //     })
            //     .catch((e) => {
            //         console.log(e)
            //     })
            //
            this.quiz = [
                {
                    "id": 9,
                    "problem": "프링*스 통은 종이 박스니까 종이류로 분리해요.",
                    "answer": false,
                    "explanation": "알루미늄, 종이가 붙어있어 재활용이 불가능해요.",
                    "img_url": ""
                },
                {
                    "id": 10,
                    "problem": "광고지, 과자 박스, A4용지는 모두 종이류로 분리수거할 수 있어요.",
                    "answer": false,
                    "explanation": "코팅된 광고지의 경우 재활용이 되지 않아 종이류가 아닌 일반 쓰레기로 버려야 해요.",
                    "img_url": ""
                },
                {
                    "id": 7,
                    "problem": "파뿌리는 일반 쓰레기에요.",
                    "answer": true,
                    "explanation": "양파껍질, 파뿌리 등 채소 껍질과 뿌리는 일반 쓰레기로 배출해야 해요.",
                    "img_url": ""
                }
            ]

            console.log(this.quiz);
        }

    }
</script>

<style scoped>
    .quiz {
        width: 1000px;
        margin: auto;
    }

    .icon-wifi {
        width: 50px;
    }

    .icon-quiz {
        width: 130.3px;
        height: 48.2px;
        border-radius: 24.1px;
        background-color: #11c85b;
        margin: auto;
        color: #ffffff;
        line-height: 48.2px;
        font-size: 20px;
        font-weight: bold;
    }

    .header-box {
        display: flex;
        align-items: center;
    }

    .body-box {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 5px 16px 1px rgba(157, 157, 157, 0.5);
        padding: 45px;
        margin-bottom: 25px;
    }

    .body-img {
        width: 250px;
    }

    .answer-container {
        width: 100%;
        display: flex;
        justify-content: center;
    }

    .btn-answer:hover {
        cursor: pointer;
        background-color: gainsboro;
    }

    .btn-answer {
        width: 100%;
        padding: 20px;

        background-color: #ffffff;
        box-shadow: 0 4px 32px 12px rgba(157, 157, 157, 0.5);
        border-radius: 12px;

        -webkit-transition: width 2s, height 2s, background-color 1s, -webkit-transform 2s ease-in-out;
        transition: width 2s, height 2s, background-color 1s, transform 2s ease-in-out;
        transform-origin: left top;
    }

    .btn-answer:hover img {
        transform: scale(1.2);
    }

    .btn-yes img, .btn-no img {
        width: 110px;
    }

    .btn-yes {
        margin-right: 10px;
    }

    .btn-no {
        margin-left: 10px;
    }

    /* On screens that are 992px or less, set the background color to blue */
    @media screen and (max-width: 992px) {
        .quiz {
            padding: 10px;
            width: auto;
        }

        .icon-quiz {
            width: 86px;
            height: 32px;
            border-radius: 24.1px;
            line-height: 32px;
            font-size: 16px;
        }

        .header-box {
            flex-direction: column;
        }

        .body-box h1 {
            font-size: 20px;
        }

        .body-img {
            width: 150px;
        }

        .btn-yes img, .btn-no img {
            width: 45px;
        }

        .btn-answer {
            padding: 25px;
        }
    }
</style>
