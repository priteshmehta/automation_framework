from helpers.element import Page
class BigPage(Page):
    def setup(self):
        self.a_button = self.element_by_selector("a.et_pb_button.et_pb_button_0.et_pb_bg_layout_light")
