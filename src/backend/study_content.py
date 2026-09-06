"""
Comprehensive Study Content Repository for B.Tech CSE
Contains notes, formulas, MCQs, examples, flashcards, and practice questions per topic
"""

# ===== YEAR 1 - SEMESTER 1 STUDY CONTENT =====

YEAR1_SEM1_CONTENT = {
    "MA101": {
        "matrices_and_determinants": {
            "title": "Matrices and Determinants",
            "summary": "Matrices are rectangular arrays of numbers used to represent linear transformations and systems of linear equations. Determinants are scalar values computed from square matrices.",
            "key_points": [
                "Matrix addition requires same dimensions",
                "Matrix multiplication is associative but not commutative",
                "Determinant exists only for square matrices",
                "det(AB) = det(A) × det(B)",
                "If det(A) ≠ 0, matrix A is invertible"
            ],
            "formulas": [
                {
                    "name": "Determinant of 2×2 Matrix",
                    "latex": "$$\\det\\begin{bmatrix}a & b \\\\ c & d\\end{bmatrix} = ad - bc$$",
                    "explanation": "Cross-multiply and subtract for 2×2 matrices"
                },
                {
                    "name": "Cramer's Rule",
                    "latex": "$$x_i = \\frac{\\det(A_i)}{\\det(A)}$$",
                    "explanation": "Solve linear systems using determinants when det(A) ≠ 0"
                },
                {
                    "name": "Inverse of 2×2 Matrix",
                    "latex": "$$A^{-1} = \\frac{1}{ad-bc}\\begin{bmatrix}d & -b \\\\ -c & a\\end{bmatrix}$$",
                    "explanation": "Swap diagonal elements, change sign of off-diagonal, divide by determinant"
                }
            ],
            "examples": [
                {
                    "question": "Find determinant of [[3, 2], [1, 4]]",
                    "answer": "det = 3×4 - 2×1 = 12 - 2 = 10",
                    "steps": ["Multiply diagonal elements: 3×4 = 12", "Multiply anti-diagonal: 2×1 = 2", "Subtract: 12 - 2 = 10"]
                },
                {
                    "question": "Solve using Cramer's Rule: 2x + 3y = 8, x - y = 1",
                    "answer": "x = 11/5, y = 6/5",
                    "steps": ["A = [[2,3],[1,-1]], det(A) = -5", "Ax = [[8,3],[1,-1]], det(Ax) = -11", "Ay = [[2,8],[1,1]], det(Ay) = -6", "x = -11/-5 = 11/5, y = -6/-5 = 6/5"]
                }
            ],
            "mcqs": [
                {"question": "For which type of matrices is determinant defined?", "options": ["Rectangular", "Square", "Column", "Row"], "correct": 1},
                {"question": "If det(A) = 0, the matrix A is:", "options": ["Invertible", "Singular", "Non-singular", "Orthogonal"], "correct": 1},
                {"question": "Cramer's Rule can be applied when:", "options": ["det(A) = 0", "det(A) ≠ 0", "A is rectangular", "A has no inverse"], "correct": 1},
                {"question": "The inverse of a matrix exists if and only if:", "options": ["det(A) > 0", "det(A) < 0", "det(A) = 0", "det(A) ≠ 0"], "correct": 3}
            ],
            "practice_questions": [
                "Find determinant of [[5, 3], [2, 7]]",
                "Solve: 3x + 2y = 12, 4x - y = 5 using Cramer's Rule",
                "Find inverse of [[4, 7], [2, 6]]",
                "Explain why det(AB) = det(A)det(B) holds for square matrices"
            ],
            "flashcards": [
                {"front": "What is the condition for a matrix to be invertible?", "back": "Determinant must be non-zero (det(A) ≠ 0)", "hint": "Non-singular matrix"},
                {"front": "State Cramer's Rule formula for solving linear systems", "back": "x_i = det(A_i) / det(A) where A_i replaces column i with constants", "hint": "Using determinants"},
                {"front": "What is det(AB) in terms of det(A) and det(B)?", "back": "det(AB) = det(A) × det(B)", "hint": "Product property"}
            ],
            "viva_questions": [
                "What is the geometric interpretation of determinant?",
                "Explain the relationship between matrix rank and determinant.",
                "Why is Cramer's Rule computationally expensive for large systems?"
            ]
        },
        "eigenvalues_eigenvectors": {
            "title": "Eigenvalues and Eigenvectors",
            "summary": "Eigenvalues and eigenvectors reveal fundamental properties of linear transformations. An eigenvector of a matrix is a vector that changes by only a scalar factor when the linear transformation is applied.",
            "key_points": [
                "Eigenvectors remain in the same direction after transformation",
                "Eigenvalue is the scaling factor for the eigenvector",
                "Sum of eigenvalues = trace of matrix",
                "Product of eigenvalues = determinant of matrix"
            ],
            "formulas": [
                {
                    "name": "Eigenvalue Equation",
                    "latex": "$$A\\mathbf{v} = \\lambda\\mathbf{v}$$",
                    "explanation": "Matrix A transforms eigenvector v by scalar λ"
                },
                {
                    "name": "Characteristic Equation",
                    "latex": "$$\\det(A - \\lambda I) = 0$$",
                    "explanation": "Solve for λ to find eigenvalues"
                },
                {
                    "name": "Cayley-Hamilton Theorem",
                    "latex": "$$p(A) = 0$$",
                    "explanation": "Every square matrix satisfies its own characteristic equation"
                }
            ],
            "examples": [
                {
                    "question": "Find eigenvalues of [[4, 1], [2, 3]]",
                    "answer": "λ = 5, 2",
                    "steps": ["Characteristic equation: det([[4-λ, 1], [2, 3-λ]]) = 0", "(4-λ)(3-λ) - 2 = 0", "λ² - 7λ + 10 = 0", "(λ-5)(λ-2) = 0", "λ = 5, 2"]
                }
            ],
            "mcqs": [
                {"question": "Eigenvectors remain in the same direction after transformation. True/False?", "options": ["True", "False"], "correct": 0},
                {"question": "The product of all eigenvalues equals:", "options": ["Trace of matrix", "Determinant of matrix", "Rank of matrix", "Frobenius norm"], "correct": 1},
                {"question": "Cayley-Hamilton theorem states:", "options": ["A = A⁻¹", "p(A) = 0", "det(A) = 1", "A² = I"], "correct": 1}
            ]
        }
    },
    "PH101": {
        "wave_optics": {
            "title": "Wave Optics",
            "summary": "Wave optics explains optical phenomena using the wave theory of light, including interference, diffraction, and polarization that cannot be explained by ray optics.",
            "key_points": [
                "Interference occurs when coherent waves superpose",
                "Diffraction is bending of light around obstacles",
                "Polarization shows light is a transverse wave",
                "Coherent sources have constant phase difference"
            ],
            "formulas": [
                {
                    "name": "Young's Double Slit",
                    "latex": "$$y = \\frac{\\lambda D}{d}$$",
                    "explanation": "Fringe width where λ=wavelength, D=distance to screen, d=slit separation"
                },
                {
                    "name": "Malus Law",
                    "latex": "$$I = I_0 \\cos^2\\theta$$",
                    "explanation": "Intensity after polarizer at angle θ"
                },
                {
                    "name": "Thin Film Interference",
                    "latex": "$$2nt = m\\lambda \\text{ (constructive)}$$",
                    "explanation": "Condition for bright fringes in thin films"
                }
            ],
            "examples": [
                {
                    "question": "In Young's double slit, λ=600nm, D=1m, d=0.5mm. Find fringe width.",
                    "answer": "1.2 mm",
                    "steps": ["y = λD/d", "y = (600×10⁻⁹)(1)/(0.5×10⁻³)", "y = 1.2×10⁻³ m = 1.2 mm"]
                }
            ]
        }
    }
}

