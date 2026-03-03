# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffcor(RPackage):
	"""Fisher's z-Tests Concerning Difference of Correlations

	Computations of Fisher's z-tests concerning different kinds of correlation differences. Additionally, approaches to estimating statistical power via Monte Carlo simulations are implemented. 
	"""
	
	cran = "diffcor" 

	version("0.8.2", md5="f2f16c818074a6d58c0da13a51fb8b6b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
