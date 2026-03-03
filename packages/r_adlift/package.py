# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdlift(RPackage):
	"""An Adaptive Lifting Scheme Algorithm

	Adaptive wavelet lifting transforms for signal denoising using optimal local neighbourhood regression, from Nunes et al. (2006) <doi:10.1007/s11222-006-6560-y>.
	"""
	
	cran = "adlift" 

	version("1.4-5", md5="eb45d92df87a63365bf082bdfb15ff14")

	depends_on("r-ebayesthresh", type=("build", "run"))