# ===== YEAR 1 - SEMESTER 2 STUDY CONTENT =====
YEAR1_SEM2_CONTENT = {
    "MA102": {
        "integral_calculus": {
            "title": "Integral Calculus",
            "summary": "Integral calculus deals with accumulation of quantities and areas under curves. It is the inverse process of differentiation.",
            "key_points": [
                "Definite integrals give net area",
                "Fundamental Theorem links differentiation and integration",
                "Improper integrals have infinite limits or discontinuities",
                "Beta and Gamma functions extend factorial to real numbers"
            ],
            "formulas": [
                {
                    "name": "Fundamental Theorem",
                    "latex": "$$\\int_a^b f(x)\\,dx = F(b) - F(a)$$",
                    "explanation": "If F'(x) = f(x), then definite integral equals F(b) - F(a)"
                },
                {
                    "name": "Integration by Parts",
                    "latex": "$$\\int u\\,dv = uv - \\int v\\,du$$",
                    "explanation": "Product rule for integration"
                },
                {
                    "name": "Beta Function",
                    "latex": "$$B(m,n) = \\int_0^1 x^{m-1}(1-x)^{n-1}\\,dx = \\frac{\\Gamma(m)\\Gamma(n)}{\\Gamma(m+n)}$$",
                    "explanation": "Beta function relates to Gamma function"
                },
                {
                    "name": "Gamma Function",
                    "latex": "$$\\Gamma(n) = \\int_0^\\infty x^{n-1}e^{-x}\\,dx = (n-1)!$$",
                    "explanation": "Generalizes factorial: Γ(n) = (n-1)!"
                }
            ],
            "examples": [
                {
                    "question": "Evaluate ∫x sin(x) dx from 0 to π",
                    "answer": "π",
                    "steps": ["Integration by parts: u=x, dv=sin(x)dx", "du=dx, v=-cos(x)", "-x cos(x)|₀^π + ∫cos(x)dx", "-π(-1) + 0 + sin(x)|₀^π = π"]
                }
            ],
            "mcqs": [
                {"question": "∫₀^∞ e⁻ˣ dx =", "options": ["0", "1", "∞", "π"], "correct": 1},
                {"question": "B(m,n) =", "options": ["Γ(m)Γ(n)", "Γ(m+n)", "Γ(m)Γ(n)/Γ(m+n)", "Γ(m)/Γ(n)"], "correct": 2}
            ]
        },
        "differential_equations": {
            "title": "Differential Equations",
            "summary": "Differential equations relate functions to their derivatives. They model dynamic systems in physics, engineering, and biology.",
            "key_points": [
                "Order = highest derivative, Degree = power of highest derivative",
                "Linear DE: dy/dx + P(x)y = Q(x)",
                "Exact DE: Mdx + Ndy = 0 where ∂M/∂y = ∂N/∂x",
                "Wronskian determines linear independence"
            ],
            "formulas": [
                {
                    "name": "Linear First Order",
                    "latex": "$$\\frac{dy}{dx} + P(x)y = Q(x)$$",
                    "explanation": "Standard form for linear first-order DE"
                },
                {
                    "name": "Integrating Factor",
                    "latex": "$$\\mu(x) = e^{\\int P(x)\\,dx}$$",
                    "explanation": "Multiply to make equation exact"
                },
                {
                    "name": "Wronskian",
                    "latex": "$$W(y_1,y_2) = \\begin{vmatrix}y_1 & y_2 \\\\ y_1' & y_2'\\end{vmatrix}$$",
                    "explanation": "Non-zero Wronskian means linearly independent solutions"
                }
            ],
            "examples": [
                {
                    "question": "Solve dy/dx + 2y = e⁻ˣ",
                    "answer": "y = e⁻ˣ + Ce⁻²ˣ",
                    "steps": ["IF = e^(∫2dx) = e²ˣ", "d/dx(y e²ˣ) = eˣ", "y e²ˣ = eˣ + C", "y = e⁻ˣ + Ce⁻²ˣ"]
                }
            ],
            "mcqs": [
                {"question": "Order of d²y/dx² + 3dy/dx + 2y = 0 is:", "options": ["1", "2", "3", "4"], "correct": 1},
                {"question": "The Wronskian being non-zero implies:", "options": ["Dependent solutions", "Independent solutions", "No solution", "Unique solution"], "correct": 1}
            ]
        }
    },
    "CS102": {
        "arrays_linked_lists": {
            "title": "Arrays and Linked Lists",
            "summary": "Arrays store elements in contiguous memory while linked lists use nodes with pointers. Each has different time complexities for operations.",
            "key_points": [
                "Arrays: O(1) access, O(n) insertion/deletion",
                "Singly Linked List: O(n) access, O(1) insertion at head",
                "Doubly Linked List: bidirectional traversal",
                "Circular Linked List: last points to first"
            ],
            "formulas": [
                {
                    "name": "Array Access",
                    "latex": "$$address = base + (index) \\times size$$",
                    "explanation": "Direct access using base address and index"
                },
                {
                    "name": "Time Complexities",
                    "latex": "Array: Access O(1), Search O(n), Insert O(n), Delete O(n)",
                    "explanation": "Array operation complexities"
                },
                {
                    "name": "Linked List Time",
                    "latex": "LL: Access O(n), Search O(n), Insert O(1), Delete O(1)",
                    "explanation": "Linked list operation complexities"
                }
            ],
            "examples": [
                {
                    "question": "Implement linked list reversal",
                    "answer": "Iterative approach with three pointers",
                    "code": """def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev"""
                }
            ],
            "mcqs": [
                {"question": "Array access complexity:", "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "correct": 0},
                {"question": "Linked list insertion at head:", "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"], "correct": 0},
                {"question": "Memory efficient for dynamic data:", "options": ["Array", "Linked List", "Both same", "None"], "correct": 1}
            ]
        },
        "trees": {
            "title": "Trees",
            "summary": "Trees are hierarchical data structures with a root and child nodes. Binary trees, BSTs, and AVL trees are fundamental tree variants.",
            "key_points": [
                "Binary Tree: each node has at most 2 children",
                "Binary Search Tree: left < root < right",
                "AVL Tree: balance factor |BF| ≤ 1",
                "Height of balanced BST: O(log n)"
            ],
            "formulas": [
                {
                    "name": "Balance Factor",
                    "latex": "$$BF = \\text{height(left)} - \\text{height(right)}$$",
                    "explanation": "For AVL trees, |BF| must be ≤ 1"
                },
                {
                    "name": "AVL Height Bound",
                    "latex": "$$h < 1.4404 \\log_2(n + 2) - 0.328$$",
                    "explanation": "Maximum height of AVL tree with n nodes"
                },
                {
                    "name": "Binary Tree Nodes",
                    "latex": "$$n_{leaves} = n_{degree2} + 1$$",
                    "explanation": "Number of leaves = number of 2-degree nodes + 1"
                }
            ],
            "examples": [
                {
                    "question": "Insert 50, 30, 70, 20, 40 into BST",
                    "answer": "Visual tree structure",
                    "steps": ["50 as root", "30 left of 50", "70 right of 50", "20 left of 30", "40 right of 30"]
                }
            ],
            "mcqs": [
                {"question": "Maximum nodes in binary tree of height h:", "options": ["2ʰ", "2ʰ⁺¹-1", "h²", "h!"], "correct": 1},
                {"question": "AVL tree balance factor range:", "options": ["0 to 1", "-1 to 1", "-2 to 2", "0 to 2"], "correct": 1},
                {"question": "Inorder traversal of BST gives:", "options": ["Reverse order", "Random order", "Sorted order", "Level order"], "correct": 2}
            ]
        }
    }
}

