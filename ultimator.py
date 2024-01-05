import httpx
from pathlib import Path


class Ultimator:
    def __init__(self, host: str):
        self.host = host
        self.baseurl = f"http://{host}/v1"

    @property
    def version(self):
        url = f"{self.baseurl}/version"
        response = httpx.get(url)

        return response.json()

    def play_sid_file(self, filepath: Path):
        url = f"{self.baseurl}/runners:sidplay"
        response = httpx.post(url, files={str(filepath.name): filepath.read_bytes()})

        return response

    def play_game_file(self, filepath: Path):
        if filepath.name.endswith("prg"):
            url = f"{self.baseurl}/runners:run_prg"
        elif filepath.name.endswith("crt"):
            url = f"{self.baseurl}/runners:run_crt"
        else:
            raise Exception("Wrong file format")
        response = httpx.post(url, files={str(filepath.name): filepath.read_bytes()})

        return response

    def reset(self):
        url = f"{self.baseurl}/machine:reset"
        return httpx.put(url)

    def reboot(self):
        url = f"{self.baseurl}/machine:reboot"
        return httpx.put(url)

    def poweroff(self):
        url = f"{self.baseurl}/machine:poweroff"
        return httpx.put(url)


if __name__ == "__main__":
    u64 = Ultimator("192.168.1.64")
    print(u64.version)
    p = Path("H:/music/CyberChip/05_Code_Veronica.sid")
    u64.play_sid_file(p)
