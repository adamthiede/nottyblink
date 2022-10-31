# systemd-nottyblink

[All credit to datagubbe.se](https://www.datagubbe.se/ttyblink/).

This package will add the following:

- the file `/etc/tmpfiles.d/cursor_blink.conf` containing `w /sys/class/graphics/fbcon/cursor_blink - - - - 0`
- a systemd service that runs `echo 0 | sudo tee /sys/class/graphics/fbcon/cursor_blink` on startup

