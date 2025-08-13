# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendextend(RPackage):
    """Extending 'dendrogram' Functionality in R

    Offers a set of functions for extending 'dendrogram' objects in R, letting
you adjust a tree's graphical parameters, extract common subtrees, and more.
It also provides several functions for comparing trees to one another."""

    cran = "dendextend"

    version("1.18.1", sha256="9d87a293a73e9399210cad62a4afc24ef4ce71e80bff05d5e74315428dd5a517")
    version("1.17.1", sha256="f131c9f3336c8b5a2426d0a4b7a444ec6e3e77f8c9f2313c9fa846e7d09bd562")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
    depends_on("r-fastcluster", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-seriation", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