# ===== YEAR 2 - SEMESTER 3 STUDY CONTENT =====
YEAR2_SEM3_CONTENT = {
    "CS201": {
        "asymptotic_analysis": {
            "title": "Asymptotic Analysis",
            "summary": "Asymptotic analysis describes the behavior of algorithms as input size approaches infinity, using Big-O, Big-Theta, and Big-Omega notations.",
            "key_points": [
                "Big-O: Upper bound (worst case)",
                "Big-Ω: Lower bound (best case)",
                "Big-Θ: Tight bound (average case)",
                "Transitivity and reflexivity properties"
            ],
            "formulas": [
                {
                    "name": "Big-O Definition",
                    "latex": "$$f(n) = O(g(n)) \\iff \\exists c, n_0 \\text{ s.t. } 0 \\leq f(n) \\leq cg(n) \\forall n \\geq n_0$$",
                    "explanation": "f(n) grows no faster than g(n)"
                },
                {
                    "name": "Master Theorem",
                    "latex": "$$T(n) = aT\\left(\\frac{n}{b}\\right) + \\Theta(n^k \\log^p n)$$",
                    "explanation": "Cases based on comparison of n^(log_b a) with n^k"
                },
                {
                    "name": "Growth Rate Hierarchy",
                    "latex": "$$1 < \\log n < \\sqrt{n} < n < n\\log n < n^2 < n^3 < 2^n < n!$$",
                    "explanation": "Standard growth rate ordering"
                }
            ],
            "examples": [
                {
                    "question": "Solve T(n) = 2T(n/2) + n using Master Theorem",
                    "answer": "Θ(n log n)",
                    "steps": ["a=2, b=2, f(n)=n", "n^(log_b a) = n^(log_2 2) = n", "f(n) = Θ(n)", "Case 2 applies", "T(n) = Θ(n log n)"]
                }
            ],
            "mcqs": [
                {"question": "T(n) = 3T(n/4) + n has complexity:", "options": ["O(n)", "O(n log n)", "O(n²)", "O(4ⁿ)"], "correct": 0},
                {"question": "Which is NOT a property of Big-O:", "options": ["Reflexive", "Symmetric", "Transitive", "Positive definite"], "correct": 1}
            ]
        },
        "divide_conquer": {
            "title": "Divide and Conquer",
            "summary": "Divide and conquer algorithms break problems into subproblems, solve them recursively, and combine solutions.",
            "key_points": [
                "Three steps: Divide, Conquer, Combine",
                " recurrence relations often solved with Master Theorem",
                "Space complexity from recursion stack depth"
            ],
            "formulas": [
                {
                    "name": "Merge Sort",
                    "latex": "$$T(n) = 2T(n/2) + \\Theta(n)$$",
                    "explanation": "Divide in half, conquer both, merge in O(n)"
                },
                {
                    "name": "Quick Sort Avg",
                    "latex": "$$T(n) = 2T(n/2) + \\Theta(n)$$",
                    "explanation": "Average case with balanced partition"
                }
            ],
            "examples": [
                {
                    "question": "Explain merge sort on [38, 27, 43, 3, 9, 82, 10]",
                    "answer": "Recursive splitting and merging",
                    "steps": ["Split until single elements", "Merge pairs in order", "Final sorted: [3, 9, 10, 27, 38, 43, 82]"]
                }
            ]
        },
        "greedy_algorithms": {
            "title": "Greedy Algorithms",
            "summary": "Greedy algorithms make locally optimal choices at each stage with the hope of finding global optimum.",
            "key_points": [
                "Greedy choice property: local optimum leads to global",
                "Optimal substructure: optimal solution contains optimal subsolutions",
                "Matroid theory characterizes greedy solvable problems"
            ],
            "formulas": [
                {
                    "name": "Kruskal's Complexity",
                    "latex": "$$O(E \\log E)$$",
                    "explanation": "Sort edges + Union-Find operations"
                },
                {
                    "name": "Prim's Complexity",
                    "latex": "$$O((V+E) \\log V)$$",
                    "explanation": "Using binary heap"
                }
            ],
            "examples": [
                {
                    "question": "Activity selection: activities with start=[1,3,0,5,3,5,6,8,8,2,12], finish=[4,5,6,7,9,9,10,11,12,13,14]",
                    "answer": "4 activities: 1,4,8,11",
                    "steps": ["Sort by finish time", "Select first activity", "Select next if start >= last finish"]
                }
            ]
        },
        "dynamic_programming": {
            "title": "Dynamic Programming",
            "summary": "Dynamic programming solves complex problems by breaking them into overlapping subproblems, solving each subproblem once, and storing results.",
            "key_points": [
                "Optimal substructure and overlapping subproblems",
                "Memoization (top-down) vs Tabulation (bottom-up)",
                "State transition equation defines relationship"
            ],
            "formulas": [
                {
                    "name": "0/1 Knapsack",
                    "latex": "$$dp[i][w] = \\max(dp[i-1][w],\\ dp[i-1][w-wt[i]] + val[i])$$",
                    "explanation": "Choose max between excluding or including item i"
                },
                {
                    "name": "LCS",
                    "latex": "$$dp[i][j] = \\begin{cases}dp[i-1][j-1]+1 & \\text{if } X[i]=Y[j] \\\\ \\max(dp[i-1][j], dp[i][j-1]) & \\text{otherwise}\\end{cases}$$",
                    "explanation": "Longest Common Subsequence"
                }
            ],
            "examples": [
                {
                    "question": "0/1 Knapsack: weights=[2,3,4,5], values=[3,4,5,6], capacity=8",
                    "answer": "Maximum value = 10",
                    "steps": ["Build DP table", "Fill using recurrence", "dp[4][8] = 10"]
                }
            ]
        },
        "graph_algorithms": {
            "title": "Graph Algorithms",
            "summary": "Graph algorithms solve problems on vertices and edges including traversal, shortest paths, and minimum spanning trees.",
            "key_points": [
                "BFS: shortest paths in unweighted graphs",
                "DFS: cycle detection, connectivity",
                "Dijkstra: non-negative edge weights",
                "Bellman-Ford: negative edge weights allowed"
            ],
            "formulas": [
                {
                    "name": "Dijkstra",
                    "latex": "$$O((V+E) \\log V)$$",
                    "explanation": "With binary heap priority queue"
                },
                {
                    "name": "Bellman-Ford",
                    "latex": "$$O(VE)$$",
                    "explanation": "Relax all edges V-1 times"
                },
                {
                    "name": "Floyd-Warshall",
                    "latex": "$$O(V^3)$$",
                    "explanation": "All-pairs shortest paths"
                }
            ],
            "examples": [
                {
                    "question": "Run Dijkstra from source A on graph with edges AB=7, AC=9, AD=14, BC=10, CD=11, BD=15",
                    "answer": "Shortest distances: A=0, B=7, C=9, D=20",
                    "steps": ["Initialize distances", "Extract min (A)", "Update neighbors", "Extract B, update C to 17", "Extract C (dist 9), update D to 20", "Extract D (dist 20)"]
                }
            ]
        }
    },
    "CS202": {
        "number_systems": {
            "title": "Number Systems",
            "summary": "Computer arithmetic uses binary, octal, and hexadecimal representations. Two's complement handles signed integers.",
            "key_points": [
                "Binary base 2, Octal base 8, Hexadecimal base 16",
                "Two's complement: invert bits + 1 for negative",
                "Overflow occurs when result exceeds representable range"
            ],
            "formulas": [
                {
                    "name": "2's Complement Range",
                    "latex": "$$-2^{n-1} \\text{ to } 2^{n-1} - 1$$",
                    "explanation": "For n-bit signed integer"
                },
                {
                    "name": "Hex to Binary",
                    "latex": "$$0xF4 = 1111\\ 0100$$",
                    "explanation": "Each hex digit = 4 binary digits"
                }
            ],
            "examples": [
                {
                    "question": "Convert 45 to 8-bit 2's complement",
                    "answer": "00101101",
                    "steps": ["45 in binary: 101101", "Pad to 8 bits: 00101101", "Positive number, done"]
                },
                {
                    "question": "Find -45 in 8-bit 2's complement",
                    "answer": "11010011",
                    "steps": ["45: 00101101", "Invert: 11010010", "Add 1: 11010011"]
                }
            ]
        },
        "pipelining": {
            "title": "Pipelining",
            "summary": "Pipelining overlaps instruction execution to improve throughput by dividing processing into stages.",
            "key_points": [
                "5-stage pipeline: IF, ID, EX, MEM, WB",
                "Hazards: data, control, structural",
                "Forwarding/bypassing solves data hazards"
            ],
            "formulas": [
                {
                    "name": "Pipeline Speedup",
                    "latex": "$$S = \\frac{n}{1 + (n-1) \\times stall\\_ratio}$$",
                    "explanation": "Speedup from pipelining"
                },
                {
                    "name": "Ideal CPI",
                    "latex": "$$CPI = 1$$",
                    "explanation": "One instruction completes per cycle"
                }
            ],
            "examples": [
                {
                    "question": "5-stage pipeline, 100 instructions, 10% branch misprediction (2 stall cycles). Calculate cycles.",
                    "answer": "118 cycles",
                    "steps": ["100 instructions × 1 cycle = 100", "10 branches × 2 stalls = 20", "But first instruction takes 5 cycles", "Total: 5 + 99 + 14 = 118"]
                }
            ]
        }
    },
    "CS203": {
        "process_management": {
            "title": "Process Management",
            "summary": "Processes are programs in execution. The OS manages process creation, termination, and inter-process communication.",
            "key_points": [
                "Process states: New, Ready, Running, Waiting, Terminated",
                "PCB (Process Control Block) stores process info",
                "Context switching saves/loads process state"
            ],
            "formulas": [
                {
                    "name": "Process States",
                    "latex": "New → Ready → Running → (Waiting) → Terminated",
                    "explanation": "Process state transition diagram"
                }
            ],
            "examples": [
                {
                    "question": "Explain fork() system call behavior",
                    "answer": "Creates child process, returns PID to parent, 0 to child",
                    "code": """pid_t pid = fork();
if (pid == 0) {
    // Child process
} else if (pid > 0) {
    // Parent process
} else {
    // Fork failed
}"""
                }
            ]
        },
        "cpu_scheduling": {
            "title": "CPU Scheduling",
            "summary": "CPU scheduling determines which process runs next. Algorithms include FCFS, SJF, Priority, Round Robin, and Multilevel Queue.",
            "key_points": [
                "FCFS: First Come First Served (non-preemptive)",
                "SJF: Shortest Job First (optimal average wait time)",
                "RR: Round Robin (preemptive, time quantum)",
                "Metrics: Turnaround time, Waiting time, Response time"
            ],
            "formulas": [
                {
                    "name": "Turnaround Time",
                    "latex": "$$TAT = Completion\\ Time - Arrival\\ Time$$",
                    "explanation": "Total time from submission to completion"
                },
                {
                    "name": "Waiting Time",
                    "latex": "$$WT = TAT - Burst\\ Time$$",
                    "explanation": "Time spent waiting in ready queue"
                },
                {
                    "name": "Average Waiting Time",
                    "latex": "$$AWT = \\frac{\\sumWT_i}{n}$$",
                    "explanation": "Mean waiting time across all processes"
                }
            ],
            "examples": [
                {
                    "question": "Processes P1(10), P2(29), P3(3) with FCFS. Calculate AWT.",
                    "answer": "19.67",
                    "steps": ["P1: WT=0", "P2: WT=10", "P3: WT=39", "AWT = (0+10+39)/3 = 16.33"]
                },
                {
                    "question": "Same processes with SJF (non-preemptive). Calculate AWT.",
                    "answer": "9.67",
                    "steps": ["P3(3): WT=0", "P1(10): WT=3", "P2(29): WT=13", "AWT = (0+3+13)/3 = 5.33"]
                }
            ]
        },
        "process_synchronization": {
            "title": "Process Synchronization",
            "summary": "Process synchronization ensures coordinated access to shared resources using critical section protocols, semaphores, and monitors.",
            "key_points": [
                "Critical section requires: mutual exclusion, progress, bounded waiting",
                "Semaphore: counter with wait/signal operations",
                "Monitor: high-level synchronization with condition variables"
            ],
            "formulas": [
                {
                    "name": "Critical Section Requirements",
                    "latex": "1. Mutual Exclusion\\n2. Progress\\n3. Bounded Waiting",
                    "explanation": "Three requirements for valid solution"
                }
            ],
            "examples": [
                {
                    "question": "Implement Producer-Consumer with semaphore",
                    "answer": "Use empty, full, mutex semaphores",
                    "code": """semaphore mutex = 1, empty = n, full = 0;

producer() {
    while (true) {
        produce item
        wait(empty)
        wait(mutex)
        put item in buffer
        signal(mutex)
        signal(full)
    }
}

consumer() {
    while (true) {
        wait(full)
        wait(mutex)
        remove item from buffer
        signal(mutex)
        signal(empty)
        consume item
    }
}"""
                }
            ]
        },
        "deadlock": {
            "title": "Deadlock",
            "summary": "Deadlock occurs when processes wait for resources held by each other. Solutions include prevention, avoidance, detection, and recovery.",
            "key_points": [
                "Coffman conditions: mutual exclusion, hold and wait, no preemption, circular wait",
                "Deadlock prevention: break one condition",
                "Banker's algorithm: safe state avoidance",
                "Detection: resource allocation graph"
            ],
            "formulas": [
                {
                    "name": "Banker's Need",
                    "latex": "$$Need = Max - Allocation$$",
                    "explanation": "Resources still needed by process"
                }
            ],
            "examples": [
                {
                    "question": "Check if system is in safe state with Available=[3,3,2], Max and Allocation matrices given",
                    "answer": "Safe sequence: P1, P0, P2",
                    "steps": ["Calculate Need", "Find process with Need ≤ Available", "Release resources, repeat"]
                }
            ]
        }
    },
    "CS204": {
        "er_modeling": {
            "title": "ER Modeling",
            "summary": "Entity-Relationship modeling visualizes database structure using entities, attributes, relationships, and cardinalities.",
            "key_points": [
                "Entities: real-world objects",
                "Attributes: properties of entities",
                "Relationships: associations between entities",
                "Cardinality: 1:1, 1:N, M:N"
            ],
            "formulas": [
                {
                    "name": "Cardinality Notation",
                    "latex": "1:1,\\ 1:N,\\ M:N",
                    "explanation": "Relationship cardinalities"
                }
            ],
            "examples": [
                {
                    "question": "Design ER for university database",
                    "answer": "Entities: Student, Course, Instructor, Department",
                    "steps": ["Identify entities and attributes", "Define relationships with cardinality", "Convert to tables"]
                }
            ]
        },
        "normalization": {
            "title": "Database Normalization",
            "summary": "Normalization organizes data to minimize redundancy. Forms range from 1NF to BCNF, each with stricter requirements.",
            "key_points": [
                "1NF: Atomic values, no repeating groups",
                "2NF: 1NF + no partial dependency",
                "3NF: 2NF + no transitive dependency",
                "BCNF: For every FD X→Y, X is superkey"
            ],
            "formulas": [
                {
                    "name": "Functional Dependency",
                    "latex": "$$X \\rightarrow Y$$",
                    "explanation": "Value of X determines value of Y"
                },
                {
                    "name": "Armstrong's Axioms",
                    "latex": "Reflexivity\\nAugmentation\\nTransitivity",
                    "explanation": "Inference rules for FDs"
                }
            ],
            "examples": [
                {
                    "question": "Decompose R(A,B,C,D) with FDs: A→B, B→C, C→D to 3NF",
                    "answer": "R1(A,B), R2(B,C), R3(C,D)",
                    "steps": ["Find candidate key: A", "Check 2NF: A→B (no partial)", "Check 3NF: B→C (B not superkey, C not prime)", "Decompose"]
                }
            ]
        }
    }
}

