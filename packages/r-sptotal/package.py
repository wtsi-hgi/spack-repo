# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSptotal(RPackage):
	"""Predicting Totals and Weighted Sums from Spatial Data

	Performs predictions of totals and weighted sums, or finite population block kriging, on spatial data using the methods in Ver Hoef (2008) <doi:10.1007/s10651-007-0035-y>. The primary outputs are an estimate of the total, mean, or weighted sum in the region, an estimated prediction variance, and a plot of the predicted and observed values. This is useful primarily to users with ecological data that are counts or densities measured on some sites in a finite area of interest. Spatial prediction for the total count or average density in the entire region can then be done using the functions in this package. 
	"""
	
	homepage = "https://highamm.github.io/sptotal/index.html"
	cran = "sptotal" 

	version("1.0.1", md5="5b35584ae70100a93968b4af362ccbf3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
