<template>
    <div v-if="userAnswer === null" class="quiz">
        <div class="header-box">
            <!--<img v-if="this.currentIndex === 1" class="icon-wifi" src="../assets/icon-wifi.png">-->
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
    <div v-else-if="userAnswer === true" class="quiz-result quiz-result-success">
        <div class="header-box">
            <Header msg="👏 짝짝짝! 정답이에요!"></Header>
            <Counter :totalCount="totalCount" :passCount="passCount"></Counter>
        </div>
        <div class="body-box">
            <h1 class="quiz-problem">{{quiz[quizIndex].problem}}</h1>
            <h1 class="quiz-answer">
                <span class="text-answer">정답 : </span>
                <img class="icon-answer icon-yes" v-if="quiz[quizIndex].answer" src="../assets/icon-yes.png" alt="">
                <img class="icon-answer icon-no" v-else src="../assets/icon-no.png" alt="">
            </h1>
            <h1 class="quiz-explanation">{{quiz[quizIndex].explanation}}</h1>
        </div>
        <div class="btn-box">
            <button @click="moveToNextProblem(false)">머그잔 인증 바로가기</button>
            <button @click="moveToNextProblem(true)">확인</button>
        </div>
    </div>
    <div v-else-if="userAnswer === false" class="quiz-result quiz-result-fail">
        <div class="header-box">
            <Header msg="😭 앗... 틀렸어요"></Header>
            <Counter :totalCount="totalCount" :passCount="passCount"></Counter>
        </div>
        <div class="body-box">
            <h1 class="quiz-problem">{{quiz[quizIndex].problem}}</h1>
            <h1 class="quiz-answer">
                <span class="text-answer">정답 : </span>
                <img class="icon-answer icon-yes" v-if="quiz[quizIndex].answer" src="../assets/icon-yes.png" alt="">
                <img class="icon-answer icon-no" v-else src="../assets/icon-no.png" alt="">
            </h1>
            <h1 class="quiz-explanation">{{quiz[quizIndex].explanation}}</h1>
        </div>
        <div class="btn-box">
            <button @click="moveToNextProblem(false)">머그잔 인증 바로가기</button>
            <button @click="moveToNextProblem(true)">확인</button>
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
                quiz: [
                    {
                        "id": 12,
                        "problem": "다 쓴 핸드폰 배터리는 일반 쓰레기봉투에 버려요.",
                        "answer": false,
                        "explanation": "배터리는 발열 위험이 있으므로 +,-극을 테이프로 막고 별도의 수거함에 버려야 해요.",
                        "img_url": ""
                    },
                    {
                        "id": 2,
                        "problem": "유리컵은 유리병과 달리 일반 쓰레기에요.",
                        "answer": true,
                        "explanation": "유리컵은 유리병과는 다르게 분리수거 항목에 포함되지 않아요.",
                        "img_url": ""
                    },
                    {
                        "id": 8,
                        "problem": "나무젓가락은 나무 재질이므로 종이류로 분리수거해야 한다.",
                        "answer": false,
                        "explanation": "나무젓가락은 일반 종이와 달리 재활용되지 않으므로 종량제 봉투에 버려주세요.",
                        "img_url": ""
                    }
                ],
                quizIndex: 0,
            }
        },
        methods: {
            fetchData() {
                const baseURI = 'http://35.226.157.77';

                this.$http.get(`${baseURI}/quizzes/`)
                    .then((result) => {
                        this.quiz = result.data.quizzes;
                        console.log(result.data.quizzes)
                    })
                    .catch((e) => {
                        console.log(e)
                    })

                // console.log(this.quiz);
            },
            isCorrectAnswer(answer) {
                console.log(this.quiz[this.quizIndex].answer)
                //TODO: 답확인
                if (answer === this.quiz[this.quizIndex].answer) {
                    this.passCount++;
                    console.log("정답!")
                    this.userAnswer = true;
                } else {
                    console.log("오답!ㅠㅠㅠ")
                    this.userAnswer = false;
                }

                // if(this.passCount === 3){
                //     this.$router.push('complete')
                // }
            },
            moveToNextProblem(isTrue) {
                //다음 문제로 이동
                if (isTrue) {
                    this.currentIndex++;
                    this.quizIndex++;
                    this.userAnswer = null;

                    if (this.passCount === this.totalCount) {
                        this.$router.push('/complete')
                    }
                    if (this.quizIndex > 2) {
                        this.fetchData();
                        this.currentIndex = 1;
                        this.quizIndex = 0;
                    }
                } else {
                    this.$router.push('/camera');
                }
            }
        }
        ,
        computed: {
            changeHeaderText() {
                if (this.userAnswer === null) {
                    switch (this.passCount) {
                        case 0:
                            return "📡 퀴즈 3개를 맞추면 WiFi에 연결할 수 있어요!";
                        case 1:
                            return "👍 당신은 분리수거 천재?";
                        case 2:
                            return "🤩 하나만 더 맞추면 돼요!"
                    }
                } else if (this.userAnswer === false) {
                    return "틀렸어요 ㅠㅠ";
                } else {
                    return ""
                }

            }
        },
        created() {
            // 뷰가 생성되고 데이터가 이미 감시 되고 있을 때 데이터를 가져온다.
            this.fetchData()
        }

    }
</script>

<style scoped>
    .quiz,.quiz-result {
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
        justify-content: space-between;
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

    .quiz-result .icon-answer {
        width: 30px;
    }

    .quiz-result .text-answer {
        font-size: 40px;
    }

    .quiz-result .btn-box {
        display: flex;
    }

    .quiz-result .btn-box button:hover {
        cursor: pointer;
        opacity: 0.8;
    }

    .quiz-result .btn-box button {
        width: 100%;
        padding: 20px;
        font-size: 1.5em;
        border-radius: 8px;
        background-color: #00a878;
        border: none;
        color: #ffffff;
        font-weight: bold;
    }

    .quiz-result .btn-box button:first-child {
        margin-right: 10px;
    }

    .quiz-result .btn-box button:last-child {
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

        .quiz-result .btn-box {
            flex-direction: column;
        }

        .quiz-result .btn-box button:first-child {
            margin: 0;
            margin-bottom: 10px;
        }

        .quiz-result .btn-box button:last-child {
            margin: 0;
            margin-top: 10px;
        }
    }
</style>
