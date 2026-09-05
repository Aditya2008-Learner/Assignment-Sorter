from typing import List, Dict, Any, Optional

# =======================================================================
# B.Tech CSE (Cyber Security) Full Curriculum — 8 Semesters, 48+ Courses
# =======================================================================

BTECH_CYBER_SECURITY_CURRICULUM: Dict[int, List[Dict[str, Any]]] = {
    # ---------------------------------------------------------------
    # SEMESTER 1 — Foundation & Basic Sciences
    # ---------------------------------------------------------------
    1: [
        {
            "code": "MA101", "name": "Engineering Mathematics I",
            "credits": 4, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Linear Algebra", "topics": ["Matrices & Determinants", "System of Linear Equations", "Rank & Consistency", "Vector Spaces", "Eigenvalues & Eigenvectors", "Diagonalization", "Quadratic Forms", "Cayley-Hamilton Theorem"]},
                {"id": "M2", "title": "Single Variable Calculus", "topics": ["Limits & Continuity", "Differentiability", "Mean Value Theorems", "Taylor & Maclaurin Series", "Indeterminate Forms & L'Hospital's Rule", "Riemann Integration", "Improper Integrals"]},
                {"id": "M3", "title": "Multivariable Calculus", "topics": ["Partial Derivatives", "Chain Rule", "Tangent Planes", "Directional Derivatives", "Maxima & Minima", "Lagrange Multipliers", "Multiple Integrals (Double & Triple)", "Polar/Cylindrical/Spherical Coordinates", "Line & Surface Integrals", "Green's Theorem", "Stokes' Theorem", "Gauss Divergence Theorem"]},
                {"id": "M4", "title": "Sequences, Series & Ordinary Differential Equations", "topics": ["Sequences & Series Convergence", "Power Series", "First Order ODEs (Variable Separable, Homogeneous, Linear, Bernoulli, Exact)", "Higher Order Linear ODEs", "Cauchy-Euler Equations", "Method of Undetermined Coefficients", "Variation of Parameters", "PDEs: Heat, Wave & Laplace Equations"]},
            ],
            "outcomes": ["Apply matrix algebra and vector space concepts to engineering problems", "Compute multivariable integrals using appropriate coordinate systems", "Formulate and solve ODEs governing physical systems"],
            "key_textbooks": ["Erwin Kreyszig — Advanced Engineering Mathematics", "B.S. Grewal — Higher Engineering Mathematics"],
            "assignments": [
                {"title": "Linear Algebra Problem Set", "marks": 50, "difficulty": "Intermediate", "types": ["Problem Solving", "Numerical", "Proof"]},
                {"title": "Calculus & ODE Applications", "marks": 50, "difficulty": "Intermediate", "types": ["Problem Solving", "Numerical"]},
            ]
        },
        {
            "code": "PH101", "name": "Engineering Physics",
            "credits": 3, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Classical Mechanics", "topics": ["Newtonian Mechanics", "Lagrangian & Hamiltonian Formulations", "Central Force Motion", "Rigid Body Dynamics", "Small Oscillations"]},
                {"id": "M2", "title": "Electromagnetic Theory", "topics": ["Electrostatics & Gauss's Law", "Magnetostatics & Ampère's Law", "Faraday's Law", "Maxwell's Equations", "Electromagnetic Wave Propagation"]},
                {"id": "M3", "title": "Optics & Photonics", "topics": ["Interference & Diffraction", "Polarization", "Laser Principles & Applications", "Fiber Optics & Communication"]},
                {"id": "M4", "title": "Quantum Mechanics & Relativity", "topics": ["Wave-Particle Duality", "Schrödinger Equation", "Hydrogen Atom", "Heisenberg Uncertainty Principle", "Special Relativity (Lorentz Transformations)"]},
            ],
            "outcomes": ["Apply Newtonian mechanics and Lagrangian formulation to engineering systems", "Use Maxwell's equations to analyze electromagnetic phenomena", "Apply quantum mechanics principles to modern technology"],
            "key_textbooks": ["Herbert Goldstein — Classical Mechanics", "David J. Griffiths — Introduction to Electrodynamics"],
        },
        {
            "code": "CH101", "name": "Engineering Chemistry",
            "credits": 3, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Water Technology & Treatment", "topics": ["Hardness & Alkalinity", "Water Softening", "Disinfection Methods", "Boiler Feed Water Treatment", "pH & Buffer Solutions"]},
                {"id": "M2", "title": "Electrochemistry & Corrosion", "topics": ["Electrochemical Cells", "Nernst Equation", "Corrosion Mechanisms", "Cathodic Protection", "Protective Coatings"]},
                {"id": "M3", "title": "Polymer Chemistry", "topics": ["Polymerization Mechanisms", "Thermoplastics & Thermosets", "Rubber & Elastomers", "Biodegradable Polymers", "Polymer Applications in IT"]},
                {"id": "M4", "title": "Materials Science", "topics": ["Crystal Structures", "Band Theory of Solids", "Semiconductors", "Nanomaterials", "Superconductors"]},
            ],
            "outcomes": ["Analyze water quality parameters for engineering applications", "Understand electrochemical and corrosion processes in engineering"],
        },
        {
            "code": "CS101", "name": "Introduction to Programming in C",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Fundamentals of C Programming", "topics": ["Data Types & Operators", "Input/Output Functions", "Control Flow (if, switch, loops)", "Functions & Recursion", "Storage Classes"]},
                {"id": "M2", "title": "Arrays, Strings & Pointers", "topics": ["1D & 2D Arrays", "String Manipulation", "Pointer Arithmetic", "Arrays of Pointers", "Dynamic Memory Allocation (malloc, calloc, realloc, free)"]},
                {"id": "M3", "title": "Structures, Unions & File Handling", "topics": ["Structures & Unions", "Bit Fields", "File I/O (fopen, fclose, fread, fwrite, fprintf, fscanf)", "Random Access Files"]},
                {"id": "M4", "title": "Preprocessor, Recursion & Problem Solving", "topics": ["Preprocessor Directives", "Macros & Conditional Compilation", "Recursive Algorithms (Fibonacci, Towers of Hanoi)", "Algorithmic Problem Solving"]},
            ],
            "outcomes": ["Write correct and efficient C programs", "Use pointers and dynamic memory effectively", "Implement file-based data processing"],
        },
        {
            "code": "EE101", "name": "Basic Electrical & Electronics Engineering",
            "credits": 3, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "DC Circuits", "topics": ["Ohm's Law", "Kirchhoff's Laws", "Thevenin's & Norton's Theorems", "Superposition Theorem", "Maximum Power Transfer"]},
                {"id": "M2", "title": "AC Circuits & Transformers", "topics": ["RMS & Average Values", "Phasor Representation", "RLC Circuits", "Resonance", "Single Phase Transformers"]},
                {"id": "M3", "title": "Electrical Machines", "topics": ["DC Generators & Motors", "Three Phase Induction Motors", "Synchronous Machines", "Speed Control Methods"]},
                {"id": "M4", "title": "Analog & Digital Electronics Basics", "topics": ["Diodes & Rectifiers", "Transistors (BJT, FET)", "Logic Gates", "Number Systems & Codes", "Boolean Algebra"]},
            ],
            "outcomes": ["Analyze linear electrical circuits using network theorems", "Understand basic analog and digital electronic circuits"],
        },
        {
            "code": "HS101", "name": "Professional Communication & Ethics",
            "credits": 2, "category": "Humanities & Social Sciences", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Communication Fundamentals", "topics": ["Barriers to Communication", "Verbal & Non-Verbal Communication", "Business Writing Skills", "Report Writing", "Technical Presentation Techniques"]},
                {"id": "M2", "title": "Professional Ethics & Engineering Practice", "topics": ["Engineering Ethics", "Code of Conduct", "Intellectual Property Rights", "Cyber Ethics", "Data Privacy Principles", "Environmental Responsibility"]},
                {"id": "M3", "title": "Employability Skills", "topics": ["Resume Building", "Interview Preparation", "Group Discussion Techniques", "Workplace Etiquette", "Team Leadership"]},
            ],
            "outcomes": ["Communicate effectively in professional engineering contexts", "Apply ethical reasoning to engineering decisions"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 2 — Foundational CS & Applied Sciences
    # ---------------------------------------------------------------
    2: [
        {
            "code": "MA102", "name": "Engineering Mathematics II",
            "credits": 4, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Linear Algebra & Vector Calculus", "topics": ["Matrix Diagonalization", "Sylvester's Law of Inertia", "Vector Differentiation (Gradient, Divergence, Curl)", "Vector Integration (Line, Surface, Volume)"]},
                {"id": "M2", "title": "Complex Analysis", "topics": ["Analytic Functions", "Cauchy-Riemann Equations", "Harmonic Functions", "Conformal Mapping", "Contour Integration", "Residue Theorem"]},
                {"id": "M3", "title": "Laplace & Fourier Transforms", "topics": ["Laplace Transform Properties & Inverse", "Convolution Theorem", "Application to ODEs & PDEs", "Fourier Series", "Fourier Transform & Inverse"]},
                {"id": "M4", "title": "Probability & Statistics", "topics": ["Discrete & Continuous Distributions", "Joint Distributions", "Central Limit Theorem", "Bayesian Estimation", "Hypothesis Testing", "Regression & Correlation", "ANOVA"]},
            ],
            "outcomes": ["Apply transform methods to solve engineering differential equations", "Use probability theory for statistical inference in engineering"],
        },
        {
            "code": "PH102", "name": "Physics for Information Technology",
            "credits": 3, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Semiconductor Physics", "topics": ["Energy Bands in Solids", "Intrinsic & Extrinsic Semiconductors", "Carrier Transport", "PN Junction Diode", "JFET & MOSFET Operation"]},
                {"id": "M2", "title": "Superconductivity & Magnetic Materials", "topics": ["Meissner Effect", "Type I & II Superconductors", "BCS Theory", "Ferro & Antiferromagnetism", "Applications in Computing"]},
                {"id": "M3", "title": "Dielectric & Optical Properties of Materials", "topics": ["Polarization Mechanisms", "Piezoelectric & Ferroelectric Materials", "Photonic Crystals", "LED & Laser Physics"]},
                {"id": "M4", "title": "Nanomaterials & Quantum Devices", "topics": ["Quantum Dots", "Carbon Nanotubes", "Graphene Properties", "Quantum Computing Fundamentals"]},
            ],
            "outcomes": ["Understand semiconductor device physics relevant to IT hardware", "Apply nanoscience concepts to emerging computing technologies"],
        },
        {
            "code": "CS102", "name": "Data Structures",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Fundamental Data Structures", "topics": ["Arrays & Linked Lists (Singly, Doubly, Circular)", "Stacks & Queues", "Applications (Expression Evaluation, Polynomial Manipulation)"]},
                {"id": "M2", "title": "Trees & Binary Trees", "topics": ["Binary Tree Traversals (Inorder, Preorder, Postorder)", "Binary Search Trees", "AVL Trees (Rotations, Insertions, Deletions)", "B-Trees & B+ Trees", "Heap & Priority Queues", "Threaded Binary Trees"]},
                {"id": "M3", "title": "Graph Algorithms", "topics": ["Graph Representations (Adjacency Matrix, List)", "BFS & DFS", "Spanning Trees (Prim's, Kruskal's)", "Shortest Path (Dijkstra's, Bellman-Ford, Floyd-Warshall)", "Topological Sort", "Strongly Connected Components"]},
                {"id": "M4", "title": "Hashing, Sorting & Searching", "topics": ["Hash Tables (Open Addressing, Chaining)", "Collision Resolution Strategies", "Sorting (Quick, Merge, Heap, Counting, Radix, Bucket)", "Linear & Binary Search", "Asymptotic Complexity Analysis"]},
            ],
            "outcomes": ["Implement and analyze all fundamental data structures", "Select appropriate data structures for specific application domains", "Analyze algorithm time and space complexity rigorously"],
        },
        {
            "code": "MA201", "name": "Discrete Mathematics",
            "credits": 4, "category": "Basic Science & Mathematics", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Mathematical Logic & Proofs", "topics": ["Propositional Logic", "Predicate Logic", "Rules of Inference", "Proof Techniques (Direct, Contradiction, Induction)"]},
                {"id": "M2", "title": "Sets, Relations & Functions", "topics": ["Set Operations", "Relations (Reflexive, Symmetric, Transitive)", "Equivalence Relations & Partitions", "Partial Orders", "Functions (Injective, Surjective, Bijective)", "Pigeonhole Principle"]},
                {"id": "M3", "title": "Combinatorics & Graph Theory", "topics": ["Permutations & Combinations", "Binomial & Multinomial Theorems", "Inclusion-Exclusion Principle", "Graph Terminology", "Euler & Hamilton Paths", "Graph Coloring", "Planar Graphs (Euler's Formula)"]},
                {"id": "M4", "title": "Algebraic Structures", "topics": ["Groups, Subgroups, Cyclic Groups", "Permutation Groups", "Rings & Ideals", "Fields", "Lattices & Boolean Algebra"]},
            ],
            "outcomes": ["Formulate and prove mathematical statements relevant to CS", "Apply combinatorial and graph-theoretic methods to CS problems"],
        },
        {
            "code": "CS103", "name": "Digital Logic & Computer Architecture",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Digital Logic Design", "topics": ["Boolean Algebra & Logic Gates", "Karnaugh Maps & Quine-McCluskey", "Combinational Circuits (Adders, Multiplexers, Decoders)", "Sequential Circuits (Flip-Flops, Counters, Registers)"]},
                {"id": "M2", "title": "Data Representation & Arithmetic", "topics": ["Number Systems & Conversions", "Signed/Unsigned Representation", "BCD & Gray Code", "Parallel Adders & Subtractors", "Booth's Multiplication Algorithm"]},
                {"id": "M3", "title": "CPU Architecture (8086 / RISC-V)", "topics": ["8086 Architecture (BIU, EU, Registers)", "Addressing Modes", "Instruction Set", "RISC-V ISA Fundamentals", "Pipelining Concepts"]},
                {"id": "M4", "title": "Memory Systems & I/O", "topics": ["Cache Memory (Associativity, Mapping)", "Virtual Memory & Paging", "I/O Techniques (Programmed, Interrupt, DMA)", "Bus Architectures"]},
            ],
            "outcomes": ["Design and analyze combinational and sequential digital circuits", "Understand processor architecture and instruction execution models"],
        },
        {
            "code": "HS102", "name": "Environmental Science & Sustainability",
            "credits": 2, "category": "Humanities & Social Sciences", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Ecosystem & Biodiversity", "topics": ["Ecosystem Structure & Function", "Biodiversity & Conservation", "Environmental Impact Assessment"]},
                {"id": "M2", "title": "Pollution & Climate Change", "topics": ["Air, Water & Soil Pollution", "E-Waste Management", "Climate Change Mechanisms", "Green Computing & Energy-Efficient IT"]},
                {"id": "M3", "title": "Sustainable Development", "topics": ["UN Sustainable Development Goals", "Circular Economy", "Renewable Energy Sources", "Sustainable Software Engineering"]},
            ],
            "outcomes": ["Understand environmental challenges and their engineering solutions", "Apply sustainability principles in IT system design"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 3 — Core CS Systems
    # ---------------------------------------------------------------
    3: [
        {
            "code": "CS201", "name": "Computer Organization & Architecture",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Instruction Set Architecture", "topics": ["ISA Design Principles", "CISC vs RISC", "Addressing Modes", "Instruction Formats", "Operand & Operator Stacks"]},
                {"id": "M2", "title": "Arithmetic Logic Unit Design", "topics": ["Fast Adders (Carry Look-Ahead, Carry Save)", "Multiplication & Division Algorithms", "Floating Point Arithmetic (IEEE 754)", "ALU Design & Integration"]},
                {"id": "M3", "title": "Control Unit Design", "topics": ["Hardwired vs Microprogrammed Control", "Microinstructions & Microoperations", "Control Memory", "Pipeline Control & Hazards"]},
                {"id": "M4", "title": "Advanced Architecture", "topics": ["Instruction Level Parallelism", "Superscalar & VLIW Architectures", "Branch Prediction", "Cache Coherence Protocols", "Multi-core & Multi-processor Systems"]},
            ],
            "outcomes": ["Design and analyze processor control and datapath architectures", "Evaluate memory hierarchy performance and optimization techniques"],
        },
        {
            "code": "CS202", "name": "Object-Oriented Programming with Java",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "OOP Fundamentals", "topics": ["Classes & Objects", "Inheritance & Polymorphism", "Encapsulation & Abstraction", "Interfaces & Abstract Classes", "Composition vs Aggregation"]},
                {"id": "M2", "title": "Java Language Features", "topics": ["Exception Handling (try, catch, finally)", "Generics & Type Safety", "Collections Framework (List, Set, Map, Queue)", "Inner Classes & Lambda Expressions"]},
                {"id": "M3", "title": "Multithreading & Concurrency", "topics": ["Thread Lifecycle", "Synchronized Methods & Blocks", "Producer-Consumer Problem", "ExecutorService & Callable/Future", "java.util.concurrent Package"]},
                {"id": "M4", "title": "Advanced Java & Design Patterns", "topics": ["I/O Streams & Serialization", "Networking (Socket Programming)", "JDBC & Database Connectivity", "Design Patterns (Singleton, Factory, Observer, Strategy)"]},
            ],
            "outcomes": ["Design and implement object-oriented solutions using Java", "Write concurrent multithreaded applications"],
        },
        {
            "code": "CS203", "name": "Operating Systems",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "OS Fundamentals & Process Management", "topics": ["OS Structure (Monolithic, Microkernel)", "Process States & Transitions", "Process Control Block", "Context Switching", "Inter-Process Communication (Pipes, Message Queues, Shared Memory)"]},
                {"id": "M2", "title": "CPU Scheduling", "topics": ["FCFS, SJF, SRTF", "Round Robin, Priority Scheduling", "Multilevel Queue & Feedback", "Gantt Chart Construction", "Response Time & Turnaround Analysis"]},
                {"id": "M3", "title": "Synchronization & Deadlocks", "topics": ["Race Conditions & Critical Section", "Peterson's Algorithm", "Semaphores & Monitors", "Deadlock Conditions & Prevention", "Banker's Algorithm", "Deadlock Detection & Recovery"]},
                {"id": "M4", "title": "Memory & File Management", "topics": ["Paging & Segmentation", "Page Replacement Algorithms (FIFO, LRU, Optimal, LFU)", "Virtual Memory", "Belady's Anomaly", "File System Implementations (Inode, FAT, NTFS)", "Disk Scheduling (FCFS, SSTF, SCAN, C-SCAN)"]},
            ],
            "outcomes": ["Analyze and compare OS scheduling algorithms", "Implement synchronization primitives and resolve deadlocks", "Design virtual memory systems and page replacement strategies"],
        },
        {
            "code": "CS204", "name": "Database Management Systems",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Relational Model & SQL", "topics": ["ER Model & ER-to-Relational Mapping", "Relational Algebra & Tuple/Domain Calculus", "SQL (DDL, DML, DCL, TCL)", "Joins, Subqueries, Views", "Triggers, Stored Procedures, Cursors"]},
                {"id": "M2", "title": "Normalization", "topics": ["Functional Dependencies", "Armstrong's Axioms", "1NF, 2NF, 3NF, BCNF, 4NF, 5NF", "Lossless & Dependency-Preserving Decomposition", "Normalization Algorithms"]},
                {"id": "M3", "title": "Transaction Processing", "topics": ["ACID Properties", "Schedule & Serializability", "Conflict & View Serializability", "Two-Phase Locking (Strict 2PL)", "Timestamp Ordering Protocol", "Multi-Version Concurrency Control"]},
                {"id": "M4", "title": "Indexing, Query Optimization & NoSQL", "topics": ["B+ Tree Indexing", "Hash-Based Indexing", "Query Execution Plans & Cost Estimation", "Nested Loop, Sort-Merge, Hash Joins", "NoSQL Concepts (Document, Column, Graph, Key-Value)"]},
            ],
            "outcomes": ["Design normalized relational schemas and write complex SQL", "Analyze transaction schedules and ensure database consistency", "Optimize query performance using appropriate indexing strategies"],
        },
        {
            "code": "CS205", "name": "Design and Analysis of Algorithms",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Algorithm Analysis & Paradigms", "topics": ["Asymptotic Notations (O, Omega, Theta, o, omega)", "Master Theorem & Recurrence Relations", "Divide and Conquer (Merge Sort, Quick Sort, Closest Pair)", "Decrease and Conquer (Binary Search, Insertion Sort)"]},
                {"id": "M2", "title": "Greedy Algorithms", "topics": ["Greedy Choice Property & Optimal Substructure", "Fractional Knapsack", "Job Sequencing with Deadlines", "Huffman Coding", "Activity Selection", "Kruskal's & Prim's MST"]},
                {"id": "M3", "title": "Dynamic Programming", "topics": ["Overlapping Subproblems & Optimal Substructure", "0/1 Knapsack", "Longest Common Subsequence", "Matrix Chain Multiplication", "Bellman-Ford Shortest Path", "Travelling Salesman Problem (Approximation)", "Edit Distance"]},
                {"id": "M4", "title": "Advanced Algorithmic Topics", "topics": ["NP-Completeness (P, NP, NP-Hard, NP-Complete)", "Reductions & Cook-Levin Theorem", "Approximation Algorithms", "Randomized Algorithms (Quickselect, randomized BST)", "Backtracking (N-Queens, Sudoku Solver)", "Branch and Bound"]},
            ],
            "outcomes": ["Design efficient algorithms using multiple paradigm strategies", "Prove algorithm correctness using loop invariants and induction", "Classify problems using NP-completeness theory"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 4 — Systems & Software Engineering
    # ---------------------------------------------------------------
    4: [
        {
            "code": "CS301", "name": "Computer Networks",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Network Models & Data Link Layer", "topics": ["OSI & TCP/IP Models", "Physical Layer (Encoding, Bandwidth, Latency)", "Data Link Layer Framing", "Error Detection & Correction (CRC, Hamming Code)", "Flow Control (Stop-and-Wait, Sliding Window)", "MAC Protocols (ALOHA, CSMA/CD, CSMA/CA)"]},
                {"id": "M2", "title": "Network Layer", "topics": ["IPv4 & IPv6 Addressing & Subnetting", "CIDR & Supernetting", "NAT & PAT", "Routing Algorithms (RIP, OSPF, BGP)", "ICMP & ARP", "Network Addressing & Forwarding"]},
                {"id": "M3", "title": "Transport Layer", "topics": ["TCP & UDP", "Three-Way Handshake & Connection Termination", "TCP Flow Control & Congestion Control (Slow Start, AIMD)", "Socket Programming", "Reliable Data Transfer"]},
                {"id": "M4", "title": "Application Layer & Network Security Basics", "topics": ["HTTP/HTTPS, FTP, SMTP, DNS, DHCP", "SSL/TLS Protocol Stack", "Firewalls & Proxies", "Network Address Translation", "Content Delivery Networks"]},
            ],
            "outcomes": ["Analyze and design network protocols across all OSI layers", "Implement network addressing and routing strategies", "Apply transport layer protocols for reliable data transfer"],
        },
        {
            "code": "CS302", "name": "Software Engineering & Project Management",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Software Development Lifecycle", "topics": ["SDLC Models (Waterfall, Spiral, V-Model)", "Agile Methodologies (Scrum, Kanban, XP)", "Requirements Engineering", "Use Case & User Story Modeling"]},
                {"id": "M2", "title": "Software Design & Architecture", "topics": ["UML Diagrams (Class, Sequence, Activity, Use Case)", "Design Principles (SOLID, DRY, KISS, YAGNI)", "Software Architecture Styles (Layered, Microservices, Event-Driven)", "Design Patterns"]},
                {"id": "M3", "title": "Quality Assurance & Testing", "topics": ["Testing Levels (Unit, Integration, System, Acceptance)", "Black-Box & White-Box Testing", "Test Coverage & Code Metrics", "Static & Dynamic Analysis", "CI/CD Pipelines"]},
                {"id": "M4", "title": "Project Management & DevOps", "topics": ["Project Scheduling (Gantt, PERT, CPM)", "Risk Management", "Configuration Management", "DevOps Practices & Tools (Docker, Kubernetes, Jenkins)"]},
            ],
            "outcomes": ["Apply SDLC models and agile practices to software projects", "Design software systems using UML and architectural patterns"],
        },
        {
            "code": "CS303", "name": "Microprocessors & Embedded Systems",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "8086 Microprocessor", "topics": ["8086 Internal Architecture", "Addressing Modes", "Instruction Set & Programming", "Assembly Language Programming"]},
                {"id": "M2", "title": "I/O & Interrupt Handling", "topics": ["I/O Mapped vs Memory Mapped I/O", "Interrupt Structure (INTR, NMI)", "Interrupt Service Routines", "DMA Controllers (8257)"]},
                {"id": "M3", "title": "Peripheral Interface Chips", "topics": ["Programmable Peripheral Interface (8255)", "Timer/Counter (8253/8254)", "Programmable Interrupt Controller (8259)", "ADC/DAC Interfacing"]},
                {"id": "M4", "title": "Embedded Systems Fundamentals", "topics": ["ARM Cortex-M Architecture", "Embedded C Programming", "RTOS Concepts", "Real-Time Applications", "IoT Basics"]},
            ],
            "outcomes": ["Program the 8086 microprocessor in assembly language", "Interface peripheral chips with microprocessors"],
        },
        {
            "code": "CS304", "name": "Theory of Computation & Formal Languages",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Automata Theory", "topics": ["Finite Automata (DFA, NFA)", "NFA to DFA Conversion", "Equivalence of FA", "Regular Expressions & Languages", "Pumping Lemma for Regular Languages"]},
                {"id": "M2", "title": "Context-Free Grammars & Pushdown Automata", "topics": ["Context-Free Grammars (CFG)", "Parse Trees & Ambiguity", "Chomsky Normal Form & Greibach Normal Form", "Pushdown Automata", "Pumping Lemma for CFLs"]},
                {"id": "M3", "title": "Turing Machines & Computability", "topics": ["Turing Machine (Basic & Variants)", "Church-Turing Thesis", "Decidability & Recognizability", "Halting Problem", "Recursive & Recursively Enumerable Languages"]},
                {"id": "M4", "title": "Computational Complexity", "topics": ["Time & Space Complexity Classes", "P vs NP Problem", "NP-Completeness & Reductions", "Space Complexity (PSPACE, L, NL)"]},
            ],
            "outcomes": ["Design and analyze finite automata and pushdown automata", "Classify languages using Chomsky hierarchy", "Determine decidability and computational complexity of problems"],
        },
        {
            "code": "CY201", "name": "Cyber Security Fundamentals",
            "credits": 3, "category": "Professional Elective", "type": "Elective",
            "modules": [
                {"id": "M1", "title": "Security Foundations", "topics": ["CIA Triad (Confidentiality, Integrity, Availability)", "Security Threats & Attack Vectors", "Risk Assessment & Management", "Security Policies & Governance"]},
                {"id": "M2", "title": "Cryptography Basics", "topics": ["Symmetric Key Cryptography (DES, AES)", "Asymmetric Key Cryptography (RSA, ECC)", "Hash Functions (MD5, SHA-256)", "Digital Signatures & Certificates"]},
                {"id": "M3", "title": "Network Security", "topics": ["Firewall Types & Configurations", "Intrusion Detection/Prevention Systems (IDS/IPS)", "VPN Technologies", "SSL/TLS Implementation", "Wireless Security (WPA2, WPA3)"]},
                {"id": "M4", "title": "Security Practices", "topics": ["Secure Coding Practices", "Vulnerability Assessment", "Penetration Testing Methodologies", "Incident Response & Forensics", "Compliance Standards (ISO 27001, GDPR)"]},
            ],
            "outcomes": ["Apply cryptographic techniques for secure communication", "Configure network security infrastructure", "Conduct vulnerability assessments and penetration tests"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 5 — Cyber Security Core & Advanced Topics
    # ---------------------------------------------------------------
    5: [
        {
            "code": "CS401", "name": "Advanced Algorithms & Optimization",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Advanced Graph Algorithms", "topics": ["Network Flow (Ford-Fulkerson, Edmonds-Karp)", "Min-Cost Max-Flow", "Matching Algorithms (Hungarian, Blossom)", "Planar Graphs & Graph Minors"]},
                {"id": "M2", "title": "Linear & Integer Programming", "topics": ["Simplex Method", "Duality Theory", "Integer Linear Programming", "Branch and Bound for IP", "Applications in Network Optimization"]},
                {"id": "M3", "title": "Advanced Dynamic Programming", "topics": ["Bitmask DP", "DP on Trees", "Digit DP", "Convex Hull Trick", "Divide and Conquer Optimization", "State Space Reduction"]},
                {"id": "M4", "title": "Randomized & Parallel Algorithms", "topics": ["Randomized Algorithms (Las Vegas, Monte Carlo)", "Skip Lists", "MapReduce Paradigm", "Parallel Computing Models", "GPU Computing (CUDA Basics)"]},
            ],
            "outcomes": ["Solve complex optimization problems using advanced algorithms", "Design parallel and randomized algorithms for large-scale data processing"],
        },
        {
            "code": "CS402", "name": "Machine Learning & AI for Cyber Security",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Machine Learning Foundations", "topics": ["Supervised Learning (Linear Regression, SVM, Decision Trees, Random Forest)", "Unsupervised Learning (K-Means, DBSCAN, PCA)", "Bias-Variance Tradeoff", "Cross-Validation & Model Selection"]},
                {"id": "M2", "title": "Deep Learning", "topics": ["Neural Networks & Backpropagation", "CNNs for Image/Pattern Analysis", "RNNs & LSTMs for Sequence Data", "Autoencoders & GANs", "Transfer Learning"]},
                {"id": "M3", "title": "ML for Security Applications", "topics": ["Intrusion Detection Systems (IDS) with ML", "Malware Classification", "Phishing Detection", "Anomaly Detection in Network Traffic", "Spam Filtering"]},
                {"id": "M4", "title": "Adversarial ML & Explainability", "topics": ["Adversarial Attacks & Defenses", "Model Robustness", "Explainable AI (XAI) Techniques", "Federated Learning for Privacy", "Ethical AI in Security"]},
            ],
            "outcomes": ["Build and evaluate ML models for security tasks", "Implement adversarial defenses for ML systems"],
        },
        {
            "code": "CS403", "name": "Cryptography & Network Security",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Symmetric Cryptography", "topics": ["Block Cipher Modes (ECB, CBC, CTR, GCM)", "AES Internals & Implementation", "Stream Ciphers (RC4, ChaCha20)", "Differential & Linear Cryptanalysis", "S-Box Design Principles"]},
                {"id": "M2", "title": "Asymmetric Cryptography & Key Management", "topics": ["RSA (Key Generation, Encryption, Signing)", "Diffie-Hellman Key Exchange", "Elliptic Curve Cryptography (ECC)", "ElGamal Encryption", "Public Key Infrastructure (PKI)", "Certificate Authorities & Trust Chains"]},
                {"id": "M3", "title": "Hash Functions & Digital Signatures", "topics": ["Collision Resistance", "HMAC & CMAC", "SHA-2 Family & SHA-3 (Keccak)", "Merkle Trees", "Digital Signature Algorithm (DSA)", "Zero-Knowledge Proofs"]},
                {"id": "M4", "title": "Protocol Security & Quantum Cryptography", "topics": ["SSL/TLS Protocol Deep Dive", "IPSec (AH & ESP)", "PGP & S/MIME", "Quantum Key Distribution (BB84 Protocol)", "Post-Quantum Cryptography Lattice-Based Approaches"]},
            ],
            "outcomes": ["Implement cryptographic protocols for secure data transmission", "Evaluate protocol security against known attacks"],
        },
        {
            "code": "CS404", "name": "Web Application Security",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "OWASP Top 10 Vulnerabilities", "topics": ["Injection (SQL, NoSQL, LDAP, OS)", "Broken Authentication", "Sensitive Data Exposure", "XML External Entities (XXE)", "Broken Access Control", "Cross-Site Scripting (XSS)"]},
                {"id": "M2", "title": "Advanced Web Attacks", "topics": ["Server-Side Request Forgery (SSRF)", "Cross-Site Request Forgery (CSRF)", "Insecure Deserialization", "Server-Side Template Injection (SSTI)", "Business Logic Flaws"]},
                {"id": "M3", "title": "Secure Web Development", "topics": ["Secure Coding Practices (Input Validation, Output Encoding)", "Content Security Policy (CSP)", "HTTPS & Certificate Pinning", "Web Application Firewalls (WAF)"]},
                {"id": "M4", "title": "Penetration Testing Tools & Methodologies", "topics": ["Burp Suite & OWASP ZAP", "SQLMap & Metasploit", "Nmap & Nikto", "Bug Bounty Methodologies", "Report Writing"]},
            ],
            "outcomes": ["Identify and exploit common web application vulnerabilities", "Implement security measures to protect web applications"],
        },
        {
            "code": "HS301", "name": "Cyber Law & Digital Forensics",
            "credits": 3, "category": "Humanities & Social Sciences", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Indian Cyber Laws", "topics": ["Information Technology Act 2000 (Amended)", "Indian Penal Code Sections on Cybercrime", "IT Act Sections 65-72", "CERT-In Guidelines"]},
                {"id": "M2", "title": "International Cyber Law Framework", "topics": ["GDPR (EU)", "CCPA (USA)", "Budapest Convention", "Data Protection & Privacy Rights", "Cross-Border Jurisdiction Issues"]},
                {"id": "M3", "title": "Digital Forensics", "topics": ["Forensic Investigation Methodology", "Disk Forensics & Imaging", "Memory Forensics", "Network Forensics", "Mobile Device Forensics", "Chain of Custody & Evidence Handling"]},
                {"id": "M4", "title": "Cybercrime Investigation", "topics": ["Email Forensics", "Malware Analysis Basics", "Dark Web Investigation", "Financial Cybercrime", "Court Admissibility of Digital Evidence"]},
            ],
            "outcomes": ["Understand the legal framework governing cyber activities", "Apply forensic methodologies to investigate cybercrime"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 6 — Advanced Security & Electives
    # ---------------------------------------------------------------
    6: [
        {
            "code": "CS501", "name": "Ethical Hacking & Penetration Testing",
            "credits": 4, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Reconnaissance & Scanning", "topics": ["Passive & Active Reconnaissance", "OSINT Techniques", "Network Scanning (Nmap, Masscan)", "Vulnerability Scanning (Nessus, OpenVAS)", "Service Enumeration"]},
                {"id": "M2", "title": "Exploitation Techniques", "topics": ["Buffer Overflow Attacks", "Privilege Escalation (Vertical & Horizontal)", "Metasploit Framework", "Shellcode Development", "Client-Side Attacks"]},
                {"id": "M3", "title": "Post-Exploitation & Persistence", "topics": ["Lateral Movement", "Pivoting & Tunneling", "Persistence Mechanisms", "Log Evasion & Anti-Forensics", "C2 Frameworks (Cobalt Strike)"]},
                {"id": "M4", "title": "Specialized Hacking", "topics": ["Wireless Network Hacking (Aircrack-ng)", "Web Application Hacking", "Mobile Application Hacking", "Social Engineering Techniques", "Red Team Operations"]},
            ],
            "outcomes": ["Conduct systematic penetration testing engagements", "Exploit vulnerabilities across multiple attack surfaces", "Document findings and remediation strategies"],
        },
        {
            "code": "CS502", "name": "Cloud Security & Virtualization",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Cloud Computing Fundamentals", "topics": ["Cloud Service Models (IaaS, PaaS, SaaS)", "Deployment Models (Public, Private, Hybrid)", "AWS/Azure/GCP Architecture", "Cloud Networking"]},
                {"id": "M2", "title": "Virtualization & Container Security", "topics": ["Hypervisors (Type 1 & 2)", "VM Escape Attacks", "Docker Security", "Kubernetes Security", "Container Orchestration Security"]},
                {"id": "M3", "title": "Cloud Security Controls", "topics": ["Identity & Access Management (IAM)", "Cloud Security Posture Management", "Encryption in the Cloud", "Cloud Access Security Brokers (CASB)", "Security Information & Event Management (SIEM)"]},
                {"id": "M4", "title": "Cloud Compliance & Forensics", "topics": ["Shared Responsibility Model", "Cloud Compliance Frameworks", "Cloud Forensics Challenges", "Serverless Security", "Zero Trust Architecture in Cloud"]},
            ],
            "outcomes": ["Design secure cloud architectures", "Implement container and Kubernetes security controls"],
        },
        {
            "code": "CS503", "name": "Malware Analysis & Reverse Engineering",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Malware Taxonomy & Behavior", "topics": ["Virus, Worm, Trojan, Ransomware, Spyware", "Rootkits & Bootkits", "Fileless Malware", "Polymorphic & Metamorphic Malware"]},
                {"id": "M2", "title": "Static Analysis", "topics": ["PE File Format", "Import/Export Table Analysis", "String Analysis", "Disassembly (IDA Pro, Ghidra)", "Signature-Based Detection"]},
                {"id": "M3", "title": "Dynamic Analysis", "topics": ["Sandboxing (Cuckoo, Joe Sandbox)", "API Hooking & Monitoring", "Memory Analysis (Volatility)", "Network Behavior Analysis", "Anti-Analysis Techniques"]},
                {"id": "M4", "title": "Advanced Reverse Engineering", "topics": ["x86/x64 Assembly for RE", "Control Flow Analysis", "Encryption/Obfuscation Bypass", "Automated Malware Classification (ML-based)"]},
            ],
            "outcomes": ["Analyze malware samples using static and dynamic techniques", "Reverse engineer binary executables to understand malicious behavior"],
        },
        {
            "code": "CS504", "name": "Blockchain & Distributed Ledger Security",
            "credits": 3, "category": "Professional Elective", "type": "Elective",
            "modules": [
                {"id": "M1", "title": "Blockchain Fundamentals", "topics": ["Cryptographic Hash Functions", "Merkle Trees", "Digital Signatures", "Consensus Mechanisms (PoW, PoS, DPoS)"]},
                {"id": "M2", "title": "Smart Contracts & DApps", "topics": ["Ethereum Architecture", "Solidity Programming", "Smart Contract Security", "Reentrancy Attacks", "Gas Optimization"]},
                {"id": "M3", "title": "Distributed Ledger Technologies", "topics": ["Hyperledger Fabric", "Permissioned vs Permissionless Blockchains", "Zero-Knowledge Proofs", "Ring Signatures & Mixing"]},
                {"id": "M4", "title": "Blockchain Security & Forensics", "topics": ["51% Attack", "Sybil Attack", "Eclipse Attack", "Transaction Analysis", "DeFi Security Vulnerabilities", "NFT Security"]},
            ],
            "outcomes": ["Develop and audit smart contracts for security vulnerabilities", "Analyze blockchain transactions for forensic investigations"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 7 — Specialization & Research
    # ---------------------------------------------------------------
    7: [
        {
            "code": "CS601", "name": "Network Forensics & Incident Response",
            "credits": 3, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Network Traffic Analysis", "topics": ["Wireshark & TShark Deep Analysis", "PCAP Analysis", "NetFlow & IPFIX", "Traffic Anomaly Detection"]},
                {"id": "M2", "title": "Network Forensics Methodology", "topics": ["Evidence Collection from Network Devices", "Log Analysis (Firewall, IDS/IPS, Proxy)", "DNS Forensics", "Email Header Analysis"]},
                {"id": "M3", "title": "Incident Response Frameworks", "topics": ["NIST IR Framework", "SANS Incident Response Steps", "Playbook Development", "Tabletop Exercises"]},
                {"id": "M4", "title": "Threat Intelligence & Attribution", "topics": ["MITRE ATT&CK Framework", "Indicators of Compromise (IoCs)", "Threat Hunting", "APT Analysis", "OSINT for Attribution"]},
            ],
            "outcomes": ["Conduct thorough network forensic investigations", "Develop and execute incident response procedures"],
        },
        {
            "code": "CS602", "name": "AI-Driven Security Automation",
            "credits": 3, "category": "Professional Elective", "type": "Elective",
            "modules": [
                {"id": "M1", "title": "Security Orchestration (SOAR)", "topics": ["SOAR Platforms", "Automated Playbooks", "Threat Intelligence Integration", "Case Management"]},
                {"id": "M2", "title": "NLP for Security", "topics": ["Phishing Email Detection with NLP", "Log Analysis with NLP", "Threat Report Parsing", "Chatbots for Security Operations"]},
                {"id": "M3", "title": "Reinforcement Learning for Security", "topics": ["RL-based Intrusion Response", "Adaptive Security Policies", "Automated Vulnerability Prioritization"]},
                {"id": "M4", "title": "Security Data Analytics", "topics": ["SIEM Correlation Rules", "UEBA (User & Entity Behavior Analytics)", "Security Dashboards (Splunk, ELK)", "Automated Compliance Monitoring"]},
            ],
            "outcomes": ["Implement AI-based security automation solutions", "Build intelligent security analytics pipelines"],
        },
        {
            "code": "CS603", "name": "Secure Software Development Lifecycle (SSDLC)",
            "credits": 3, "category": "Professional Elective", "type": "Elective",
            "modules": [
                {"id": "M1", "title": "Secure Design & Threat Modeling", "topics": ["STRIDE & DREAD", "Attack Trees", "Abuse Cases", "Security Architecture Review"]},
                {"id": "M2", "title": "Secure Coding Standards", "topics": ["CERT Secure Coding Standards", "MISRA for Security", "Language-Specific Security (Python, Java, C++)", "Memory Safety"]},
                {"id": "M3", "title": "Security Testing", "topics": ["SAST (Static Application Security Testing)", "DAST (Dynamic Application Security Testing)", "IAST & RAST", "Fuzzing Techniques"]},
                {"id": "M4", "title": "DevSecOps & Supply Chain Security", "topics": ["CI/CD Security Integration", "Container Image Scanning", "Software Bill of Materials (SBOM)", "Dependency Scanning", "Secret Management"]},
            ],
            "outcomes": ["Integrate security into every phase of the software development lifecycle"],
        },
        {
            "code": "CS699", "name": "Research Project (Phase 1)",
            "credits": 8, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Research Methodology", "topics": ["Literature Survey & Related Work", "Research Problem Formulation", "Hypothesis Development", "Experimental Design"]},
                {"id": "M2", "title": "Implementation", "topics": ["System Architecture Design", "Prototype Development", "Data Collection & Benchmarking", "Tool Development"]},
            ],
            "outcomes": ["Conduct original research in a cyber security domain", "Write and present a technical research paper"],
        },
    ],

    # ---------------------------------------------------------------
    # SEMESTER 8 — Capstone & Specialization
    # ---------------------------------------------------------------
    8: [
        {
            "code": "CS701", "name": "Advanced Persistent Threats (APT) & Defense",
            "credits": 3, "category": "Professional Elective", "type": "Elective",
            "modules": [
                {"id": "M1", "title": "APT Landscape", "topics": ["Notable APT Groups (APT28, APT29, Lazarus)", "Kill Chain Model", "MITRE ATT&CK Mapping", "Nation-State Cyber Operations"]},
                {"id": "M2", "title": "Detection & Analysis", "topics": ["Behavioral Analysis", "YARA Rules", "Sigma Rules", "Threat Hunting Methodologies", "Deception Technologies"]},
                {"id": "M3", "title": "Defense Strategies", "topics": ["Zero Trust Architecture", "Microsegmentation", "Endpoint Detection & Response (EDR)", "Network Detection & Response (NDR)"]},
                {"id": "M4", "title": "Case Studies", "topics": ["SolarWinds Attack Analysis", "Colonial Pipeline Incident", "Log4Shell Analysis", "Supply Chain Attacks"]},
            ],
            "outcomes": ["Analyze advanced persistent threats and develop defense strategies"],
        },
        {
            "code": "CS702", "name": "IoT & Industrial Control Systems Security",
            "credits": 3, "category": "Professional Elective", "type": "Elective",
            "modules": [
                {"id": "M1", "title": "IoT Architecture & Protocols", "topics": ["MQTT, CoAP, Zigbee, LoRaWAN", "IoT Device Lifecycle", "Edge Computing Security"]},
                {"id": "M2", "title": "ICS/SCADA Security", "topics": ["SCADA Systems Architecture", "Modbus & DNP3 Protocols", "ICS-Specific Threats", "Air-Gapped Network Security"]},
                {"id": "M3", "title": "IoT Penetration Testing", "topics": ["Firmware Analysis", "Hardware Hacking (UART, JTAG)", "Wireless Protocol Attacks", "Radio Frequency Analysis"]},
                {"id": "M4", "title": "Smart City & Critical Infrastructure", "topics": ["Smart Grid Security", "Autonomous Vehicle Security", "Healthcare IoT Security", "Regulatory Compliance"]},
            ],
            "outcomes": ["Secure IoT deployments and ICS/SCADA systems"],
        },
        {
            "code": "CS798", "name": "Industry Internship",
            "credits": 10, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Industry Practice", "topics": ["16-Week Industry Placement", "Real-World Security Operations", "SOC Analyst Workflows", "Security Engineering Projects"]},
                {"id": "M2", "title": "Professional Development", "topics": ["Industry Certification Preparation (CEH, CompTIA Security+)", "Professional Networking", "Career Development"]},
            ],
            "outcomes": ["Apply academic knowledge in professional security environments"],
        },
        {
            "code": "CS799", "name": "Research Project (Phase 2) & Thesis",
            "credits": 8, "category": "Professional Core", "type": "Core",
            "modules": [
                {"id": "M1", "title": "Research Completion", "topics": ["Advanced Implementation", "Results & Analysis", "Comparison with State-of-the-Art", "Publication Preparation"]},
                {"id": "M2", "title": "Thesis & Presentation", "topics": ["Thesis Writing (ACM/IEEE Format)", "Viva Voce Preparation", "Demo & Exhibition", "Research Impact Assessment"]},
            ],
            "outcomes": ["Complete original research and publish findings", "Defend thesis before an academic committee"],
        },
    ],
}

