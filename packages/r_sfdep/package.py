# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfdep(RPackage):
	"""Spatial Dependence for Simple Features

	An interface to 'spdep' to integrate with 'sf' objects and the 'tidyverse'.
	"""
	
	homepage = "https://sfdep.josiahparry.com"
	cran = "sfdep" 

	version("0.2.4", md5="61d0bd2287e708a2f3db2ae845ef796e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
