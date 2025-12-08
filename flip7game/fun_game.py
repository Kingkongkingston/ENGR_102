# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maya Ayoubi
#               Divya Challa        
#               Gia Huynh
#               Kingston Alexander
# Section:      509
# Assignment:   Team Lab 13
# Date:         03 Dec 2025
###############################################################################


import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import random
import json
from collections import namedtuple

# ---------------------------------------------------------
# THEME COLORS 
# ---------------------------------------------------------
Card = namedtuple("Card", ["type", "value", "name"])

COLOR_BG        = "#F2F3F4"     # window background
COLOR_LEFT      = "#D6EAF8"     # left player list panel
COLOR_CENTER    = "#FBFCFC"     # center table
COLOR_RIGHT     = "#FEF5E7"     # right control panel

COLOR_TILE_BORDER   = "#1B2631"
COLOR_NUMBER        = "#2E86C1"
COLOR_MODIFIER      = "#27AE60"
COLOR_ACTION        = "#F39C12"
COLOR_BUST          = "#C0392B"
COLOR_STAY          = "#95A5A6"
COLOR_TEXT_ON_TILE  = "#FFFFFF"
COLOR_PANEL_TITLE   = "#0B5345"

CARD_WIDTH = 68
CARD_HEIGHT = 96

# ---------------------------------------------------------
# DECK CREATION
# ---------------------------------------------------------
def make_deck():
    """
    Create and return a shuffled deck for Flip 7.
    Deck composition follows the rulebook summary:
    - Number cards 1..12 appear with counts matching their numeric frequency:
      12 copies of 12, 11 copies of 11, ... 1 copy of 1. Also one 0.
    - Add a modest number of action and modifier cards (simplified counts).
    """
    deck = []
    deck.append(Card('number', 0, '0'))
    for n in range(1, 13):
        for _ in range(n):
            deck.append(Card('number', n, str(n)))
    modifiers = [
        (('add', 2), "+2"),
        (('add', 4), "+4"),
        (('add', 6), "+6"),
        (('add', 8), "+8"),
        (('add',10), "+10"),
        (('mul', 2), "x2"),
    ]
    for spec, name in modifiers:
        count = 3 if spec[0]=='add' and spec[1] in (2,4) else 2
        if name=="x2": count=3
        for _ in range(count):
            deck.append(Card('modifier', spec, name))
    for _ in range(4):
        deck.append(Card('action', 'flip_three', 'Flip Three'))
    for _ in range(4):
        deck.append(Card('action', 'freeze', 'Freeze'))
    for _ in range(6):
        deck.append(Card('action','second_chance','Second Chance'))
    random.shuffle(deck)
    return deck

class Deck:
    def __init__(self):
        self.cards = make_deck()
    def draw(self):
        return self.cards.pop() if self.cards else None
    def replenish(self):
        self.cards = make_deck()
    def count(self): return len(self.cards)


# ---------------------------------------------------------
# PLAYER MODEL
# ---------------------------------------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.number_cards = []
        self.modifiers = []
        self.action_cards = []
        self.active=True
        self.stayed=False
        self.busted=False

    def reset_round(self):
        self.number_cards=[]
        self.modifiers=[]
        self.action_cards=[]
        self.active=True
        self.stayed=False
        self.busted=False

    def add_card(self, card):
        """Place a card in front of player. Returns info about what happened."""
        if card.type=='number':
            val = card.value
            if val in self.number_cards:
                if 'Second Chance' in self.action_cards:
                    self.action_cards.remove('Second Chance')
                    return ("second_chance_used", val)
                else:
                    self.busted=True
                    self.active=False
                    return ("bust", val)
            self.number_cards.append(val)
            return ("number_added",val)

        elif card.type=='modifier':
            self.modifiers.append(card.value)
            return ("modifier_added",card.value)

        elif card.type=='action':
            if card.value=='second_chance':
                if 'Second Chance' not in self.action_cards:
                    self.action_cards.append('Second Chance')
                    return ("second_chance_added",None)
                return ("second_chance_already",None)
            else:
                self.action_cards.append(card.name)
                return ("action_added",card.name)

    def compute_score(self):
        """
        Compute the score following rules:
        1. Sum number cards
        2. Apply multiplicative modifiers (x2) to the sum of number cards first (may be multiple)
        3. Add additive modifiers (+2..+10)
        4. If Flip7 achieved, add +15 bonus
        """
        if self.busted: return 0
        s=sum(self.number_cards)
        mul=1
        add=0
        for mod in self.modifiers:
            if mod[0]=='mul': mul*=mod[1]
            else: add+=mod[1]
        score = s*mul + add
        if len(self.number_cards)>=7:
            score+=15
        return score

    def has_flip7(self):
        return len(self.number_cards)>=7


