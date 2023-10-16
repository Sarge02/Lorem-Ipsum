function changeFrame(change){
    console.log("changeFrame called with:", change);
    document.getElementById('jsonIframe').src = change;
}

function changeParentToIframe(source){
    window.parent.changeParentIframe(source);
}