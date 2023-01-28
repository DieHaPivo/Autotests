import xml.etree.ElementTree as ET

import pytest

from Pages.ConfPage import ConfPage
from Pages.SnapshotPage import SnapshotPage
from api.cam import CamApi


class TestSnapshot:

    @pytest.mark.parametrize("quality", ['1', '2', '3', '4', '5', '6', '7'])
    def test_snapshot_params(self, page, quality):
        conf_page = ConfPage(page)
        snap_page = SnapshotPage(page)
        conf_page.av_button.click()
        conf_page.snapshot_button.click()
        snap_page.quality_selector.select_option(quality)
        snap_page.interval_input.fill("123")
        snap_page.save_button.click(force=True)
        snap_request = CamApi().get_snap_info()
        snap_quality_from_api = ET.fromstring(snap_request.content)[0][1].text
        assert snap_quality_from_api == quality
        snap_interval_from_api = ET.fromstring(snap_request.content)[0][2].text
        assert snap_interval_from_api == "123"
