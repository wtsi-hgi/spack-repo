# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofcopula(RPackage):
	"""Goodness-of-Fit Tests for Copulae

	Several Goodness-of-Fit (GoF) tests for Copulae are provided. A new hybrid test, Zhang et al. (2016) <doi:10.1016/j.jeconom.2016.02.017> is implemented which supports all of the individual tests in the package, e.g. Genest et al. (2009) <doi:10.1016/j.insmatheco.2007.10.005>. Estimation methods for the margins are provided and all the tests support parameter estimation and predefined values. The parameters are estimated by pseudo maximum likelihood but if it fails the estimation switches automatically to inversion of Kendall's tau. For reproducibility of results, the functions support the definition of seeds. Also all the tests support automatized parallelization of the bootstrapping tasks. The package provides an interface to perform new GoF tests by submitting the test statistic.
	"""
	
	cran = "gofCopula" 

	version("0.4-1", md5="abbea428df8a705f650cafe61d495c4e")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-copula@1.0.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-sparsegrid", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-vinecopula@2.0.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-yarrr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
