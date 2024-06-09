from z3 import Bool, Solver, Or, And, Not

def knights_and_knaves(statements):
    solver = Solver()

    A_knight = Bool('A_knight')
    B_knight = Bool('B_knight')
    C_knight = Bool('C_knight')

    constraints = []

    constraints.append(A_knight == (A_knight == True))  # A says: "I am a knight."
    constraints.append(B_knight == (A_knight == False))  # B says: "A is a knave."
    constraints.append(C_knight == (B_knight == True))  # C says: "B is a knight."

    for constraint in constraints:
        solver.add(constraint)

    if solver.check() == z3.sat:
        model = solver.model()
        A_is_knight = model[A_knight]
        B_is_knight = model[B_knight]
        C_is_knight = model[C_knight]
        
        result = {
            "A": "Knight" if A_is_knight else "Knave",
            "B": "Knight" if B_is_knight else "Knave",
            "C": "Knight" if C_is_knight else "Knave"
        }
        return result
    else:
        return "No solution found"

statements = [
    ("A", "I am a knight."),
    ("B", "A is a knave."),
    ("C", "B is a knight.")
]

result = knights_and_knaves(statements)
print(result)