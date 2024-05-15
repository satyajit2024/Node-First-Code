import time
import Adafruit_ADS1x15

def get_current():
    # Initialize ADC
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 2/3  # Set gain to 2/3 (acceptable for 0-5V range)
    # ACS712 parameters
    sensitivity = 0.185  # mV per Amp
    zero_current_voltage = 2500  # mV
    # Read ADC value
    adc_value = adc.read_adc(0, gain=GAIN)
    # Convert ADC value to voltage
    voltage = adc_value / 32767.0 * 4.096  # 4.096V is the full scale range for ADS1115 with GAIN = 2/3
    # Calculate AC current
    ac_current = (voltage - zero_current_voltage) / sensitivity
    ac_current = ac_current/1000
    #print("AC Current: {:.2f} mA".format(ac_current))
    print("AC Current: {:.2f} A".format(ac_current))
    time.sleep(1)
    return ac_current
# Call the function to start measuring AC current
# get_current()