# Helper functions
def get_all_courses() -> List[Dict[str, Any]]:
    courses = []
    for semester, sem_courses in BTECH_CYBER_SECURITY_CURRICULUM.items():
        for c in sem_courses:
            c_copy = dict(c)
            c_copy["semester"] = semester
            courses.append(c_copy)
    return courses

def get_semester_courses(semester: int) -> List[Dict[str, Any]]:
    return BTECH_CYBER_SECURITY_CURRICULUM.get(semester, [])

def get_course_by_code(code: str) -> Optional[Dict[str, Any]]:
    for semester, courses in BTECH_CYBER_SECURITY_CURRICULUM.items():
        for c in courses:
            if c["code"].upper() == code.upper():
                result = dict(c)
                result["semester"] = semester
                return result
    return None

def get_all_semesters() -> List[int]:
    return sorted(BTECH_CYBER_SECURITY_CURRICULUM.keys())

def get_semester_stats() -> Dict[int, int]:
    return {sem: len(courses) for sem, courses in BTECH_CYBER_SECURITY_CURRICULUM.items()}

def get_total_credits() -> int:
    total = 0
    for courses in BTECH_CYBER_SECURITY_CURRICULUM.values():
        for c in courses:
            total += c.get("credits", 0)
    return total

def get_course_categories() -> List[str]:
    categories = set()
    for courses in BTECH_CYBER_SECURITY_CURRICULUM.values():
        for c in courses:
            categories.add(c.get("category", ""))
    return sorted(list(categories))

def search_courses(query: str) -> List[Dict[str, Any]]:
    q = query.lower()
    results = []
    for semester, courses in BTECH_CYBER_SECURITY_CURRICULUM.items():
        for c in courses:
            text_to_search = f"{c['code']} {c['name']} {c.get('category', '')}".lower()
            if q in text_to_search:
                result = dict(c)
                result["semester"] = semester
                results.append(result)
    return results

def get_curriculum_summary() -> Dict[str, Any]:
    all_courses = get_all_courses()
    return {
        "program": "B.Tech Computer Science & Engineering (Cyber Security)",
        "total_semesters": 8,
        "total_courses": len(all_courses),
        "total_credits": get_total_credits(),
        "semesters": get_semester_stats(),
        "categories": get_course_categories(),
    }

BTECH_CYBER_SECURITY_SUMMARY = get_curriculum_summary()
