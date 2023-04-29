
let login_metamask = async () => {
    eth = window.ethereum;

    if (!eth) {
        console.log("MetaMask Wallet not found!");
        alert("Please install a metamask wallet to use this!");
        return;
    }

    let wallets = await window.ethereum.request({ method: 'eth_accounts'});

    if (wallets.length === 0) {
        alert("There was no wallets found!");
    }

    console.log("Wallet address: ", wallets[0]);
}