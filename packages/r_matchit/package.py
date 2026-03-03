# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchit(RPackage):
	"""Nonparametric Preprocessing for Parametric Causal Inference

	Selects matched samples of the original treated and
    control groups with similar covariate distributions -- can be
    used to match exactly on covariates, to match on propensity
    scores, or perform a variety of other matching procedures.  The
    package also implements a series of recommendations offered in
    Ho, Imai, King, and Stuart (2007) <DOI:10.1093/pan/mpl013>. (The 
    'gurobi' package, which is not on CRAN, is optional and comes with 
    an installation of the Gurobi Optimizer, available at 
    <https://www.gurobi.com>.)
	"""
	
	homepage = "https://kosukeimai.github.io/MatchIt/"
	cran = "MatchIt" 

	version("4.5.5", md5="868543cc83c7567510e676e52daf3819")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-backports@1.1.9:", type=("build", "run"))
	depends_on("r-chk@0.8.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
