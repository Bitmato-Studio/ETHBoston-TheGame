function checkWalletIsConnected ()  {
    const { ethereum } = window;

    if (!ethereum) {
        console.log("Make sure you have Metamask installed!");
        return;
    } else {
        console.log("Wallet Exists!");
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
        $.ajax({
            url: `/login/${accounts[0]}`,
            method: "POST",
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    } catch (err) {
        console.log(err);
        alert("There was an error!\n", err);
    }
    
}

function update_board(cmp_data) {
    console.log(cmp_data);
    for (let key in cmp_data) {
        // get the values
        let cvalue = document.getElementById(`${key}-value`);
        let ctotalshares = document.getElementById(`${key}-total-shares`);

        cvalue.innerHTML = cmp_data[key].value;
        ctotalshares.innerHTML = cmp_data[key].total_shares;
    }
}

function update_player(player_data) {
    let holdings_table = document.getElementById("player-holdings");

    let playerHoldings = player_data.holdings;
    holdings_table.innerHTML = ""; // clear it out

    for (let company in playerHoldings) {
        holdings_table.innerHTML += `
            <tr>
                <td class="custom-border">${company}</td>
                <td class="custom-border">${playerHoldings[company]}</td>
            </tr>
        `;
    }
}

function get_player_data() {
    btn = document.getElementById("wallet_connect");
    account = btn.innerHTML;

    if (account === "Connect Wallet") { return; }

    $.ajax({
        url: `/player/${account}`,
        method: "GET",
        success: function(response) {
            update_player(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function get_game_state() {
    $.ajax({
        url: `/gamestate`,
        method: "GET",
        success: function(response) {
            update_board(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}


function doTrade(isBuy) {
    btn = document.getElementById("wallet_connect");
    account = btn.innerHTML;
    if (account === "Connect Wallet") { return; }

    cmp = document.getElementById("company").value;
    shares = document.getElementById("shares").value;

    $.ajax({
        url: `/trade/${account}/${isBuy ? "buy" : "sell"}/${shares}/${cmp}`,
        method: "POST",
        success: function(response) {
            update_board(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

/* `setInterval(() => { get_game_state(); get_player_data(); }, 2000);` is a function that is
repeatedly calling the `get_game_state()` and `get_player_data()` functions every 2 seconds (2000
milliseconds). This is used to update the game board and player data in real-time without the need
for the user to manually refresh the page. */
setInterval(() => {
    get_game_state();
    get_player_data();
}, 2000); 