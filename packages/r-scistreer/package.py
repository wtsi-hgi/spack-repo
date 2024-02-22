# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScistreer(RPackage):
	"""Maximum-Likelihood Perfect Phylogeny Inference at Scale

	Fast maximum-likelihood phylogeny inference from noisy single-cell data using the 'ScisTree' algorithm by Yufeng Wu (2019) <doi:10.1093/bioinformatics/btz676>. 'scistreer' provides an 'R' interface and improves speed via 'Rcpp' and 'RcppParallel', making the method applicable to massive single-cell datasets (>10,000 cells).
	"""
	
	homepage = "https://github.com/kharchenkolab/scistreer"
	cran = "scistreer" 

	version("1.2.0", md5="310321c2b47b15f1b2afd14ce99eb773")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
