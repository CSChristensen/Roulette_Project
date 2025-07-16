#!/usr/bin/env python3
"""
Main entry point for the Enhanced Roulette Game.

This file serves as the primary executable for the roulette game simulation
with support for both color betting and number betting.

Features:
- Color betting: Red/Black (2:1), Green (35:1)
- Number betting: Any number 0-36 (35:1)
- Multiple bets per round
- Interactive user interface
- Comprehensive input validation

Usage:
    python main.py
    python -m src.Rouletee
"""

from src.Rouletee import main

if __name__ == "__main__":
    main()