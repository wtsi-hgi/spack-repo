# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInformativecensoring(RPackage):
	"""Multiple Imputation for Informative Censoring

	Multiple Imputation for Informative Censoring.
    This package implements two methods. Gamma Imputation
    described in <DOI:10.1002/sim.6274> and Risk Score Imputation
    described in <DOI:10.1002/sim.3480>.
	"""
	
	homepage = "https://github.com/jwb133/InformativeCensoring"
	cran = "InformativeCensoring" 

	version("0.3.6", md5="caa4f2c1a064d064590463823c06b8db")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-survival@2.36.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
