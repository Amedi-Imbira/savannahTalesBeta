import './assets/main.css'
import './assets/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import axios from 'axios'

import App from './App.vue'
import router from './router'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


/* import specific icons */
import { faBell, faBookmark, faMoon, faSearch, faUserSecret, faPlus, faReply, faHeart, faComment, faEllipsis, faBookBookmark } from '@fortawesome/free-solid-svg-icons'
import { faAddressBook } from '@fortawesome/free-regular-svg-icons'


/* add icons to the library */
library.add(faSearch, faBookmark, faBell, faMoon, faPlus, faReply, faHeart, faComment, faEllipsis, faAddressBook, faBookBookmark,)

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(createPinia())
app.use(router)

app.mount('#app')
