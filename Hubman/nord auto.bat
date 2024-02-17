@echo off
C:
cd "C:\Program Files\NordVPN\"

:x

nordvpn -c -g "United States"
timeout 300

nordvpn -c -g "Canada"
timeout 300

nordvpn -c -g "United Kingdom"
timeout 300

goto x