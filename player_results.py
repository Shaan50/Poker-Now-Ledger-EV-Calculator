import csv
import os
from collections import defaultdict
import plotly.graph_objects as go

# -------------------------
# Player ID → Display Name
# -------------------------
PLAYER_ID_MAP = {
    "4gI6I84ZVK": "Nick",
    "grMuvW-X0V": "JIGGILY",
    "XbdE6lHXYH": "Chase",
    "DQEuZRscyo": "Dil",
    "3a8wWh_QDc": "Colin",
    "x8S_Ji604V": "ak",
    "FknElUCwfq": "roddy",
    "4iic2A6j-1": "shaan",
    "dbYuwWoGQS": "luckypoker",
    "kinSywjHRk": "aleksey",
    "_to1309KyP": "Manan",
    "8-K-ctj40p": "Fred",
    "EJd9KHwjJa": "Dan",
    "XQMYope2zs": "Joe",
    "ww_4zi8xdt": "Kerry",
    "gocEfwmKIU": "Spence",
    "8FJWmNLuTA": "Derek",
    "n-m4ymDhwV": "Cookie",
    "1szHs5_ZYW": "Aace",
    "d9WYK547-f": "Jk",
    "47rIsBiwbI": "Flaming",
    "co_9sNWQ3W": "Ajay",
    "WsJ1gE8m_C": "Ajen",
    "cWSOjIh86G": "Michael",
    "BeqzqNLiva": "Alex",
    "akgR0uz6JH": "Chris",
    "TQ5futb_ph": "Michael",
    "TXcDAR-yuu": "VQ",
    "6-STeBhFEr": "Bryand",
    "iLhrhRTNoc": "Ryan",
    "0czt4R_v1I": "qilin",
    "hjaoASonwz": "Jon",
    "TUuhUR8Hnw": "DXMA",
    "O4iYJSgS_D": "Aace",
    "71IJ9gWcDV": "Lucy",
    "VnavLzbyHv": "Narayan",
    "_wscNRJOby": "AlexM",
    "NtCox6lbjw": "MaxValuePoker",
    "X_av1o4H8n": "Caden",
    "tihO-0MWCV": "Ivan",
    "77fzIv97b_": "Anna",
    "bMlLkCJm41": "Victoria",
    "DBQyLsjCGE": "Ian",
    "NMdU2MV3Sf": "Broke",
    "3admN9pfA2": "nyzhang",
    "xKt9MBgnLl": "Maxg",
    "xo-BUgA2cb": "Josh",
    "4O93enV1-1": "Anson",
    "JZ19Unv_Ct": "Nico",
    "PoUn3Bwd97": "Matt",
    "NXBoXq3--S": "Andre",
    "aQvwk6FZnx": "Andre?",
    "3t-WRvfyKw": "Aryan",
    "wR9zCdRaEh": "Ashen",
    "o758R7MTt8": "Chen",
    "CqP4kv9hTI": "Chen?",
    "_B-kAaIQyL": "Oscar",
    "7Qdix44Qn3": "ben",
    "F8s-PhiSH6": "Bilal",
    "4CnFViT52A": "Ronald",
    "ZdrlG7zD8E": "Different Oscar?",
    "YYZYS5Vzg2": "Different Derek?",
    "2_uzk3X3SJ": "Adi",
    "wAGUyJuhMa": "jason1000",
    "HVlyNO1Dqr": "dylan",
    "mXZJbT46Ur": "Jason K",
    "qzXiBHdZij": "nahi",
    "fk8WwuZ_Z3": "manraj",
}

# ---------------------------------
# Folder where ledgers are stored
# ---------------------------------
BASE_PATH = "./logs/"

