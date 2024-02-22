# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCati(RPackage):
	"""Community Assembly by Traits: Individuals and Beyond

	Detect and quantify community assembly processes using trait values of individuals or populations, the T-statistics and other metrics, and dedicated null models.
	"""
	
	homepage = "https://github.com/adrientaudiere/cati"
	cran = "cati" 

	version("0.99.4", md5="4cc9697b0c7e3606284aa7b16efdcca2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-hypervolume", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