# ===== YEAR 2 - SEMESTER 4 STUDY CONTENT =====
YEAR2_SEM4_CONTENT = {
    "CS301": {
        "network_fundamentals": {
            "title": "Network Fundamentals",
            "summary": "Computer networks connect devices for communication. The OSI and TCP/IP models standardize network layers.",
            "key_points": [
                "OSI: 7 layers (Physical to Application)",
                "TCP/IP: 4 layers (Link to Application)",
                "Encapsulation adds headers at each layer",
                "Protocols: IP, TCP, UDP, HTTP, DNS"
            ],
            "formulas": [
                {
                    "name": "Encapsulation",
                    "latex": "Data → Segment → Packet → Frame → Bits",
                    "explanation": "Layer-by-layer header addition"
                }
            ],
            "examples": [
                {
                    "question": "Trace HTTP request through OSI layers",
                    "answer": "Application → Presentation → Session → Transport → Network → Data Link → Physical",
                    "steps": ["HTTP request created", "TLS encryption (Presentation)", "Session management", "TCP segment", "IP packet", "MAC frame", "Binary signal"]
                }
            ]
        },
        "data_link_layer": {
            "title": "Data Link Layer",
            "summary": "The data link layer provides reliable node-to-node delivery using framing, error detection, and MAC protocols.",
            "key_points": [
                "Framing: delimiting message boundaries",
                "Error detection: CRC for bit-level errors",
                "MAC protocols: CSMA/CD, CSMA/CA"
            ],
            "formulas": [
                {
                    "name": "CRC",
                    "latex": "$$Remainder = Data \\mod Generator$$",
                    "explanation": "Cyclic Redundancy Check for error detection"
                },
                {
                    "name": "CSMA/CD Efficiency",
                    "latex": "$$\\eta = \\frac{1}{1 + 6.4 \\times (T_p/T_t)}$$",
                    "explanation": "Efficiency for Ethernet with collision detection"
                },
                {
                    "name": "Propagation Factor",
                    "latex": "$$a = \\frac{T_p}{T_t}$$",
                    "explanation": "Ratio of propagation time to transmission time"
                }
            ],
            "examples": [
                {
                    "question": "Data=101101, Generator=1011. Find CRC remainder.",
                    "answer": "010",
                    "steps": ["Append 3 zeros: 101101000", "Divide by 1011 using XOR", "Remainder = 010"]
                }
            ]
        }
    },
    "CS302": {
        "oop_concepts": {
            "title": "OOP Concepts",
            "summary": "Object-Oriented Programming uses objects, classes, inheritance, polymorphism, and encapsulation.",
            "key_points": [
                "Encapsulation: bundling data and methods",
                "Inheritance: code reuse",
                "Polymorphism: same interface, different implementations",
                "Abstraction: hiding implementation details"
            ],
            "formulas": [
                {
                    "name": "Java Class Template",
                    "latex": "$$public\\ class\\ ClassName\\ \\{\\\\\\ private\\ fields\\\\\\ public\\ methods\\ \\}$$",
                    "explanation": "Basic class structure"
                }
            ],
            "examples": [
                {
                    "question": "Implement inheritance in Java",
                    "answer": "Use extends keyword",
                    "code": """class Animal {
    void eat() { System.out.println("eating"); }
}
class Dog extends Animal {
    void bark() { System.out.println("barking"); }
}
class TestInheritance {
    public static void main(String args[]) {
        Dog d = new Dog();
        d.eat(); // inherited
        d.bark(); // own
    }
}"""
                }
            ]
        }
    }
}

