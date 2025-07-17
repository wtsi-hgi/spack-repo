# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsqcgui(RPackage):
    """A graphical user interface for MSstatsQC package

    MSstatsQCgui is a Shiny app which provides longitudinal system suitability monitoring and quality control tools for proteomic experiments.
    """

    homepage = "http://msstats.org/msstatsqc"
    bioc = "MSstatsQCgui"

    version("1.28.0", commit="916ac36a070a2edce86bfa3b7414ee4226b0dc26")
    version("1.22.0", commit="edab08dc46d6b07d327d566f1345dd3f2d22e150")

    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-msstatsqc", type=("build", "run"))
    depends_on("r-ggextra", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
