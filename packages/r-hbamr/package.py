# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbamr(RPackage):
	"""Hierarchical Bayesian Aldrich-McKelvey Scaling via 'Stan'

	Perform hierarchical Bayesian Aldrich-McKelvey scaling using Hamiltonian Monte
    Carlo via 'Stan'. Aldrich-McKelvey ('AM') scaling is a method for estimating the ideological 
    positions of survey respondents and political actors on a common scale using positional survey 
    data. The hierarchical versions of the Bayesian 'AM' model included in this package outperform 
    other versions both in terms of yielding meaningful posterior distributions for respondent 
    positions and in terms of recovering true respondent positions in simulations. The package 
    contains functions for preparing data, fitting models, extracting estimates, plotting key 
    results, and comparing models using cross-validation. The original version of the default 
    model is described in Bølstad (2024) <doi:10.1017/pan.2023.18>.
	"""
	
	homepage = "https://jbolstad.github.io/hbamr/"
	cran = "hbamr" 

	version("2.3.0", md5="8753551b95556e4306a569633a12c474")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.26.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26.22:", type=("build", "run"))
