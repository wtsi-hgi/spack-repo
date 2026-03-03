# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorphotools2(RPackage):
	"""Multivariate Morphometric Analysis

	Tools for multivariate analyses of morphological data, wrapped in one package, to make the workflow convenient and fast. Statistical and graphical tools provide a comprehensive framework for checking and manipulating input data, statistical analyses, and visualization of results. Several methods are provided for the analysis of raw data, to make the dataset ready for downstream analyses. Integrated statistical methods include hierarchical classification, principal component analysis, principal coordinates analysis, non-metric multidimensional scaling, and multiple discriminant analyses: canonical, stepwise, and classificatory (linear, quadratic, and the non-parametric k nearest neighbours). The philosophy of the package is described in Šlenker et al. 2022.
	"""
	
	homepage = "https://github.com/MarekSlenker/MorphoTools2"
	cran = "MorphoTools2" 

	version("1.0.1.1", md5="b28efc189f9b776d6756f34f08012873", url="https://cran.r-project.org/src/contrib/MorphoTools2_1.0.1.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-candisc", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-heplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
