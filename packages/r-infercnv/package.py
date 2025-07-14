# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfercnv(RPackage):
	"""Infer Copy Number Variation from Single-Cell RNA-Seq Data

	Using single-cell RNA-Seq expression to visualize CNV in cells.
	"""
	
	homepage = "https://github.com/broadinstitute/inferCNV/wiki"
	bioc = "infercnv" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/infercnv_1.18.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/infercnv/infercnv_1.18.1.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.1", sha256="eadc079ffc2681efddfb760b52adee870914f168251c94c8be2159a1e1b031b5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phyclust", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hiddenmarkov", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-argparse", type=("build", "run"))
	depends_on("jags@4:", type=("build", "link", "run"))
