import win32com.client

# Start LabVIEW
labview = win32com.client.Dispatch("LabVIEW.Application")

# Full path of your VI
vi_path = r"F:\Shankh_Academy\Labview Series\Digital StopWatch\StopWatch_Panel.vi"

# Open VI
vi = labview.GetVIReference(vi_path)

# Show front panel
vi.FPWinOpen = True

print("VI Opened Successfully!")