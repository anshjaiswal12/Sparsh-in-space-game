#importing libraries for qiskit to work
from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

#message ---------------------------------------------------
#if you reading this message then it means you got my source code, I want to share this source code becuase 
#I want to share with you how to apply shor's algorithm in qiskit library
#qiskit is a great tool that will help you to apply quantum
#algoirthm using python language and their qiskit module/library
#this this has advantages like you can create qunatum computer at your home just like me
#I am sharing this source code with Yuvraj Singh of coder's eduyear 
#I want to thank Yuvraj Singh for letting me share this code with you
#what is shor's algorithm-----------------------------------
#Shor's algorithm is a great replacement of RSA algorithm that
#makes impossible to hack a regular computer with a normal computer 
# RSA comes from the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman who developed alorithm
#Shor's algorithm is quantum computer algorithm developed american mathematician Peter Shor
#this can be greatly applied in cyber security that will make almost impossible to them hack
#for more information I will recommend you to read the wikipieda articles on Shor's algorithm and RSA algorithm
# how to contact me ------------------------------------- 
#if you have any question you can email me on anshjaiswal.quark@gmail.com
#or can text me on instagram if I have not changed my username or deleted my account on the_alike
#----This is Ansh Jaiswal


backend= Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)
values=Shor(N=15,a=2,quantum_instance=quantum_instance)

Shor.run(values)

def quant_func1(a,power):
    U = QuantumCircuit(4)
    for iteration in range(power):
        U.swap(2,3)
        U.swap(1,2)
        for q in range(4):
            U.x(q)
    U=U.to_gate()
    U.name="%i^%i mod 15" %(a,power)
    c_U= U.control()
    return c_U

n_count = 10
a= 5

def quant_dagger(n):
    """n-qubit QFTdagger the first n qubits in circ"""
    qc = QuantumCircuit(n)
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cu1(-np.pi/float(2**(j-m)), m, j)
        qc.h(j)
    qc.name = "QFT dagger"
    return qc


qc = QuantumCircuit(n_count + 4, n_count)
for q in range(n_count):
    qc.h(q)
qc.x(3+n_count)
for q in range(n_count):
    qc.append(quant_func1(a, 2**q), [q]+[i+n_count for i in range(4)])
qc.append(quant_dagger(n_count), range(n_count))
qc.measure(range(n_count), range(n_count))
qc.draw('text') #for drawging the quantum circuits


backend = Aer.get_backend('qasm_simulator')
results = execute(qc, backend, shots=100).result()
counts= results.get_counts()
plot_histogram(counts)# this code will help to print the histogram
