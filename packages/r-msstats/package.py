# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstats(RPackage):
    """Protein Significance Analysis in DDA, SRM and DIA for Label-free or Label-based Proteomics Experiments

    A set of tools for statistical relative protein significance analysis in DDA, SRM and DIA experiments.
    """

    homepage = "http://msstats.org"
    bioc = "MSstats"

    version("4.16.1", commit="a221510ca0f02dd27f500827bfeb7e359bd0e0eb")
    version("4.10.1", commit="c4264fc5d602f8967508667ac3fe2040fd49a5e4")
    version("4.10.0", md5="fac3a495f2e627a75b10a9b941d3674d")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-msstatsconvert", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
