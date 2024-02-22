# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmbc(RPackage):
	"""Model Based Clustering of Binary Dissimilarity Measurements

	Functions for fitting a Bayesian model for grouping binary
    dissimilarity matrices in homogeneous clusters. Currently, it includes
    methods only for binary data (<doi:10.18637/jss.v100.i16>).
	"""
	
	cran = "dmbc" 

	version("1.0.2", md5="0e059385d93878446eadbde00052ec9c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bayesplot@1.7:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.8.1:", type=("build", "run"))
	depends_on("r-modeltools@0.2.22:", type=("build", "run"))
	depends_on("r-robustbase@0.93.5:", type=("build", "run"))
	depends_on("r-robustx@1.2.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
