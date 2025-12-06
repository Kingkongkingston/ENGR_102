import json
import time
import sys
from collections import Counter
import random
from collections import Counter, namedtuple

# Card representation
Card = namedtuple("Card", ["type", "value", "name"])
# type: 'number', 'action', 'modifier'
# value: for number cards -> int (0..12)
#        for modifiers -> details (e.g., ('add', 4) or ('mul', 2))
#        for actions -> action id strings like 'flip_three', 'freeze', 'second_chance'


def make_deck():
    """
    Create and return a shuffled deck for Flip 7.
    Deck composition follows the rulebook summary:
    - Number cards 1..12 appear with counts matching their numeric frequency:
      12 copies of 12, 11 copies of 11, ... 1 copy of 1. Also one 0.
    - Add a modest number of action and modifier cards (simplified counts).
    """
    deck = []

    # Number cards: 1..12 with counts equal to the number; plus one 0
    deck.append(Card('number', 0, '0'))
    for n in range(1, 13):
        for _ in range(n):  # n copies of card n, e.g., 12 copies of 12
            deck.append(Card('number', n, str(n)))

    # Modifier cards (simplified counts)
    modifiers = [
        (('add', 2), "+2"),
        (('add', 4), "+4"),
        (('add', 6), "+6"),
        (('add', 8), "+8"),
        (('add', 10), "+10"),
        (('mul', 2), "x2"),
    ]
    # duplicates to approximate variety
    for spec, name in modifiers:
        count = 3 if spec[0] == 'add' and spec[1] in (2, 4) else 2
        if name == "x2":
            count = 3
        for _ in range(count):
            deck.append(Card('modifier', spec, name))

    # Action cards (simplified counts)
    # Flip Three, Freeze, Second Chance
    for _ in range(4):
        deck.append(Card('action', 'flip_three', 'Flip Three'))
    for _ in range(4):
        deck.append(Card('action', 'freeze', 'Freeze'))
    for _ in range(6):
        deck.append(Card('action', 'second_chance', 'Second Chance'))

    random.shuffle(deck)
    return deck


