import subprocess

conf = "port <port>\n \
cluster-enabled yes\n \
cluster-config-file nodes.conf\n \
cluster-node-timeout 5000\n \
append-only yes\n \
bind 127.0.0.1"

for i in range(7001, 7007):
    subprocess.run(["mkdir " + str(i)])
    subprocess.run(["cd " + str(i)])
    subprocess.run(["mkdir " + str(i)])
    subprocess.run(["echo " + conf + " > redis.conf"])
    subprocess.run(["mkdir " + str(i)])
    subprocess.run(["docker run -v ./" + str(i) + "/redis.conf:/usr/local/etc/redis/redis.conf -d --net=host --name server-" + str(i) + " redis redis-server /usr/local/etc/redis/redis.conf"])




