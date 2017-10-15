""" Sample controller """
from kervi.controller import Controller
from kervi.values import DynamicBoolean

class SystemController(Controller):
    def __init__(self):
        Controller.__init__(self, "systemController", "System")
        self.type = "system_power"

        self.power_button = self.inputs.add("power", "Power", DynamicBoolean)
        self.power_button.link_to_dashboard(
            "system",
            "power",
            #inline=True,
            button_text=None,
            button_icon="power-off",
            type="switch"
        )

        self.reboot_button = self.inputs.add("reboot", "Reboot", DynamicBoolean)
        self.reboot_button.link_to_dashboard(
            "system",
            "power",
            #inline=True,
            button_text=None,
            button_icon="repeat",
            type="button",
            #button_width="5rem",
            #button_height="6rem"
        )

        self.reboot_button.link_to_dashboard(
            "*",
            "header_right",
            #inline=True,
            label=None,
            button_text="Reboot",
            button_icon="repeat",
            type="button"
        )

    def input_changed(self, changed_input):
        if changed_input == self.power_button:
            print("power", changed_input.value)
        if changed_input == self.reboot_button:
            print("reboot", changed_input.value)

SYSTEM_CONTROLLER = SystemController()
