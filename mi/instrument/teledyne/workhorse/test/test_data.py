
# NOTE, this NEWLINE differs from the driver NEWLINE
# The driver NEWLINE represents what we SEND to the instrument
# This NEWLINE represents what is received FROM the instrument
NEWLINE = '\r\n'

# binary data, represent as a bytearray for convenience
RSN_SAMPLE_RAW_DATA = str(bytearray([
    127, 127, 104,   8,   0,   6,  18,   0,  77,   0, 142,   0, 176,   3,  66,   5, 212,   6,   0,   0,
     50,  40, 200,  65,   0,  53,   4, 100,   1,   0, 128,  12, 192,   2,   1,  64,  17,   0, 208,   7,
      0,   1,   0,   0,   0,   0,   0,   0, 125,  61, 235,  15,  16,  13,   1,   5,  50,   0, 198,   0,
    130,   0,   0,   6, 255,  35, 229,   9,   0,   0, 255,   0,  12,  72,   0,   0,  20, 128,   0,   5,
      0,  13,   3,  15,  21,  33,   2,  46,   0,   0,   0, 243,   5,   0,   0, 101,  20, 207, 237,  47,
    238,  35,   0,   2,   8,   0,   0,   0,   0,   0,   0, 116, 169,  88,  79,  79,   0,   0,   0,   0,
      0,   0,   0,   4, 144,  81, 242, 255, 255,   0,   0,   0,   0,   0,  20,  13,   3,  15,  21,  33,
      2,  46,   0,   1,  19,   0, 244, 255, 179,   0,  77,   0,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,   0, 128,
      0, 128,   0, 128,   0,   2,  77,  89,  87,  93,  15,  13,  21,  10,   7,   4,   8,   9,   7,   4,
     16,   4,   7,   8,  11,   9,   5,   9,  11,   6,   7,   5,  11,   9,   7,  11,   5,   6,   5,   8,
      7,   9,   9,  13,   3,   6,   6,   3,   8,  10,  10,  11,   7,   7,   5,  10,   6,   9,   4,   4,
      2,   6,   6,   7,   5,   6,   5,   2,   3,  10,   4,   4,  12,   7,   7,   7,  13,  12,   7,   5,
      2,  10,  11,   9,   4,   7,   6,   2,   6,  11,  10,  14,   6,  10,   3,   7,   2,   7,   4,   2,
      6,   9,   4,  10,   8,   4,   4,   4,   6,  11,   5,   3,  11,   4,   2,   6,  10,   6,   4,   5,
      2,   7,   5,  10,  12,   5,   7,   7,   7,  14,   5,   6,  13,   6,   7,   9,   4,   2,   4,   8,
      7,   9,   6,   9,   6,  11,   7,   5,   7,  17,   2,   7,   7,   3,   4,   4,   8,  10,   3,   4,
      7,   9,   9,   8,   6,   3,   2,   7,   9,   7,   4,   7,   7,   6,   4,   9,   4,   6,   3,   7,
      6,  10,   4,   4,   3,  13,   6,  13,  14,   9,   5,   6,   7,   4,   3,   4,   4,   8,   2,   9,
      4,  13,   4,   4,   9,   3,   2,   7,   7,  10,   3,   4,   4,   1,   6,   9,   4,  11,  10,  10,
      6,   9,   7,   9,   7,   6,   5,   8,   9,  12,   2,  10,   3,   2,   7,   4,   8,   7,   5,   6,
      9,   9,   6,   6,   6,  10,   4,   6,   5,  12,   6,   2,   5,  12,   4,   8,   4,   7,   3,   9,
      9,   8,   6,   6,   4,   6,   5,   2,   4,  11,   4,  11,  11,  14,   3,   5,   9,  12,   5,   3,
      2,  11,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   3,  97,  93, 113,  99,  47,  47,  56,  51,  41,  42,  48,  46,
     40,  42,  48,  46,  40,  41,  48,  46,  40,  41,  47,  46,  41,  41,  47,  46,  40,  41,  47,  46,
     40,  42,  47,  46,  40,  42,  47,  46,  40,  41,  46,  45,  40,  41,  48,  46,  40,  41,  48,  46,
     40,  42,  47,  46,  40,  42,  48,  46,  40,  42,  48,  46,  40,  42,  47,  46,  40,  41,  47,  46,
     40,  41,  47,  46,  39,  41,  47,  46,  40,  41,  47,  46,  40,  42,  47,  45,  40,  41,  47,  46,
     40,  42,  47,  45,  41,  42,  47,  46,  40,  42,  48,  46,  40,  42,  47,  46,  40,  42,  47,  46,
     40,  41,  47,  46,  39,  41,  48,  46,  40,  42,  47,  47,  40,  42,  47,  46,  40,  41,  48,  46,
     40,  41,  48,  46,  41,  41,  47,  46,  39,  41,  47,  45,  40,  41,  48,  46,  40,  41,  47,  46,
     40,  41,  48,  45,  40,  41,  46,  45,  40,  41,  47,  46,  40,  42,  48,  47,  40,  41,  48,  45,
     40,  41,  47,  45,  40,  41,  47,  46,  40,  42,  47,  46,  40,  41,  47,  45,  40,  41,  47,  45,
     40,  41,  47,  46,  40,  41,  48,  46,  40,  41,  47,  46,  40,  41,  46,  46,  40,  41,  47,  46,
     41,  41,  48,  46,  40,  41,  48,  46,  40,  42,  48,  46,  40,  41,  47,  45,  40,  41,  47,  45,
     40,  42,  47,  46,  40,  41,  47,  45,  40,  41,  47,  46,  40,  41,  47,  46,  40,  42,  47,  46,
     40,  41,  46,  45,  41,  41,  47,  46,  40,  41,  46,  45,  40,  41,  47,  46,  40,  42,  47,  46,
     40,  41,  47,  46,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   4, 100, 100, 100, 100,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 125, 242,  47,  32,
]))


