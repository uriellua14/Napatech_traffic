import libtmux
import time

server = libtmux.Server()
session = server.find_where({"session_name": "session_test"})

session = server.new_session(session_name="session_test", kill_session=True, attach=False)
window = session.new_window(attach=True, window_name="session_test")
pane1 = window.attached_pane
pane2 = window.split_window(vertical=False)

pane3 = window.split_window(vertical=True)
pane4 = window.split_window(vertical=True)
pane5 = window.split_window(vertical=True)
pane6 = window.split_window(vertical=True)



pane1.send_keys('/opt/napatech3/bin/ntload.sh')
time.sleep(1)
pane1.send_keys('/opt/napatech3/bin/ntservice')
time.sleep(15)
pane2.send_keys('/opt/napatech3/bin/monitoring')
time.sleep(1)
pane3.send_keys('/opt/napatech3/bin/ntpcap_capture -i napa1')
time.sleep(1)
pane5.send_keys('/opt/napatech3/bin/ntpcap_capture -i napa0')
time.sleep(1)
pane4.send_keys('/opt/napatech3/bin/pktgen -p 0 -n 0 -s 64:10000 -r 0 -t empty')
time.sleep(1)
pane6.send_keys('/opt/napatech3/bin/pktgen -p 1 -n 0 -s 64:10000 -r 0 -t empty')

window.select_layout('tiled')

server.attach_session(target_session="session_test")
