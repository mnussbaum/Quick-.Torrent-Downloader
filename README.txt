A command line tool that begins the torrenting process by searching for a
given term and result name, downloading the .torrent file and opening it in
your default BitTorrent client.

Invoke the program with 'qtd' and the following flags:
    -s  search term
    -r  name of result to download

Downloads from:
    thepiratebay.org
    www.btmon.com
    btjunkie.org
    fenopy.com
    www.torrenthound.com

Additional trackers can easily be added by subclassing BaseTracker and
following the model of the other trackers.

Search results are from torrentz.eu
