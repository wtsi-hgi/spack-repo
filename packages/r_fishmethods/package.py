# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishmethods(RPackage):
	"""Fishery Science Methods and Models

	Functions for applying a wide range of fisheries stock assessment methods.
	"""
	
	cran = "fishmethods" 

	version("1.12-1", md5="89d1b97b28e17c6b3ef1a10ca159a3a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