# ===== YEAR 3 - SEMESTER 5 STUDY CONTENT =====
YEAR3_SEM5_CONTENT = {
    "CS401": {
        "search_algorithms": {
            "title": "Search Algorithms",
            "summary": "Search algorithms explore state spaces to find solutions. uninformed (BFS, DFS) and informed (A*, Hill Climbing) approaches.",
            "key_points": [
                "BFS: Complete, optimal for uniform cost",
                "DFS: Not optimal, uses less memory",
                "A*: Complete, optimal with admissible heuristic",
                "Hill Climbing: Local optimum problem"
            ],
            "formulas": [
                {
                    "name": "A* Heuristic",
                    "latex": "$$f(n) = g(n) + h(n)$$",
                    "explanation": "g(n)=cost so far, h(n)=estimated to goal"
                },
                {
                    "name": "Admissible Heuristic",
                    "latex": "$$h(n) \\leq h^*(n)$$",
                    "explanation": "Never overestimates true cost"
                }
            ],
            "examples": [
                {
                    "question": "A* search on graph with h(n) = straight-line distance",
                    "answer": "Expands nodes with lowest f(n)=g(n)+h(n)",
                    "steps": ["Start at initial state", "Generate successors", "Calculate f(n) for each", "Expand node with minimum f(n)"]
                }
            ]
        },
        "machine_learning_basics": {
            "title": "Machine Learning Basics",
            "summary": "Machine learning enables computers to learn from data without explicit programming. Types include supervised, unsupervised, and reinforcement learning.",
            "key_points": [
                "Supervised: labeled data (classification, regression)",
                "Unsupervised: unlabeled data (clustering, dimensionality reduction)",
                "Reinforcement: learning from interactions",
                "Training set, test set, validation set split"
            ],
            "formulas": [
                {
                    "name": "Accuracy",
                    "latex": "$$Accuracy = \\frac{TP + TN}{TP + TN + FP + FN}$$",
                    "explanation": "Classification accuracy"
                },
                {
                    "name": "Precision",
                    "latex": "$$Precision = \\frac{TP}{TP + FP}$$",
                    "explanation": "Relevance of positive predictions"
                },
                {
                    "name": "Recall",
                    "latex": "$$Recall = \\frac{TP}{TP + FN}$$",
                    "explanation": "Fraction of positives retrieved"
                }
            ],
            "examples": [
                {
                    "question": "Calculate precision and recall for classifier",
                    "answer": "Given confusion matrix values",
                    "steps": ["TP=50, FP=10, FN=5, TN=100", "Precision = 50/(50+10) = 0.833", "Recall = 50/(50+5) = 0.909"]
                }
            ]
        }
    },
    "CS402": {
        "regression": {
            "title": "Regression",
            "summary": "Regression predicts continuous values. Linear regression models linear relationships, logistic regression handles classification.",
            "key_points": [
                "Linear regression: y = mx + c",
                "Gradient descent: iterative optimization",
                "Cost function: MSE for linear regression"
            ],
            "formulas": [
                {
                    "name": "Linear Regression",
                    "latex": "$$y = \\beta_0 + \\beta_1 x$$",
                    "explanation": "Simple linear regression"
                },
                {
                    "name": "Cost Function (MSE)",
                    "latex": "$$J(\\theta) = \\frac{1}{2m} \\sum_{i=1}^m (h_\\theta(x^{(i)}) - y^{(i)})^2$$",
                    "explanation": "Mean Squared Error"
                },
                {
                    "name": "Gradient Descent Update",
                    "latex": "$$\\theta_j := \\theta_j - \\alpha \\frac{\\partial J}{\\partial \\theta_j}$$",
                    "explanation": "Update rule for optimization"
                }
            ],
            "examples": [
                {
                    "question": "Gradient descent for y = 2x + 1 with noisy data",
                    "answer": "Iteratively update θ to minimize cost",
                    "steps": ["Initialize θ randomly", "Compute gradient", "Update θ = θ - α × gradient", "Repeat until convergence"]
                }
            ]
        },
        "classification": {
            "title": "Classification",
            "summary": "Classification predicts discrete labels. Decision trees, SVM, Naive Bayes, and KNN are popular algorithms.",
            "key_points": [
                "Decision trees: split on features",
                "SVM: find optimal hyperplane",
                "Naive Bayes: probabilistic with feature independence",
                "KNN: lazy learning based on neighbors"
            ],
            "formulas": [
                {
                    "name": "Information Gain",
                    "latex": "$$IG(S, A) = H(S) - \\sum_{v \\in Values(A)} \\frac{|S_v|}{|S|} H(S_v)$$",
                    "explanation": "Decision tree splitting criterion"
                },
                {
                    "name": "Bayes Theorem",
                    "latex": "$$P(y|x) = \\frac{P(x|y)P(y)}{P(x)}$$",
                    "explanation": "Naive Bayes classification"
                }
            ],
            "examples": [
                {
                    "question": "Decision tree for weather data",
                    "answer": "Split on outlook, then temperature, humidity, wind",
                    "steps": ["Calculate entropy of dataset", "Calculate information gain for each feature", "Split on highest gain feature", "Repeat recursively"]
                }
            ]
        }
    }
}

