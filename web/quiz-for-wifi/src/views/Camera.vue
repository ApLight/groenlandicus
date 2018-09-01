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
                // client: undefined
            }
        },
        mounted: function () {
            let video = this.$el.querySelector('.video');
            navigator.mediaDevices.getUserMedia({video: true}).then((stream) => {
                    video.srcObject = stream
                }
            );
            video.height = window.innerHeight

            // this.client = new vision.ImageAnnotatorClient();

        },
        methods: {
            captureImage() {
                let canvas = this.$el.querySelector('#snapshot');
                let context = canvas.getContext('2d');
                let video = this.$el.querySelector('.video');
                // Draw the video frame to the canvas.
                context.drawImage(video, 0, 0, canvas.width,
                    canvas.height);

                // Creates a client
                // const client = new vision.ImageAnnotatorClient();
                //
                // // Performs label detection on the image file
                // client
                //     .labelDetection('./assets/logo.png')
                //     .then(results => {
                //         const labels = results[0].labelAnnotations;
                //
                //         console.log('Labels:');
                //         labels.forEach(label => console.log(label.description));
                //     })
                //     .catch(err => {
                //         console.error('ERROR:', err);
                //     });
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