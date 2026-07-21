"""
Visualisation functionality.
This module creates Bokeh plots for training functions, selected ideal
functions and mapped test points.
"""

from pathlib import Path
from bokeh.plotting import figure, output_file, save

class Visualiser(object):
    """
    Create Bokeh plots for training functions, ideal functions and test points.
    One HTML plot is generated per training function and saved to the output folder.
    """

    def __init__(self, output_directory="outputs/plots"):
        """
        Initialise the visualiser.
        output_directory: folder where the HTML plot files are saved.
        """
        self.output_directory = Path(output_directory)
        # create the output folder if it does not already exist.
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
        train_data: DataFrame containing x-values and training y-values.
        ideal_data: DataFrame containing x-values and ideal function y-values.
        mapped_test_points: DataFrame containing the mapped test points.
        training_function: name of the training function column
        ideal_function: name of the selected ideal function column
        """
        output_file(
            self.output_directory / f"{training_function}_{ideal_function}.html"
        )

        plot = figure(
            title=f"{training_function} matched with {ideal_function}",
            x_axis_label="x",
            y_axis_label="y",
            width=900,
            height=500
        )

        # APA style background & border
        plot.background_fill_color = "white"
        plot.border_fill_color = "white"
        plot.outline_line_color = None

        # APA title style
        plot.title.text_font = "Arial"
        plot.title.text_font_size = "12pt"
        plot.title.text_font_style = "normal"  
        plot.title.align = "center"
        plot.title.text_color = "black"

        # APA style axis 
        for axis in [plot.xaxis, plot.yaxis]:
            axis.axis_label_text_font = "Arial"             
            axis.axis_label_text_font_style = "italic"      
            axis.major_label_text_font = "Arial"            
            axis.minor_tick_line_color = None 

        # remove grid lines
        plot.xgrid.grid_line_color = None          
        plot.ygrid.grid_line_color = None

        # plot the training function as a solid line.
        plot.line(
            train_data["x"],
            train_data[training_function],
            legend_label=f"Training function {training_function}",
            line_width=2.5,
            line_color= "black"
        )

        # plot the ideal function as a dashed line for visual distinction.
        plot.line(
            ideal_data["x"],
            ideal_data[ideal_function],
            legend_label=f"Ideal function {ideal_function}",
            line_width=2,
            line_dash=[10, 6],
            line_color= "#2196F3"
        )

        related_test_points = mapped_test_points[
            mapped_test_points["training_function"] == training_function
        ]

        # only plot test points if any were mapped to this training function.
        if not related_test_points.empty:
            plot.scatter(
                related_test_points["x"],
                related_test_points["y"],
                legend_label="Mapped test points",
                size=7,
                fill_color="white",
                line_color="#E53935"
            )

        legend = plot.legend[0]
        legend.border_line_color = None
        legend.label_text_font = "Arial"
        plot.add_layout(legend, "right")

        # plot files are saved in outputs
        save(plot)