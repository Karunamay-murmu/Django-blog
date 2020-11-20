class Blog {
    constructor() { }
    static toggleSideMenu() {
        try {
            const burger = document.querySelector('#burger')
            const cross = document.querySelector('#cross')
            const nav = document.querySelector('#navigation-menu')

            burger.onclick = function () {
                nav.classList.add('showSideMenu')
                cross.classList.add('showCross')
            }

            cross.onclick = function () {
                nav.classList.remove('showSideMenu')
                cross.classList.remove('showCross')
            }

        } catch (error) {
            console.log(error)
        }
    }
}

Blog.toggleSideMenu()
