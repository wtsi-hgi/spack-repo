# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaggr(RPackage):
	"""Bayesian Aggregate Treatment Effects

	Running and comparing meta-analyses of data with hierarchical 
    Bayesian models in Stan, including convenience functions for formatting
    data, plotting and pooling measures specific to meta-analysis. This implements many models
    from Meager (2019) <doi:10.1257/app.20170299>.
	"""
	
	homepage = "https://github.com/wwiecek/baggr"
	cran = "baggr" 

	version("0.7.8", md5="40cf3532f867d324d19eedf26883a24b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.17:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
