#!/bin/bash
elevate=$(command -v doas || command -v sudo)
blinkOn(){
	echo 1 | $elevate tee /sys/class/graphics/fbcon/cursor_blink
}
blinkOff(){
	echo 0 | $elevate tee /sys/class/graphics/fbcon/cursor_blink
}
case $1 in
	enable|on)
		blinkOn
		;;
	disable|off)
		blinkOff
		;;
	*)
		echo "To enable cursor blinking, run `systemd-ttyblink.sh on`"
		echo "To disable cursor blinking, run `systemd-ttyblink.sh off`"
esac

