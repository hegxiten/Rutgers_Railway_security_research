import networkx as nx
import matplotlib.pyplot as plt
import simpy
import numpy as np
import time
import collections
from collections import defaultdict
import heapq
# import pandas as pd

def networkX_write():
    '''
    ## generate a network graph in simple grids and save it into 'gpickle' file.
    '''
    number = 120
    G = nx.MultiGraph()

    ## define the position (coordinates on the graph) of all nodes represented on the graph, it should be a dictionary
    pos = {}

    for i in range(1, number+1):
        col = ((i-1) % 20) + 1 if ((i-1) // 20) % 2 == 0 else 20 - (i-1) % 20
        row = i // 20 if i % 20 != 0 else i // 20 - 1
        pos[i] = [col, row]

    nodes = []
    edges = []
    for i in range(1, number+1):
        nodes.append(i)
        if i < number:
            edges.append((i, i+1))
    
    siding = [15, 35, 55, 75]    
    for c in siding:
        nodes.append(c)
        G.add_path((c - 1, c + 1))
    
    ## define siding locations in the grids and add corresponding links to the graph generated 
     
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.set_node_attributes(G, pos, 'pos')
    nx.write_gpickle(G, "a.gpickle")
    

def networkX_read():
    '''
    read "gpickle" file (basemap + data features 'pos')
    dynamically display the node: change the color of a node from red to green every second.
    data are stored in gpickle file together with the basemap
    '''

    G = nx.read_gpickle("a.gpickle")
    pos = nx.get_node_attributes(G, 'pos')

    ncolor = []
    for i in range(len(pos)):
        ncolor.append('r')

    #plt.ion()
    for index in range(len(ncolor)):
        plt.cla()
        ncolor[index] = 'g'
        if index > 0:
            ncolor[index-1] = 'r'
        nx.draw_networkx_nodes(G, pos, node_color=ncolor)
        nx.draw_networkx_labels(G, pos, font_size=16)
        nx.draw_networkx_edges(G, pos)

        # plt.pause(0.01)
    #plt.ioff()
    plt.show()
    #plt.pause(0.2)
    plt.cla()
    plt.close('all')
    return

'''
# code in main class
import networkX_w_r
networkX_w_r.networkX_write()
networkX_w_r.networkX_read()
'''

## Update starts here 20190313
class RailNetwork:
    '''
    Class RailNetwork serves as the base map where the trains are operating on.
    '''
    def __init__(self, G = nx.Graph()):
        self.G = G
    
    @property    
    def single_track_init(self, block_length = [0.5]*100):
        corridor_path = range(length(block_length))
        self.G.add_path(corridor_path)
        for i in range(length(block_length)+1):
                    self.G[i-1][i]['dist'] = block_length[i-1]
                    self.G[i-1][i]['attr'] = None    
        
    def siding_init(self, siding = [10, 20, 30, 40, 50, 60, 70, 80, 90]):
            for i in siding:
                if isinstance(i, int):
                    self.G[i-1][i]['attr'] = 'siding'
                else:
                    self.G[i[0]][i[1]]['attr'] = 'siding'

class Simulator:
    def __init__(self, strt_t, stop_t, speed, time_log):
        ## define the feature parameters of a train object
        self.refresh = 2
        self.all_schedule = {}
        self.strt_t_ticks = time.mktime(time.strptime(strt_t, "%Y-%m-%d %H:%M:%S"))
        self.stop_t_ticks = time.mktime(time.strptime(stop_t, "%Y-%m-%d %H:%M:%S"))
    
    def scheduling(self):
    
    def attack_DoS(self, DoS_strt_t, DoS_stop_t, DoS_block):

class Train_generator:
    def __init__(self):
        
        
            
            

class single_train:
    '''
    many trains are generated by one control point,
    here I want to output the schedule of each train.
    '''

    def __init__(self, strt_t, stop_t, is_DoS, DoS_strt_t, DoS_stop_t, DoS_block, siding, block):
        ## strt_t and stop_t are string for time, the format is '2018-01-01 00:00:00'
        # the position of siding. ps: siding is a list of integer
        self.siding = siding
        # self.block is the length of each block
        self.block = block
        self.refresh = 2
        self.all_schedule = {}
        self.T = time
        # turn strt_t and stop_t into the number ticks from 1970 to now.
        self.strt_t_ticks = time.mktime(time.strptime(strt_t, "%Y-%m-%d %H:%M:%S"))
        self.stop_t_ticks = time.mktime(time.strptime(stop_t, "%Y-%m-%d %H:%M:%S"))
        ## dummy information of DoS (if DoS is in-place or not)
        self.is_DoS = is_DoS    
        self.DoS_strt_t_ticks = time.mktime(time.strptime(DoS_strt_t, "%Y-%m-%d %H:%M:%S"))
        self.DoS_stop_t_ticks = time.mktime(time.strptime(DoS_stop_t, "%Y-%m-%d %H:%M:%S"))
        self.DoS_block = DoS_block
        # self.number is the number of refresh.
        self.number = 0
        # we get a new self.one_schedule after each refresh
        self.one_schedule = {}
        self.one_detail = {}
        self.speed = {}
        # parameter of headway
        self.headway_exp = 30
        self.headway_dev = 5
        # distance of each train
        ## distance means x-axis coordinates
        self.distance = collections.defaultdict(int)
        self.cur_block = collections.defaultdict(lambda: 1)
        self.sum_block_dis = collections.defaultdict(lambda: self.block[0])
        ## trick to avoid KeyError when the key is not existed. 
        ## distance is the dictionary for trains with the Key Value as train indices (integers)

        self.time = {1: self.strt_t_ticks}
        ## time is the dictionary for trains with with the Key Value as train indices (integers) 
        self.G = nx.read_gpickle("a.gpickle")
        self.pos = nx.get_node_attributes(self.G, 'pos')
        self.labels = {}
        self.pos_labels = {}
        # define which siding that late/fast train surpass previous/slow trains
        self.isPass = defaultdict(lambda: float('inf'))
        # in order to solve problem: the number of trains is not the rank of trains. I use dict rank[n]
        self.rank = collections.defaultdict(int)
        self.weight = collections.defaultdict(int)


        # use simpy library to define the process of train system
        env = simpy.Environment()
        env.process(self.train(env))
        duration = self.stop_t_ticks - self.strt_t_ticks
        env.run(until=duration)

    def train(self, env):
        def get_sum_and_cur_block(number):
            # if (distance > block_begin), block go further; if (distance < block_end), block go close.
            while not (self.sum_block_dis[number] - self.block[self.cur_block[number]]) < self.distance[number] <= (self.sum_block_dis[number]):
                if self.distance[number] >= self.sum_block_dis[number]:
                    self.sum_block_dis[number] += self.block[self.cur_block[number]]
                    self.cur_block[number] += 1

                elif self.distance[number] <= (self.sum_block_dis[number] - self.block[self.cur_block[number]]):
                    self.sum_block_dis[number] -= self.block[self.cur_block[number]]
                    self.cur_block[number] -= 1

        # ranking is used for find which train will be surpass next
        rank = {}
        for i in range(1000):
            rank[i] = i

        # n is used for create many "one_detail", otherwise all "one_schedule" will be the same
        n = 1
        temp = 0
        np.random.seed()
        self.speed[1] = np.random.normal(3, 0.5)
        self.weight[1] = np.random.randint(1, 4)
        # self.distance[1] = 0
        headway = np.random.normal(self.headway_exp, self.headway_dev)
        while True:
            # initialize label and color
            plt.clf()
            self.labels.clear()
            self.pos_labels.clear()
            self.ncolor = []
            # default empty block to 'green'
            for i in range(len(self.pos)):
                self.ncolor.append('g')
            # default block which have siding to 'black'
            for i in self.siding:
                self.ncolor[i] = 'black'

            # because headway > refresh time, so we need to decide if there is a new train.
            if temp < headway:
                temp += self.refresh
            else:
                ## generate a new train
                temp = headway % self.refresh
                self.number += 1
                self.speed[self.number] = np.random.normal(3, 0.5)  # miles per second
                self.time[self.number] = self.strt_t_ticks + temp * 60
                self.weight[self.number] = np.random.randint(1, 4)

                # update the [distance] and [number of block] of the new generated train
                self.distance[self.number] += self.speed[self.number] * temp
                get_sum_and_cur_block(self.number)

                # headway = np.random.normal(10, 3)
                headway = np.random.normal(self.headway_exp, self.headway_dev)

            self.all_schedule[self.number] = {}

            for x in xrange(1, self.number + 1):
                i = rank[x]
                self.one_detail = {}
                self.time[i] += self.refresh * 60

                if self.is_DoS is True:
                    # self.time[n] is (the time for a train to move) + (strt_t time), so self.train[1] is current time.
                    if self.DoS_strt_t_ticks < self.time[1] < self.DoS_stop_t_ticks:
                        if self.cur_block[i] != self.DoS_block:
                            self.distance[i] += self.speed[i] * self.refresh
                            get_sum_and_cur_block(i)
                    else:
                        self.distance[i] += self.speed[i] * self.refresh
                        get_sum_and_cur_block(i)

                elif self.is_DoS is False:
                    self.distance[i] += self.speed[i] * self.refresh
                    get_sum_and_cur_block(i)

                '''
                Traverse the rank of all train, if low rank catch up high rank, it should follow instead of surpass. 
                Unless there is a siding.
                '''
                if x > 1:
                    # The block position of prev train and current train
                    '''
                    Overtake Policy:
                    
                    # when block small enough and speed large enough, there would be a bug
                    '''
                    if self.cur_block[rank[x - 1]] <= self.cur_block[rank[x]] + 1:
                        for j in self.siding:
                            if self.cur_block[rank[x - 1]] == j:
                                if self.speed[rank[x-1]] < self.speed[rank[x]]:
                                    rank[x], rank[x - 1] = rank[x - 1], rank[x]
                                    self.distance[rank[x]] -= self.speed[rank[x]] * self.refresh
                                    get_sum_and_cur_block(i)
                                break

                            elif j == self.siding[-1]:
                                self.distance[rank[x]] = self.sum_block_dis[rank[x]] - self.block[self.cur_block[rank[x]]]
                                self.distance[rank[x]] = max(0, self.distance[rank[x]])
                                get_sum_and_cur_block(i)

                k = self.cur_block[i]

                # set the color of train node
                if 0 < k < len(self.pos):
                    self.ncolor[k-1] = 'r'

                if 0 < k < len(self.pos):
                    self.labels[k] = i
                    self.pos_labels[k] = self.pos[k]

                self.one_detail['time'] = round(self.speed[i], 2)
                self.one_detail['speed(mils/min)'] = round(self.speed[i], 2)
                self.one_detail['distance(miles)'] = round(self.distance[i], 2)
                self.one_detail['headway(mins)'] = round(headway, 2)
                self.one_detail['weight(1-3)'] = self.weight[i]
                time_standard = self.T.strftime("%Y-%m-%d %H:%M:%S", self.T.localtime(self.time[1]))
                self.one_schedule[time_standard] = self.one_detail
                self.all_schedule[i][time_standard] = self.one_schedule[time_standard]
                n += 1

            # draw the train map
            # nx.draw_networkx_nodes(self.G, self.pos, node_color=self.ncolor, node_size=200)
            # nx.draw_networkx_labels(self.G, self.pos_labels, self.labels, font_size=10)
            # nx.draw_networkx_edges(self.G, self.pos)
            
            # networkX pause 0.01 seconds
            # plt.pause(0.05)
            yield env.timeout(self.refresh*60)

    def string_diagram(self):
        # draw the train working diagram
        '''begin comment__train stringline diagram'''
        x = []; y = []
        for i in self.all_schedule:
            x.append([])
            y.append([])

            for j in self.all_schedule[i]:
                x[i-1].append((time.mktime(time.strptime(j, "%Y-%m-%d %H:%M:%S")) - self.strt_t_ticks) / 3600)
                y[i-1].append(self.all_schedule[i][j]['distance(miles)'])

            x[i-1].sort()
            y[i-1].sort()

        plt.title('Result Analysis')
        for n in range(len(x)-1):
            if n % 4 == 0:
                plt.plot(x[n], y[n], color='green')
            if n % 4 == 1:
                plt.plot(x[n], y[n], color='blue')
            if n % 4 == 2:
                plt.plot(x[n], y[n], color='red')
            if n % 4 == 3:
                plt.plot(x[n], y[n], color='black')

        plt.legend()
        plt.xlabel('time /hours')
        plt.ylabel('distance /miles')
        plt.show()
        '''end comment__train stringline diagram'''

        # print self.all_schedule
        return self.all_schedule

'''
# single_train
from single_train import single_train

import networkX_w_r
networkX_w_r.networkX_write()

a = single_train('2018-01-01 00:00:00', '2018-01-03 00:00:00', [200, 400, 600, 800])
print a.string_diagram()
'''

class multi_dirc:
    '''
    many trains are generated by two control points,
    here I want to output the schedule of each train.
    '''

    def __init__(self, strt_t, stop_t, dis_miles, buffer_list):
        # define parameters
        self.buffer = 3
        self.all_schedule_A = {}
        self.dis = dis_miles
        self.buffer_list = buffer_list
        self.T = time
        self.strt_t_ticks = time.mktime(time.strptime(strt_t, "%Y-%m-%d %H:%M:%S"))
        self.stop_t_ticks = time.mktime(time.strptime(stop_t, "%Y-%m-%d %H:%M:%S"))
        self.number = 1
        self.one_schedule_A = {}
        self.one_schedule_B = {}
        self.one_detail_A = {}
        self.one_detail_B = {}
        self.speed_A = {}
        self.speed_B = np.random.normal(3, 0.5)
        self.distance_A = {1: 0}
        self.time = {1: self.strt_t_ticks}
        env = simpy.Environment()
        env.process(self.train(env))
        duration = self.stop_t_ticks - self.strt_t_ticks
        env.run(until=duration)

    def train(self, env):
        # n is used for create many "one_detail_A", otherwise all "one_schedule_A" will be the same
        n = 0
        index_A = 0
        index_B = len(self.buffer_list)

        while True:
            np.random.seed()
            self.speed_A[self.number] = np.random.normal(3, 0.5) # miles per minute
            headway = np.random.normal(20, 5)
            self.all_schedule_A[self.number] = {}
            self.time[self.number] = self.strt_t_ticks
            self.distance_A[self.number] = 0

            for i in xrange(1, self.number+1):
                self.one_detail_A[n] = {}
                self.time[i] += headway * 60
                self.distance_A[i] += self.speed_A[i] * headway
                distance_B = (self.speed_B * (self.time[1] - self.strt_t_ticks)) / 60
                if i > 1:
                    if self.distance_A[i] > self.distance_A[i-1] - self.speed_A[i-1] * self.buffer:
                        self.distance_A[i] = self.distance_A[i-1] - self.speed_A[i-1] * self.buffer
                dirc = 'A'
                self.one_detail_A[n]['dirc'] = dirc
                self.one_detail_A[n]['speed_A(mils/min)'] = round(self.speed_A[i], 2)
                self.one_detail_A[n]['distance_A(miles)'] = round(self.distance_A[i], 2)
                self.one_detail_A[n]['headway(mins)'] = round(headway, 2)

                # get A and B pass through which buffer
                for x in range(len(self.buffer_list)):
                    if self.buffer_list[x] < self.distance_A[i]:
                        index_A = x + 1
                for x in range(len(self.buffer_list), 0):
                    if self.dis - self.buffer_list[x] < distance_B:
                        index_B = x + 1
                # A and B
                if index_B - index_A == 2:
                    time_arrive_buffer_A = self.buffer_list[index_A-1] / self.speed_A[i]
                    time_arrive_buffer_B = (self.dis - self.buffer_list[index_B-1]) / self.speed_B
                    if time_arrive_buffer_A < time_arrive_buffer_B:
                        self.distance_A[i] -= (time_arrive_buffer_B - time_arrive_buffer_A) * self.speed_A[i]
                    else:
                        distance_B -= (time_arrive_buffer_A - time_arrive_buffer_B) * self.speed_B

                self.one_detail_A[n]['buffer_index'] = index_A
                time_standard = self.T.strftime("%Y-%m-%d %H:%M:%S", self.T.localtime(self.time[i]))
                self.one_schedule_A[time_standard] = self.one_detail_A[n]
                self.all_schedule_A[i][time_standard] = self.one_schedule_A[time_standard]
                n += 1
            self.number += 1
            yield env.timeout(headway * 60)

    def string_diagram(self):
        return self.all_schedule_A

'''
# code in main class

from multi_dirc import multi_dirc
a = multi_dirc('2018-01-01 00:00:00', '2018-01-02 00:00:00', 1000, [500, 1000, 1500, 2000, 2500])
print a.string_diagram()
'''


