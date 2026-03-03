# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGasfluxes(RPackage):
	"""Greenhouse Gas Flux Calculation from Chamber Measurements

	Functions for greenhouse gas flux calculation from chamber
    measurements.
	"""
	
	homepage = "https://git-dmz.thuenen.de/fuss/gasfluxes"
	cran = "gasfluxes" 

	version("0.6-2", md5="240ca52ea23d12390625862645bf37a9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
