# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMelissa(RPackage):
	"""Bayesian clustering and imputationa of single cell methylomes

	Melissa is a Baysian probabilistic model for jointly clustering and imputing single cell methylomes. This is done by taking into account local correlations via a Generalised Linear Model approach and global similarities using a mixture modelling approach.
	"""
	
	bioc = "Melissa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Melissa_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Melissa/Melissa_1.18.0.tar.gz"]

	version("1.18.0", sha256="66e8b0c98a16936859eacd5d21c42fad7443a59412f3edb487e5a2e35c3be27f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bprmeth", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
