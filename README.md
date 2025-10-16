# IAction Home Assistant Add-ons Repository

This repository hosts the IAction Camera AI add-on for Home Assistant. The add-on is published as a standard Supervisor add-on with ingress and MQTT integration.

## Repository structure
- `iaction/` - add-on sources (manifest, Dockerfile, rootfs scripts)
- `repository.yaml` - metadata file consumed by Home Assistant when the repository is added
- `.gitignore`, `.gitattributes` - standard git configuration files

## Usage
1. Add `https://github.com/lfpoulain/iaction-ha-addon` to the Home Assistant add-on repositories list.
2. Open the "IAction Camera AI" entry and install it.
3. Adjust the add-on options to match your setup (AI backend, MQTT, capture mode, etc.).
4. Start the add-on and open the ingress panel to access the web interface.

Home Assistant Supervisor automatically builds the container image using the Dockerfile in `iaction/`.