# ---------------------------------------------------------
# SECOND CHANCE PASSING
# ---------------------------------------------------------
def pass_second_chance(holder, players):
    for p in players:
        if p is not holder and p.active and 'Second Chance' not in p.action_cards:
            p.action_cards.append('Second Chance')
            return ("second_chance_passed", p.name)
    return ("second_chance_discarded",None)


# ---------------------------------------------------------
# CARD TILE WIDGET
# ---------------------------------------------------------
class CardTile(ttk.Frame):
    def __init__(self, master, card):
        super().__init__(master, width=CARD_WIDTH, height=CARD_HEIGHT)
        self.card = card
        self.canvas = tk.Canvas(self, width=CARD_WIDTH, height=CARD_HEIGHT, highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')
        self._flash_after_id=None
        self.draw_card()

    def draw_card(self):
        c = self.card
        if c.type=='number':
            bg=COLOR_NUMBER
            text=c.name
            sub=""
        elif c.type=='modifier':
            bg=COLOR_MODIFIER
            text=c.name
            sub=""
        else:
            bg=COLOR_ACTION
            parts=c.name.split()
            text=parts[0]
            sub=" ".join(parts[1:]) if len(parts)>1 else ""

        self.canvas.delete("all")
        self.canvas.create_rectangle(3,3,CARD_WIDTH-3,CARD_HEIGHT-3,
                                     fill=bg, outline=COLOR_TILE_BORDER, width=2, tags="bg")
        self.canvas.create_text(CARD_WIDTH/2, CARD_HEIGHT/2-10, text=text,
                                font=("Helvetica",13,"bold"), fill=COLOR_TEXT_ON_TILE)
        if sub:
            self.canvas.create_text(CARD_WIDTH/2, CARD_HEIGHT/2+14, text=sub,
                                    font=("Helvetica",9), fill=COLOR_TEXT_ON_TILE)

    def flash(self, times=4, interval=120):
        def step(n):
            if n<=0:
                self.canvas.itemconfigure("bg", outline=COLOR_TILE_BORDER)
                return
            new = "#FFFFFF" if n%2==0 else COLOR_TILE_BORDER
            self.canvas.itemconfigure("bg", outline=new)
            self._flash_after_id=self.after(interval, lambda: step(n-1))
        step(times)


# ---------------------------------------------------------
# SCROLLABLE FRAME
# ---------------------------------------------------------
class ScrollFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.canvas = tk.Canvas(self, bg=COLOR_CENTER, highlightthickness=0)
        self.v = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.h = ttk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.v.set, xscrollcommand=self.h.set)

        self.v.pack(side='right', fill='y')
        self.h.pack(side='bottom', fill='x')
        self.canvas.pack(side='left', fill='both', expand=True)

        self.inner = ttk.Frame(self.canvas)
        self.win = self.canvas.create_window((0,0), window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))


# ---------------------------------------------------------
# MAIN GUI
# ---------------------------------------------------------
SCORE_FILE="flip7_scores_gui.json"

