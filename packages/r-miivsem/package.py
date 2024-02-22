# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiivsem(RPackage):
	"""Model Implied Instrumental Variable (MIIV) Estimation of
Structural Equation Models

	Functions for estimating structural equation models using 
    instrumental variables.
	"""
	
	homepage = "https://github.com/zackfisher/MIIVsem"
	cran = "MIIVsem" 

	version("0.5.8", md5="0f01b6eb995efbe9f964c4618ba2b52a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
