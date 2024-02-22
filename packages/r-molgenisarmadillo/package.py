# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMolgenisarmadillo(RPackage):
	"""Armadillo Client for the Armadillo Service

	A set of functions to manage data shared on a 
  'MOLGENIS Armadillo' server.
	"""
	
	homepage = "https://github.com/molgenis/molgenis-r-armadillo/"
	cran = "MolgenisArmadillo" 

	version("2.3.0", md5="3b32442dca8c6817046a8ad05713330d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-molgenisauth@0.0.25:", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
