from pbn.process_image_text.pb_info import PBInfo


class PBInfo(PBInfo):
    def get_current_time(self) -> float:
        return 0

    def get_pb(self) -> float:
        return 0

    def get_last_delta(self) -> float:
        return 0
