import tkinter as tk
from difflib import SequenceMatcher

class PlagiarismChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Checker")
        
        self.text1_label = tk.Label(root, text="Text 1:")
        self.text1_label.pack()
        
        self.text1_entry = tk.Text(root, height=10, width=50)
        self.text1_entry.pack()
        
        self.text2_label = tk.Label(root, text="Text 2:")
        self.text2_label.pack()
        
        self.text2_entry = tk.Text(root, height=10, width=50)
        self.text2_entry.pack()
        
        self.check_button = tk.Button(root, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    
    def check_plagiarism(self):
        text1 = self.text1_entry.get("1.0", tk.END)
        text2 = self.text2_entry.get("1.0", tk.END)
        
        similarity_ratio = self.calculate_similarity(text1, text2)
        
        if similarity_ratio > 0.8:
            result = "High similarity: Likely plagiarized"
        elif similarity_ratio > 0.5:
            result = "Moderate similarity: Possible plagiarism"
        else:
            result = "Low similarity: Unlikely plagiarism"
        
        self.result_label.config(text=result)
    
    def calculate_similarity(self, text1, text2):
        return SequenceMatcher(None, text1, text2).ratio()

if __name__ == "__main__":
    root = tk.Tk()
    plagiarism_checker = PlagiarismChecker(root)
    root.mainloop()
