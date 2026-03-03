# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgcorset(RPackage):
	"""The Corset Plot

	Corset plots are a visualization technique used strictly to visualize repeat measures 
  at 2 time points (such as pre- and post- data). The distribution of measurements are visualized at 
  each time point, whilst the trajectories of individual change are visualized by connecting the pre- 
  and post- values linearly. These lines can be coloured to represent the magnitude of change, or 
  other user-defined value. This method of visualization is ideal for showing the heterogeneity of 
  data, including differences by sub-groups. The package relies on 'ggplot2' allowing for easy 
  integration so that users can customize their visualizations as required. Users can create corset 
  plots using data in either wide or long format using the functions gg_corset() or gg_corset_elongated(), respectively.
	"""
	
	cran = "ggcorset" 

	version("0.4.5", md5="1d39e6e050df9eeb5d85640c0839b739")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gghalves", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
