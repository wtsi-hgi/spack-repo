# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperheat(RPackage):
	"""A Graphical Tool for Exploring Complex Datasets Using Heatmaps

	A system for generating extendable and customizable heatmaps for exploring complex datasets, including big data and data with multiple data types.
	"""
	
	cran = "superheat" 

	version("0.1.0", md5="c4b19907e318c4bf31655da69a476919")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gtable@0.1.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-scales@0.3:", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
