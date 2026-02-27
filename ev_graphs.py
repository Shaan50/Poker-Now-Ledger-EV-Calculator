import pandas as pd
import re
import itertools
import random
import matplotlib.pyplot as plt
import plotly.express as px
from adjustText import adjust_text
from treys import Card, Evaluator, Deck
import json
import os

# =============================
# CONFIG
# =============================
POKERNOW_LOGS = [
    "poker_now_log_pglKfyzNLHXqp_nt7u8dGYqrs.csv", #1/31
    "poker_now_log_pglBLsgSHwhqQmrXkbPDz9Uth.csv", #1/31
    "poker_now_log_pgln_NnDCDnektkOb40Q1wtbS.csv", #2/1
    "poker_now_log_pglzwbTGG8SHlFH_o-lM3luCa.csv", #2/1
    "poker_now_log_pglgJSEwgygV0MRiGfdCnXWOj.csv", #2/2
    "poker_now_log_pgl-p1ZOb_n4CsE7UNWxDLAsR.csv", #2/2
    "poker_now_log_pgl1_MrSucnEQtXiL8QxSbCb_.csv", #2/3
    "poker_now_log_pglkMi41tvsbMtWbyshOnhoJQ.csv", #2/3
    "poker_now_log_pgl31Tmpwlmz3BAMxPADe5rPQ.csv", #2/4
    "poker_now_log_pgloIPEtdjF-K8lKtIEJWFUWO.csv", #2/5
    "poker_now_log_pglSHw9kb98zEGHwOF3yISxkQ.csv", #2/5
    "poker_now_log_pglvBh9HC58Wopgsc6_ACuJq-.csv", #2/6
    "poker_now_log_pgln6Z2K8z6abddEhUCi94zAz.csv", #2/7
    "poker_now_log_pgl2qzFQ9bB7AaYeSxQArqCyx.csv", #2/7
    "poker_now_log_pglNHrdtftYWPHmzLpZmb9v5O.csv", #2/8
    "poker_now_log_pglQBAFeob5TiSs3ypKb0ejSb.csv", #2/9
    "poker_now_log_pglKjqFzm3oHbP3L--VrmrrHu.csv", #2/10
    "poker_now_log_pglZQTm2AaJNDgTEHZsoDfi9e.csv", #2/11
    "poker_now_log_pglR8-uXAeW1GKZOTBcqcldxW.csv", #2/11
    "poker_now_log_pglGD7D5HcL6Jw6eIe7YRcp4N.csv", #2/12
    "poker_now_log_pglRSb30ZKNSotMpSmIt2RR1w.csv", #2/12
    "poker_now_log_pgle-0VEizvelyLyvHQ99e0VN.csv", #2/12
    "poker_now_log_pglWXrnKOgT1uXkuLxVDiSM7z.csv", #2/12
    "poker_now_log_pglIdTAAgZCxsiWkC-aeQeK5H.csv", #2/13
    "poker_now_log_pgldHzUhKVeMSiX7wD6txoTeY.csv", #2/13
    "poker_now_log_pglRvVcWCsLGvxtTj-l9iqBHT.csv", #2/13
    "poker_now_log_pglBflXz0_S0e3KtKz45Frk-Z.csv", #2/14
    "poker_now_log_pgloUdVhHNBCWe6J5k_wHnzPL.csv", #2/14
    "poker_now_log_pglHaOUmiluw8c3Grj960w0VS.csv", #2/15
    "poker_now_log_pglJGPPJ0_M4m5v57_8cSt2s6.csv", #2/16
    "poker_now_log_pgl-odxZLNh2Y-0EA7emx4SvC.csv", #2/16
    "poker_now_log_pglEQobIRy_lzjsmFr-IROXz1.csv", #2/16
    "poker_now_log_pglCKrrm9ebKVCGvAO5PhTs4U.csv", #2/17
    "poker_now_log_pgldNhc9d84kNqymCrCOtbUAt.csv", #2/17
    "poker_now_log_pglO4jM7IJ6k_eYeEHnflb4R7.csv", #2/17
    "poker_now_log_pglxt-LIzLhL6Eq31AHM4yehF.csv", #2/18
    "poker_now_log_pglPnojOicQtEppiPvKc2TGph.csv", #2/19
    "poker_now_log_pglp5IFopIxWTKKfVpHlusNic.csv", #2/19
    "poker_now_log_pglTMhM6-ubeZZwKFSBq_qy0J.csv", #2/20
    "poker_now_log_pgludVu_SHcPGMzBtX5i0uqog.csv", #2/20
    "poker_now_log_pglc-x6aEAGn2fhIeezBid_Yj.csv", #2/21
    "poker_now_log_pgltHng_bzFNQlF5YzyFRKoOa.csv", #2/21
    "poker_now_log_pgllgJZOZ4Ji0vmzjex2x-PR3.csv", #2/21
    "poker_now_log_pgl-Ki6DLRnilYtU5uh6A7YLT.csv", #2/22
    "poker_now_log_pglGTkb_PjQiWYInUrFZzuIwr.csv", #2/22
    "poker_now_log_pglpelcXqaQ31B4ZeXd3T605c.csv", #2/23
    "poker_now_log_pglPFrhO6ub1P059hGuzAD7_s.csv", #2/23
    "poker_now_log_pglgj_dqFZj_rihIaBTofwwGE.csv", #2/23
    "poker_now_log_pgl8B50jzIDkBGIxcC72DScok.csv", #2/23
    "poker_now_log_pgliiFBwTIPRFAXJyEhcmBI6q.csv", #2/24
    "poker_now_log_pglkq5iR7Aaed878Nd6NLGD31.csv", #2/24
    "poker_now_log_pglpL_tXOgCdHLK8FuOi8zWxv.csv", #2/24
    "poker_now_log_pglUFNFkUT8oV7ZDeSpWCMuuH.csv", #2/24
    "poker_now_log_pglyLb1C-v2bag1BC7g3_DMjb.csv", #2/25
    "poker_now_log_pgljPoHCY8cz6Nc-h78kMHsiD.csv", #2/25    
    "poker_now_log_pgldRw9zLg7sdtkvM9k6nubKk.csv", #2/25
    #"poker_now_log_pglNGEnG9PFycb_YXKWvnB56A.csv", #2/26
]

