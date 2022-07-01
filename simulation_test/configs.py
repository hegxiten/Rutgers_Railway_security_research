import random
from datetime import datetime

from simulation_core.network.System.System import System

sim_init_time = datetime.strptime('2018-01-10 10:00:00', "%Y-%m-%d %H:%M:%S")
sim_term_time = datetime.strptime('2018-01-11 08:25:00', "%Y-%m-%d %H:%M:%S")  # 70 trains
sim_term_time = datetime.strptime('2018-01-10 15:30:00', "%Y-%m-%d %H:%M:%S")
spd_container = [random.uniform(0.01, 0.02) for i in range(20)]
acc_container = [random.uniform(2.78e-05 * 0.85, 2.78e-05 * 1.15) for i in range(20)]
dcc_container = [15 * random.uniform(2.78e-05 * 0.85, 2.78e-05 * 1.15) for i in range(20)]
headway = 1000
refresh_time = 50
dos_period = ['2018-01-10 11:30:00', '2018-01-10 12:30:00']
dos_pos = (10, 15)
dos_pos = (-1, -1)

max_spd_list = \
    [0.01475340986844738, 0.01660291601215959, 0.016046999434042558, 0.010319479729381258, 0.010010810099605458,
     0.019781433217420204, 0.013833919193622167, 0.011189234295572144, 0.010010810099605458, 0.012768540274073863,
     0.010319479729381258, 0.016063432265851614, 0.019781433217420204, 0.013833919193622167, 0.013833919193622167,
     0.013843145856378946]

max_acc_list = \
    [2.424314960644662e-05, 3.0330485297301608e-05, 3.0330485297301608e-05, 2.4021359061956585e-05,
     2.3712254715176332e-05, 3.1723383677253564e-05, 3.0229466241545034e-05, 2.424314960644662e-05,
     2.6761496620604544e-05, 3.19164944838674e-05, 3.183365099077468e-05, 2.424314960644662e-05, 3.183365099077468e-05,
     3.19164944838674e-05, 3.183365099077468e-05, 2.771306657842114e-05]

max_dcc_list = \
    [5.883539286575239e-05, 4.757595753525881e-05, 6.197474902742935e-05, 5.030273339453036e-05, 6.027159769023904e-05,
     6.349674614496509e-05, 5.530601963409951e-05, 6.349674614496509e-05, 5.747398467270075e-05, 5.883539286575239e-05,
     6.356094601002195e-05, 6.197474902742935e-05, 6.022911228379602e-05, 5.89700701109698e-05, 5.305450390539007e-05,
     5.89700701109698e-05]

init_time_list = \
    [1515597350.0, 1515598300.0, 1515599450.0, 1515600650.0, 1515601900.0, 1515603150.0, 1515604350.0, 1515605550.0,
     1515606750.0, 1515608100.0, 1515609300.0, 1515610500.0, 1515611700.0, 1515612900.0, 1515614100.0, 1515615500.0]

if __name__ == "__main__":
    print(len(max_spd_list), len(max_acc_list), len(max_dcc_list))
