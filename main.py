#Noah McGehee 11/24/2023
from project_summary_app import ProjectSummaryApp
from ttkthemes import ThemedTk

if __name__ == "__main__":
    root = ThemedTk(theme="yaru")
    app = ProjectSummaryApp(root)
    root.mainloop()
