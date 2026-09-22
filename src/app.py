import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    A small amount of setup is needed for napari to coexist with marimo's asyncio
    loop. Copy the cell below into your own notebook — it pumps Qt events from a
    background task so the viewer stays responsive without blocking the kernel.
    """)
    return


@app.cell
def _():
    import sys
    import asyncio
    from qtpy.QtWidgets import QApplication

    # Create QApplication on the kernel main thread
    qapp = QApplication.instance() or QApplication(sys.argv)


    # Pump Qt events from marimo's asyncio loop.
    async def _qt_pump_coro():
        while True:
            qapp.processEvents()
            await asyncio.sleep(0.01)


    # Must precede any napari import
    qt_pump_task = asyncio.create_task(_qt_pump_coro())
    import napari

    return


if __name__ == "__main__":
    app.run()
