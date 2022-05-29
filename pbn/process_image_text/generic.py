from pbn.process_image_text.pb_info import PBInfoBase


class PBInfo(PBInfoBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lines = self.get_lines()

    def get_current_time(self) -> float:
        return 0

    def get_pb(self) -> float:
        return 0

    def get_last_delta(self) -> float:
        return 0

    def get_lines(self):
        return [l for l in self.text.split("\n") if l != ""]
