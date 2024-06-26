# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWildlifedi(RPackage):
	"""Calculate Indices of Dynamic Interaction for Wildlife Tracking
Data

	Dynamic interaction refers to spatial-temporal associations in the movements of two (or more) animals. This package provides tools for calculating a suite of indices used for quantifying dynamic interaction with wildlife telemetry data. For more information on each of the methods employed see the references within. The package (as of version >= 0.3) also has new tools for automating contact analysis in large tracking datasets. The package (as of version 1.0) uses the 'move2' class of objects for working with tracking dataset.
	"""
	
	homepage = "https://github.com/jedalong/wildlifeDI"
	cran = "wildlifeDI" 

	version("1.0.0", md5="c4ae6e778631de6e7645f989cb28fa4e")
	version("0.5.1", md5="9a7f80b4176a1f760d6c8274e196e935")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-move2", type=("build", "run"))
	depends_on("r-adehabitatlt", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
