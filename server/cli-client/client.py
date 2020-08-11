import imp
import os
import multiprocessing
import requests
import json

# Init global vars
current_dir_path = os.path.dirname(os.path.realpath(__file__))
utils_libs_dir_path = current_dir_path+"/../../utils/"

# Init external libs/modules
maplocalnetwork = imp.load_source('maplocalnetwork', utils_libs_dir_path+"maplocalnetwork.py")

class Client:
    def __init__(self):
        self.local_maplocalnetwork = maplocalnetwork.MapLocalNetwork()
        self.local_ips = self.local_maplocalnetwork.map_network()
    def get_local_ips(self):
        return self.local_ips
    def get_all_info_by_one_machine(self, job_q, results_q):
        while True:
            ip = job_q.get()
            # print(ip)
            if ip is None:
                break
            try:
                response = requests.get("http://{}:55802/allinfo".format(ip))
                allinfo = response.content.decode('utf-8')
                allinfo = {ip: json.loads(allinfo)}
                # allinfo = json.dumps(allinfo)
                results_q.put(allinfo)
                pass
            except:
                pass
    def get_all_info_from_all_machines_in_local_network(self):
        allinfo_list = list()

        # prepare the jobs queue
        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()

        pool_size=len(self.local_ips)+1
        # pool_size=255
        pool = [multiprocessing.Process(target=self.get_all_info_by_one_machine, args=(jobs, results)) for i in range(pool_size)]

        for p in pool:
            p.start()
        # cue hte ping processes
        jobs.put('192.168.21.89') # Необходимо также проверить собственный адрес
        for ip in self.local_ips:
            jobs.put(ip)
        
        for p in pool:
            jobs.put(None)

        for p in pool:
            p.join()

        # collect he results
        while not results.empty():
            allinfo = results.get()
            allinfo_list.append(allinfo)

        return json.dumps(allinfo_list)

# a = Client()
# b = a.get_all_info_from_all_machines_in_local_network()
# print(b)
