# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesvarsel(RPackage):
	"""Bayes Factors, Model Choice and Variable Selection in Linear
Models

	Bayes factors and posterior probabilities in Linear models, 
    aimed at provide a formal Bayesian answer to testing and variable 
    selection problems. 
	"""
	
	homepage = "https://github.com/comodin19/BayesVarSel"
	cran = "BayesVarSel" 

	version("2.2.5", md5="d6b8bf3c31b810c0feb897f317d694e1")

	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.5:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
