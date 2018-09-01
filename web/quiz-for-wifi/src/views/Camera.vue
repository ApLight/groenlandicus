<template>
    <div class="camera">
        <video class="video" autoplay></video>
        <button class="btn-back" @click="moveToHome()">돌아가기</button>
        <button id="capture" @click="captureImage()">머그컵 사진 캡쳐</button>
        <canvas id="snapshot" width=320 height=240></canvas>
    </div>
</template>

<script>
    export default {
        name: 'camera',
        data: function () {
            return {
                constraints: {video: true},
                loader: false,
                result: false,
                apiKey: "AIzaSyBBNonS0K3J-lZtXH6_qZJy9DTdd4s7XE4",  //google cloud api  Browser key
                data: {               //type vision api Request
                    "requests": [{
                        "features": [{
                            "type": "LABEL_DETECTION"
                        }],
                        "image": {
                            "content": null
                        }
                    }]
                }
            }
        },
        mounted: function () {
            const video = this.$el.querySelector('.video');
            navigator.mediaDevices.getUserMedia({video: true}).then((stream) => {
                    video.srcObject = stream
                    video.play();
                }
            );

        },
        methods: {
            captureImage() {
                const canvas = this.$el.querySelector('#snapshot');
                const context = canvas.getContext('2d');
                const video = this.$el.querySelector('.video');
                // Draw the video frame to the canvas.
                context.drawImage(video, 0, 0, canvas.width,
                    canvas.height);


                const vm = this;
                this.result = false;
                this.loader = true;

                const base64 = canvas.toDataURL();
                const finalImage = base64.replace("data:image/png;base64,", "");
                this.data.requests[0].image.content = finalImage;

                const baseURI = `https://vision.googleapis.com/v1/images:annotate?key=${this.apiKey}`;

                this.$http.post(`${baseURI}`,this.data)
                    .then(response => {
                        let detectResult = response.data.responses[0].labelAnnotations;

                        let count = 0;
                        // console.log(detectResult)
                        for(let i=0 ; i < detectResult.length; i++){
                            if( detectResult[i].description === 'bottle' || detectResult[i].description === 'glass'){
                                if(detectResult[i].topicality > 0.6)
                                    count++
                            }
                        }

                        if(count === 1){
                            this.$router.push('/camera/ok')
                        }else
                            this.$router.push('/')
                        vm.loader = false;
                        vm.result = true;
                    }).catch(error => {
                    console.log(error);
                })
                // .then((res) => {
                //     console.log(res)
                //     // const result = response.data.responses[0].faceAnnotations[0];
                //     vm.loader = false;
                //     vm.result = true;
                // })
                // .catch((e) => {
                //     console.log(e)
                // })
            },
            moveToHome() {
                this.$router.push('/')
            }
        }
    }
</script>
<style scoped>
    .camera {
        width: 1000px;
        height: 100%;
        margin: auto;
    }

    .camera video {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -100;
        top: 50%;
        left: 50%;
        /* bring your own prefixes */
        transform: translate(-50%, -50%);
    }

    button {
        width: 100%;
        padding: 20px;
        font-size: 1.5em;
        border-radius: 8px;
        background-color: #00a878;
        border: none;
        color: #ffffff;
        font-weight: bold;
    }

    .btn-back {
        background-color: lightskyblue;
    }

    @media screen and (max-width: 992px) {
        .camera {
            width: auto;
            margin: 0;
            padding: 0;
        }

    }
</style>