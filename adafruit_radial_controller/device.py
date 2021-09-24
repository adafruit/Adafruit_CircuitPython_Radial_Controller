# SPDX-FileCopyrightText: Copyright (c) 2021 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long
"""
`adafruit_radial_controller.device`
================================================================================

* Author(s): Dan Halbert

The radial controller report descriptor used is described by Microsoft
`here <https://docs.microsoft.com/en-us/windows-hardware/design/component-guidelines/radial-controller-sample-report-descriptors>`_.
"""
# pylint: enable=line-too-long

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Radial_Controller.git"

import usb_hid


def device(report_id):
    """Create a `usb_hid.Device` for a radial controller.

    :param int report_id: The report ID to use for the device.
    """
    return usb_hid.Device(
        # fmt: off
        report_descriptor=bytes((
            0x05, 0x01,       # Usage Page (Generic Desktop)
            0x09, 0x0e,       # Usage (System Multi-Axis Controller)
            0xa1, 0x01,       # Collection (Application)
            0x85, report_id,  #   Report Id (Radial Controller)
            0x05, 0x0d,       #   Usage Page (Digitizers)
            0x09, 0x21,       #   Usage (Puck)
            0xa1, 0x00,       #   Collection (Physical)

            # Button
            0x05, 0x09,       #     Usage Page (Buttons)
            0x09, 0x01,       #     Usage (Button 1)
            0x15, 0x00,       #     Logical Minimum (0)
            0x25, 0x01,       #     Logical Maximum (1)
            0x75, 0x01,       #     Report Size (1)
            0x95, 0x01,       #     Report Count (1)
            0x81, 0x02,       #     Input (Data,Var,Abs)

            # Padding
            # Making the button be one byte instead of one bit does not work,
            # so we include this padding.
            0x75, 0x07,       #     Report Size (7)
            0x95, 0x01,       #     Report Count (1)
            0x81, 0x01,       #     Input (Data,Var,Abs)

            # Rotation
            0x05, 0x01,       #     Usage Page (Generic Desktop)
            0x09, 0x37,       #     Usage (Dial)
            0x15, 0x81,       #     Logical Minimum (-127)
            0x25, 0x7F,       #     Logical Maximum (127)
            0x75, 0x08,       #     Report Size (8)
            0x95, 0x01,       #     Report Count (1)
            0x81, 0x06,       #     Input (Data,Var,Rel)

            0xc0,             #   End Collection
            0xc0,             # End Collection
            )),
        # fmt: on
        usage_page=0x01,
        usage=0x0E,
        report_ids=(report_id,),
        in_report_lengths=(2,),
        out_report_lengths=(0,),
    )
