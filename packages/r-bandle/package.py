# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBandle(RPackage):
	"""An R package for the Bayesian analysis of differential subcellular localisation experiments

	The Bandle package enables the analysis and visualisation of differential localisation experiments using mass-spectrometry data. Experimental methods supported include dynamic LOPIT-DC, hyperLOPIT, Dynamic Organellar Maps, Dynamic PCP. It provides Bioconductor infrastructure to analyse these data.
	"""
	
	homepage = "http://github.com/ococrook/bandle"
	bioc = "bandle" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/bandle_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/bandle/bandle_1.6.0.tar.gz"]

	version("1.6.0", md5="9c8dd928dd2b7900ff453ddc590ad6e4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-proloc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-prolocdata", type=("build", "run"))
	depends_on("r-lbfgs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
