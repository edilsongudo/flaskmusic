const buttonplayer = document.querySelector('button.toggleplayer')
const buttonhome = document.querySelector('button.togglehome')
const player = document.querySelector('div.player')
const list = document.querySelector('div.home')

buttonplayer.addEventListener('click', function () {
    list.style.display = 'none'
    player.style.display = 'block'

})
buttonhome.addEventListener('click', function () {
    player.style.display = 'none'
    list.style.display = 'block'

})

const musicinfo = document.querySelectorAll('div.music-info')
const imgcontainer = document.querySelectorAll('div.img-container')

// BE CAREFULL TO NOT REACT TO FOOTER TOO, BECAUSE IT DOESNT HAVE SONG ID AND WILL CAUSE A VERY CRITICAL AND HARD TO DETECT BUG
musicinfo.forEach(mc => {
    mc.addEventListener('click', function() {
        list.style.display = 'none'
        player.style.display = 'block'
        if (audio.id != mc.id && mc.id != "footer-music") {
            loadSong(mc.id)
            playSong()
        }

    })
})

// BE CAREFULL TO NOT REACT TO FOOTER TOO, BECAUSE IT DOENST HAVE SONG ID AND WILL CAUSE A VERY CRITICAL AND HARD TO DETECT BUG
imgcontainer.forEach(mc => {
    mc.addEventListener('click', function() {
        list.style.display = 'none'
        player.style.display = 'block'
        if (audio.id != mc.id && mc.id != "footer-img") {
            loadSong(mc.id)
            playSong()
        }
    })
})

function showlyrics() {
    document.querySelector('.lyrics').style.display = 'block'
}

function closelyrics() {
    document.querySelector('.lyrics').style.display = 'none'

}
