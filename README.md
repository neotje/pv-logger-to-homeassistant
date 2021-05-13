# pv-logger-to-homeassistant

## global installation
```
chmod 777 setup
./setup
python3 -m pip install -e .
```

### add to home assistant config
mqtt discovery not working for now, so you need to add it manually.

configuration.yaml
```yaml
sensor:
 - platform: mqtt
   unique_id: "name of the table with logs"
   name: "inverter name"
   state_topic: "homeassistant/sensor/[table]/state"
   device_class: "energy"
   unit_of_measurement: "watt"
   qos: 0
```

total sensor:
```yaml
 - platform: mqtt
   unique_id: "TOTAL_INVERTERS"
   name: "total power"
   state_topic: "homeassistant/sensor/TOTAL_INVERTERS/state"
   device_class: "energy"
   unit_of_measurement: "watt"
   qos: 0
```

## dev setup
```
chmod 777 setup
./setup
```

run:
```
source venv/bin/activate
hassinverter
```