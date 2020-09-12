
from Network import Network
from Util import create_topology, clear_file, create_network
from time import time
from copy import deepcopy
from PushRelabel import PushRelabel
node_num = 5
edge_num = 10
max_capacity = 10
start = 1
des = 4
clear_file("topology.txt")
create_topology(node_num, edge_num, max_capacity, "topology.txt")
network = Network(node_num)
create_network(network, "topology.txt")

start_time_PR = time()
push_relabel = PushRelabel(start, des, deepcopy(network))
max_flow_pr = push_relabel.get_max_flow()
end_time_PR = time()
run_time_PR = end_time_PR-start_time_PR
# print(run_time_PR)
print("push-relabel(1->4)的最大流："+str(max_flow_pr))