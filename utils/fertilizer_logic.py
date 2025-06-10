# utils/fertilizer_logic.py

def recommend_fertilizer(N, P, K):
    ideal_N, ideal_P, ideal_K = 90, 45, 45  # Hypothetical ideal values (e.g., for rice or balanced mix)
    
    deficiency = []
    excess = []

    if N < ideal_N - 10:
        deficiency.append("Nitrogen")
    elif N > ideal_N + 10:
        excess.append("Nitrogen")

    if P < ideal_P - 10:
        deficiency.append("Phosphorus")
    elif P > ideal_P + 10:
        excess.append("Phosphorus")

    if K < ideal_K - 10:
        deficiency.append("Potassium")
    elif K > ideal_K + 10:
        excess.append("Potassium")

    if deficiency:
        return f"Your soil lacks {', '.join(deficiency)}. Consider using fertilizers rich in these."
    elif excess:
        return f"Your soil has excess {', '.join(excess)}. Avoid adding more of these nutrients."
    else:
        return "Your soil nutrients are well balanced! ✅"
