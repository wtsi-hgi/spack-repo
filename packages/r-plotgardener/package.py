# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotgardener(RPackage):
    """Coordinate-Based Genomic Visualization Package for R

    Coordinate-based genomic visualization package for R. It grants users the ability to programmatically produce complex, multi-paneled figures. Tailored for genomics, plotgardener allows users to visualize large complex genomic datasets and provides exquisite control over how plots are placed and arranged on a page.
    """

    homepage = "https://phanstiellab.github.io/plotgardener"
    bioc = "plotgardener"

    version("1.14.0", commit="f5d39c83f238d2a46da322ed67a97cae5b379866")
    version("1.8.3", commit="d97c3b358427ce2aed891704bfa6287e9abd674d")
    version("1.8.2", md5="ddd679b0595dcf2798a5bcc6e3a8c692")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplotify", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-plyranges", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-strawr", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