class Flip7GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flip 7 — Final GUI")
        self.configure(bg=COLOR_BG)
        self.geometry("1500x850")
        self.minsize(1300,750)

        self.players=[]
        self.scores={}
        self.deck=Deck()
        self.current_idx=0
        self.game_in_progress=False

        self._build_layout()
        self._prompt_initial_players()

    # -----------------------------------------------------
    # BUILD PANELS
    # -----------------------------------------------------
    def _build_layout(self):

        # LEFT
        self.left = tk.Frame(self, bg=COLOR_LEFT)
        self.left.grid(row=0,column=0,sticky="nsew", padx=(10,6), pady=10)

        # CENTER
        self.center = tk.Frame(self, bg=COLOR_CENTER)
        self.center.grid(row=0,column=1,sticky="nsew", padx=6, pady=10)

        # RIGHT
        self.right = tk.Frame(self, bg=COLOR_RIGHT)
        self.right.grid(row=0,column=2,sticky="nsew", padx=(6,10), pady=10)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=8)
        self.grid_columnconfigure(2,weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_left()
        self._build_center()
        self._build_right()
        self._build_menu()
    
    # LEFT PANEL ------------------------
    def _build_left(self):
        tk.Label(self.left,text="Players",bg=COLOR_LEFT,
                 fg=COLOR_PANEL_TITLE,font=("Helvetica",14,"bold")).pack(anchor='nw', padx=12, pady=(10,6))

        self.lb = tk.Listbox(self.left, height=9, width=18)
        self.lb.pack(fill='x', padx=12)

        fr = tk.Frame(self.left, bg=COLOR_LEFT)
        fr.pack(pady=6)
        ttk.Button(fr,text="Add", command=self._add_player_dialog).pack(side='left', padx=4)
        ttk.Button(fr,text="Remove", command=self._remove_selected).pack(side='left', padx=4)
        ttk.Button(fr,text="New Game", command=self._new_game).pack(side='left', padx=4)

        tk.Label(self.left,text="Scores",bg=COLOR_LEFT,fg=COLOR_PANEL_TITLE,font=("Helvetica",12,"bold")).pack(anchor='nw', padx=12, pady=(10,4))
        self.scorebox = tk.Text(self.left, height=6, width=18, bg=COLOR_LEFT, bd=0)
        self.scorebox.pack(fill='x', padx=12)

    # CENTER PANEL ----------------------
    def _build_center(self):
        tk.Label(self.center,text="Table",bg=COLOR_CENTER,
                 fg=COLOR_PANEL_TITLE,font=("Helvetica",14,"bold")).pack(anchor='nw', padx=12,pady=(10,6))

        self.scroll = ScrollFrame(self.center)
        self.scroll.pack(fill='both',expand=True,padx=20,pady=(0,10))
        self.table_inner = self.scroll.inner
        self.player_frames=[]

    # RIGHT PANEL -----------------------
    def _build_right(self):
        tk.Label(self.right,text="Controls",bg=COLOR_RIGHT,
                 fg=COLOR_PANEL_TITLE,font=("Helvetica",14,"bold")).pack(anchor='nw', padx=12,pady=(10,6))

        fr=tk.Frame(self.right,bg=COLOR_RIGHT)
        fr.pack(padx=12,pady=4)

        self.btn_hit = tk.Button(fr,text="HIT",bg="#1ABC9C",fg="white",width=14, command=self._hit)
        self.btn_stay = tk.Button(fr,text="STAY",bg="#F39C12",fg="white",width=14, command=self._stay)
        self.btn_start = tk.Button(fr,text="Start Round",bg="#3498DB",fg="white",width=14, command=self._start_round)

        self.btn_hit.pack(pady=6)
        self.btn_stay.pack(pady=6)
        self.btn_start.pack(pady=6)

        self.btn_hit.config(state='disabled')
        self.btn_stay.config(state='disabled')

        ttk.Separator(self.right,orient='horizontal').pack(fill='x',padx=12,pady=10)

        tk.Label(self.right,text="Game Log",bg=COLOR_RIGHT,
                 fg=COLOR_PANEL_TITLE,font=("Helvetica",14,"bold")).pack(anchor='nw', padx=12)
        self.log = tk.Text(self.right,height=18,bg="white")
        self.log.pack(fill='both',expand=True,padx=12,pady=(0,10))

        self.status = tk.Label(self.right,text="Status: Waiting",bg=COLOR_RIGHT,anchor='w')
        self.status.pack(fill='x', padx=12,pady=(0,6))

    # MENU ------------------------------
    def _build_menu(self):
        m=tk.Menu(self)
        g=tk.Menu(m,tearoff=0)
        g.add_command(label="New Game", command=self._new_game)
        g.add_command(label="Start Round", command=self._start_round)
        g.add_separator()
        g.add_command(label="Quit", command=self.quit)
        m.add_cascade(label="Game",menu=g)

        h=tk.Menu(m,tearoff=0)
        h.add_command(label="Rules", command=self._rules)
        m.add_cascade(label="Help",menu=h)
        self.config(menu=m)

    # -----------------------------------------------------
    # PLAYER MGMT
    # -----------------------------------------------------
    def _prompt_initial_players(self):
        n = simpledialog.askinteger("Players","Number of players (2-8):",minvalue=2,maxvalue=12)
        if not n: n=2
        for i in range(n):
            name = simpledialog.askstring("Name",f"Player {i+1}:")
            if not name: name=f"Player{i+1}"
            self._add_player(name)
        self._render_players()

    def _add_player_dialog(self):
        name = simpledialog.askstring("Add player","Name:")
        if name:
            self._add_player(name)
            self._render_players()

    def _add_player(self,name):
        self.players.append(Player(name))
        self.scores.setdefault(name,0)
        self._update_lb()

    def _remove_selected(self):
        s=self.lb.curselection()
        if not s: return
        name=self.lb.get(s[0])
        self.players=[p for p in self.players if p.name!=name]
        if name in self.scores: del self.scores[name]
        self._render_players()

    def _update_lb(self):
        self.lb.delete(0,tk.END)
        for p in self.players:
            self.lb.insert(tk.END,p.name)

    # -----------------------------------------------------
    # RENDER PLAYER PANELS IN CENTER
    # -----------------------------------------------------
    def _render_players(self):
        for w in self.table_inner.winfo_children():
            w.destroy()
        self.player_frames=[]

        cols=2
        for i,p in enumerate(self.players):
            r=i//cols
            c=i%cols
            f=tk.Frame(self.table_inner,bg=COLOR_CENTER,relief='raised',bd=2)
            f.grid(row=r,column=c,sticky="nsew",padx=12,pady=12)

            self.table_inner.grid_rowconfigure(r,weight=1)
            self.table_inner.grid_columnconfigure(c,weight=1)

            tk.Label(f,text=p.name,bg=COLOR_CENTER,fg=COLOR_PANEL_TITLE,
                     font=("Helvetica",12,"bold")).pack(anchor='nw',padx=6,pady=(6,2))
            tk.Label(f,text=f"Total: {self.scores.get(p.name,0)}",bg=COLOR_CENTER).pack(anchor='nw',padx=6)

            # number tiles
            nf=tk.Frame(f,bg=COLOR_CENTER); nf.pack(fill='x',padx=6,pady=(8,4))
            tk.Label(nf,text="Numbers:",bg=COLOR_CENTER).pack(side='left')
            num_tiles=tk.Frame(nf,bg=COLOR_CENTER); num_tiles.pack(side='left',padx=6)

            mf=tk.Frame(f,bg=COLOR_CENTER); mf.pack(fill='x',padx=6,pady=4)
            tk.Label(mf,text="Modifiers:",bg=COLOR_CENTER).pack(side='left')
            mod_tiles=tk.Frame(mf,bg=COLOR_CENTER); mod_tiles.pack(side='left',padx=6)

            af=tk.Frame(f,bg=COLOR_CENTER); af.pack(fill='x',padx=6,pady=4)
            tk.Label(af,text="Actions:",bg=COLOR_CENTER).pack(side='left')
            act_tiles=tk.Frame(af,bg=COLOR_CENTER); act_tiles.pack(side='left',padx=6)

            status=tk.Label(f,text="Status: Ready",bg=COLOR_CENTER,anchor='w',relief='groove')
            status.pack(fill='x',padx=6,pady=(6,8))

            self.player_frames.append({
                "player":p,
                "frame":f,
                "num_tiles":num_tiles,
                "mod_tiles":mod_tiles,
                "act_tiles":act_tiles,
                "status":status,
                "created_num":[],
                "created_mod":[],
                "created_act":[]
            })

        self._refresh_tiles()
        self._update_lb()
        self._update_scorebox()

    # -----------------------------------------------------
    # UPDATE SCORE BOX (LEFT)
    # -----------------------------------------------------
    def _update_scorebox(self):
        self.scorebox.delete("1.0",tk.END)
        for name,val in sorted(self.scores.items()):
            self.scorebox.insert(tk.END,f"{name}: {val}\n")

    # -----------------------------------------------------
    # REFRESH PLAYER TILE AREAS
    # -----------------------------------------------------
    def _refresh_tiles(self):
        for pf in self.player_frames:
            p=pf["player"]

            for holder in (pf["num_tiles"],pf["mod_tiles"],pf["act_tiles"]):
                for w in holder.winfo_children(): w.destroy()

            pf["created_num"].clear()
            pf["created_mod"].clear()
            pf["created_act"].clear()

            for v in p.number_cards:
                card=Card('number',v,str(v))
                t=CardTile(pf["num_tiles"],card)
                t.canvas.itemconfigure("bg",fill=COLOR_NUMBER,outline=COLOR_TILE_BORDER)
                t.pack(side='left',padx=6,pady=6)
                pf["created_num"].append((card.name,t))

            for mod in p.modifiers:
                name=f"x{mod[1]}" if mod[0]=='mul' else f"+{mod[1]}"
                card=Card('modifier',mod,name)
                t=CardTile(pf["mod_tiles"],card)
                t.canvas.itemconfigure("bg",fill=COLOR_MODIFIER,outline=COLOR_TILE_BORDER)
                t.pack(side='left',padx=6,pady=6)
                pf["created_mod"].append((card.name,t))

            for act in p.action_cards:
                if act.lower().startswith("flip"):
                    card=Card('action','flip_three','Flip Three')
                elif act.lower().startswith("freeze"):
                    card=Card('action','freeze','Freeze')
                elif act.lower().startswith("second"):
                    card=Card('action','second_chance','Second Chance')
                else:
                    card=Card('action',None,act)
                t=CardTile(pf["act_tiles"],card)
                t.canvas.itemconfigure("bg",fill=COLOR_ACTION,outline=COLOR_TILE_BORDER)
                t.pack(side='left',padx=6,pady=6)
                pf["created_act"].append((card.name,t))

            # status
            if p.busted:
                pf["status"].config(text="Status: BUSTED")
            elif p.stayed:
                pf["status"].config(text="Status: Stayed")
            elif p.active:
                pf["status"].config(text="Status: Active")
            else:
                pf["status"].config(text="Status: Inactive")

    # -----------------------------------------------------
    # START ROUND
    # -----------------------------------------------------
    def _start_round(self):
        if len(self.players)<2:
            messagebox.showinfo("Not enough", "At least 2 players required.")
            return
        self.deck=Deck()
        for p in self.players:
            p.reset_round()
        self.game_in_progress=True
        self._log("New round started. Dealing initial cards...")

        for p in self.players:
            c=self.deck.draw()
            if not c:
                self.deck.replenish()
                c=self.deck.draw()
            self._log(f"{p.name} receives {c.name}")
            res=p.add_card(c)
            if c.type=='action':
                if c.value=='flip_three':
                    self._log(f"Flip Three during deal -> resolving for {p.name}")
                    self._flip_three(p)
                elif c.value=='freeze':
                    p.stayed=True
                    p.active=False
                elif c.value=='second_chance':
                    self._log(f"{p.name} gains a Second Chance.")

        self._refresh_players_after_change(start=True)
        self.btn_hit.config(state='normal')
        self.btn_stay.config(state='normal')
        self.btn_start.config(state='disabled')
        self.status.config(text="Status: Round in progress")

    # -----------------------------------------------------
    # REFRESH + SET TURN
    # -----------------------------------------------------
    def _refresh_players_after_change(self, start=False):
        self._refresh_tiles()
        # choose next active
        self._next_active(start)

    def _next_active(self, start=False):
        n=len(self.players)
        if n==0: return
        tries=0
        if not start:
            self.current_idx=(self.current_idx+1)%n
        while tries<n:
            p=self.players[self.current_idx]
            if p.active and not p.stayed and not p.busted:
                break
            self.current_idx=(self.current_idx+1)%n
            tries+=1
        else:
            self._end_round()
            return
        self._highlight_current()

    def _highlight_current(self):
        for i,pf in enumerate(self.player_frames):
            if i==self.current_idx:
                pf["frame"].config(bd=3,relief='groove')
                pf["status"].config(text="Status: Your Turn")
            else:
                pf["frame"].config(bd=1,relief='raised')
                p=pf["player"]
                if p.busted: s="BUSTED"
                elif p.stayed: s="Stayed"
                elif p.active: s="Active"
                else: s="Inactive"
                pf["status"].config(text=f"Status: {s}")

    # -----------------------------------------------------
    # HIT
    # -----------------------------------------------------
    def _hit(self):
        if not self.game_in_progress: return
        p=self.players[self.current_idx]
        if not (p.active and not p.stayed and not p.busted):
            self._next_active()
            return

        c=self.deck.draw()
        if not c:
            self.deck.replenish()
            c=self.deck.draw()
            self._log("Deck replenished.")
        self._log(f"{p.name} flips {c.name}")

        if c.type=='action' and c.value=='flip_three':
            p.add_card(c)
            self._log(f"{p.name} triggers Flip Three!")
            self._flip_three(p)
        elif c.type=='action' and c.value=='freeze':
            p.add_card(c)
            p.stayed=True
            p.active=False
            self._log(f"{p.name} froze and leaves round.")
            self._refresh_players_after_change()
        elif c.type=='action' and c.value=='second_chance':
            res=p.add_card(c)
            if res[0]=='second_chance_already':
                others=[pl for pl in self.players if pl is not p and pl.active and 'Second Chance' not in pl.action_cards]
                if others:
                    names=", ".join([o.name for o in others])
                    choice=simpledialog.askstring("Pass Second Chance",
                                                  f"Who receives it? Options: {names}")
                    if choice in [o.name for o in others]:
                        for o in others:
                            if o.name==choice:
                                o.action_cards.append("Second Chance")
                                self._log(f"{p.name} passes it to {choice}")
                                break
                    else:
                        r=pass_second_chance(p,self.players)
                        self._log(str(r))
                else:
                    r=pass_second_chance(p,self.players)
                    self._log(str(r))
            else:
                self._log(f"{p.name} gains a Second Chance.")
            self._refresh_players_after_change()
        else:
            res=p.add_card(c)
            if res[0]=='bust':
                self._log(f"{p.name} BUSTED on {res[1]}!")
            elif res[0]=='second_chance_used':
                self._log(f"{p.name} used Second Chance on {res[1]}.")
            self._refresh_players_after_change()

            if p.has_flip7():
                self._log(f"{p.name} achieved Flip 7! Round ends.")
                self._end_round()
                return

    # -----------------------------------------------------
    # STAY
    # -----------------------------------------------------
    def _stay(self):
        if not self.game_in_progress: return
        p=self.players[self.current_idx]
        if not (p.active and not p.stayed and not p.busted):
            self._next_active()
            return
        p.stayed=True
        p.active=False
        self._log(f"{p.name} stays and banks points.")
        self._refresh_players_after_change()

    # -----------------------------------------------------
    # FLIP THREE RESOLUTION
    # -----------------------------------------------------
    def _flip_three(self, player):
        """
    Flip Three: player must accept next three cards one at a time.
    Returns a list of events for each drawn card.
    game_state: dict to allow passing a Second Chance card to others if needed (see rules)
    """
        drawn=[]
        for _ in range(3):
            if not player.active: break
            c=self.deck.draw()
            if not c:
                self.deck.replenish()
                c=self.deck.draw()
            drawn.append(c)

        def process(i):
            if i>=len(drawn) or player.busted:
                if 'Freeze' in player.action_cards:
                    player.stayed=True
                    player.active=False
                    player.action_cards.remove('Freeze')
                    self._log(f"{player.name} freeze resolved after Flip Three.")
                self._refresh_players_after_change()
                return

            c=drawn[i]
            res=player.add_card(c)
            self._log(f"{player.name} FlipThree draws {c.name}")
            if c.type=='action' and c.value=='second_chance' and res[0]=='second_chance_already':
                r=pass_second_chance(player,self.players)
                self._log(str(r))

            self._refresh_tiles()
            self._flash_tile(player,c)

            if res[0]=='bust':
                self._log(f"{player.name} BUSTED on {res[1]} (Flip Three)")
            elif res[0]=='second_chance_used':
                self._log(f"{player.name} uses Second Chance during Flip Three.")

            self.after(420, lambda: process(i+1))

        process(0)

    # flash tile that matches card
    def _flash_tile(self, player, card):
        for pf in self.player_frames:
            if pf["player"] is player:
                for lst in (pf["created_num"],pf["created_mod"],pf["created_act"]):
                    for name,tile in reversed(lst):
                        if name==card.name:
                            tile.flash()
                            return

    # -----------------------------------------------------
    # END ROUND
    # -----------------------------------------------------
    def _end_round(self):
        self._log("Round finished. Scoring...")
        for p in self.players:
            pts = p.compute_score()
            self.scores[p.name] = self.scores.get(p.name,0)+pts
            self._log(f"{p.name}: +{pts} (Total={self.scores[p.name]})")

        self.game_in_progress=False
        self.btn_hit.config(state='disabled')
        self.btn_stay.config(state='disabled')
        self.btn_start.config(state='normal')
        self._refresh_tiles()
        self._update_scorebox()
        self._save_scores()
        self.status.config(text="Status: Round complete")

    # -----------------------------------------------------
    # LOGGING / MISC
    # -----------------------------------------------------
    def _log(self,msg):
        self.log.insert(tk.END,msg+"\n")
        self.log.see(tk.END)

    def _rules(self):
        messagebox.showinfo("Rules",
            "Flip 7 Rules (Short):\n"
            "- Unique numbers only; duplicate = bust unless Second Chance.\n"
            "- 7 unique numbers gives immediate +15 bonus and ends round.\n"
            "- Modifiers: x2 multiplies total, +N adds after.\n"
            "- Actions: Flip Three, Freeze, Second Chance.\n"
        )

    def _new_game(self):
        """
    Play one round until either:
    - No active players remain
    - A player flips 7 unique numbers -> round ends immediately
    Returns updated scores dict and cards to discard.
    """
        if messagebox.askyesno("New Game","Reset scores?"):
            self.scores={p.name:0 for p in self.players}
            for p in self.players: p.reset_round()
            self.game_in_progress=False
            self.btn_hit.config(state='disabled')
            self.btn_stay.config(state='disabled')
            self.btn_start.config(state='normal')
            self._render_players()
            self.status.config(text="Status: New Game")

    def _save_scores(self):
        try:
            with open(SCORE_FILE,'w') as f:
                json.dump(self.scores,f,indent=2)
        except: pass


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------
if __name__ == "__main__":
    Flip7GUI().mainloop()
