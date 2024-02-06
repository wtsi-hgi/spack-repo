# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAshr(RPackage):
	"""Methods for Adaptive Shrinkage, using Empirical Bayes

	The R package 'ashr' implements an Empirical Bayes
    approach for large-scale hypothesis testing and false discovery
    rate (FDR) estimation based on the methods proposed in
    M. Stephens, 2016, "False discovery rates: a new deal",
    <DOI:10.1093/biostatistics/kxw041>. These methods can be applied
    whenever two sets of summary statistics---estimated effects and
    standard errors---are available, just as 'qvalue' can be applied
    to previously computed p-values. Two main interfaces are
    provided: ash(), which is more user-friendly; and ash.workhorse(),
    which has more options and is geared toward advanced users. The
    ash() and ash.workhorse() also provides a flexible modeling
    interface that can accommodate a variety of likelihoods (e.g.,
    normal, Poisson) and mixture priors (e.g., uniform, normal).
	"""
	
	homepage = "https://github.com/stephens999/ashr"
	cran = "ashr" 

	version("2.2-63", md5="9695c659d7d8a5b718679142a25a9dab")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mixsqp", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
	depends_on("r-etrunct", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
