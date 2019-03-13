#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:09:52 2019

@author: shanedaly
"""

jobs = {1:(67,65),
            2:(75,65),
            3:(15,13),
            4:(7,1),
            5:(11,7),
            6:(59,52),
            7:(64,57),
            8:(17,11),
            9:(35,33),
            10:(57,51),
            11:(55,49),
            12:(17,11),
            13:(57,50),
            14:(48,40),
            15:(75,73),
            16:(91,86),
            17:(44,43),
            18:(48,46),
            19:(29,23),
            20:(72,65)}


def firstCome(jobs):
    print("First Come First Served:")
    print("Job\tTime\tDue\tFin\tTardy")
    job_completion = 0
    tardy = []
    completion_times = []
    for key in jobs: 
        tardiness = 0
        job_time = jobs[key][0]
        due_time = jobs[key][1]
        job_completion += job_time
        completion_times.append(job_completion)
        
        if job_completion > due_time:
            tardiness = job_time - due_time
            tardy.append(tardiness)
    
        print("{}\t{}\t{}\t{}\t{}".format(key, job_time, due_time, job_completion, tardiness))
        
    return tardy, completion_times

def shortestProcessing(jobs):
    min_value = min(jobs, key=lambda k: jobs[k][0])
    job_completion = 0
    tardy = []
    completion_times = []

    tardiness = 0
    job_time = jobs[min_value][0]
    due_time = jobs[min_value][1]
    job_completion += job_time
    completion_times.append(job_completion)
    
    if job_completion > due_time:
        tardiness = job_time - due_time
        tardy.append(tardiness)

    print("{}\t{}\t{}\t{}\t{}".format(min_value, job_time, due_time, job_completion, tardiness))
    del jobs[min_value]
    return tardiness, job_completion
    
def earliestDue(jobs):
    min_value = min(jobs, key=lambda k: jobs[k][1])
    job_completion = 0
    tardy = []
    completion_times = []

    tardiness = 0
    job_time = jobs[min_value][0]
    due_time = jobs[min_value][1]
    job_completion += job_time
    completion_times.append(job_completion)
    
    if job_completion > due_time:
        tardiness = job_time - due_time
        tardy.append(tardiness)

    print("{}\t{}\t{}\t{}\t{}".format(min_value, job_time, due_time, job_completion, tardiness))
    del jobs[min_value]
    return tardiness, job_completion

def comparisons(FC1, FC2, SP1, SP2, ED1, ED2):
    print("\nFCFC:")
    print("Tardiness:")
    print("Average", sum(FC1) / len(FC1)) # average
    print("Max", max(FC1))
    print("Completion:")
    print("Average ", sum(FC2) / len(FC2)) # average
    print("Max: ", max(FC2))
    
    print("\nSPT:")
    print("Tardiness:")
    print("Average", sum(SP1) / len(SP1)) # average
    print("Max", max(SP1))
    print("Completion:")
    print("Average ", sum(SP2) / len(SP2)) # average
    print("Max: ", max(SP2))
    
    print("\nEDD:")
    print("Tardiness:")
    print("Average", sum(ED1) / len(ED1)) # average
    print("Max", max(ED1))
    print("Completion:")
    print("Average ", sum(ED2) / len(ED2)) # average
    print("Max: ", max(ED2))
    
    pass


def main(jobs):
    # -------------- FCFS -------------------
    FC_tardy, FC_complete = firstCome(jobs)
    
     # -------------- SPT ------------------- 
    SP_tardy = []
    SP_complete = []
    print("\nShortest Processing Time:")
    print("Job\tTime\tDue\tFin\tTardy")
    bJob = jobs.copy()
    for x in range(0,len(jobs)):
        tardy, complete = shortestProcessing(bJob)
        SP_tardy.append(tardy)
        SP_complete.append(complete)
    
     # -------------- EDD -------------------
    ED_tardy = []
    ED_complete = []
    print("\nEarliest Due Date:")
    print("Job\tTime\tDue\tFin\tTardy")
    cJob = jobs.copy()
    for x in range(0,len(jobs)):
        tardy, complete = earliestDue(cJob)
        ED_tardy.append(tardy)
        ED_complete.append(complete)
        
    
    comparisons(FC_tardy, FC_complete, SP_tardy, SP_complete, ED_tardy, ED_complete)
    
main(jobs)