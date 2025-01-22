const app = Vue.createApp({
    //data, functions
    //template: '<h2>i am the template</h2>'
    data(){
        return {
            showBooks: false,
            //inputTitle: '',
            //title: 'The Final Empire',
            //author: 'Brandon Sanderson',
            books: [
                { title: 'Ikigai', author: 'Hector Garcia', img: 'assets/th (1).jpg', isFav: true},
                { title: 'Byens spor', author: 'Lars Saabye', img: 'assets/th.jpg', isFav: false },
                { title: 'The confession', author: 'John Grisham', img: 'assets/thd.jpg', isFav: true },
            ],
            //url: 'http://www.vg.no',
            //age: 45,
            //x: 0,
            //y: 0,
        }
    },
    methods: {
        // changeTitle(titleString){
        //     //title='The Next Empire'
        //     this.title = titleString;
        // },
        changeTitle(){
            this.title = this.inputTitle;
        },
        changeShowBooks(){
            this.showBooks = !this.showBooks;
        },
        toggleFav(book){
            book.isFav = !book.isFav;
        }
        // handleEvent(e, data){
        //     console.log(e, e.type)
        //     if(data){
        //         console.log(data)
        //     }
        // },
        // handleMouseMove(e){
        //     this.x = e.offsetX;
        //     this.y = e.offsetY;
        // }

    },
    computed: {
        filteredBooks(){
            return this.books.filter(book => book.isFav)
        }
    },
})

app.mount('#app')