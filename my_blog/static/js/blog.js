function toggleSideMenu() {
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

function toggleProfileOptions() {
    const profileIcon = document.getElementById('profileButton')
    const optionCard = profileIcon.nextElementSibling;
    let optionCardVisible = false

    profileIcon.onmouseenter = function (e) {
        optionCard.classList.add('display');
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

toggleSideMenu()
toggleProfileOptions()
