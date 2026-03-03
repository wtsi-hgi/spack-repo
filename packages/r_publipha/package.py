# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPublipha(RPackage):
	"""Bayesian Meta-Analysis with Publications Bias and P-Hacking

	Tools for Bayesian estimation of meta-analysis models that account
    for publications bias or p-hacking. For publication bias, this package
    implements a variant of the p-value based selection model of Hedges (1992)
    <doi:10.1214/ss/1177011364> with discrete selection probabilities. It also
    implements the mixture of truncated normals model for p-hacking described
    in Moss and De Bin (2019) <arXiv:1911.12445>.
	"""
	
	cran = "publipha" 

	version("0.1.2", md5="cc8b338904a5dd36b327f93c908f80d3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp@0.12.19:", type=("build", "run"))
	depends_on("r-rstan@2.21.8:", type=("build", "run"))
	depends_on("r-rstantools@1.5.1:", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-bh@1.72.0.2:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
	depends_on("r-stanheaders@2.21.0.7:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
