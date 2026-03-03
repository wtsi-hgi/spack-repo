# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSongevo(RPackage):
	"""An Individual-Based Model of Bird Song Evolution

	Simulates the cultural evolution of quantitative traits of bird song. 'SongEvo' is an individual- (agent-) based model. 'SongEvo' is spatially-explicit and can be parameterized with, and tested against, measured song data. Functions are available for model implementation, sensitivity analyses, parameter optimization, model validation, and hypothesis testing. 
	"""
	
	cran = "SongEvo" 

	version("1.0.0", md5="270482729e42181f88a179303dda76c0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
