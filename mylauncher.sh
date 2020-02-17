#! /bin/sh

[ -e "$SNAP_USER_DATA/config.toml" ] || touch $SNAP_USER_DATA/config.toml

[ -e "$SNAP_USER_DATA/energy-data.json" ] || echo "{}" >> $SNAP_USER_DATA/energy-data.json

[ -e "$SNAP_USER_DATA/power-data.json" ] || echo "{}" >> $SNAP_USER_DATA/power-data.json

exec "$@"