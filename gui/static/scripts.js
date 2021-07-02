async function api(command, action) {
    document.getElementById("feedback").innerHTML = "Running......"
    let myPromise = new Promise(function(myResolve, myReject) {
        let req = new XMLHttpRequest();
        req.open('GET', ' http://127.0.0.1:7607/api?task=' + command + "&action=" + action)
        req.onload = function() {
            if (req.status == 200) { myResolve(req.response); } else { myResolve("Error"); }
        };
        req.send();
    });
    document.getElementById("feedback").innerHTML = await myPromise;
}