# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyrData(RPackage):
	"""Data Only Package to 'healthyR'

	Provides data for functions typically used in the 'healthyR' package.
	"""
	
	homepage = "https://github.com/spsanderson/healthyR.data"
	cran = "healthyR.data" 

	version("1.0.3", md5="422a74d9e10f952de42c0d4baf563128")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
