# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTframeplus(RPackage):
	"""Time Frame Coding Kernel Extensions

	Extensions and additional 'tframe' utilities.
	"""
	
	homepage = "http://tsanalysis.r-forge.r-project.org/"
	cran = "tframePlus" 

	version("2024.2-1", md5="35dbd69330e235d50c9da9dafe779909")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-tframe@2015.1.1:", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
