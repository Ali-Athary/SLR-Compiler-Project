# SLR for: Quantum Computing Progress

## Paper 1
**Title:** Thermodynamic optimization of quantum algorithms: On-the-go erasure of
  qubit registers
**Abstract:** We consider two bottlenecks in quantum computing: limited memory size and
noise caused by heat dissipation. Trying to optimize both, we investigate
"on-the-go erasure" of quantum registers that are no longer needed for a given
algorithm: freeing up auxiliary qubits as they stop being useful would
facilitate the parallelization of computations. We study the minimal
thermodynamic cost of erasure in these scenarios, applying results on the
Landauer erasure of entangled quantum registers. For the class of algorithms
solving the Abelian hidden subgroup problem, we find optimal on-the-go erasure
protocols. We conclude that there is a trade-off: if we have enough partial
information about a problem to build efficient on-the-go erasure, we can use it
to instead simplify the algorithm, so that fewer qubits are needed to run the
computation in the first place. We provide explicit protocols for these two
approaches.
**Overview:** The paper addresses two key challenges in quantum computing: limited memory capacity and noise from heat dissipation. It explores the concept of "on-the-go erasure" of quantum registers, which involves erasing auxiliary qubits that are no longer needed as an algorithm progresses. This approach could enhance parallel processing by freeing up qubit resources in real-time. The authors examine the thermodynamic costs associated with this type of erasure using principles from Landauer's erasure of entangled registers.

For specific algorithms like those solving the Abelian hidden subgroup problem, optimal erasure protocols are derived. A key insight is the trade-off between obtaining partial information to enable efficient erasure and simplifying the algorithm so that fewer qubits are necessary initially. The paper provides explicit protocols for both strategies.

In quantum computation, a typical strategy is to reset qubit registers to |0⟩ after completing an algorithm. However, this might not be suitable when qubits are limited, or multiple algorithms need to run concurrently. Erasing registers on-the-go can optimize memory use and potentially reduce heat dissipation. A brute-force erasure of the auxiliary qubits dissipates significant heat, while Bennett's reversible erasure method avoids heat dissipation but is complex and inefficacious for probabilistic algorithms.

The paper focuses on Noisy Intermediate-Scale Quantum (NISQ) technology, where existing reversible techniques are not yet feasible. The authors suggest that further research into optimizing the thermodynamics of quantum computing could advance its efficiency and practical

---
