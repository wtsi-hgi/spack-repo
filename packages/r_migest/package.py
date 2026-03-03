# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigest(RPackage):
	"""Methods for the Indirect Estimation of Bilateral Migration

	Tools for estimating, measuring and working with migration data.
	"""
	
	homepage = "http://guyabel.github.io/migest/"
	cran = "migest" 

	version("2.0.4", md5="96c33daa54c6d835a0ed048d980a2c21")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-migration-indices", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-mipfp", type=("build", "run"))
