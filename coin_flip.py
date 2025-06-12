#!/usr/bin/env python3
import random

def coin_flip():
    """Simple coin flip game"""
    print("🪙 Welcome to Coin Flip Game! 🪙")
    print("-" * 30)
    
    score = {"wins": 0, "losses": 0}
    
    while True:
        # Get user's guess
        print("\nFlipping a coin...")
        guess = input("Call it! (h)eads or (t)ails? (q to quit): ").lower()
        
        if guess == 'q':
            break
        elif guess not in ['h', 'heads', 't', 'tails']:
            print("Invalid input! Use 'h' for heads, 't' for tails, or 'q' to quit.")
            continue
        
        # Flip the coin
        result = random.choice(['heads', 'tails'])
        coin_emoji = "🙂" if result == "heads" else "👑"
        
        print(f"The coin landed on: {result.upper()} {coin_emoji}")
        
        # Check if user won
        user_choice = 'heads' if guess in ['h', 'heads'] else 'tails'
        
        if user_choice == result:
            print("🎉 You won!")
            score["wins"] += 1
        else:
            print("😔 You lost!")
            score["losses"] += 1
        
        print(f"Score: Wins: {score['wins']} | Losses: {score['losses']}")
    
    print(f"\nFinal Score: {score['wins']} wins, {score['losses']} losses")
    print("Thanks for playing! 🪙")

if __name__ == "__main__":
    coin_flip()
