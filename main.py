from nicegui import ui, run

ui.label("Hello World")
ui.upload(multiple=True, label="Upload Contracts", auto_upload=True)

ui.run()