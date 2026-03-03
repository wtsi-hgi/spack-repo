# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrgmm(RPackage):
	"""Bayesian Robust Generalized Mixed Models for Longitudinal Data

	To perform model estimation using MCMC algorithms with Bayesian methods for incomplete longitudinal studies on binary and ordinal outcomes that are measured repeatedly on subjects over time with drop-outs. Details about the method can be found in the vignette or <https://sites.google.com/view/kuojunglee/r-packages/bayesrgmm>.
	"""
	
	homepage = "https://sites.google.com/view/kuojunglee/r-packages"
	cran = "BayesRGMM" 

	version("2.2", md5="98fc9de54e64b7496233edb96554ebc6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-batchmeans", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
