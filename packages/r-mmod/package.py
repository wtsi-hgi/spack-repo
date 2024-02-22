# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmod(RPackage):
	"""Modern Measures of Population Differentiation

	Provides functions for measuring
    population divergence from genotypic data.
	"""
	
	homepage = "https://github.com/dwinter/mmod"
	cran = "mmod" 

	version("1.3.3", md5="957b63e23536053a16e24434d06b13d6")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
