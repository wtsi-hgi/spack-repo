# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpbayes(RPackage):
	"""Univariate and Multivariate Spatial-Temporal Modeling

	Fits univariate and multivariate spatio-temporal
        random effects models for point-referenced data using Markov chain Monte Carlo (MCMC). Details are given in Finley, Banerjee, and Gelfand (2015) <doi:10.18637/jss.v063.i13> and Finley and Banerjee <doi:10.1016/j.envsoft.2019.104608>.
	"""
	
	homepage = "https://www.finley-lab.com"
	cran = "spBayes" 

	version("0.4-7", md5="891cc642736e6a5eca7a6654c6b26c2a")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
