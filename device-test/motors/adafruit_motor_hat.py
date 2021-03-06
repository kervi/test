if __name__ == '__main__':
    from kervi.application import Application

    APP = Application()

    #add dashboard and panel
    from kervi.dashboard import Dashboard, DashboardPanel
    DASHBOARD = Dashboard("dashboard", "adafruit motor driver dc test", is_default=True)
    DASHBOARD.add_panel(DashboardPanel("input", columns=2, rows=4, title="input"))

    #define a light controller
    #from kervi.hal import GPIO
    from kervi.controller import Controller
    from kervi.devices.motors.adafruit_i2c_motor_hat import AdafruitMotorHAT

    motor_controller = AdafruitMotorHAT()
    motor_controller.dc_motors[0].speed.link_to_dashboard("dashboard")

    # class TestController(Controller):
    #     def __init__(self):
    #         Controller.__init__(self, "controller.test", "test")
    #         self.type = "test"

    #         self.motor_controller = AdafruitMotorHAT()
    #         self.dc_motor = self.motor_controller.dc_motors[0]
    #         self.dc_motor.steps = 48
    #         self.stepper_motor = self.motor_controller.stepper_motors[1]

    #         #print("motor driver:", self.motor_controller.device_name)

    #         self.speed = UINumberControllerInput("speed", "dc speed", self)
    #         self.speed.link_to_dashboard("dashboard.ctrl", "input")


    #         self.steps = UINumberControllerInput("steps", "Steps", self)
    #         self.steps.link_to_dashboard("dashboard.ctrl", "input")

    #         self.step_interval = UINumberControllerInput("step_interval", "Step interval", self)
    #         self.step_interval.link_to_dashboard("dashboard.ctrl", "input")

    #         self.step_type = UISelectControllerInput("step_type", "step type", self)
    #         self.step_type.add_option("1", "SINGLE")
    #         self.step_type.add_option("2", "DOUBLE")
    #         self.step_type.add_option("3", "Interleave")
    #         self.step_type.add_option("4", "MICROSTEP")

    #         self.step_type.link_to_dashboard("dashboard.ctrl", "input")

    #         self._step = UIButtonControllerInput("step", "Step", self)
    #         self._step.link_to_dashboard("dashboard.ctrl", "input")

    #         self._stepper_dir = UISwitchButtonControllerInput("start_stepper", "Direction", self)
    #         self._stepper_dir.link_to_dashboard("dashboard.ctrl", "input")

    #     def input_changed(self, changed_input):
    #         self.user_log_message("input changed:{0} value:{1}".format(changed_input.input_id, changed_input.value))
    #         if changed_input == self.speed:
    #             self.dc_motor.set_speed(changed_input.value)

    #         if changed_input == self.step_interval:
    #             self.stepper_motor.step_interval = changed_input.value

    #         if changed_input == self.step_type:
    #             print("st", changed_input.value)
    #             self.stepper_motor.step_type = int(changed_input.value)

    #         if changed_input == self._step:
    #             if changed_input.value:
    #                 self.stepper_motor.step(self.steps.value)
    #                 self.stepper_motor.release()

    #     def exit(self):
    #         self.stepper_motor.release()

    # TestController()

    APP.run()