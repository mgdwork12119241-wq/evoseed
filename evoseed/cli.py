from __future__ import annotations

import argparse

from .core import EvolutionLedger, next_generation


def main() -> None:
    parser = argparse.ArgumentParser(prog="evoseed")
    sub = parser.add_subparsers(dest="command", required=True)

    start = sub.add_parser("seed", help="create the next proposed generation")
    start.add_argument("--goal", required=True)
    start.add_argument("--root", default=".evoseed")

    status = sub.add_parser("status", help="show generation history")
    status.add_argument("--root", default=".evoseed")

    args = parser.parse_args()
    ledger = EvolutionLedger(args.root)

    if args.command == "seed":
        generation = next_generation(ledger, args.goal)
        print(f"generation-{generation.number:04d}: {generation.goal}")
        return

    for generation in ledger.all():
        print(f"{generation.number:04d} | {generation.status:9} | {generation.score:6.2f} | {generation.goal}")


if __name__ == "__main__":
    main()
