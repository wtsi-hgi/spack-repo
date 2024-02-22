# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenmx(RPackage):
	"""Extended Structural Equation Modelling

	Create structural equation models that can be manipulated programmatically.
    Models may be specified with matrices or paths (LISREL or RAM)
    Example models include confirmatory factor, multiple group, mixture
    distribution, categorical threshold, modern test theory, differential
    Fit functions include full information maximum likelihood, maximum likelihood, and weighted least squares.
    equations, state space, and many others.
	Support and advanced package binaries available at <http://openmx.ssri.psu.edu>.
    The software is described in Neale, Hunter, Pritikin, Zahery, Brick,
    Kirkpatrick, Estabrook, Bates, Maes, & Boker (2016) <doi:10.1007/s11336-014-9435-8>.
	"""
	
	homepage = "http://openmx.ssri.psu.edu"
	cran = "OpenMx" 

	version("2.21.11", md5="01c7dafc8a54ab6da5ff7ba5d0c0f14a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.4:", type=("build", "run"))
	depends_on("r-stanheaders@2.10.0.2:", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
	depends_on("r-rpf@0.45:", type=("build", "run"))
