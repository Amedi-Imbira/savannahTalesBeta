import './assets/main.css'
import './assets/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import axios from 'axios'

import App from './App.vue'
import router from './router'

// Vue.prototype.$http = axios;

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faBell, faBookmark, faMoon, faSearch, faUserSecret, faPlus } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret, faSearch, faBookmark, faBell, faMoon, faPlus)

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(createPinia())
app.use(router)

app.mount('#app')
