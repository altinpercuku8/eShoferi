// Selektojme button-at dhe body-in e modal per te ndryshar kontentin

const modalBody = document.getElementById('modalBodyConfirm')
const filloButon = document.getElementById('startButton')
const modalBtns = [...document.getElementsByClassName('modal-button')]

const urlLocation = document.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numberOfQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const time = modalBtn.getAttribute('data-time')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    modalBody.innerHTML = `
    <div class="h5 mb-3">Ju po filloni "<b>${name}</b>"!</div>
    <div class="text-muted">
        <ul>
            <li>Veshtiresia : <b>${difficulty.toUpperCase()}</b></li>
            <li>Numri i pyetjeve : <b>${numberOfQuestions}</b></li>
            <li>Kohezgjatja : <b>${time} MIN</b></li>
            <li>Kalueshmeria : <b>${scoreToPass}%</b></li>
        </ul>
    </div>
    `
    console.log(pk)

    filloButon.addEventListener('click', () =>{
        window.location.href = urlLocation+ 'quiz/' + pk
    })
}))