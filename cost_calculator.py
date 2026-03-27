#!/usr/bin/env python3
"""
Netflix vs AI Content Cost Calculator
Calculates how many AI assets you can generate for the price of a streaming subscription.

Usage: python cost_calculator.py --budget 19.99
"""

import argparse

# NexaAPI pricing (as of 2026-03-27, source: nexa-api.com)
NEXAAPI_IMAGE_COST = 0.003   # per image
NEXAAPI_VIDEO_COST = 0.03    # per video clip (estimate)
NEXAAPI_TTS_COST = 0.001     # per audio clip (estimate)

# Netflix pricing (as of 2026-03-27, source: Ars Technica)
NETFLIX_PLANS = {
    "Standard with Ads": 8.99,
    "Standard": 19.99,
    "Premium": 24.99,
}


def calculate(budget: float):
    images = int(budget / NEXAAPI_IMAGE_COST)
    videos = int(budget / NEXAAPI_VIDEO_COST)
    audio = int(budget / NEXAAPI_TTS_COST)

    print(f"\n💰 Budget: ${budget:.2f}")
    print(f"{'─' * 50}")
    print(f"  AI Images  (${NEXAAPI_IMAGE_COST}/each):  {images:,} images")
    print(f"  AI Videos  (${NEXAAPI_VIDEO_COST}/each):  {videos:,} video clips")
    print(f"  TTS Audio  (${NEXAAPI_TTS_COST}/each): {audio:,} audio clips")
    print(f"{'─' * 50}")
    print(f"  → Your own AI content studio for ${budget:.2f}/month")
    print()


def main():
    parser = argparse.ArgumentParser(description="Netflix vs AI Content Cost Calculator")
    parser.add_argument("--budget", type=float, help="Budget in USD")
    args = parser.parse_args()

    print("\n🎬 Netflix vs AI Content Cost Calculator")
    print("=" * 50)
    print("\n📺 Netflix Plans (March 2026 pricing):")
    for plan, cost in NETFLIX_PLANS.items():
        print(f"  {plan}: ${cost}/month")

    print("\n🤖 NexaAPI (nexa-api.com) — CREATE instead of watch:")
    print(f"  Image generation: ${NEXAAPI_IMAGE_COST}/image")
    print(f"  Video generation: ~${NEXAAPI_VIDEO_COST}/clip")
    print(f"  Text-to-speech:   ~${NEXAAPI_TTS_COST}/clip")

    print("\n📊 What you could generate with each Netflix plan:")
    for plan, cost in NETFLIX_PLANS.items():
        print(f"\n  [{plan} — ${cost}/month]")
        calculate(cost)

    if args.budget:
        print(f"\n📊 Custom budget: ${args.budget}")
        calculate(args.budget)

    print("\n🔗 Get started free:")
    print("  Website:    https://nexa-api.com")
    print("  RapidAPI:   https://rapidapi.com/user/nexaquency")
    print("  Python SDK: pip install nexaapi  (https://pypi.org/project/nexaapi/)")
    print("  Node SDK:   npm install nexaapi  (https://www.npmjs.com/package/nexaapi)")
    print()


if __name__ == "__main__":
    main()
