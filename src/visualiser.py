"""
Visualisation functionality for the DLMDSPWP01 assignment.

This module creates Bokeh plots for training functions, selected ideal
functions and mapped test points.
"""

from pathlib import Path

from bokeh.plotting import figure, output_file, save


class Visualiser:
    """
    Create visualisations for curve matching results.

    The class uses Bokeh to generate HTML plots that show training functions,
    selected ideal functions and mapped test data points.
    """

    def __init__(self, output_directory="outputs/plots"):
        """
        Initialise the visualiser.

        Parameters
        ----------
        output_directory : str
            Directory where the HTML plot files are saved.
        """
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def plot_training_and_ideal_function(
        self,
        train_data,
        ideal_data,
        mapped_test_points,
        training_function,
        ideal_function
    ):
        """
        Plot one training function, its selected ideal function and mapped points.

        Parameters
        ----------
        train_data : pandas.DataFrame
            Training dataset containing x-values and training y-values.
        ideal_data : pandas.DataFrame
            Ideal function dataset containing x-values and ideal y-values.
        mapped_test_points : pandas.DataFrame
            Mapped test points.
        training_function : str
            Name of the training function column, for example "y1".
        ideal_function : str
            Name of the selected ideal function column, for example "y42".
        """
        plot = figure(
            title=f"{training_function} matched with {ideal_function}",
            x_axis_label="x",
            y_axis_label="y",
            width=900,
            height=500
        )

        plot.line(
            train_data["x"],
            train_data[training_function],
            legend_label=f"Training function {training_function}",
            line_width=2
        )

        plot.line(
            ideal_data["x"],
            ideal_data[ideal_function],
            legend_label=f"Ideal function {ideal_function}",
            line_width=2,
            line_dash="dashed"
        )

        related_test_points = mapped_test_points[
            mapped_test_points["training_function"] == training_function
        ]

        if not related_test_points.empty:
            plot.scatter(
                related_test_points["x"],
                related_test_points["y"],
                legend_label="Mapped test points",
                size=7
            )

        plot.legend.location = "top_left"

        output_path = self.output_directory / (
            f"{training_function}_{ideal_function}.html"
        )

        output_file(output_path)
        save(plot)