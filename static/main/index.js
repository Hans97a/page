const spanEl = document.querySelector("main h2 span");
const txtArr = ["Back-End Developer", "Hans"];
let index = 0;
let currentTxt = txtArr[index].split("");

function writeTxt(){
    spanEl.textContent+=currentTxt.shift();
    if(currentTxt.length !=0){
        setTimeout(writeTxt, Math.floor(Math.random()*100));
    }else{
        currentTxt=spanEl.textContent.split("");
        setTimeout(deleteTxt, 3000);
    }
}
function deleteTxt(){
    currentTxt.pop();
    spanEl.textContent=currentTxt.join("");
    if(currentTxt.length !=0){
        setTimeout(deleteTxt, Math.floor(Math.random()*100));
    }else{
        index=(index+1)%txtArr.length;
        currentTxt=txtArr[index].split("");
        writeTxt();
    }
}
writeTxt();

const animationMove=function(selector){
    const targetEl=document.querySelector(selector);
    const browserScrollY=window.pageYOffset;
    const targetScrollY=targetEl.getBoundingClientRect().top+browserScrollY;
    window.scrollTo({top: targetScrollY, behavior: 'smooth'});
}

const scrollMoveEl=document.querySelectorAll('[data-animation-scroll="true"]');
for(let i = 0; i<scrollMoveEl.length;i++){
    scrollMoveEl[i].addEventListener('click', function(e){
        const target=this.dataset.target;
        animationMove(target);
    });
}

const cvEl=document.querySelector('.download');
cvEl.onclick = () => {
    alert('on Preparation Steps');
}