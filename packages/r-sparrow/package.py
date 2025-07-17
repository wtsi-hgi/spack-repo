# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparrow(RPackage):
    """Take command of set enrichment analyses through a unified interface

    Provides a unified interface to a variety of GSEA techniques from different bioconductor packages. Results are harmonized into a single object and can be interrogated uniformly for quick exploration and interpretation of results. Interactive exploration of GSEA results is enabled through a shiny app provided by a sparrow.shiny sibling package.
    """

    homepage = "https://github.com/lianos/sparrow"
    bioc = "sparrow"

    version("1.14.0", commit="faf172b573e1dba391dfde7f93733a4702272886")
    version("1.8.0", commit="115a98fb42462058dccae5c54ae9a9a6abb6b14e")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-babelgene@21.4:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocset", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-complexheatmap@2:", type=("build", "run"))
    depends_on("r-data-table@1.10.4:", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-edger@3.18.1:", type=("build", "run"))
    depends_on("r-ggplot2@2.2:", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-plotly@4.9:", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
