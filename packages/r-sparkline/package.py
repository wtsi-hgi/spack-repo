# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkline(RPackage):
    """Include interactive sparkline charts in all R contexts with the convenience of 'htmlwidgets'."""

    cran = "sparkline"

    version("2.0", sha256="a2ca2674bc0afbf48de283acfa12945aa736c265a3b83afa896d00732a0d3953")

    depends_on("r-formattable", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
