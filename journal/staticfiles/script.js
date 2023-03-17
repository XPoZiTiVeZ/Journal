console.log('Hello world!')

const spinner = document.getElementById('spinner')
const data = document.getElementById('data')

$.ajax({
    type: 'GET',
    url: '/home',
    succes: function(response) {
        console.log(response)
    },
    error: function(response) {
        console.log(response)
    }
})