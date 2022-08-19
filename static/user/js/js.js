
function makeFont() {
    let screenWidth = window.innerWidth
    let fonts = document.querySelectorAll('.nav-element-text');
    if (screenWidth < 500) {
        fonts.forEach((item)=> item.style.fontSize = '.8em')
    } else if(screenWidth<800) {
        fonts.forEach((item)=> item.style.fontSize = '1em')
    } else
        fonts.forEach((item)=> item.style.fontSize = '1.3em')
    }


makeFont()
