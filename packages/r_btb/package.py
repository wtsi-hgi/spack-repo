# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtb(RPackage):
	"""Beyond the Border - Kernel Density Estimation for Urban
Geography

	The kernelSmoothing() function allows you to square and smooth geolocated data. It calculates a classical kernel smoothing (conservative) or a geographically weighted median. There are four major call modes of the function. 
        The first call mode is kernelSmoothing(obs, epsg, cellsize, bandwidth) for a classical kernel smoothing and automatic grid.
        The second call mode is kernelSmoothing(obs, epsg, cellsize, bandwidth, quantiles) for a geographically weighted median and automatic grid.
        The third call mode is kernelSmoothing(obs, epsg, cellsize, bandwidth, centroids) for a classical kernel smoothing and user grid.
        The fourth call mode is kernelSmoothing(obs, epsg, cellsize, bandwidth, quantiles, centroids) for a geographically weighted median and user grid.
        Geographically weighted summary statistics : a framework for localised exploratory data analysis, C.Brunsdon & al., in Computers, Environment and Urban Systems C.Brunsdon & al. (2002) <doi:10.1016/S0198-9715(01)00009-6>, 
        Statistical Analysis of Spatial and Spatio-Temporal Point Patterns, Third Edition, Diggle, pp. 83-86, (2003) <doi:10.1080/13658816.2014.937718>.
	"""
	
	homepage = "https://github.com/InseeFr/btb"
	cran = "btb" 

	version("0.2.0", md5="984c6e44f8b3f78cf47fa50dcce38e1f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mapsf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-bh@1.60.0.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