ledger_files = [
    "ledger_pglKfyzNLHXqp_nt7u8dGYqrs.csv", #1/31
    "ledger_pglBLsgSHwhqQmrXkbPDz9Uth.csv", #1/31
    "ledger_pgln_NnDCDnektkOb40Q1wtbS.csv", #2/1
    "ledger_pglzwbTGG8SHlFH_o-lM3luCa.csv", #2/1
    "ledger_pglgJSEwgygV0MRiGfdCnXWOj.csv", #2/2
    "ledger_pgl-p1ZOb_n4CsE7UNWxDLAsR.csv", #2/2
    "ledger_pgl1_MrSucnEQtXiL8QxSbCb_.csv", #2/3
    "ledger_pglkMi41tvsbMtWbyshOnhoJQ.csv", #2/3
    "ledger_pgl31Tmpwlmz3BAMxPADe5rPQ.csv", #2/4
    "ledger_pgloIPEtdjF-K8lKtIEJWFUWO.csv", #2/5
    "ledger_pglSHw9kb98zEGHwOF3yISxkQ.csv", #2/5
    "ledger_pglvBh9HC58Wopgsc6_ACuJq-.csv", #2/6
    "ledger_pgln6Z2K8z6abddEhUCi94zAz.csv", #2/7
    "ledger_pgl2qzFQ9bB7AaYeSxQArqCyx.csv", #2/7
    "ledger_pglNHrdtftYWPHmzLpZmb9v5O.csv", #2/8
    "ledger_pglQBAFeob5TiSs3ypKb0ejSb.csv", #2/9
    "ledger_pglKjqFzm3oHbP3L--VrmrrHu.csv", #2/10
    "ledger_pglZQTm2AaJNDgTEHZsoDfi9e.csv", #2/11
    "ledger_pglR8-uXAeW1GKZOTBcqcldxW.csv", #2/11
    "ledger_pglGD7D5HcL6Jw6eIe7YRcp4N.csv", #2/12
    "ledger_pglRSb30ZKNSotMpSmIt2RR1w.csv", #2/12
    "ledger_pgle-0VEizvelyLyvHQ99e0VN.csv", #2/12
    "ledger_pglWXrnKOgT1uXkuLxVDiSM7z.csv", #2/12
    "ledger_pglIdTAAgZCxsiWkC-aeQeK5H.csv", #2/13
    "ledger_pgldHzUhKVeMSiX7wD6txoTeY.csv", #2/13
    "ledger_pglRvVcWCsLGvxtTj-l9iqBHT.csv", #2/13
    "ledger_pglBflXz0_S0e3KtKz45Frk-Z.csv", #2/14
    "ledger_pgloUdVhHNBCWe6J5k_wHnzPL.csv", #2/14
    "ledger_pglHaOUmiluw8c3Grj960w0VS.csv", #2/15
    "ledger_pglJGPPJ0_M4m5v57_8cSt2s6.csv", #2/16
    "ledger_pgl-odxZLNh2Y-0EA7emx4SvC.csv", #2/16
    "ledger_pglEQobIRy_lzjsmFr-IROXz1.csv", #2/16
    "ledger_pglCKrrm9ebKVCGvAO5PhTs4U.csv", #2/17
    "ledger_pgldNhc9d84kNqymCrCOtbUAt.csv", #2/17
    "ledger_pglO4jM7IJ6k_eYeEHnflb4R7.csv", #2/17
    "ledger_pglxt-LIzLhL6Eq31AHM4yehF.csv", #2/18
    "ledger_pglPnojOicQtEppiPvKc2TGph.csv", #2/19
    "ledger_pglp5IFopIxWTKKfVpHlusNic.csv", #2/19
    "ledger_pglTMhM6-ubeZZwKFSBq_qy0J.csv", #2/20
    "ledger_pgludVu_SHcPGMzBtX5i0uqog.csv", #2/20
    "ledger_pglc-x6aEAGn2fhIeezBid_Yj.csv", #2/21
    "ledger_pgltHng_bzFNQlF5YzyFRKoOa.csv", #2/21
    "ledger_pgllgJZOZ4Ji0vmzjex2x-PR3.csv", #2/21
    "ledger_pgl-Ki6DLRnilYtU5uh6A7YLT.csv", #2/22
    "ledger_pglGTkb_PjQiWYInUrFZzuIwr.csv", #2/22
    "ledger_pglpelcXqaQ31B4ZeXd3T605c.csv", #2/23
    "ledger_pglPFrhO6ub1P059hGuzAD7_s.csv", #2/23
    "ledger_pglgj_dqFZj_rihIaBTofwwGE.csv", #2/23
    "ledger_pgl8B50jzIDkBGIxcC72DScok.csv", #2/23
    "ledger_pgliiFBwTIPRFAXJyEhcmBI6q.csv", #2/24
    "ledger_pglkq5iR7Aaed878Nd6NLGD31.csv", #2/24
    "ledger_pglpL_tXOgCdHLK8FuOi8zWxv.csv", #2/24
    "ledger_pglUFNFkUT8oV7ZDeSpWCMuuH.csv", #2/24
    "ledger_pglyLb1C-v2bag1BC7g3_DMjb.csv", #2/25
    "ledger_pgljPoHCY8cz6Nc-h78kMHsiD.csv", #2/25
    "ledger_pgldRw9zLg7sdtkvM9k6nubKk.csv", #2/25
    #"ledger_pglNGEnG9PFycb_YXKWvnB56A.csv", #2/26
]


