#!/usr/bin/env python3

import numpy as np

if __name__ == '__main__':

    # Gups Options
    x = [
        "100",
        "10",
        "1",
        "0.1"
    ]

    y = [
        [390253538,392045610,386752342, 392624086, 392332798],
        [1551980106,1464746446,1411930996,1414402916,1464003992],
        [3122586874,3149646724,3119176704,3125037134,3282740630],
        [17817596162,19300929594,17741638244,18122775078,17781817500],
    ]

    np.save("/root/memsim/bench/gups_on_nvm/hotset/gups_on_nvm", y)