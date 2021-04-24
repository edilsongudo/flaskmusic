const musicContainer = document.getElementById('music-container2');
const playBtn = document.getElementById('play');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

const audio = document.getElementById('audio');
const progress = document.getElementById('progress');
const progressContainer = document.getElementById('progress-container');
const title = document.getElementById('title');
const artist = document.getElementById('artist')
const cover = document.getElementById('cover');

// Keep track of song
var songIndex = 0

// Initially load song details into DOM
loadSong(songs[songIndex]['filename']);

// Update song details
function loadSong(song) {

  const obj = songs.find(x => x.filename === song)

  if (obj['title'] != null) {
    var song_title = obj['title']
  } else {
    var song_title = song
  }

  if (obj['artist'] != null) {
    artist.innerText = obj['artist']
  } else {
    artist.innerText = 'Unknown Artist'
  }

  if (song_title.length > 25 ) {
        title.innerHTML = '<marquee behaviour="left" id="title">' + song_title + '</marquee>'
  } else {
      title.innerHTML = '<p id="title">' + song_title + '</p>'
  }
  // audio.src = `../static/music/${song}.mp3`;
    audio.src = `../static/music/${song}`; // flask sends the audio with the extension
    audio.id = song

  // cover.src = `../static/images/${song}.jpg`;
}

// Play song
function playSong() {
  musicContainer.classList.add('play');
  playBtn.querySelector('i.fas').classList.remove('fa-play');
  playBtn.querySelector('i.fas').classList.add('fa-pause');

  audio.play();

    playBtns.forEach(btn => {

    console.log(`${btn.parentElement.id}`)
    console.log(audio.id)

    if (`${btn.parentElement.id}` == audio.id) {

      if (btn.children[0].classList.contains('fa-play')) {
          btn.children[0].classList.remove('fa-play')
          btn.children[0].classList.add('fa-pause')
          currentPlaying = '../static/music/' + audio.id

          }

          } else {
              btn.children[0].classList.remove('fa-pause')
              btn.children[0].classList.add('fa-play')
            }

    })

}

// Pause song
function pauseSong() {
  musicContainer.classList.remove('play');
  playBtn.querySelector('i.fas').classList.add('fa-play');
  playBtn.querySelector('i.fas').classList.remove('fa-pause');

  playBtns.forEach(btn => {
    if (`${btn.parentElement.id}` == audio.id) {

      if (btn.children[0].classList.contains('fa-pause')) {
          btn.children[0].classList.remove('fa-pause')
          btn.children[0].classList.add('fa-play')
          }
    }
  })

  audio.pause();
}

// Previous song
function prevSong() {
  songIndex--;

  if (songIndex < 0) {
    songIndex = songs.length - 1;
  }

  loadSong(songs[songIndex]['filename']);

  playSong();
}

// Next song
function nextSong() {
  songIndex++;

  if (songIndex > songs.length - 1) {
    songIndex = 0;
  }

  loadSong(songs[songIndex]['filename']);

  playSong();
}

// Update progress bar
function updateProgress(e) {
  const { duration, currentTime } = e.srcElement;
  const progressPercent = (currentTime / duration) * 100;
  progress.style.width = `${progressPercent}%`;
}

// Set progress bar
function setProgress(e) {
  const width = this.clientWidth;
  const clickX = e.offsetX;
  const duration = audio.duration;

  audio.currentTime = (clickX / width) * duration;
}

// Event listeners
playBtn.addEventListener('click', () => {
  const isPlaying = musicContainer.classList.contains('play');

  if (isPlaying) {
    pauseSong();
  } else {
    playSong();
  }
});

// Change song
prevBtn.addEventListener('click', prevSong);
nextBtn.addEventListener('click', nextSong);

// Time/song update
audio.addEventListener('timeupdate', updateProgress);

// Click on progress bar
progressContainer.addEventListener('click', setProgress);

// Song ends
audio.addEventListener('ended', nextSong);


const playBtns = document.querySelectorAll('#play2');
var currentPlaying = ""

playBtns.forEach(btn => {
  btn.addEventListener('click', event => {

        if (currentPlaying == '../static/music/' + event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className) {
          console.log('Already playing audio')
        } else {
          console.log('Changed')
          loadSong(event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className)
            currentPlaying = '../static/music/' + event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className
            audio.src = '../static/music/' + event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className
        }

    if (event.currentTarget.children[0].classList.contains('fa-play')) {

      // Pause all other btns
        playBtns.forEach(btn => {
          if (btn.children[0].classList.contains('fa-pause')) {
              btn.children[0].classList.remove('fa-pause')
              btn.children[0].classList.add('fa-play')
              }
        })

      event.currentTarget.children[0].classList.remove('fa-play')
      event.currentTarget.children[0].classList.add('fa-pause')
      playSong()

    } else {
      event.currentTarget.children[0].classList.remove('fa-pause')
      event.currentTarget.children[0].classList.add('fa-play')
      pauseSong()
    }

  })
})
