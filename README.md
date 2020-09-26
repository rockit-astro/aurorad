## Aurora Cloud Sensor III daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/aurorad.svg?branch=master)](https://travis-ci.org/warwick-one-metre/aurorad)

Part of the observatory software for the Warwick La Palma telescopes.

`aurorad` wraps a Eurotech Aurora Cloud Sensor III attached via a USB-RS232 adaptor and
makes the latest measurement available for other services via Pyro.

`aurora` is a commandline utility that reports the latest data from the SuperWASP unit.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

The `aurorad` service will be automatically started when the USB-Serial converter with serial number `FT4O44R9` is plugged in to the machine.
If this ever changes then the udev rule in `10-superwasp-aurora.rules` should be updated to match.

If the `observatory-aurora-server` package is (re-)installed after the device is attached then it may be manually started using
```
sudo systemctl start aurorad
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9031/tcp --permanent
sudo firewall-cmd --reload
```
