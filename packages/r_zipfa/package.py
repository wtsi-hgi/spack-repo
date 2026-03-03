# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipfa(RPackage):
	"""Zero Inflated Poisson Factor Analysis

	Estimation methods for zero-inflated Poisson factor analysis (ZIPFA) on sparse data. 
    It provides estimates of coefficients in a new type of zero-inflated regression. 
    It provides a cross-validation method to determine the potential rank of the data in the ZIPFA 
    and conducts zero-inflated Poisson factor analysis based on the determined rank.
	"""
	
	homepage = "https://zjph602xtc.github.io/ZIPFA/"
	cran = "ZIPFA" 

	version("0.8.1", md5="c8a58823de2bb217d779592f68832444")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-trustoptim", type=("build", "run"))
