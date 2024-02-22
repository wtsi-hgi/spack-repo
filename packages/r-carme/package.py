# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarme(RPackage):
	"""CAR-MM Modelling in Stan

	'Stan' based functions to estimate CAR-MM models. These models allow to estimate Generalised Linear Models with CAR (conditional autoregressive) spatial random effects for spatially and temporally misaligned data, provided a suitable Multiple Membership matrix. The main references are Gramatica, Liverani and Congdon (2023) <doi:10.1214/23-BA1370>, Petrof, Neyens, Nuyts, Nackaerts, Nemery and Faes (2020) <doi:10.1002/sim.8697> and Gramatica, Congdon and Liverani <doi:10.1111/rssc.12480>.
	"""
	
	cran = "CARME" 

	version("0.1.1", md5="8e22550cca4054d660f3ffaf781253d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