RSN_CALIBRATION_RAW_DATA = (
    'ACTIVE FLUXGATE CALIBRATION MATRICES in NVRAM' + NEWLINE +
    '               Calibration date and time: 9/14/2012  09:25:32' + NEWLINE +
    '                             S inverse' + NEWLINE +
    '          \xda                                                  \xbf' + NEWLINE +
    '     Bx   \xb3   3.9218e-01  3.9660e-01 -3.1681e-02  6.4332e-03 \xb3' + NEWLINE +
    '     By   \xb3  -2.4320e-02 -1.0376e-02 -2.2428e-03 -6.0628e-01 \xb3' + NEWLINE +
    '     Bz   \xb3   2.2453e-01 -2.1972e-01 -2.7990e-01 -2.4339e-03 \xb3' + NEWLINE +
    '     Err  \xb3   4.6514e-01 -4.0455e-01  6.9083e-01 -1.4291e-02 \xb3' + NEWLINE +
    '          \xc0                                                  \xd9' + NEWLINE +
    '                             Coil Offset' + NEWLINE +
    '                         \xda                \xbf' + NEWLINE +
    '                         \xb3   3.4233e+04   \xb3' + NEWLINE +
    '                         \xb3   3.4449e+04   \xb3' + NEWLINE +
    '                         \xb3   3.4389e+04   \xb3' + NEWLINE +
    '                         \xb3   3.4698e+04   \xb3' + NEWLINE +
    '                         \xc0                \xd9' + NEWLINE +
    '                             Electrical Null' + NEWLINE +
    '                              \xda       \xbf' + NEWLINE +
    '                              \xb3 34285 \xb3' + NEWLINE +
    '                              \xc0       \xd9' + NEWLINE +
    '                    TILT CALIBRATION MATRICES in NVRAM' + NEWLINE +
    '                Calibration date and time: 9/14/2012  09:14:45' + NEWLINE +
    '              Average Temperature During Calibration was   24.4 \xf8C' + NEWLINE +
    NEWLINE +
    '                   Up                              Down' + NEWLINE +
    NEWLINE +
    '        \xda                           \xbf     \xda                           \xbf' + NEWLINE +
    ' Roll   \xb3   7.4612e-07  -3.1727e-05 \xb3     \xb3  -3.0054e-07   3.2190e-05 \xb3' + NEWLINE +
    ' Pitch  \xb3  -3.1639e-05  -6.3505e-07 \xb3     \xb3  -3.1965e-05  -1.4881e-07 \xb3' + NEWLINE +
    '        \xc0                           \xd9     \xc0                           \xd9' + NEWLINE +
    NEWLINE +
    '        \xda                           \xbf     \xda                           \xbf' + NEWLINE +
    ' Offset \xb3   3.2808e+04   3.2568e+04 \xb3     \xb3   3.2279e+04   3.3047e+04 \xb3' + NEWLINE +
    '        \xc0                           \xd9     \xc0                           \xd9' + NEWLINE +
    NEWLINE +
    '                             \xda       \xbf' + NEWLINE +
    '                      Null   \xb3 33500 \xb3' + NEWLINE +
    '                             \xc0       \xd9' + NEWLINE +
    NEWLINE + NEWLINE + NEWLINE + NEWLINE + NEWLINE + '>')


