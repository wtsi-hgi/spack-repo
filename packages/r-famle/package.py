# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamle(RPackage):
	"""Maximum Likelihood and Bayesian Estimation of Univariate
Probability Distributions

	Estimate parameters of univariate probability distributions 
  with maximum likelihood and Bayesian methods.
	"""
	
	homepage = "https://github.com/tpetzoldt/FAmle"
	cran = "FAmle" 

	version("1.3.7", md5="ab722452c22bd5e50e4e4a9832ea0550")

	depends_on("r-mvtnorm", type=("build", "run"))
