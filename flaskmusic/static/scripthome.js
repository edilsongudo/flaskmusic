// $(document).ready(function() {

//     $('a').click(function(e) {
//         e.preventDefault()
//         var csrfToken = $('input[name="csrf_token"]').val()
//         var dict = {"last": e.target.id}
//         var json = JSON.stringify(dict)
//         console.log(json)

//            $.ajax({
//               url: `player`,
//               headers: {'X-CSRFToken': csrfToken},
//               dataType: 'json',
//               data: json,
//               type: 'post',
//               success: function(response) {
//                 console.log(response)
//                   window.location.href = response
//               }
//           })
//     })
// });


const musicContainer = document.querySelectorAll('#music-container');
const playBtn = document.querySelectorAll('#play');
const prevBtn = document.querySelectorAll('#prev');
const nextBtn = document.querySelectorAll('#next');

const audio = document.querySelector('#audio')
const progress = document.querySelectorAll('#progress');
const progressContainer = document.querySelectorAll('#progress-container');
const title = document.querySelectorAll('#title');
const cover = document.querySelectorAll('#cover');

var currentPlaying = ""

playBtn.forEach(btn => {
  btn.addEventListener('click', event => {

        if (currentPlaying == '../static/music/' + event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className) {
          console.log('Already playing audio')
        } else {
          console.log('Changed')
            currentPlaying = '../static/music/' + event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className
            audio.src = '../static/music/' + event.currentTarget.parentElement.parentElement.childNodes.item('span').nextElementSibling.className
        }

    if (event.currentTarget.children[0].classList.contains('fa-play')) {

      // Pause all other btns
        playBtn.forEach(btn => {
          if (btn.children[0].classList.contains('fa-pause')) {
              btn.children[0].classList.remove('fa-pause')
              btn.children[0].classList.add('fa-play')
              }
        })

      event.currentTarget.children[0].classList.remove('fa-play')
      event.currentTarget.children[0].classList.add('fa-pause')
      audio.play()

    } else {
      event.currentTarget.children[0].classList.remove('fa-pause')
      event.currentTarget.children[0].classList.add('fa-play')
      audio.pause()
    }

  })
})

