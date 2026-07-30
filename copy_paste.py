import plotly.express as px
import pandas as pd

# Define your project schedule
tasks = [
    {"Task": "Finalize Chapters 1–3, Literature Review, Architectural Design", "Start": "2026-07-29", "Finish": "2026-08-11"},
    {"Task": "Smart Contract Development (Anchor, Rust) + Token 2022 Integration", "Start": "2026-08-12", "Finish": "2026-09-02"},
    {"Task": "Database Setup (Supabase) + Backend API Routing (Next.js)", "Start": "2026-09-03", "Finish": "2026-09-16"},
    {"Task": "Frontend UI/UX Design (Next.js) + Web3 Wallet Integration", "Start": "2026-09-17", "Finish": "2026-10-07"},
    {"Task": "System Integration, Devnet Deployment, Security Testing", "Start": "2026-10-08", "Finish": "2026-10-21"},
    {"Task": "Final Documentation, Reporting, Defense Preparation", "Start": "2026-10-22", "Finish": "2026-11-04"},
]

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Create Gantt chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
fig.update_yaxes(autorange="reversed")  # So tasks are listed top-down
fig.update_layout(title="Project Work Plan Gantt Chart", xaxis_title="Timeline", yaxis_title="Tasks")

# Show chart
fig.show()