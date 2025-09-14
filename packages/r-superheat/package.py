# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperheat(RPackage):
    """A Graphical Tool for Exploring Complex Datasets Using Heatmaps.

    superheat generates extendable and customizable heatmaps for exploring
    complex datasets, including big data and data with multiple data types.
    """

    homepage = "https://github.com/rlbarter/superheat"
    git = "https://github.com/rlbarter/superheat.git"

    license("CC0-1.0")

    # No releases on CRAN for >=1.0.0; track GitHub commit.
    version("20200907", commit="2c619578c2ae8bc46e1383183276f98b66b44a53")

    depends_on("r@3.1:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-dplyr@0.4.3:")
        depends_on("r-ggplot2@2.0.0:")
        depends_on("r-gtable@0.1.2:")
        depends_on("r-magrittr@1.5:")
        depends_on("r-plyr@1.8.3:")
        depends_on("r-scales@0.3.0:")
        depends_on("r-stringr@1.2.0:")
        depends_on("r-ggdendro")
        depends_on("r-forcats")

