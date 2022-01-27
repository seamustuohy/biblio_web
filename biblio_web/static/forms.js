function fill_paragraphs(id) {
    var element = document.querySelector(id)
    element.value = element.value.replace(/(?<!\n)(\r\n?|\n)(?!\n)/g, ' ')
}
