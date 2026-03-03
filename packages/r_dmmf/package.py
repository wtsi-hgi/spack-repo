# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmmf(RPackage):
	"""Daily Based Morgan-Morgan-Finney (DMMF) Soil Erosion Model

	Implements the daily based Morgan-Morgan-Finney (DMMF) soil erosion model (Choi et al., 2017 <doi:10.3390/w9040278>) for estimating surface runoff and sediment budgets from a field or a catchment on a daily basis.
	"""
	
	cran = "DMMF" 

	version("0.5.2.0", md5="20c7e3d69cd06c87995176d1a28989f8")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
