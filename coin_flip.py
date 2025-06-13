#!/usr/bin/env python3
import random

def coin_flip():
    """Simple coin flip game with checkpoints every 100 rounds"""
    print("🪙 Welcome to Coin Flip Game! 🪙")
    print("-" * 30)
    
    score = {"wins": 0, "losses": 0}
    round_count = 0
    
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
        
        round_count += 1
        print(f"Score: Wins: {score['wins']} | Losses: {score['losses']} | Round: {round_count}")
        
        # Check for milestone checkpoints
        if round_count % 100 == 0:
            total_rounds = score["wins"] + score["losses"]
            win_percentage = (score["wins"] / total_rounds) * 100 if total_rounds > 0 else 0
            
            print("\n" + "="*50)
            print(f"🎯 CHECKPOINT REACHED - ROUND {round_count}! 🎯")
            print(f"You won {score['wins']}/{total_rounds} rounds ({win_percentage:.1f}%)")
            print(f"Wins: {score['wins']} | Losses: {score['losses']}")
            print("="*50)
            
            # Ask if they want to continue
            continue_game = input("\nContinue playing? (y/n): ").lower()
            if continue_game in ['n', 'no']:
                break
    
    # Final summary
    total_rounds = score["wins"] + score["losses"]
    if total_rounds > 0:
        win_percentage = (score["wins"] / total_rounds) * 100
        print(f"\n🏁 FINAL RESULTS:")
        print(f"Total rounds played: {total_rounds}")
        print(f"Final Score: {score['wins']} wins, {score['losses']} losses")
        print(f"Win percentage: {win_percentage:.1f}%")
    
    print("Thanks for playing! 🪙")

if __name__ == "__main__":
    coin_flip()