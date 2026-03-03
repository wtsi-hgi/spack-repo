# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFueleconomy(RPackage):
	"""EPA Fuel Economy Data

	Fuel economy data from the EPA, 1985-2015,
    conveniently packaged for consumption by R users.
	"""
	
	homepage = "https://github.com/hadley/fueleconomy"
	cran = "fueleconomy" 

	version("1.0.0", md5="d8a0ec3dc0d730d2ef6fd23cd64d78eb")

	depends_on("r@3.1:", type=("build", "run"))
