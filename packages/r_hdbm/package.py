# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdbm(RPackage):
	"""High Dimensional Bayesian Mediation Analysis

	Perform mediation analysis in the presence of high-dimensional
    mediators based on the potential outcome framework. High dimensional
    Bayesian mediation (HDBM), developed by Song et al (2018)
    <doi:10.1101/467399>, relies on two Bayesian sparse linear mixed models to
    simultaneously analyze a relatively large number of mediators for a
    continuous exposure and outcome assuming a small number of mediators are
    truly active. This sparsity assumption also allows the extension of
    univariate mediator analysis by casting the identification of active
    mediators as a variable selection problem and applying Bayesian methods
    with continuous shrinkage priors on the effects.
	"""
	
	cran = "hdbm" 

	version("0.9.0", md5="3d33b08788295dd28788cb74ae8d3661")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
