# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPodcall(RPackage):
    """Positive Droplet Calling for DNA Methylation Droplet Digital PCR

    Reads files exported from 'QX Manager or QuantaSoft' containing amplitude values from a run of ddPCR (96 well plate) and robustly sets thresholds to determine positive droplets for each channel of each individual well. Concentration and normalized concentration in addition to other metrics is then calculated for each well. Results are returned as a table, optionally written to file, as well as optional plots (scatterplot and histogram) for both channels per well written to file. The package includes a shiny application which provides an interactive and user-friendly interface to the full functionality of PoDCall.
    """

    bioc = "PoDCall"

    version("1.16.0", commit="2502146738906bc5aa2b4f17d7feba6e07e7d818")
    version("1.10.1", commit="e26a93b0e1c73693e6b64dd10cdd870eb0a5804f")

    # depends_on("r@4.5:", type=("build", "run"), when="@1.16:")
    depends_on("r@4.3:", type=("build", "run"), when="@1.10:")
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-diptest", type=("build", "run"))
    depends_on("r-rlist", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-laplacesdemon", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
