from pathlib import Path

from nicegui import ui

from local_file_picker import local_file_picker
from settings import HOST, SID_PATH, GAMES_PATH
from ultimator import Ultimator


async def pick_game_file() -> None:
    result, = await local_file_picker(directory=GAMES_PATH)
    if result.endswith(".prg") or result.endswith("crt"):
        ui.notify(f"Loading {result}")
        u64 = Ultimator(HOST)
        response = u64.play_game_file(Path(result))
        ui.notify(response)


async def pick_sid_file() -> None:
    result, = await local_file_picker(SID_PATH)
    if result.endswith(".sid"):
        ui.notify(f"Loading {result}")
        u64 = Ultimator(HOST)
        response = u64.play_sid_file(Path(result))
        ui.notify(response)
    else:
        ui.notify("Not a SID-File")


async def reset() -> None:
    u64 = Ultimator(HOST)
    response = u64.reset()
    ui.notify(response)


async def reboot() -> None:
    u64 = Ultimator(HOST)
    response = u64.reboot()
    ui.notify(response)


async def poweroff() -> None:
    u64 = Ultimator(HOST)
    response = u64.poweroff()
    ui.notify(response)


def main():
    ui.markdown("## Ultimate Control")
    with ui.row():
        ui.button("Choose game", on_click=pick_game_file, icon="folder")
        ui.button("Choose SID-track", on_click=pick_sid_file, icon="folder")
        ui.button("Reset", on_click=reset)
        ui.button("Reboot", on_click=reboot)
        ui.button("Power Off", on_click=poweroff)

    ui.run()


if __name__ in ["__main__", "__mp_main__"]:
    main()
