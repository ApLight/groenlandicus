<template>
    <div class="camera">
        <source class="video" autoplay></source>
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
            navigator.mediaDevices.getUserMedia(this.constraints).then((stream) => {
                    this.$el.querySelector('.video').srcObject = stream
                }
            );
        }
    }
</script>
