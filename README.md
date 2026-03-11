# IRAVS

Intelligent Runtime Allocation and Virtualization Selector.

IRAVS is a research prototype that predicts the optimal execution
environment for a workload between:

• Native OS
• Docker containers
• KVM virtual machines

Instead of brute-force benchmarking, IRAVS analyzes workload behavior
before execution and routes it to the best runtime environment.

## Architecture

Input Script
      ↓
Workload Analyzer
      ↓
Classification Engine
      ↓
Execution Router
      ↓
Environment Executor

## Technologies

Python  
Docker  
KVM / libvirt  
sysbench  
fio
