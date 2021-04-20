// needs to be the first script loaded in the page
const input = document.getElementById("music")
input.hidden = true

// another script
// const sounds = document.getElementsByTagName('audio')
// for (i=0; i < sounds.length; i++) {sounds[i].pause()}

// third script
const actualBtn = document.getElementById('music')
const fileChosen = document.getElementById('file-chosen')

actualBtn.addEventListener('change', function() {
    fileChosen.textContent = this.files[0].name
    this.form.submit() })