# ---------------------------------
# Data Storage
# ---------------------------------
cumulative_pnl = defaultdict(float)

# Each player will have:
# session_numbers[player_id] = [1, 3, 5]
# session_history[player_id] = [100, 250, 180]
session_numbers = defaultdict(list)
session_history = defaultdict(list)

# ---------------------------------
# Process Ledgers
# ---------------------------------
for session_index, ledger_file in enumerate(ledger_files, start=1):

    session_pnl = defaultdict(float)
    full_path = os.path.join(BASE_PATH, ledger_file)

    with open(full_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            player_id = row["player_id"]
            net = row["net"]

            if not net:
                continue

            session_pnl[player_id] += int(net) / 100.0  # cents → dollars



    # Only update players who actually played this session
    for player_id, profit in session_pnl.items():

        cumulative_pnl[player_id] += profit

        #if player_id=="DnrLCLJPDL":print("pokernow.com/games/"+ledger_file[7:-4], "| Result: $"+str(profit))

        #MANUAL ADJUSTMENTS
        if player_id=="ABCDEFG" and ledger_file=="ledger_pglkMi41tvsbMtWbyshOnhoJQ.csv":
            cumulative_pnl[player_id] -= 224.50

        session_numbers[player_id].append(session_index)
        session_history[player_id].append(cumulative_pnl[player_id])

# ---------------------------------
# Sort players by final cumulative profit
# ---------------------------------
sorted_players = sorted(
    session_history.keys(),
    key=lambda pid: session_history[pid][-1],
    reverse=True
)

# ---------------------------------
# Print Leaderboard
# ---------------------------------
print("\n=== FINAL LEADERBOARD ===\n")

for rank, player_id in enumerate(sorted_players, start=1):
    name = PLAYER_ID_MAP.get(player_id, player_id)
    final_profit = session_history[player_id][-1]
    print(f"{rank:>2}. {name:<15} ${final_profit:>10.2f}")

print("\n")

# ---------------------------------
# Plotly Graph
# ---------------------------------
fig = go.Figure()

for player_id in sorted_players:
    name = PLAYER_ID_MAP.get(player_id, player_id)

    fig.add_trace(go.Scatter(
        x=session_numbers[player_id],   # only sessions they played
        y=session_history[player_id],
        mode='lines+markers',
        name=name,
        hovertemplate=
            "<b>%{text}</b><br>" +
            "Session: %{x}<br>" +
            "Cumulative: $%{y:.2f}<extra></extra>",
        text=[name] * len(session_history[player_id])
    ))

fig.update_layout(
    title="Cumulative Profit/Loss by Player 1/31-2/19",
    xaxis_title="Session Number",
    yaxis_title="Cumulative Profit ($)",
    hovermode="closest",
    template="plotly_dark"
)

fig.show()
fig.write_html("player_results_graph.html")
