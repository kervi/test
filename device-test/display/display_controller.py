if __name__ == '__main__':
    from kervi.application import Application
    APP = Application()


    from kervi.sensors.sensor import Sensor
    from kervi.devices.platforms.common.sensors.cpu_use import CPULoadSensorDeviceDriver
    from kervi.devices.platforms.common.sensors.cpu_temp import CPUTempSensorDeviceDriver
    #build in sensor that measures cpu use
    SENSOR_CPU_LOAD = Sensor("CPULoadSensor", "CPU", CPULoadSensorDeviceDriver())
    #link to sys area top right
    SENSOR_CPU_LOAD.link_to_dashboard("*", "sys-header")
    #link to a panel, show value in panel header and chart in panel body
    SENSOR_CPU_LOAD.link_to_dashboard(type="value", size=2, link_to_header=True)
    SENSOR_CPU_LOAD.link_to_dashboard(type="chart", size=2)

    #build in sensor that measures cpu temperature
    SENSOR_CPU_TEMP = Sensor("CPUTempSensor", "", CPUTempSensorDeviceDriver())
    #link to sys area top right
    SENSOR_CPU_TEMP.link_to_dashboard("*", "sys-header")


    from kervi.devices.displays.dummy_display_driver import DummyCharDisplayDriver, DummyBitmapDisplayDriver
    from kervi.displays import Display, DisplayPage

    page1 = DisplayPage("p1")
    page1.template = "CPU: {CPULoadSensor}%\nLine 2"
    page1.link_value(SENSOR_CPU_LOAD)

    page2 = DisplayPage("p2")
    page2.template = "temp: {CPUTempSensor}%"
    page2.link_value(SENSOR_CPU_TEMP)


    display = Display("d1", "Display", DummyCharDisplayDriver())
    display.text.link_to_dashboard()
    display.add_page(page1)

    display1 = Display("d2", "Display 2", DummyBitmapDisplayDriver(128,32))
    display1.line_height = 16
    display1.text.link_to_dashboard()
    display1.add_page(page1)
    display1.add_page(page2)
    display1.activate_page_scroll()


    APP.run()