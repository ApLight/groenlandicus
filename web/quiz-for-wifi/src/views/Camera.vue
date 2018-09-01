<template>
    <div class="camera">
        <video class="video" autoplay></video>
        <button id="capture" @click="captureImage()">Capture</button>
        <canvas id="snapshot" width=320 height=240></canvas>
    </div>
</template>

<script>
    export default {
        name: 'camera',
        data: function () {
            return {
                constraints: { video: true },
            }
        },
        mounted: function () {
            let video = this.$el.querySelector('.video');
            navigator.mediaDevices.getUserMedia({video: true}).then((stream) => {
                    video.srcObject = stream
                }
            );
            video.height = window.innerHeight

        },
        methods:{
            captureImage(){
                let canvas = this.$el.querySelector('#snapshot');
                let context = canvas.getContext('2d');
                let video = this.$el.querySelector('.video');
                // Draw the video frame to the canvas.
                context.drawImage(video, 0, 0, canvas.width,
                    canvas.height);
            },
        }
    }
</script>
<style scoped>
    .camera{
        width: 1000px;
        height: 100%;
        margin: auto;
    }
    .camera video{
        position: fixed; right: 0; bottom: 0;
        min-width: 100%; min-height: 100%;
        width: auto; height: auto; z-index: -100;
        top: 50%;
        left: 50%;
        /* bring your own prefixes */
        transform: translate(-50%, -50%);
    }
    @media screen and (max-width: 992px) {
        .camera{
            width: auto;
            margin: 0;
            padding: 0;
        }

    }
</style>