# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhm(RPackage):
	"""Non-Homogeneous Markov and Hidden Markov Multistate Models

	Fits non-homogeneous Markov multistate models and misclassification-type hidden Markov models in continuous time to intermittently observed data. Implements the methods in Titman (2011) <doi:10.1111/j.1541-0420.2010.01550.x>. Uses direct numerical solution of the Kolmogorov forward equations to calculate the transition probabilities.
	"""
	
	cran = "nhm" 

	version("0.1.1", md5="646fd06219c24203fbe61e842909f3e2")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
