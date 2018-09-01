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
            navigator.mediaDevices.getUserMedia({video: true}).then((stream) => {
                    this.$el.querySelector('.video').srcObject = stream
                }
            );
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
