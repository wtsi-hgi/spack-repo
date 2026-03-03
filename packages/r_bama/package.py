# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBama(RPackage):
	"""High Dimensional Bayesian Mediation Analysis

	Perform mediation analysis in the presence of high-dimensional
    mediators based on the potential outcome framework. Bayesian Mediation
    Analysis (BAMA), developed by Song et al (2019) <doi:10.1111/biom.13189> and
    Song et al (2020) <arXiv:2009.11409>,
    relies on two Bayesian sparse linear mixed models to simultaneously analyze
    a relatively large number of mediators for a continuous exposure and outcome
    assuming a small number of mediators are truly active. This sparsity
    assumption also allows the extension of univariate mediator analysis by
    casting the identification of active mediators as a variable selection
    problem and applying Bayesian methods with continuous shrinkage priors on
    the effects.
	"""
	
	homepage = "https://github.com/umich-cphds/bama"
	cran = "bama" 

	version("1.3.0", md5="172c31d9b9118bc797181ca786b6d85e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
