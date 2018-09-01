import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

console.log(` _                                         _
| |__   ___  _ __  _   _ ___    __ _ _   _(_)____
| '_ \\ / _ \\| '_ \\| | | / __|  / _\` | | | | |_  /
| |_) | (_) | | | | |_| \\__ \\ | (_| | |_| | |/ / 
|_.__/ \\___/|_| |_|\\__,_|___/  \\__, |\\__,_|_/___|
                                  |_|            
`)
console.log("앗! 콘솔을 켠 당신! 보너스 퀴즈를 풀어보시겠어요?")
console.log("관심이 있으시면 yes를 입력하세요.")

window.yes = `문제를 시작합니다.\n 2018년 플래닛 해커톤의 모티브가 된 애니메이션의 이름을 입력해주세요`

window["지구방위대"] = "정답입니다. 마이쮸를 드리겠습니다"