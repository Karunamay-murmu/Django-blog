function incrementLikeOnPost() {
    const likeButton = document.querySelector('#likeButton');
    const url = `http://127.0.0.1:8000${path}`;
    const postid = postId;

    const incrementLikeAndChangeColor = likes => {
        const likesOnPost = document.querySelector('#postLikeCount');
        const likeButtonSVG = document.querySelector('#likeButtonSVG')

        likesOnPost.textContent = likes;
        likeButtonSVG.classList.add('liked')
        likeButton.disabled = true;
    }

    function like(e) {
        e.preventDefault();
        const csrftoken = likeButton.previousElementSibling.getAttribute('value')
        const data = {
            postid
        }
        try {
            fetch(url, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify(data)
            }).then(data => data.json())
                .then(response => {
                    const likes = response.likes
                    incrementLikeAndChangeColor(likes)
                }).catch((error) => {
                    console.error(error)
                });
        } catch (error) {
            console.error(error)
        }
    }

    likeButton.addEventListener("click", like, { passive: true })
    likeButton.addEventListener("touchstart", like, { passive: true })
}

incrementLikeOnPost();