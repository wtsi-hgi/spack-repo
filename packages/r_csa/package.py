# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsa(RPackage):
	"""A Cross-Scale Analysis Tool for Model-Observation Visualization
and Integration

	Integration of Earth system data from various sources is a challenging task. Except for their qualitative heterogeneity, different data records exist for describing similar Earth system process at different spatio-temporal scales. Data inter-comparison and validation are usually performed at a single spatial or temporal scale, which could hamper the identification of potential discrepancies in other scales. 'csa' package offers a simple, yet efficient, graphical method for synthesizing and comparing observed and modelled data across a range of spatio-temporal scales. Instead of focusing at specific scales, such as annual means or original grid resolution, we examine how their statistical properties change across spatio-temporal continuum.  
	"""
	
	homepage = "https://github.com/imarkonis/csa"
	cran = "csa" 

	version("0.7.1", md5="c33d7b3c543ecc43f4513a9dab9c02f2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-lmoments", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
