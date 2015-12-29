import bencode, hashlib, base64, urllib
torrent = open('The.Royals.2015.S02E07.720p.HDTV.x264-KILLERS[eztv].mkv.torrent', 'rb').read()
# torrent = open('B298DD7E3BF7B300FF1F235B90FD5441002FE440.torrent', 'rb').read()
metadata = bencode.bdecode(torrent)
hashcontents = bencode.bencode(metadata['info'])
digest = hashlib.sha1(hashcontents).digest().encode('hex')

params = {'xt': 'urn:btih:%s' % digest,
      'dn': metadata['info']['name'],
      'tr': metadata['announce'],
      'xl': metadata['info']['length']}
paramstr = urllib.urlencode(params)
magneturi = 'magnet:?xt=urn:btih:%s' % digest
print magneturi

# http://bt.box.n0808.com/4f/89/4f993ef559b1586da63f5175771ceb7c7d68eb89.torrent'