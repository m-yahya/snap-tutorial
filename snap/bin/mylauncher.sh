#! /bin/sh

[ -e "$SNAP_USER_DATA/config.toml" ] || touch $SNAP_USER_DATA/config.toml

exec "$@"