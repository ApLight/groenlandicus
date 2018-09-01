<template>
    <div class="camera">
        <video class="video" autoplay></video>
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
        }
    }
</script>
