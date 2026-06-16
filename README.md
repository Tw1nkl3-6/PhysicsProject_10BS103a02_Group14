# PhysicsProject_10BS103a02_Group14
# Bouncing Ball Physics Analysis Tool

This project provides a Python-based data analysis tool to investigate the physics of bouncing balls (inelastic collisions) using experimental acoustic datasets exported from the **Phyphox** app. 

It validates the mathematical model of a bouncing ball's energy decay and explores the non-linear boundary constraints at the limit of total bounce time ($t_\infty$), referencing the academic framework by Paul J. Hatchell (2021).

## 📂 Project Structure

* `BouncingBallAnalyzer.py`: The main Python script utilizing `pandas`, `numpy`, and `matplotlib` for automated data processing and advanced visualization.
* `basketball_1.csv` ~ `basketball_3.csv`: Experimental trial datasets for a basketball bounce sequence.
* `tabletennis_1.csv` ~ `tabletennis_3.csv`: Experimental trial datasets for a table tennis ball bounce sequence.

## 🚀 Key Features & Analysis Scope

1. **Swapped Axes Kinematics Plotting**: Plots `Bounce Number vs Time (s)` to visually demonstrate Zeno's Paradox and the empirical convergence toward the finite total bounce duration ($t_\infty$).
2. **Coefficient of Restitution ($\epsilon$) Tracking**: Calculates the ratio of successive time intervals ($\Delta t_{next} / \Delta t_{prev}$) per bounce.
3. **Non-Linear Dissipation Demonstration**: Highlights the drop and fluctuation of $\epsilon$ in later stages due to the interference of post-bounce residual vibrations between the ball and the surface.

## 🛠️ How to Run

1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib numpy
   ```

2. Place the target `.csv` data files in the same directory as the script (`BouncingBallAnalyzer.py`).

3. **Select the target data file inside the script**:
   Open `BouncingBallAnalyzer.py` in your code editor and change the `FILE_NAME` variable inside the `if __name__ == "__main__":` block to analyze different datasets (e.g., from basketball to table tennis).
   ```python
   # Inside BouncingBallAnalyzer.py
   FILE_NAME = 'tabletennis_1.csv'  # Modify this string to switch between experimental trials
   ```

4. Run the script via your terminal:
   ```bash
   python BouncingBallAnalyzer.py
   ```
