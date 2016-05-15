#!/bin/sh

#
# George Skouroupathis
# tags: pgp, gpg, public key, keyserver
#

# Searched PGP keyservers for given key ID

echo Searching for $1
declare -a arr=("adler.dlrg.de" "belgium.keyserver.net" "ds.carnet.hr" "gnv.us.ks.cryptnet.net" "keys.iif.hu" "keys.pgpi.net" "keyserver.kjsl.com" "keyserver.linux.it" "keyserver.topnet.de" "minf.vub.ac.be" "ms.pgp.cz" "palunko.srce.hr" "pgp.dtype.org" "pgp.es.net" "pgp.es.net" "pgp.escomposlinux.org" "pgp.loxinfo.co.th" "pgp.lsi.upc.es" "pgp.mit.edu" "pgp.ndlug.nd.edu" "pgp.nic.ad.jp" "pgp.rasip.fer.hr" "pgp.rediris.es" "pgp.surfnet.nl" "pgp.uk.demon.net" "pgp.uk.demon.net" "pgp.uni-mainz.de" "pgp.zdv.uni-mainz.de" "pgpkeys.mit.edu" "pgpkeys.tuwien.ac.at" "pks.pgp.cz" "stinkfoot.org" "the.earth.li" "www.keyserver.de" "www.keyserver.net" "www.rediris.es" "wwwkeys.at.pgp.net" "wwwkeys.ch.pgp.net" "wwwkeys.de.pgp.net" "wwwkeys.es.pgp.net" "wwwkeys.eu.pgp.net" "wwwkeys.nl.pgp.net" "wwwkeys.pgp.net" "wwwkeys.uk.pgp.net" "wwwkeys.us.pgp.net")
for server in "${arr[@]}"
do
serverr="hkp://$server"
echo --------------- $serverr ---------------
gpg --keyserver $serverr --recv-keys $1
#46726FC6
done
