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

function resetRowsForDwidth(totalPost, obj) {
    if (totalPost < 4) {
        let rows;
        switch (totalPost) {
            case 1:
                rows = 3
                break
            case 2:
                rows = 4
                break
            case 3:
                rows = 5
                break
            default:
                rows = 8
        }
        obj.style.gridTemplateRows = `repeat(${0 || rows}, 80px)`
    }
}
function resetRowsForTwidth(totalPost, obj) {
    let rows;
    if (totalPost <= 2) {
        rows = 3
    } else if (totalPost <= 4) {
        rows = 5
    } else { rows = 7 }

    obj.style.gridTemplateRows = `repeat(${rows}, 150px)`
}
function resetRowsForMwidth(totalPost, obj) {
    obj.style.gridTemplateRows = `repeat(${totalPost}, 250px)`

}


(function grid() {
    const postsGrid = document.querySelectorAll('.posts-grid')
    const tWidth = window.matchMedia('(max-width: 768px)');
    const mWidth = window.matchMedia('(max-width: 525px)');

    postsGrid.forEach(obj => {
        const totalPost = obj.children.length;
        if (mWidth.matches) {
            resetRowsForMwidth(totalPost, obj)
        }
        else if (tWidth.matches) {
            resetRowsForTwidth(totalPost, obj)
        } else {
            resetRowsForDwidth(totalPost, obj)
        }
    })
})()