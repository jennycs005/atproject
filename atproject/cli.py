import libtorrent as lt
import time
import os

filename = raw_input ("Please input torrent file name:")
print 'current directory is ',os.getcwd()
path = raw_input ("please input path of file:")

while (not os.path.exists(path)):
	path = raw_input ("Path does not exists, Please input path of file:")

ses = lt.session()
ses.listen_on(6881, 6891)
e = lt.bdecode(open(path + "/" + filename, 'rb').read())
info = lt.torrent_info(e)

params = { 'save_path': '.', \
        'storage_mode': lt.storage_mode_t.storage_mode_sparse, \
        'ti': info }
h = ses.add_torrent(params)
s = h.status()
while (not s.is_seeding):
        s = h.status()

        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']
        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state])

        time.sleep(1)