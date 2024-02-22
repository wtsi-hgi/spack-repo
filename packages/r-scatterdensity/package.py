# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatterdensity(RPackage):
	"""Density Estimation and Visualization of 2D Scatter Plots

	The user has the option to utilize the two-dimensional density estimation techniques called smoothed density published by Eilers and Goeman (2004) <doi:10.1093/bioinformatics/btg454>, and pareto density which was evaluated for univariate data by Thrun, Gehlert and Ultsch, 2020 <doi:10.1371/journal.pone.0238835>. Moreover, it provides visualizations of the density estimation in the form of two-dimensional scatter plots in which the points are color-coded based on increasing density. Colors are defined by the one-dimensional clustering technique called 1D distribution cluster algorithm (DDCAL) published by Lux and Rinderle-Ma (2023) <doi:10.1007/s00357-022-09428-6>.
	"""
	
	homepage = "https://www.deepbionics.org/"
	cran = "ScatterDensity" 

	version("0.0.4", md5="3dff0074369254f85a6dbf0177bd9063")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
