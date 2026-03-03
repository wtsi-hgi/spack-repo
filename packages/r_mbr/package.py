# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbr(RPackage):
	"""Mass Balance Reconstruction

	Mass-balance-adjusted Regression algorithm for streamflow reconstruction at sub-annual resolution (e.g., seasonal or monthly). The algorithm implements a penalty term to minimize the differences between the total sub-annual flows and the annual flow. The method is described in Nguyen et al (2020) <DOI:10.1002/essoar.10504791.1>.
	"""
	
	homepage = "https://github.com/ntthung/mbr"
	cran = "mbr" 

	version("0.0.1", md5="04fecc959b33a0322ccaf195e409a296")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
