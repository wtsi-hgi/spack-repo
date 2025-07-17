# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvygapse(RPackage):
    """A SummarizedExperiment for Ivy-GAP data

    Define a SummarizedExperiment and exploratory app for Ivy-GAP glioblastoma image, expression, and clinical data.
    """

    bioc = "ivygapSE"

    version("1.30.0", commit="79352811151a99688984c23cf8266395bb4ab87d")
    version("1.24.0", commit="0d051fba432625ce3c669b14772d7d93cfbca656")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-survminer", type=("build", "run"))
    depends_on("r-hwriter", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-upsetr", type=("build", "run"))