BASE_PATH = "./logs/"
MC_SIMS = 5_000   # Monte Carlo sims for preflop all-ins

# =============================
# LOOKUP TABLE CONFIG
# =============================
LOOKUP_PATH = "equity_lookup.json"
LOOKUP_SAVE_INTERVAL = 1
lookup_dirty = 0

equity_lookup = {}

if os.path.exists(LOOKUP_PATH):
    try:
        if os.path.getsize(LOOKUP_PATH) > 0:
            with open(LOOKUP_PATH, "r") as f:
                equity_lookup = json.load(f)
        else:
            equity_lookup = {}
    except json.JSONDecodeError:
        print("equity_lookup.json corrupted — starting fresh")
        equity_lookup = {}



# =============================
# PLAYER ID → NAME MAPPING
# =============================
PLAYER_ID_MAP = {
    # "player_id": "Display Name"
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

# =============================
# Helpers
# =============================
def extract_player_id(entry: str):
    m = re.search(r"@ ([\w\-]+)", entry)
    return m.group(1) if m else None


def display_name(pid: str):
    return PLAYER_ID_MAP.get(pid, pid)


def parse_cards(card_str):
    suit_map = {'♠': 's', '♥': 'h', '♦': 'd', '♣': 'c'}
    rank_map = {
        'A': 'A', 'K': 'K', 'Q': 'Q', 'J': 'J',
        '10': 'T', '9': '9', '8': '8', '7': '7',
        '6': '6', '5': '5', '4': '4', '3': '3', '2': '2'
    }
    cards = []
    for c in card_str.split(","):
        c = c.strip()
        raw_rank = c[:-1]
        cards.append(Card.new(rank_map[raw_rank] + suit_map[c[-1]]))
    return cards

def card_to_str(card_int):
    return Card.int_to_str(card_int)


def canonical_key(hands, board):
    """
    Returns a canonical key string for the lookup table,
    and a map to reorder equities back to original hands.
    """
    # Convert hands to sorted string tuples
    hand_strs = []
    for h in hands:
        cards = tuple(sorted(card_to_str(c) for c in h))
        hand_strs.append(cards)

    # Sort hands for key
    sorted_hands_with_idx = sorted(enumerate(hand_strs), key=lambda x: x[1])
    sorted_hands = [h for _, h in sorted_hands_with_idx]
    idx_map = [i for i, _ in sorted_hands_with_idx]  # map from sorted to original

    board_str = tuple(sorted(card_to_str(c) for c in board))

    key = json.dumps({"hands": sorted_hands, "board": board_str})
    return key, idx_map



def monte_carlo_equity(hands, board_cards, sims=MC_SIMS):
    evaluator = Evaluator()
    equities = [0.0] * len(hands)

    used = set(itertools.chain.from_iterable(hands)) | set(board_cards)
    deck = [c for c in Deck.GetFullDeck() if c not in used]
    needed = 5 - len(board_cards)

    for _ in range(sims):
        runout = random.sample(deck, needed)
        board = board_cards + runout
        scores = [evaluator.evaluate(board, h) for h in hands]
        best = min(scores)
        winners = scores.count(best)
        for i, s in enumerate(scores):
            if s == best:
                equities[i] += 1 / winners

    return [e / sims for e in equities]


def exact_equity(hands, board_cards):
    evaluator = Evaluator()
    used = set(itertools.chain.from_iterable(hands)) | set(board_cards)
    deck = [c for c in Deck.GetFullDeck() if c not in used]
    needed = 5 - len(board_cards)

    equities = [0.0] * len(hands)
    total = 0

    for runout in itertools.combinations(deck, needed):
        board = board_cards + list(runout)
        scores = [evaluator.evaluate(board, h) for h in hands]
        best = min(scores)
        winners = scores.count(best)
        for i, s in enumerate(scores):
            if s == best:
                equities[i] += 1 / winners
        total += 1

    return [e / total for e in equities]

def lookup_exact_equity(hands, board_cards):
    global lookup_dirty

    key, idx_map = canonical_key(hands, board_cards)

    # HIT
    if key in equity_lookup:
        #print("HIT")
        # Reorder stored equities to match input hand order
        stored_equities = equity_lookup[key]
        reordered = [0.0] * len(stored_equities)
        for sorted_idx, original_idx in enumerate(idx_map):
            reordered[original_idx] = stored_equities[sorted_idx]
        return reordered

    # MISS → compute exact
    equities = exact_equity(hands, board_cards)

    # Store in sorted order
    sorted_equities = [equities[i] for i in idx_map]  # equities in canonical order
    equity_lookup[key] = sorted_equities
    #print("STORED")
    lookup_dirty += 1

    # Periodic save
    if lookup_dirty >= LOOKUP_SAVE_INTERVAL:
        with open(LOOKUP_PATH, "w") as f:
            json.dump(equity_lookup, f)
        lookup_dirty = 0

    # Reorder back to original hand order
    reordered = [0.0] * len(equities)
    for sorted_idx, original_idx in enumerate(idx_map):
        reordered[original_idx] = equities[sorted_idx]

    return reordered


# =============================
# GLOBAL AGGREGATION
# =============================
player_stats = {}  # pid -> {"ev": x, "collected": y}

# =============================
# MAIN LOOP
# =============================
for LOG in POKERNOW_LOGS:
    df = pd.read_csv(BASE_PATH + LOG).sort_values("order")

    current_board = []
    board_at_all_in = []
    shown_cards = {}
    collected = {}
    total_pot = 0.0
    showdown = False

    for _, row in df.iterrows():
        entry = str(row["entry"]).strip()

        # -------------------------
        # New hand
        # -------------------------
        if entry.startswith("-- starting hand"):
            current_board = []
            board_at_all_in = []
            shown_cards = {}
            collected = {}
            total_pot = 0.0
            showdown = False
            continue

        # -------------------------
        # Board tracking (ignore river AFTER all-in)
        # -------------------------
        if not showdown:
            if entry.startswith("Flop:"):
                current_board = parse_cards(re.search(r"\[(.*)\]", entry).group(1))
            elif entry.startswith("Turn:"):
                current_board += parse_cards(re.search(r"\[(.*)\]", entry).group(1))

        # -------------------------
        # All-in trigger
        # -------------------------
        if "remaining players decide" in entry.lower():
            showdown = True
            board_at_all_in = list(current_board)

        # -------------------------
        # Showdown cards (1 at a time safe)
        # -------------------------
        if showdown and "shows a" in entry.lower():
            pid = extract_player_id(entry)
            if pid:
                cards = parse_cards(re.search(r"shows a (.*)\.", entry).group(1))
                shown_cards.setdefault(pid, []).extend(cards)

        # -------------------------
        # Pot collection
        # -------------------------
        if "collected" in entry.lower() and "from pot" in entry.lower():
            pid = extract_player_id(entry)
            if pid:
                amt = float(re.search(r"collected ([\d\.]+)", entry).group(1))
                collected[pid] = collected.get(pid, 0.0) + amt
                total_pot += amt

        # -------------------------
        # End hand → compute EV
        # -------------------------
        if showdown and entry.startswith("-- ending hand") and len(shown_cards) >= 2:
            players = list(shown_cards.keys())
            hands = [shown_cards[p] for p in players]
            if len(hands[0])==4:
                continue

            '''if len(board_at_all_in) == 0:
                equities = monte_carlo_equity(hands, board_at_all_in)
            else:
                equities = exact_equity(hands, board_at_all_in)'''
            equities = lookup_exact_equity(hands, board_at_all_in)

            for pid, eq in zip(players, equities):
                ev = eq * total_pot
                col = collected.get(pid, 0.0)

                diff = col - ev  # single all-in result

                if pid not in player_stats:
                    player_stats[pid] = {
                        "history": [],
                        "cumulative": 0.0
                    }

                player_stats[pid]["cumulative"] += diff
                player_stats[pid]["history"].append(player_stats[pid]["cumulative"])

            showdown = False


# =============================
# PLOTTING
# =============================

import plotly.graph_objects as go

fig = go.Figure()

# Sort players by final run-good amount
sorted_players = sorted(
    player_stats.keys(),
    key=lambda pid: player_stats[pid]["history"][-1],
    reverse=True
)

print("\n=== FINAL ALL-IN RUN GOOD / BAD ===\n")

for rank, pid in enumerate(sorted_players, start=1):
    name = display_name(pid)
    history = player_stats[pid]["history"]
    final = history[-1]
    allins = len(history)

    print(f"{rank:>2}. {name:<15} All-ins: {allins:<4} Amount Above/Below EV: ${final:.2f}")

    fig.add_trace(go.Scatter(
        x=list(range(1, allins + 1)),
        y=history,
        mode="lines+markers",
        name=name,
        hovertemplate=
            "<b>%{text}</b><br>" +
            "All-in #: %{x}<br>" +
            "Amount Above/Below EV: $%{y:.2f}<extra></extra>",
        text=[name] * allins
    ))

# Add zero reference line
max_allins = max(len(player_stats[p]["history"]) for p in player_stats)

fig.add_shape(
    type="line",
    x0=1,
    y0=0,
    x1=max_allins,
    y1=0,
    line=dict(dash="dash")
)

fig.update_layout(
    title="All-in EV vs Actual 1/31-2/19",
    xaxis_title="All-in Number",
    yaxis_title="Cumulative (Collected − EV) ($)",
    template="plotly_dark",
    hovermode="closest",
)

fig.show()
fig.write_html("ev_graphs.html")

# Final save of lookup table
with open(LOOKUP_PATH, "w") as f:
    json.dump(equity_lookup, f)

print("\nDONE")
