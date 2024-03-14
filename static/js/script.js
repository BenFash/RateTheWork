const commentEditButtons = document.querySelectorAll('.btn-comment-edit');

for (let button of commentEditButtons) {
    button.addEventListener("click", (e) => {
        let ratingId = e.target.getAttribute("data-rating_id");
        let ratingContent = document.getElementById(`rating${ratingId}`).innerText;
        ratingText.value = ratingContent;
        submitButton.innerText = "Update";
        ratingForm.setAttribute("action", `edit_rating/${ratingId}`);
    });
}