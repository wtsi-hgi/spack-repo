# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatmaply(RPackage):
    """Interactive Cluster Heat Maps Using plotly and ggplot2"""

    cran = "heatmaply"

    version("1.5.0", md5="c681c66008c0a446bc5c1c5083229996")

    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
