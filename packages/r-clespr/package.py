# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClespr(RPackage):
	"""Composite Likelihood Estimation for Spatial Data

	Composite likelihood approach is implemented to estimating statistical models for spatial ordinal and proportional data based on Feng et al. (2014) <doi:10.1002/env.2306>. Parameter estimates are identified by maximizing composite log-likelihood functions using the limited memory BFGS optimization algorithm with bounding constraints, while standard errors are obtained by estimating the Godambe information matrix.
	"""
	
	cran = "clespr" 

	version("1.1.2", md5="2751152449ad2247a2522677912a761a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-aer@1.2.5:", type=("build", "run"))
	depends_on("r-pbivnorm@0.6:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-magic@1.5.6:", type=("build", "run"))
	depends_on("r-survival@2.37.5:", type=("build", "run"))
	depends_on("r-clordr@1.0.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.2:", type=("build", "run"))
