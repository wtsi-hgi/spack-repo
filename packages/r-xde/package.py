# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXde(RPackage):
	"""a Bayesian hierarchical model for cross-study analysis of
	   differential gene expression.

	Multi-level model for cross-study detection of differential gene
	expression."""

	bioc = "XDE"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/XDE_2.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/XDE/XDE_2.48.0.tar.gz"]

	version("2.48.0", md5="aaf179de92edd3a7105c0fe20254f3d6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-genemeta", type=("build", "run"))
	depends_on("r-siggenes", type=("build", "run"))
