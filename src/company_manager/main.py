from .views import CompanyApp 

def run_app():
    """Function to be called by pyproject.toml or manually"""
    app = CompanyApp()
    app.mainloop()

if __name__ == "__main__":
    run_app()