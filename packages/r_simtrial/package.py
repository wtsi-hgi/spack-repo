# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimtrial(RPackage):
	"""Clinical Trial Simulation

	Provides some basic routines for simulating a
    clinical trial. The primary intent is to provide some tools to
    generate trial simulations for trials with time to event outcomes.
    Piecewise exponential failure rates and piecewise constant
    enrollment rates are the underlying mechanism used to simulate
    a broad range of scenarios such as those presented in
    Lin et al. (2020) <doi:10.1080/19466315.2019.1697738>.
    However, the basic generation of data is done using pipes to allow
    maximum flexibility for users to meet different needs.
	"""
	
	homepage = "https://merck.github.io/simtrial/"
	cran = "simtrial" 

	version("0.3.2", md5="702c4cb64e30535ba12d28fb3a0b8d32")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
