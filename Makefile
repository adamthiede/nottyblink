#!/usr/bin/env bash
ifndef PREFIX
  PREFIX = /usr/
endif
DESTDIR=${PREFIX}

default:
	install

install:
	install -Dm 0755 systemd-ttyblink.sh ${DESTDIR}/bin/systemd-ttyblink.sh
	install -Dm 0644 systemd-nottyblink.service ${DESTDIR}/lib/systemd/system/systemd-nottyblink.service
	install -Dm 0644 cursor_blink.conf /etc/tmpfiles.d/cursor_blink.conf

