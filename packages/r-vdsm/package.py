# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdsm(RPackage):
	"""Visualization of Distribution of Selected Model

	Although model selection is ubiquitous in scientific discovery, the stability and uncertainty of the selected model is often hard to evaluate. How to characterize the random behavior of the model selection procedure is the key to understand and quantify the model selection uncertainty. This R package offers several graphical tools to visualize the distribution of the selected model. For example, Gplot(), Hplot(), VDSM_scatterplot() and VDSM_heatmap(). To the best of our knowledge, this is the first attempt to visualize such a distribution. About what distribution of selected model is and how it work please see Qin,Y.and Wang,L. (2021) "Visualization of Model Selection Uncertainty" <https://homepages.uc.edu/~qinyn/VDSM/VDSM.html>.
	"""
	
	cran = "VDSM" 

	version("0.1.1", md5="f8ff4e43b79bc2e599f7b1a6ac4d1720")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