class Deck:
    def __init__(self, cards=None):
        self.cards = cards if cards is not None else make_deck()

    def draw(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def shuffle_in(self, cards):
        """Shuffle a list of discarded cards back into the deck."""
        self.cards.extend(cards)
        random.shuffle(self.cards)

    def count(self):
        return len(self.cards)


# Part 2: Player model & scoring


class Player:
    def __init__(self, name):
        self.name = name
        self.number_cards = []     # list of int values
        # list of modifier specs: ('add',2) or ('mul',2)
        self.modifiers = []
        self.action_cards = []     # stored action cards like 'Second Chance'
        self.active = True         # active in the current round
        self.stayed = False        # has chosen to Stay
        self.busted = False

    def reset_round(self):
        self.number_cards = []
        self.modifiers = []
        self.action_cards = []
        self.active = True
        self.stayed = False
        self.busted = False

    def add_card(self, card):
        """Place a card in front of player. Returns info about what happened."""
        if card is None:
            return ("no_card", None)

        if card.type == 'number':
            val = card.value
            # check for duplicate number -> bust unless have second chance
            if val in self.number_cards:
                # if they have a Second Chance action stored, consume it and discard the duplicate number
                if 'Second Chance' in self.action_cards:
                    self.action_cards.remove('Second Chance')
                    return ("second_chance_used", val)
                else:
                    self.busted = True
                    self.active = False
                    return ("bust", val)
            else:
                self.number_cards.append(val)
                # if they've flipped 7 unique numbers they'll end the round (handled externally)
                return ("number_added", val)

        elif card.type == 'modifier':
            self.modifiers.append(card.value)
            return ("modifier_added", card.value)

        elif card.type == 'action':
            # action placed in player's action area
            if card.value == 'second_chance':
                # For Second Chance, it is stored and can prevent the next duplicate
                # Only one Second Chance at a time. If already have one, will be passed or discarded (handled externally)
                if 'Second Chance' not in self.action_cards:
                    self.action_cards.append('Second Chance')
                    return ("second_chance_added", None)
                else:
                    return ("second_chance_already", None)
            else:
                # For Freeze and Flip Three, store them for immediate resolution if needed
                # store 'Freeze' or 'Flip Three'
                self.action_cards.append(card.name)
                return ("action_added", card.name)

    def has_flip7(self):
        """Return True if player has 7 unique number cards."""
        return len(self.number_cards) >= 7

    def compute_score(self):
        """
        Compute the score following rules:
        1. Sum number cards
        2. Apply multiplicative modifiers (x2) to the sum of number cards first (may be multiple)
        3. Add additive modifiers (+2..+10)
        4. If Flip7 achieved, add +15 bonus
        """
        num_sum = sum(self.number_cards)
        # apply multipliers
        mul_total = 1
        add_total = 0
        for mod in self.modifiers:
            if mod[0] == 'mul':
                mul_total *= mod[1]
            elif mod[0] == 'add':
                add_total += mod[1]

        score = num_sum * mul_total + add_total
        if self.has_flip7():
            score += 15
        return int(score)

    def snapshot(self):
        """Return a readable snapshot of player's front-of-table cards."""
        return {
            "name": self.name,
            "numbers": list(self.number_cards),
            "modifiers": list(self.modifiers),
            "actions": list(self.action_cards),
            "busted": self.busted,
            "stayed": self.stayed,
        }


# Part 3: Action & Modifier resolution


def resolve_freeze(player, game_state):
    """
    Freeze: player banks all current points and is out of the round.
    We'll mark them as stayed/inactive; the caller should add their score to totals.
    """
    player.stayed = True
    player.active = False
    # Freeze doesn't immediately remove cards; it ends player's active participation this round
    return ("freeze_resolved", player.name)


def resolve_flip_three(player, deck, game_state):
    """
    Flip Three: player must accept next three cards one at a time.
    Returns a list of events for each drawn card.
    game_state: dict to allow passing a Second Chance card to others if needed (see rules)
    """
    events = []
    for i in range(3):
        if not player.active:
            break
        card = deck.draw()
        if card is None:
            events.append(("no_deck", None))
            break
        # If card is an action and it's Flip Three or Freeze, per rules those are resolved AFTER drawing 3 unless bust happened.
        # We'll add the card to the player's action area, but delay special action resolution until the end of the three-flip, unless it caused immediate duplicate bust.
        if card.type == 'number':
            result = player.add_card(card)
            events.append((result[0], result[1], card))
            if player.busted:
                # stop further flips
                break
        elif card.type == 'modifier':
            result = player.add_card(card)
            events.append((result[0], result[1], card))
        elif card.type == 'action':
            # If Second Chance is drawn during Flip Three: keep it for player.
            # If Flip Three or Freeze drawn, record them to resolve AFTER the three flips (but store in player's action_cards so snapshot shows it).
            result = player.add_card(card)
            events.append((result[0], result[1], card))
            # do not immediately resolve flip_three or freeze here
    # After the three flips, resolve any Flip Three/Freeze action cards that were added during the flipping,
    # but only if player hasn't busted.
    if not player.busted:
        # Check for Freeze
        if 'Freeze' in player.action_cards:
            # resolve freeze (player banks and becomes inactive)
            resolve_freeze(player, game_state)
            events.append(("freeze_resolved_post", player.name))
            # remove Freeze card from action list once resolved
            try:
                player.action_cards.remove('Freeze')
            except ValueError:
                pass
        # Check for Flip Three cards that were drawn during the sequence (rare recursive); we won't chain them automatically to avoid infinite loops,
        # but we'll let the action persist for later if needed. (Simplified rule)
    return events


def pass_second_chance(card_holder, players):
    """
    Rule: If a Second Chance card is drawn when the player already has one, they must choose another active player to give it to.
    Since we don't have interactive passing within this helper, we implement simple logic:
    - Find another active player without Second Chance and give it to them.
    - If none, discard it.
    """
    for p in players:
        if p.active and 'Second Chance' not in p.action_cards:
            p.action_cards.append('Second Chance')
            return ("second_chance_passed", p.name)
    return ("second_chance_discarded", None)


# Part 4: Game flow, UI, file I/O


# Assume Deck, Card, Player, resolve_flip_three, resolve_freeze, pass_second_chance are available in the same file.

SCORE_FILE = "flip7_scores.json"


def save_scores(highscores):
    try:
        with open(SCORE_FILE, 'w') as f:
            json.dump(highscores, f, indent=2)
    except Exception as e:
        print("Error saving scores:", e)


def load_scores():
    try:
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return {}


def display_rules():
    print("\n--- Flip 7 (simplified rules) ---")
    print("Objective: Be the first to reach 200 points.")
    print("Collect number cards (0-12). If you ever get a duplicate number you bust and score 0 this round unless you have Second Chance.")
    print("Flip 7 unique number cards -> +15 bonus and you end the round immediately.")
    print("Modifiers change scoring: x2 doubles number-sum, +N adds N after multipliers.")
    print("Action cards: Flip Three forces 3 flips, Freeze banks player immediately, Second Chance protects one duplicate.")
    print("Full rules in provided PDF.\n")


def prompt_int(prompt, minv=None, maxv=None):
    """Safe integer input with try-except."""
    while True:
        try:
            val = int(input(prompt))
            if minv is not None and val < minv:
                print("Value too small.")
                continue
            if maxv is not None and val > maxv:
                print("Value too large.")
                continue
            return val
        except ValueError:
            print("Invalid integer; try again.")


def create_players():
    n = prompt_int("Number of players (2-8 recommended): ", 2, 12)
    players = []
    for i in range(n):
        name = input(f"Name for player {i+1}: ").strip() or f"Player{i+1}"
        players.append(Player(name))
    return players


def initial_deal(deck, players):
    """Deal one card face-up to each player in turn, resolve actions revealed during dealing immediately."""
    for p in players:
        card = deck.draw()
        if card is None:
            print("Deck ran out while dealing.")
            break
        print(f"Dealt to {p.name}: {card.name}")
        if card.type == 'action':
            # immediate resolution if action appears during deal
            if card.value == 'flip_three':
                p.add_card(card)  # store the action
                print(f"{p.name} got Flip Three during deal -> must flip three now.")
                events = resolve_flip_three(p, deck, game_state={})
                for ev in events:
                    print("  event:", ev)
            elif card.value == 'freeze':
                p.add_card(card)
                resolve_freeze(p, {})
                print(f"{p.name} got Freeze during deal -> frozen and out of round.")
            elif card.value == 'second_chance':
                res = p.add_card(card)
                print(f"{p.name} got Second Chance during deal.")
        else:
            p.add_card(card)


def round_loop(deck, players, scores):
    """
    Play one round until either:
    - No active players remain
    - A player flips 7 unique numbers -> round ends immediately
    Returns updated scores dict and cards to discard.
    """
    # reset players for round
    for p in players:
        p.reset_round()

    # track discarded cards to reshuffle later
    discarded = []

    # initial deal
    initial_deal(deck, players)

    # main turns: dealer offers Hit/Stay in turn order repeatedly
    turn_index = 0
    def active_players_exist(): return any(
        p.active and not p.stayed for p in players)
    while active_players_exist():
        p = players[turn_index % len(players)]
        turn_index += 1
        if not p.active or p.stayed or p.busted:
            continue

        print("\n--- Turn for", p.name)
        print("Front:", p.snapshot())
        # If they have no cards, they cannot Stay (rule requires at least one card to stay)
        can_stay = bool(p.number_cards or p.modifiers or p.action_cards)

        action = None
        while True:
            if can_stay:
                choice = input(
                    "Choose: (h)it, (s)tay, (i)nfo: ").strip().lower()
            else:
                choice = input(
                    "You have no cards in front. Choose: (h)it, (i)nfo: ").strip().lower()
                if choice == 's':
                    print("You can't stay with no cards.")
                    continue
            if choice in ('h', 'hit'):
                action = 'hit'
                break
            elif choice in ('s', 'stay') and can_stay:
                action = 'stay'
                break
            elif choice in ('i', 'info'):
                print("Info:", p.snapshot())
            else:
                print("Invalid choice. Try again.")

        if action == 'stay':
            p.stayed = True
            p.active = False
            print(p.name, "stays and banks points.")
            continue

        # action == 'hit'
        card = deck.draw()
        if card is None:
            print("Deck exhausted.")
            break
        print(f"{p.name} flipped: {card.name}")

        if card.type == 'action' and card.value == 'flip_three':
            p.add_card(card)
            events = resolve_flip_three(p, deck, game_state={})
            for ev in events:
                print("  event:", ev)
        elif card.type == 'action' and card.value == 'freeze':
            p.add_card(card)
            resolve_freeze(p, {})
            print(f"{p.name} is frozen (banks and out).")
        elif card.type == 'action' and card.value == 'second_chance':
            res = p.add_card(card)
            if res[0] == 'second_chance_already':
                # pass to another active player per rules
                res2 = pass_second_chance(p, players)
                print("Second Chance could not be kept:", res2)
            else:
                print(f"{p.name} keeps a Second Chance.")
        else:
            # number or modifier
            res = p.add_card(card)
            print("Result:", res)
            if res[0] == 'bust':
                print(p.name, "busted on", res[1])
            elif res[0] == 'second_chance_used':
                print(
                    p.name, "used a Second Chance to avoid duplicate", res[1])

        # check for Flip7 finish
        if p.has_flip7():
            print(p.name, "has Flip 7 (7 unique numbers)! Round ends.")
            break

    # End of round: compute scores for everyone who didn't bust
    for p in players:
        round_score = 0 if p.busted else p.compute_score()
        scores[p.name] = scores.get(p.name, 0) + round_score
        print(f"{p.name} scored {round_score} — Total: {scores[p.name]}")

    # assemble all players' cards into discard pile (we do not shuffle them back in this round)
    # (In a fuller simulation we'd track exact cards; here we just approximate by reshuffling nothing.)
    return scores, discarded


def main():
    print("Welcome to Flip 7 (console edition).")
    highscores = load_scores()
    while True:
        print("\nMenu: (p)lay  (r)ules  (s)cores  (q)uit")
        cmd = input("Choice: ").strip().lower()
        if cmd in ('q', 'quit'):
            print("Bye.")
            save_scores(highscores)
            break
        elif cmd in ('r', 'rules'):
            display_rules()
        elif cmd in ('s', 'scores'):
            print("Highscores:", highscores)
        elif cmd in ('p', 'play'):
            players = create_players()
            deck = Deck()
            scores = {p.name: 0 for p in players}
            # Play rounds until someone reaches 200
            while max(scores.values()) < 200:
                print("\nStarting new round. Deck cards remaining:", deck.count())
                scores, discards = round_loop(deck, players, scores)
                # When deck low, reshuffle discards (here discards empty in this simplified version)
                if deck.count() < 10:
                    # In real game we'd collect all used cards; for now, remake deck to keep game going
                    print("Resupplying deck.")
                    deck = Deck()
                print("Scores after round:", scores)
                cont = input("Continue playing? (y/n) ").strip().lower()
                if cont != 'y':
                    break
            # update highscores
            for k, v in scores.items():
                highscores[k] = max(highscores.get(k, 0), v)
            save_scores(highscores)
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
