#Noah McGehee 11/24/2023
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pdf_generator import create_pdf
from pdf_importer import import_project_from_pdf


class ProjectSummaryApp:
    def __init__(self, master):
        #Rinky dink app page
        self.master = master
        self.master.title("Project Summary Creator")

        self.style = ttk.Style()
        self.master.set_theme("yaru")

        self.style.configure("Left.TLabel", padding=(10, 0, 0, 0), background=self.master.cget("background"))

        ttk.Label(master, text="Project Title:", style="Left.TLabel").grid(row=0, column=0, sticky='w')
        self.title_entry = ttk.Entry(master)
        self.title_entry.grid(row=0, column=1)

        ttk.Label(master, text="Description:", style="Left.TLabel").grid(row=1, column=0, sticky='w')
        self.description_entry = tk.Text(master, height=5, width=30)
        self.description_entry.grid(row=1, column=1)
        self.description_entry.bind("<Tab>", self.focus_next_widget)
        self.description_checkbox = ttk.Checkbutton(master, variable=tk.BooleanVar(value=True), command=self.generate_project_summary)
        self.description_checkbox.grid(row=1, column=2, sticky='w')

        ttk.Label(master, text="Technologies Used:", style="Left.TLabel").grid(row=2, column=0, sticky='w')
        self.technologies_entry = tk.Text(master, height=5, width=30)
        self.technologies_entry.grid(row=2, column=1)
        self.technologies_entry.bind("<Tab>", self.focus_next_widget)
        self.technologies_checkbox = ttk.Checkbutton(master, variable=tk.BooleanVar(value=True), command=self.generate_project_summary)
        self.technologies_checkbox.grid(row=2, column=2, sticky='w')

        ttk.Label(master, text="Challenges Faced:", style="Left.TLabel").grid(row=3, column=0, sticky='w')
        self.challenges_entry = tk.Text(master, height=5, width=30)
        self.challenges_entry.grid(row=3, column=1)
        self.challenges_entry.bind("<Tab>", self.focus_next_widget)
        self.challenges_checkbox = ttk.Checkbutton(master, variable=tk.BooleanVar(value=True), command=self.generate_project_summary)
        self.challenges_checkbox.grid(row=3, column=2, sticky='w')

        ttk.Label(master, text="Image Path:", style="Left.TLabel").grid(row=4, column=0, sticky='w')
        self.image_path_entry = ttk.Entry(master)
        self.image_path_entry.grid(row=4, column=1)
        self.image_path_entry.bind("<Tab>", self.focus_next_widget)
        self.image_path_button = ttk.Button(master, text="Browse", command=self.browse_image)
        self.image_path_button.grid(row=4, column=2)

        self.preview_text = tk.Text(master, height=10, width=30, state=tk.DISABLED)
        self.preview_text.grid(row=0, column=3, rowspan=5, padx=10)

        ttk.Button(master, text="Generate Project Summary", command=self.generate_project_summary).grid(row=5, column=0, columnspan=3, pady=10)
        ttk.Button(master, text="Export to PDF", command=self.export_to_pdf).grid(row=5, column=3, pady=10)
        ttk.Button(master, text="Import from PDF", command=self.import_from_pdf).grid(row=4, column=3, padx=50, pady=10)

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def generate_project_summary(self):
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        technologies_used = self.technologies_entry.get("1.0", "end-1c")
        challenges_faced = self.challenges_entry.get("1.0", "end-1c")
        image_path = self.image_path_entry.get()

        project_summary_content = f"Project Title: {title}\n\n"

        if self.description_checkbox.instate(['selected']):
            project_summary_content += f"Description: {description}\n\n"

        if self.technologies_checkbox.instate(['selected']):
            project_summary_content += f"Technologies Used: {technologies_used}\n\n"

        if self.challenges_checkbox.instate(['selected']):
            project_summary_content += f"Challenges Faced: {challenges_faced}\n\n"

        self.preview_text.config(state=tk.NORMAL)
        self.preview_text.delete("1.0", "end")
        self.preview_text.insert("1.0", project_summary_content)
        self.preview_text.config(state=tk.DISABLED)

    def browse_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        self.image_path_entry.delete(0, "end")
        self.image_path_entry.insert(0, image_path)

    def export_to_pdf(self):
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        technologies_used = self.technologies_entry.get("1.0", "end-1c")
        challenges_faced = self.challenges_entry.get("1.0", "end-1c")
        image_path = self.image_path_entry.get()

        project_summary_content = f"Project Title: {title}\n\n"

        if self.description_checkbox.instate(['selected']):
            project_summary_content += f"Description: {description}\n\n"

        if self.technologies_checkbox.instate(['selected']):
            project_summary_content += f"Technologies Used: {technologies_used}\n\n"

        if self.challenges_checkbox.instate(['selected']):
            project_summary_content += f"Challenges Faced: {challenges_faced}\n\n"

        file_path = f"{title}_project_summary.pdf"
        create_pdf(file_path, project_summary_content, image_path)
        messagebox.showinfo("Export Successful", f"The project summary has been exported to {file_path}")

    def import_from_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            project_data = import_project_from_pdf(file_path)
            if project_data:
                self.title_entry.delete(0, "end")
                self.title_entry.insert(0, project_data["project_title"])
                self.description_entry.delete("1.0", "end")
                self.description_entry.insert("1.0", project_data["description"])
                self.technologies_entry.delete("1.0", "end")
                self.technologies_entry.insert("1.0", project_data["technologies_used"])
                self.challenges_entry.delete("1.0", "end")
                self.challenges_entry.insert("1.0", project_data["challenges_faced"])
                messagebox.showinfo("Import Successful", "Project data imported from PDF.")
            else:
                messagebox.showwarning("Import Error", "Failed to import project data from PDF.")

