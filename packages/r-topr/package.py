# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopr(RPackage):
	"""Create Custom Plots for Viewing Genetic Association Results

	A collection of functions for visualizing,exploring and annotating genetic association results.Association results from multiple traits can be viewed simultaneously along with gene annotation, over the entire genome (Manhattan plot) or in the more detailed regional view.
	"""
	
	homepage = "https://github.com/totajuliusd/topr"
	cran = "topr" 

	version("2.0.0", md5="fbad4c3ac65ca75ad38e5ac06977324c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-enshuman", type=("build", "run"))
