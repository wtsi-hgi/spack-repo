# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrain(RPackage):
	"""Graphical Independence Networks

	Probability propagation in graphical independence networks, also
    known as Bayesian networks or probabilistic expert systems. Documentation
    of the package is provided in vignettes included in the package and in
    the paper by Højsgaard (2012, <doi:10.18637/jss.v046.i10>).
    See 'citation("gRain")' for details. 
	"""
	
	homepage = "https://people.math.aau.dk/~sorenh/software/gR/"
	cran = "gRain" 

	version("1.4.1", md5="2036089229e229216219935538d9ab2b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp@0.11.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