RSN_PS0_RAW_DATA = (
    "Instrument S/N:  18444" + NEWLINE +
    "       Frequency:  76800 HZ" + NEWLINE +
    "   Configuration:  4 BEAM, JANUS" + NEWLINE +
    "     Match Layer:  10" + NEWLINE +
    "      Beam Angle:  20 DEGREES" + NEWLINE +
    "    Beam Pattern:  CONVEX" + NEWLINE +
    "     Orientation:  UP" + NEWLINE +
    "       Sensor(s):  HEADING  TILT 1  TILT 2  DEPTH  TEMPERATURE  PRESSURE" + NEWLINE +
    "Pressure Sens Coefficients:" + NEWLINE +
    "              c3 = -1.927850E-11" + NEWLINE +
    "              c2 = +1.281892E-06" + NEWLINE +
    "              c1 = +1.375793E+00" + NEWLINE +
    "          Offset = +1.338634E+01" + NEWLINE +
    NEWLINE +
    "Temp Sens Offset:  -0.01 degrees C" + NEWLINE +
    NEWLINE +
    "    CPU Firmware:  50.40 [0]" + NEWLINE +
    "   Boot Code Ver:  Required:  1.16   Actual:  1.16" + NEWLINE +
    "    DEMOD #1 Ver:  ad48, Type:  1f" + NEWLINE +
    "    DEMOD #2 Ver:  ad48, Type:  1f" + NEWLINE +
    "    PWRTIMG  Ver:  85d3, Type:   7" + NEWLINE +
    NEWLINE +
    "Board Serial Number Data:" + NEWLINE +
    "   72  00 00 06 FE BC D8  09 HPA727-3009-00B " + NEWLINE +
    "   81  00 00 06 F5 CD 9E  09 REC727-1004-06A" + NEWLINE +
    "   A5  00 00 06 FF 1C 79  09 HPI727-3007-00A" + NEWLINE +
    "   82  00 00 06 FF 23 E5  09 CPU727-2011-00E" + NEWLINE +
    "   07  00 00 06 F6 05 15  09 TUN727-1005-06A" + NEWLINE +
    "   DB  00 00 06 F5 CB 5D  09 DSP727-2001-06H" + NEWLINE +
    ">")


PT2_RAW_DATA = (
    "Ambient  Temperature =    20.32 Degrees C" + NEWLINE +
    "  Attitude Temperature =    24.65 Degrees C" + NEWLINE +
    "  Internal Moisture    = 8F0Ah" + NEWLINE +
    ">")


PT4_RAW_DATA = (
    "IXMT    =      2.0 Amps rms  [Data=b0h]" + NEWLINE +
    "VXMT    =     60.1 Volts rms [Data=9eh]" + NEWLINE +
    "   Z    =     29.8 Ohms"  + NEWLINE +
    "Transmit Test Results = $0 ... PASS" + NEWLINE +
    ">")

VADCP_SLAVE_PS0_RAW_DATA = (
    "  Instrument S/N:  61247" + NEWLINE +
    "       Frequency:  614400 HZ" + NEWLINE +
    "   Configuration:  4 BEAM, JANUS" + NEWLINE +
    "     Match Layer:  10" + NEWLINE +
    "      Beam Angle:  20 DEGREES" + NEWLINE +
    "    Beam Pattern:  CONVEX" + NEWLINE +
    "     Orientation:  UP" + NEWLINE +
    "       Sensor(s):  HEADING  TILT 1  TILT 2  TEMPERATURE" + NEWLINE +
    "Temp Sens Offset:  0.03 degrees C" + NEWLINE +
    ""
    "    CPU Firmware:  50.40 [0]" + NEWLINE +
    "   Boot Code Ver:  Required:  1.16   Actual:  1.16" + NEWLINE +
    "    DEMOD #1 Ver:  ad48, Type:  1f" + NEWLINE +
    "    DEMOD #2 Ver:  ad48, Type:  1f" + NEWLINE +
    "    PWRTIMG  Ver:  85d3, Type:   6" + NEWLINE +
    "" + NEWLINE +
    "Board Serial Number Data:"
    "   9A  00 00 06 83 8B 94  09 CPU727-2011-00E" + NEWLINE +
    "   B8  00 00 06 B2 B7 C6  09 DSP727-2001-03H" + NEWLINE +
    "   3B  00 00 06 B3 32 FD  09 PIO727-3000-00G" + NEWLINE +
    "   40  00 00 06 B2 D8 57  09 REC727-1000-03E" + NEWLINE +
    ">")