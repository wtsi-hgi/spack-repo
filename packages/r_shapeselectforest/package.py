# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapeselectforest(RPackage):
	"""Shape Selection for Landsat Time Series of Forest Dynamics

	Landsat satellites collect important data about global forest conditions. Documentation about Landsat's role in forest disturbance estimation is available at the site <https://landsat.gsfc.nasa.gov/>. By constrained quadratic B-splines, this package delivers an optimal shape-restricted trajectory to a time series of Landsat imagery for the purpose of modeling annual forest disturbance dynamics to behave in an ecologically sensible manner assuming one of seven possible "shapes", namely, flat, decreasing, one-jump (decreasing, jump up, decreasing), inverted vee (increasing then decreasing), vee (decreasing then increasing), linear increasing, and double-jump (decreasing, jump up, decreasing, jump up, decreasing). The main routine selects the best shape according to the minimum Bayes information criterion (BIC) or the cone information criterion (CIC), which is defined as the log of the estimated predictive squared error. The package also provides parameters summarizing the temporal pattern including year(s) of inflection, magnitude of change, pre- and post-inflection rates of growth or recovery. In addition, it contains routines for converting a flat map of disturbance agents to time-series disturbance maps and a graphical routine displaying the fitted trajectory of Landsat imagery. 
	"""
	
	cran = "ShapeSelectForest" 

	version("1.7", md5="70a1a15ad2c7b27200ffd264d90445fd")

	depends_on("r-coneproj@1.6:", type=("build", "run"))
	depends_on("r-raster@2.3.40:", type=("build", "run"))
	depends_on("r@3.0.2:", type=("build", "run"))
