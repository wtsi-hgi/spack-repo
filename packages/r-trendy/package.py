# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendy(RPackage):
    """Breakpoint analysis of time-course expression data

    Trendy implements segmented (or breakpoint) regression models to estimate breakpoints which represent changes in expression for each feature/gene in high throughput data with ordered conditions.
    """

    homepage = "https://github.com/rhondabacher/Trendy"
    bioc = "Trendy"

    version("1.30.0", commit="5654c51c6b9cbb1869e29137ddeccb296910b9e6")
    version("1.24.1", commit="c09b4ae6acc75f86614372fc667c4225dca73404")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-segmented", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyfiles", type=("build", "run"))
