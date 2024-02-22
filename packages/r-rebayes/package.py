# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebayes(RPackage):
	"""Empirical Bayes Estimation and Inference

	Kiefer-Wolfowitz maximum likelihood estimation for mixture models
    and some other density estimation and regression methods based on convex
    optimization.  See Koenker and Gu (2017) REBayes: An R Package for Empirical
    Bayes Mixture Methods, Journal of Statistical Software, 82, 1--26, 
    <DOI:10.18637/jss.v082.i08>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "REBayes" 

	version("2.54", md5="e255c6405c50ea80d129405d65c10320")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
