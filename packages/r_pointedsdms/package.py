# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPointedsdms(RPackage):
	"""Fit Models Derived from Point Processes to Species Distributions
using 'inlabru'

	Integrated species distribution modeling is a rising field in quantitative ecology thanks to significant rises in the quantity of data available, increases in computational speed and the proven benefits of using such models. 
  Despite this, the general software to help ecologists construct such models in an easy-to-use framework is lacking. 
  We therefore introduce the R package 'PointedSDMs': which provides the tools to help ecologists set up integrated models and perform inference on them.
  There are also functions within the package to help run spatial cross-validation for model selection, as well as generic plotting and predicting functions.
  An introduction to these methods is discussed in Issac, Jarzyna, Keil, Dambly, Boersch-Supan, Browning, Freeman, Golding, Guillera-Arroita, Henrys, Jarvis, Lahoz-Monfort, Pagel, Pescott, Schmucki, Simmonds and O’Hara (2020) <doi:10.1016/j.tree.2019.08.006>.
	"""
	
	homepage = "https://github.com/PhilipMostert/PointedSDMs"
	cran = "PointedSDMs" 

	version("1.3.2", md5="ded4d8fe314b307ba0e74f9d39f19249")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-inlabru@2.8:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp@1.4.5:", type=("build", "run"))
	depends_on("r-r-devices", type=("build", "run"))
	depends_on("r-blockcv@3:", type=("build", "run"))
