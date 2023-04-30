function checkWalletIsConnected ()  {
    const { ethereum } = window;

    if (!ethereum) {
        console.log("Make sure you have Metamask installed!");
        return;
    } else {
        console.log("Wallet Exists!")
    }
}

async function connectWalletHandler() {  
    const { ethereum } = window;

    if (!ethereum) {
        alert("Please install Metamask!");
    }
    try {
        const accounts = await ethereum.request({ method: "eth_requestAccounts"});
        console.log("Found an account! Address: ", accounts[0]);
        btn = document.getElementById("wallet_connect");
        btn.innerHTML = accounts[0];
    } catch (err) {
        console.log(err);
        alert("There was an error!\n", err)
    }
    
}