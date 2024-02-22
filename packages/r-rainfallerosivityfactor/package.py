# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRainfallerosivityfactor(RPackage):
	"""The Rainfall-Runoff Erosivity Factor

	Determination of rainfall-runoff erosivity factor.
	"""
	
	cran = "RainfallErosivityFactor" 

	version("0.1.0", md5="c965e2b5a12511e2fa8ee101dfd20ebf")

	depends_on("r@2.10:", type=("build", "run"))
