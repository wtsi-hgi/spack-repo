# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikiprofiler(RPackage):
	"""'WikiPathway' Based Data Integration and Visualization

	Queries online 'WikiPathway' graphics and allows mapping user data (e.g., expression values) on the graph. The package designs a grammar of graphic syntax that using pipe operator to add graphic layer.
	"""
	
	cran = "wikiprofiler" 

	version("0.1.3", md5="1c22a11b57bda96fd55a7bb15ecc25af")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-gson", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