# ===== YEAR 3 - SEMESTER 6 STUDY CONTENT =====
YEAR3_SEM6_CONTENT = {
    "CS501": {
        "syntax_analysis": {
            "title": "Syntax Analysis",
            "summary": "Syntax analysis (parsing) checks if source code follows language grammar. Top-down and bottom-up are two parsing approaches.",
            "key_points": [
                "Top-down: predictive, recursive descent",
                "Bottom-up: shift-reduce, LR parsers",
                "LL(1) and LR(1) are common parser types",
                "Ambiguity causes parsing problems"
            ],
            "formulas": [
                {
                    "name": "LL(1) Grammar",
                    "latex": "$$Predictive\\ parsing\\ with\\ 1\\ token\\ lookahead$$",
                    "explanation": "Left-to-right, Leftmost derivation, 1 token"
                }
            ],
            "examples": [
                {
                    "question": "Parse 'id + id * id' using operator precedence",
                    "answer": "id + (id * id)",
                    "steps": ["id has highest precedence", "* has higher than +", "Parse as id + (id * id)"]
                }
            ]
        }
    }
}

# ===== YEAR 4 - SEMESTER 7 STUDY CONTENT =====
YEAR4_SEM7_CONTENT = {
    "CS601": {
        "deep_neural_networks": {
            "title": "Deep Neural Networks",
            "summary": "Deep neural networks have multiple hidden layers, enabling learning of complex representations for tasks like image recognition and NLP.",
            "key_points": [
                "Depth enables hierarchical feature learning",
                "Backpropagation computes gradients",
                "Dropout and batch normalization prevent overfitting",
                "Adam optimizer combines momentum and adaptive learning"
            ],
            "formulas": [
                {
                    "name": "ReLU Activation",
                    "latex": "$$ReLU(x) = \\max(0, x)$$",
                    "explanation": "Rectified Linear Unit"
                },
                {
                    "name": "Dropout",
                    "latex": "$$output = \\begin{cases}0 & \\text{with probability p} \\\\ \\frac{input}{1-p} & \\text{otherwise}\\end{cases}$$",
                    "explanation": "Randomly sets inputs to zero during training"
                },
                {
                    "name": "Batch Normalization",
                    "latex": "$$\\hat{x} = \\frac{x - \\mu_B}{\\sqrt{\\sigma_B^2 + \\epsilon}}$$",
                    "explanation": "Normalizes layer inputs"
                }
            ],
            "examples": [
                {
                    "question": "MLP for binary classification",
                    "answer": "Input → Hidden layers → Sigmoid output",
                    "code": """model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])"""
                }
            ]
        },
        "convolutional_neural_networks": {
            "title": "Convolutional Neural Networks",
            "summary": "CNNs use convolution layers to automatically extract features from images, making them ideal for computer vision tasks.",
            "key_points": [
                "Convolution: filter slides over input",
                "Pooling: downsample feature maps",
                "Transfer learning: reuse pre-trained models",
                "Data augmentation: increase training data"
            ],
            "formulas": [
                {
                    "name": "Convolution Output Size",
                    "latex": "$$Output = \\frac{W - F + 2P}{S} + 1$$",
                    "explanation": "W=input size, F=filter size, P=padding, S=stride"
                },
                {
                    "name": "Max Pooling",
                    "latex": "$$Output_{i,j} = \\max_{(x,y) \\in window} Input_{i+x, j+y}$$",
                    "explanation": "Selects maximum in each window"
                }
            ],
            "examples": [
                {
                    "question": "LeNet architecture for MNIST",
                    "answer": "2 conv + 2 pooling + 2 fully connected",
                    "code": """model = Sequential([
    Conv2D(6, (5,5), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(16, (5,5), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(120, activation='relu'),
    Dense(84, activation='relu'),
    Dense(10, activation='softmax')
])"""
                }
            ]
        },
        "recurrent_neural_networks": {
            "title": "Recurrent Neural Networks",
            "summary": "RNNs process sequences by maintaining hidden state that captures information from previous timesteps.",
            "key_points": [
                "Hidden state carries information across timesteps",
                "Vanishing gradient problem in deep RNNs",
                "LSTM and GRU use gating mechanisms",
                "Bidirectional RNNs process in both directions"
            ],
            "formulas": [
                {
                    "name": "RNN Hidden State",
                    "latex": "$$h_t = \\tanh(W_{hh}h_{t-1} + W_{xh}x_t + b_h)$$",
                    "explanation": "Standard RNN recurrence"
                },
                {
                    "name": "LSTM Gate",
                    "latex": "$$f_t = \\sigma(W_f [h_{t-1}, x_t])$$",
                    "explanation": "Forget gate in LSTM"
                }
            ],
            "examples": [
                {
                    "question": "LSTM for text generation",
                    "answer": "Character-level RNN",
                    "code": """model = Sequential([
    LSTM(128, input_shape=(seq_len, vocab_size)),
    Dense(vocab_size, activation='softmax')
])"""
                }
            ]
        }
    },
    "CS602": {
        "hadoop_ecosystem": {
            "title": "Hadoop Ecosystem",
            "summary": "Hadoop is a distributed computing framework for processing big data across clusters of computers.",
            "key_points": [
                "HDFS: distributed file system",
                "MapReduce: distributed processing model",
                "YARN: resource management",
                "Ecosystem tools: Hive, Pig, HBase, Spark"
            ],
            "formulas": [
                {
                    "name": "HDFS Block Size",
                    "latex": "$$Default = 128\\ MB\\ (Hadoop\\ 2.x)$$",
                    "explanation": "Default block size for HDFS"
                }
            ],
            "examples": [
                {
                    "question": "HDFS write process",
                    "answer": "Client → NameNode → DataNodes",
                    "steps": ["Client requests write", "NameNode checks permissions and namespace", "Client splits file into blocks", "Blocks replicated to DataNodes"]
                }
            ]
        }
    }
}

# ===== UNION OF ALL CONTENT =====
# Add Year 4 Semester 7 content if available
_year4_sem7 = YEAR4_SEM7_CONTENT if 'YEAR4_SEM7_CONTENT' in globals() else {}

ALL_STUDY_CONTENT = {
    **YEAR1_SEM1_CONTENT,
    **YEAR1_SEM2_CONTENT,
    **YEAR2_SEM3_CONTENT,
    **YEAR2_SEM4_CONTENT,
    **YEAR3_SEM5_CONTENT,
    **YEAR3_SEM6_CONTENT,
    **YEAR4_SEM7_CONTENT,
}

def get_subject_content(subject_code: str):
    """Get all study content for a subject"""
    return ALL_STUDY_CONTENT.get(subject_code, {})

def get_topic_content(subject_code: str, topic_name: str):
    """Get specific topic content"""
    subject = get_subject_content(subject_code)
    return subject.get(topic_name.lower().replace(" ", "_"), {})

def get_all_subjects():
    """Get list of all subject codes"""
    return list(ALL_STUDY_CONTENT.keys())
