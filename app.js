let username = document.querySelector('#searchBar')
let button = document.querySelector('#searchBtn')
let firstScreen = document.querySelector('#firstScreen')
let secondScreen = document.querySelector('#secondScreen')

let loginName = document.querySelector('#name')
let avatar = document.querySelector('#avatar')
let bio = document.querySelector('#bio')
let repos = document.querySelector('#repos')



secondScreen.style.display = "none";


button.addEventListener('click',function(e){
    loadUser();
}

)

async function loadUser() {
    const response = await fetch(`https://api.github.com/users/${username.value}`);
    const data = await response.json();
    console.log(data); 
    username.value = ""
    firstScreen.style.display = "none"
    secondScreen.style.display = "block"
    loginName.innerText = data.name
    avatar.src = data.avatar_url
    bio.innerText = data.bio
    repos.innerText = data.public_repos




  }
