# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistregVis(RPackage):
	"""Framework for the Visualization of Distributional Regression
Models

	Functions for visualizing distributional regression models fitted using the 'gamlss', 'bamlss' or 'betareg' R package. The core of the package consists of a 'shiny' application, where the model results can be interactively explored and visualized.
	"""
	
	homepage = "https://github.com/Stan125/distreg.vis"
	cran = "distreg.vis" 

	version("1.7.5", md5="9bc2c48b5c6b8ed1f0907b6927e96d31")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.0.3:", type=("build", "run"))
	depends_on("r-bamlss@0.1.2:", type=("build", "run"))
	depends_on("r-gamlss@5.0.6:", type=("build", "run"))
	depends_on("r-gamlss-dist@5.1.0:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-rhandsontable@0.3.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-formatr@1.5:", type=("build", "run"))
	depends_on("r-betareg@3.1.2:", type=("build", "run"))
