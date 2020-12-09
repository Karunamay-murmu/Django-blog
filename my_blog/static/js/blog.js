class Blog {
    constructor() { }
    static toggleSideMenu() {
        const burger = document.querySelector('#burger')
        const cross = document.querySelector('#cross')
        const nav = document.querySelector('#navigation-menu')

        burger.onclick = function () {
            nav.classList.add('showSideMenu')
            cross.classList.add('display')
        }

        cross.onclick = function () {
            nav.classList.remove('showSideMenu')
            cross.classList.remove('display')
        }
    }

    static async toggleProfileOptions() {
        const profileIcon = document.getElementById('profileButton')
        const optionCard = profileIcon.nextElementSibling;
        let optionCardVisible = false

        profileIcon.onclick = function (e) {
            optionCard.classList.toggle('display');
            optionCardVisible = true;

            if (optionCardVisible) {
                e.stopImmediatePropagation();
                document.onclick = function () {
                    optionCard.classList.remove('display')
                }
                optionCardVisible = false
            }

        }

    }
}

Blog.toggleSideMenu()
Blog.toggleProfileOptions()
