import sys
from typing import Optional

from compose import MCTextComposer

USAGE = "usage: python3 compose_cli.py <file_or_dir> [start_word] [length]"


def parse_args(argv: list[str]) -> Optional[tuple[str, Optional[str], int]]:
    if len(argv) < 2 or len(argv) > 4:
        return None

    path = argv[1]
    start_word: Optional[str] = None
    length: int = 50

    if len(argv) >= 3 and argv[2]:
        start_word = argv[2]
    if len(argv) == 4 and argv[3]:
        try:
            length = int(argv[3])
        except ValueError:
            return None

    return path, start_word, length


def main() -> None:
    parsed = parse_args(sys.argv)
    if parsed is None:
        print(USAGE)
        return

    path, start_word, length = parsed

    composer = MCTextComposer(path)
    if start_word:
        print(composer.compose_chain_from(start_word, length))
    else:
        print(composer.compose_random_chain(length))


if __name__ == "__main__":
    main()
