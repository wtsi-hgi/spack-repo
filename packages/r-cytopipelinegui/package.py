# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytopipelinegui(RPackage):
    """GUI's for visualization of flow cytometry data analysis pipelines

    This package is the companion of the `CytoPipeline` package. It provides GUI's (shiny apps) for the visualization of flow cytometry data analysis pipelines that are run with `CytoPipeline`. Two shiny applications are provided, i.e. an interactive flow frame assessment and comparison tool and an interactive scale transformations visualization and adjustment tool.
    """

    bioc = "CytoPipelineGUI"

    version("1.6.0", commit="8514162a41af6ae9f4fcbf54b9ceff9779ff5ea4")
    version("1.0.0", commit="3f955711a91ff82a6c3953382e0f2c9503421609")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-cytopipeline", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
