import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class BouncingBallAnalyzer:
    """Class to analyze bouncing ball (inelastic collision) experiment data from the Phyphox app"""
    
    def __init__(self, file_path):
        # 1. Error handling logic for reading file
        try:
            # First attempt: Assume default comma (,) delimiter and skip malformed lines.
            self.df = pd.read_csv(file_path, on_bad_lines='skip')
        except Exception:
            # Second attempt: Retry with semicolon (;) delimiter and comma (,) decimal points.
            print("Failed to read with default format. Retrying with semicolon (;) delimiter.")
            self.df = pd.read_csv(file_path, sep=';', decimal=',', on_bad_lines='skip')

        # 2. Verify and extract column names
        column_name = 'Time (s)'  # This must match the exact column name in the CSV file.
        
        # Strip whitespaces from column names if any exist to prevent matching errors
        self.df.columns = [col.strip() for col in self.df.columns]
        
        # Print available columns to console if the target column is missing.
        if column_name not in self.df.columns:
            print(f"\n[Error] Column '{column_name}' not found.")
            print(f"Available columns in the file: {self.df.columns.tolist()}")
            raise ValueError(f"Please check the list above and update column_name = '{column_name}' with the correct name.")

        # Extract data
        self.t = self.df[column_name].dropna().values
        self.bounces = np.arange(len(self.t))
        self.epsilon = []

    def calculate_restitution(self):
        """Calculate Coefficient of Restitution using time intervals between successive collisions"""
        for i in range(1, len(self.t) - 1):
            dt_next = self.t[i+1] - self.t[i]
            dt_prev = self.t[i] - self.t[i-1]
            
            if dt_prev != 0:
                e = dt_next / dt_prev
                self.epsilon.append(e)
            else:
                self.epsilon.append(np.nan)

    def plot_results(self):
        """Visualize time trends and changes in the coefficient of restitution"""
        fig, axs = plt.subplots(1, 2, figsize=(14, 5))

        # 1. Bounce number versus collision time (Axes Swapped)
        # x-axis: self.t (Time), y-axis: self.bounces (Bounce Number)
        axs[0].plot(self.t, self.bounces, marker='o', linestyle='-', color='#1f77b4', markersize=4)
        axs[0].set_title('Bounce Number vs Time')
        axs[0].set_xlabel('Time (s)')
        axs[0].set_ylabel('Bounce Number')
        axs[0].grid(True, linestyle='--', alpha=0.7)

        # 2. Coefficient of restitution versus bounce number
        valid_bounces = self.bounces[1:-1]
        axs[1].plot(valid_bounces, self.epsilon, marker='x', linestyle='', color='#d62728')
        axs[1].set_title('Restitution Coefficient ($\epsilon$) vs Bounce Number')
        axs[1].set_xlabel('Bounce Number')
        axs[1].set_ylabel('Restitution Coefficient')
        axs[1].grid(True, linestyle='--', alpha=0.7)
        axs[1].set_ylim(0.5, 1.0) 

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Change to your specific data file name (e.g., tabletennis_1_fixed.csv)
    FILE_NAME = 'tabletennis_1.csv' 
    
    try:
        analyzer = BouncingBallAnalyzer(FILE_NAME)
        analyzer.calculate_restitution()
        analyzer.plot_results()
    except Exception as e:
        print(f"An error occurred during execution: {e}")