# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseehex(RPackage):
    """iSEE extension for summarising data points in hexagonal bins

    This package provides panels summarising data points in hexagonal bins for `iSEE`. It is part of `iSEEu`, the iSEE universe of panels that extend the `iSEE` package.
    """

    homepage = "https://github.com/iSEE/iSEEhex"
    bioc = "iSEEhex"

    version("1.10.0", commit="4458daf04c5af05515eb8ecac9a7030fd25f1455")
    version("1.4.0", commit="314bd5f24016a0d24cdf329943a5b82ab19f8cf1")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-isee", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
