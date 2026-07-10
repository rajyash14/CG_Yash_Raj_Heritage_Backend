def explain_selection_vs_bubble():
    explanation = """
    Bubble Sort compares adjacent elements and swaps them constantly 
    to push the largest value to the end. This leads to many swaps 
    during a single pass.
    
    Selection Sort scans the unsorted part to find the exact minimum 
    (or maximum) element first, and only makes ONE single swap at the 
    end of each pass.
    """
    print(explanation)

explain_selection_vs_bubble()