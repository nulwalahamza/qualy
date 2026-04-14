import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt
import os

# ---- SETUP ----
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')
plotting.setup_mpl()

# ---- LOAD SESSION ----
session = fastf1.get_session(2026, 'China', 'Q')
session.load()

# ---- TELEMETRY COMPARISON ----
laps_ham = session.laps.pick_driver('HAM').pick_fastest()
laps_lec = session.laps.pick_driver('LEC').pick_fastest()

tel_ham = laps_ham.get_car_data().add_distance()
tel_lec = laps_lec.get_car_data().add_distance()

fig, ax = plt.subplots(3, 1, figsize=(12, 10))

ax[0].plot(tel_ham['Distance'], tel_ham['Speed'], label='Hamilton', color='blue')
ax[0].plot(tel_lec['Distance'], tel_lec['Speed'], label='Leclerc', color='red')
ax[0].set_ylabel('Speed (km/h)')
ax[0].legend()

ax[1].plot(tel_ham['Distance'], tel_ham['Throttle'], color='blue')
ax[1].plot(tel_lec['Distance'], tel_lec['Throttle'], color='red')
ax[1].set_ylabel('Throttle (%)')

ax[2].plot(tel_ham['Distance'], tel_ham['Brake'], color='blue')
ax[2].plot(tel_lec['Distance'], tel_lec['Brake'], color='red')
ax[2].set_ylabel('Brake')
ax[2].set_xlabel('Distance (m)')

plt.suptitle('2026 China Q - HAM vs LEC Telemetry')
plt.tight_layout()
plt.show()