const unfillButtons = document.querySelectorAll("button.unfill")

function fill_paragraphs(e) {
    var button_id = e.target.getAttribute('id')
    // Buttons are given the ID button_[ID-OF-TEXTAREA-THEY-MODIFY]
    // This is done in the jinja template for the django form
    // Change button id into query selector for area of text they modify
    var target_id = button_id.replace(/^(button_)/,'#');
    console.log(target_id)
    var element = document.querySelector(target_id)
    console.log(element)
    element.value = element.value.replace(/(?<!\n)(\r\n?|\n)(?!\n)/g, ' ')
}

for (let i = 0; i < unfillButtons.length; i++) {
    var btn = unfillButtons[i]
    btn.addEventListener('click', fill_paragraphs);
}
